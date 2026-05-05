# static-site-generator

A Markdown-to-HTML static site generator built from scratch in Python. Parses inline Markdown into an HTML node tree and renders it to static files — no external Markdown libraries used.

## Features

- Custom HTML node tree (`HTMLNode`, `LeafNode`, `ParentNode`)
- Inline Markdown parsing via `TextNode` and `TextType`
- Supports: plain text, **bold**, *italic*, `code`, [links](url), and images
- Full unit test suite

## Tech Stack

- Python 3.x
- No external dependencies

## Getting Started

```bash
git clone https://github.com/B0OGI3/static-site-generator.git
cd static-site-generator
bash main.sh
```

Run the tests:

```bash
bash test.sh
```

## Project Structure

```
static-site-generator/
├── main.sh         # Runs the generator
├── test.sh         # Runs the test suite
├── src/
│   ├── main.py     # Entry point
│   ├── htmlnode.py # HTMLNode, LeafNode, ParentNode — HTML tree classes
│   ├── textnode.py # TextNode and TextType — inline Markdown representation
│   └── test_node.py# Unit tests for HTML and text node behavior
└── public/         # Generated output
```

## How It Works

Markdown content is parsed into `TextNode` objects with typed inline formatting. Each `TextNode` is then converted to an `HTMLNode` and rendered to an HTML string via `.to_html()`.

| TextType | Output |
|---|---|
| `TEXT` | Raw text (no tag) |
| `BOLD` | `<b>text</b>` |
| `ITALIC` | `<i>text</i>` |
| `CODE` | `<code>text</code>` |
| `LINK` | `<a href="url">text</a>` |
| `IMAGE` | `<img src="url" alt="text">` |
