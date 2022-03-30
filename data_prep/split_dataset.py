import argparse
import os
from glob import glob
import random
import shutil

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Split dataset into different folders")
    parser.add_argument(
        "--processed-data", "-i", type=str, help="Directory of hdf5 files"
    )
    parser.add_argument(
        "--output-path", "-o", type=str, help="Directory of output path"
    )
    args = parser.parse_args()

    random.seed(42)
    files = glob(os.path.join(args.processed_data, "*.hdf5"))
    random.shuffle(files)

    train_files = files[: int(0.8 * len(files))]
    val_files = files[int(0.8 * len(files)) : int(0.9 * len(files))]
    test_files = files[int(0.9 * len(files)) :]

    for fs, split in [(train_files, "train"), (val_files, "val"), (test_files, "test")]:
        save_dir = os.path.join(args.output_path, split)
        os.makedirs(save_dir, exist_ok=True)
        for f in fs:
            shutil.move(f, save_dir)
