# Note: This script is used to extract keywords from an image's EXIF data
# and optionally group images into a folder based on a ke yword found in
# their EXIF data. This works for images generated with Midjourney web interface.

import os
from PIL import Image, ExifTags
from shutil import move
from pathlib import Path
import pyexifinfo as pex


def get_exif_data(image_path):
    exif_data = pex.get_json(image_path)
    return exif_data[0]


def extract_description(image_path):
    try:
        exif_data = get_exif_data(image_path)

        if not exif_data:
            print(f"No EXIF data found in {image_path}.")
            return ""

        return exif_data["PNG:Description"]
    except IOError:
        print(f"Cannot open {image_path}.")
        return ""


def search_metadata(source_dir, query):
    """For each image in source_dir, search its EXIF data for the query.
    Return a list of matching image paths."""
    ExifTags.TAGS.keys()
    matching_paths = []
    valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    for image_path in source_dir.rglob("*"):
        if image_path.suffix.lower() in valid_extensions and image_path.is_file():
            description = extract_description(image_path)
            if query.lower() in description.lower():
                matching_paths.append(image_path)

    return matching_paths


def group_images_by_keyword(source_dir, dest_dir, query):
    """Group images into a folder based on a query found in their EXIF data."""
    source_dir = Path(source_dir)
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(exist_ok=True)

    valid_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}

    for image_path in source_dir.rglob("*"):
        if image_path.suffix.lower() in valid_extensions and image_path.is_file():
            description = extract_description(image_path)
            if query.lower() in description.lower():
                target_path = dest_dir / image_path.name
                move(str(image_path), target_path)
                print(f"Moved {image_path} to {target_path}")
