# puggle

## Overview

Image Cataloger is a Python-based tool designed to organize and search through a local collection of abstract images. It utilizes advanced image processing techniques to catalog images based on features like color, texture, and semantic content extracted from EXIF data. The tool supports a command-line interface for easy interaction. It's named for the goddess Echidna, [sort of](https://arc.net/l/quote/tkurvvhu).

## Features

- Color and texture analysis for image cataloging
- EXIF data extraction for semantic content analysis
- Local SQLite database for efficient data management
- Command-line interface for searching and organizing images

## Prerequisites

- conda or miniconda
- Python 3.6 or higher
- Pip for Python package installation

## Setup Instructions

### 1. Clone the Repository

You got this.

### 4. Setting Up the Environment with Conda

1. **Install Anaconda**: Download and install Anaconda from the official website.
2. **Create and Activate the Environment**: Navigate to your project directory and run:

```bash
conda env create -f environment.yml
conda activate env
```

### 5. Initialize the Database

`python initialize_database.py`

### 6. Running the Application

To start using the Image Cataloger, run:
`python app.py`

## Usage Instructions

To search for images by keyword:
`python find_by_prompt.py --keyword "sunset"`

To organize images into folders based on EXIF data:
`python organize.py --directory "/path/to/images"`

## Contributing

We welcome contributions! Please read our contributing guidelines in `CONTRIBUTING.md` for details on how to submit pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
