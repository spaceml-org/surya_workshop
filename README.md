# README

## Overview
This repository contains documentation and guide materials for the Surya workshop.

## Submodules

This repository includes the following submodule(s):

- **surya_workshop** - https://github.com/SwRI-IDEA-Lab/surya_workshop

### Cloning with Submodules

To clone this repository with all submodules initialized:

```bash
git clone --recurse-submodules https://github.com/spaceml-org/surya_workshop
```

If you've already cloned the repository, initialize submodules with:

```bash
git submodule update --init --recursive
```

## Structure

- `/docs/source` - Documentation files
- `/surya_workshop` - GitHub repository for the Surya workshop sessions

## Getting Started

This content is designed to guide you through the Surya workshop sessions, providing detailed explanations, code examples, and resources to help you understand and apply the concepts covered in the workshop. The documentation is built using Sphinx and MyST Markdown, allowing for rich formatting and easy navigation.

For ease of use, a requirements file is included to set up the necessary environment for building and viewing the documentation locally.

To install the required dependencies, run:

```bash
poetry install 
```

Then build the documentation with:

```bash
sphinx-build -b html docs/source docs/build/html
```
or using the helper script:

```bash
. ./build.sh
```

Also included is a GitHub Actions workflow that automatically builds and deploys the documentation to GitHub Pages whenever changes are pushed to the main branch.

## Contributing

See [CONTRIBUTING.md](./docs/source/contributing.md) for guidelines on how to contribute to this documentation.