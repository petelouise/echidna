import argparse
import os
import glob
from hashlib import sha256
from imageio.v2 import imread
import mahotas as mh
import numpy as np
from database import db
from models import Image, ImageFeature
from peewee import IntegrityError

created_count = 0
exists_count = 0
error_count = 0
error_files = []


def compute_image_hash(image_path):
    with open(image_path, "rb") as image_file:
        return sha256(image_file.read()).hexdigest()


def compute_haralick_features(image_path):
    image = imread(image_path, mode="F")

    image = image.astype("float")
    image /= image.max()  # Normalize to [0, 1]
    image = (image * 255).astype(np.uint8)  # Rescale to [0, 255]

    f = mh.features.haralick(image).mean(axis=0)

    return {
        "energy": f[0],
        "contrast": f[1],
        "correlation": f[2],
        "variance": f[3],
        "local_homogeneity": f[4],
        "sum_average": f[5],
        "sum_variance": f[6],
        "sum_entropy": f[7],
        "entropy": f[8],
        "difference_variance": f[9],
        "difference_entropy": f[10],
        "info_measure_correlation_1": f[11],
        "info_measure_correlation_2": f[12],
    }


def process_image(image_path):
    global created_count, exists_count, error_count, error_files

    if not os.path.exists(image_path):
        print(f"Warning: The file {image_path} does not exist. Skipping...")
        return

    with db.atomic():
        try:
            image_hash = compute_image_hash(image_path)
            features = compute_haralick_features(image_path)
            image, created = Image.get_or_create(
                hash=image_hash, defaults={"path": image_path}
            )

            if created:
                ImageFeature.create(image=image, **features)
                print("\033[92m.\033[0m", end="")  # Green dot
                created_count += 1
            else:
                print("\033[93m.\033[0m", end="")  # Yellow dot
                exists_count += 1
        except Exception as e:
            print("\033[91m.\033[0m", end="")  # Red dot
            error_count += 1
            error_files.append(
                os.path.join(
                    os.path.basename(os.path.dirname(image_path)),
                    os.path.basename(image_path),
                )
            )
        finally:
            print("", end="")


def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                process_image(os.path.join(root, filename))


def process_glob_pattern(glob_pattern):
    for image_path in glob.glob(glob_pattern):
        process_image(image_path)


def main(input_path):
    if os.path.isdir(input_path):
        process_directory(input_path)
    elif os.path.isfile(input_path):
        process_image(input_path)
    else:
        process_glob_pattern(input_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Import images and compute Haralick features."
    )
    parser.add_argument(
        "input_path",
        type=str,
        help="The path to an image, directory, or glob pattern of images to process.",
    )

    args = parser.parse_args()
    main(args.input_path)

    # Summary
    print(
        f"\n\nSummary:\nCreated: {created_count}, Already Exists: {exists_count}, Errors: {error_count}"
    )
    if error_count > 0:
        print("Errored Files:")
        for file in error_files:
            print(file)
