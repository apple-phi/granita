import logging
import os
import pathlib
import shutil

import markdown
import frontmatter
import pyquery

from .config import (
    templates,
    default_template,
    content_selector,
    public,
    pages,
    static,
    extra_data,
)


def insert_content(template: os.PathLike, mapping: dict[str, str]):
    document = pyquery.PyQuery(filename=template)
    if not document("head > title"):
        document("head").append("<title/>")
    for selector, content in {**extra_data, **mapping}.items():
        element = document.find(selector)
        if not element:
            logging.warning(
                f"No matches found for selector `{selector}` in template `{template}`"
            )
        element.html(content)
    return document.outer_html()


def process_file(file_path: os.PathLike):
    with open(file_path) as f:
        post = frontmatter.load(f)
    post[content_selector] = markdown.markdown(post.content)
    template = templates / post.get("template", default_template)
    return insert_content(template, post.metadata)


def process_folder(directory: os.PathLike):
    for dirpath, _, files in os.walk(directory, followlinks=True):
        for file in files:
            if file.endswith(".md"):
                pubdir = public / pathlib.Path(dirpath).relative_to(directory)
                filename = file.replace(".md", ".html")
                pubdir.mkdir(parents=True, exist_ok=True)
                logging.info(f"Writing {pubdir / file}")
                with open(pubdir / filename, "w") as f:
                    f.write(process_file(os.path.join(dirpath, file)))


def build(clean=False):
    if clean:
        logging.info(f"Cleaning out existing public folder {public}")
        shutil.rmtree(public, ignore_errors=True)
    process_folder(pages)
    logging.info(f"Copying static folder {static}")
    if (public / static).exists():
        shutil.copytree(static, public / static, dirs_exist_ok=True)
