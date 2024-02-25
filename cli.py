import argparse
from search import search_metadata
from pathlib import Path


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Find images based on EXIF description."
    )
    parser.add_argument("source_dir", type=Path, help="Directory to search for images.")
    parser.add_argument(
        "query", type=str, help="Query to search for in image EXIF data."
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    paths = search_metadata(args.source_dir, args.query)
    print(list(map(str, paths)))


if __name__ == "__main__":
    main()
