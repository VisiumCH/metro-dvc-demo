"""mnist dataset."""

import pathlib
import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np

# TODO(mnist): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
Description is **formatted** as markdown.

It should also contain any processing which has been applied (if any),
(e.g. corrupted example skipped, images cropped,...):
"""

# TODO(mnist): BibTeX citation
_CITATION = """
"""
_MNIST_IMAGE_SIZE = 28
MNIST_IMAGE_SHAPE = (_MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
MNIST_NUM_CLASSES = 10

class MyMnist(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for mnist dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
      return tfds.core.DatasetInfo(
          builder=self,
          description=("The MNIST database of handwritten digits."),
          features=tfds.features.FeaturesDict({
              "image": tfds.features.Image(shape=MNIST_IMAGE_SHAPE),
              "label": tfds.features.ClassLabel(num_classes=MNIST_NUM_CLASSES),
          }),
          supervised_keys=("image", "label"),
          homepage="http://yann.lecun.com/exdb/mnist/",
          # fileFormat="",
          citation="",
      )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(mnist): Downloads the data and defines the splits
    # data_url = get_url("images/mnist/data", repo="https://github.com/VisiumCH/metro-dvc-demo")


    # Make use of dvc to get the data instead of dl_manager
    data_path = pathlib.Path(__file__).parent.absolute() / "data"
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                num_examples=60_000,
                data_path=f"{data_path}/train-images-idx3-ubyte",
                label_path=f"{data_path}/train-labels.idx1-ubyte",
            )),
        tfds.core.SplitGenerator(
            name=tfds.Split.TEST,
            gen_kwargs=dict(
                num_examples=10_000,
                data_path=f"{data_path}/t10k-images.idx3-ubyte",
                label_path=f"{data_path}/t10k-labels.idx1-ubyte",
            )),
    ]


  def _generate_examples(self, num_examples, data_path, label_path):
    """Generate MNIST examples as dicts.
    Args:
      num_examples (int): The number of example.
      data_path (str): Path to the data files
      label_path (str): Path to the labels
    Yields:
      Generator yielding the next examples
    """
    images = _extract_mnist_images(data_path, num_examples)
    labels = _extract_mnist_labels(label_path, num_examples)
    data = list(zip(images, labels))

    # Using index as key since data is always loaded in same order.
    for index, (image, label) in enumerate(data):
      record = {"image": image, "label": label}
      yield index, record


def _extract_mnist_images(image_filepath, num_images):
  with tf.io.gfile.GFile(image_filepath, "rb") as f:
    f.read(16)  # header
    buf = f.read(_MNIST_IMAGE_SIZE * _MNIST_IMAGE_SIZE * num_images)
    data = np.frombuffer(
        buf,
        dtype=np.uint8,
    ).reshape(num_images, _MNIST_IMAGE_SIZE, _MNIST_IMAGE_SIZE, 1)
    return data

def _extract_mnist_labels(labels_filepath, num_labels):
  with tf.io.gfile.GFile(labels_filepath, "rb") as f:
    f.read(8)  # header
    buf = f.read(num_labels)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    return labels