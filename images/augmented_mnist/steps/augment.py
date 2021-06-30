from pathlib import Path
import argparse
import os
import numpy as np

import tensorflow as tf

import glob



_MNIST_IMAGE_SIZE = 28
MNIST_IMAGE_SHAPE = (_MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)



def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

def _extract_mnist_labels(labels_filepath, num_labels):
	with tf.io.gfile.GFile(labels_filepath, "rb") as f:
		f.read(8)  # header
		buf = f.read(num_labels)
		labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
	return labels

def _extract_mnist_images(image_filepath, num_images):
	with tf.io.gfile.GFile(image_filepath, "rb") as f:
	    f.read(16)  # header
	    buf = f.read(_MNIST_IMAGE_SIZE * _MNIST_IMAGE_SIZE * num_images)
	    data = np.frombuffer(
	        buf,
	        dtype=np.uint8,
	    ).reshape(num_images, _MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
	return data

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--input', type=dir_path)
	parser.add_argument('--output')
	args = parser.parse_args()

	output_folder = Path(args.output)

	output_folder.mkdir(exist_ok=True)

	# augment test data
	data = _extract_mnist_images(Path(args.input) / "t10k-images.idx3-ubyte", 10_000)
	label = _extract_mnist_labels(Path(args.input) / "t10k-labels.idx1-ubyte", 10_000)

	data = 255 - data

	np.save(output_folder / "aug_test_data.npy", data)
	np.save(output_folder / "aug_test_labels.npy", label)

	# augment train data

	data = _extract_mnist_images(Path(args.input) / "train-images-idx3-ubyte", 60_000)
	label = _extract_mnist_labels(Path(args.input) / "train-labels.idx1-ubyte", 60_000)

	data = 255 - data

	np.save(output_folder / "aug_train_data.npy", data)
	np.save(output_folder / "aug_train_labels.npy", label)