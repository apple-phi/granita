# Granita

A super-simple static site generator, with sensible opinionated defaults.

## Installation

```sh
pip install granita
```

## Quickstart

Run the following commands in your terminal, then open the file `my_app/public/index.html` in your browser.

```sh
granita init my_app
cd my_app
granita build
```

## What this is

At a basic level, you write Markdown in the `pages` directory, and Granita combines them with HTML templates from the `templates` directory.

For example, take the following Markdown:

```markdown
# Hello world!

> *I'm learning how to use [Granita](https://github.com/apple-phi/granita)*
```

This would be translated into HTML before being inserted inside the `<Content/>` element in the template.
By default, if a template is not specified, Granita will try to find and use file called `default.html` in your templates directory.

Files listed in the `static` directory will be copied as-is to the output `public` directory.

## Frontmatter

To specify your own parameters, you can use a format called frontmatter. It looks like this:

```markdown
---
title: "My app"
template: my_template.html
---
# Hello world!

> *I'm learning how to use [Granita](https://github.com/apple-phi/granita)*
```

`title` and `template` are treated specially by Granita. Here's what they do:

- `title` specifies the title of the webpage, by creating a `<title>` element if it doesn't already exist in the template.
- `template` specifies the HTML template to embed the Markdown in, with the path relative to the `templates` directory.

Additionally, the frontmatter keys are treated as CSS selectors for prepending content to the template. So if you had the following frontmatter:

```yaml
---
"#my_element": "some text"
---
```

Then the element with the id `my_element` will have the text `some text` prepended inside it.
And this will happen for all elements matched by the CSS selector. For example, if you duplicate the `<Content/>` tag in the default template generated by `granita init` and rebuild, then you will see two copies of the page content.

## Further configuration

If you are unsatisfied with the default paths and settings, you can create a `granita.config.json` file to override them. Here's what the default configuration looks like:

```json
{
 "pages": "pages", // path to pages dir
 "static": "static", // path to static dir
 "public": "public", // path to output dir
 "templates": "templates", // path to template dir
 "default-template": "default.html", // fallback template path
 "content-selector": "Content", // CSS selector to insert Markdown into
 "global-stylesheet": null, // a stylesheet to be applied to all templates
 "extra-data": {} // key : value pairs of CSS selector : HTML data
}
```

You don't have to provide customisation for all settings; the defaults will be used if left unspecified.

## License

MIT License, which can be found [here](https://github.com/apple-phi/granita/blob/main/LICENSE)

© Copyright 2021, apple-phi.
