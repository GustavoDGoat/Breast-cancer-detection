import gdown
import os


def download_weights():
    file_id = "1--7p9rRJy7WU4OmomkzM8i0veetZctTT"
    url = f"https://drive.google.com/uc?id={file_id}"
    output = "weights/modeldense1.h5"

    # Create directory if it doesn't exist
    if not os.path.exists("weights"):
        os.makedirs("weights")

    # Download only if the file isn't already there
    if not os.path.exists(output):
        print("Downloading model weights...")
        gdown.download(url, output, quiet=False)
    else:
        print("Weights already present. Skipping download.")

