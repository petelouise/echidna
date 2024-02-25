# puggle

## Overview

Image Cataloger is a Python-based tool designed to organize and search through a local collection of abstract images. It utilizes advanced image processing techniques to catalog images based on features like color, texture, and semantic content extracted from EXIF data. The tool supports a command-line interface for easy interaction. It's named for the goddess Echidna, [sort of](https://arc.net/l/quote/tkurvvhu).

## Features

- Color and texture analysis for image cataloging
- EXIF data extraction for semantic content analysis
- Local SQLite database for efficient data management
- Command-line interface for searching and organizing images

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Python 3.11 or higher
- Pip for Python package installation

## Setup Instructions

### Clone the Repository

You got this.

### Setting Up the Environment with Conda

```bash
conda env create -f environment.yml
conda activate puggle
```

### Initialize the Database

`python initialize_database.py`

### Importing Images from Command Line

`python import.py <path-to-image-directory>`

### Running the Application

`python app.py`

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
