"""Octane dataset."""

import pathlib
import tensorflow_datasets as tfds
import tensorflow as tf
import numpy as np
import scipy.io

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

class Octane(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Octane dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
      return tfds.core.DatasetInfo(
          builder=self,
          description=("Some Octane data."),
          features=tfds.features.FeaturesDict({
              "data": tfds.features.Tensor(shape=(226,), dtype=tf.float64),
              "label": tfds.features.Tensor(shape=(1,), dtype=tf.float64),
          }),
          supervised_keys=("data", "label"),
          citation="",
      )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(mnist): Downloads the data and defines the splits
    # data_url = get_url("images/mnist/data", repo="https://github.com/VisiumCH/metro-dvc-demo")

    # Make use of dvc to get the data instead of dl_manager
    data_path = pathlib.Path(__file__).parent.absolute() / "data/raw"
    return [
        tfds.core.SplitGenerator(
            name=tfds.Split.TRAIN,
            gen_kwargs=dict(
                data_path=f"{data_path}/octane.mat",
            )),
    ]


  def _generate_examples(self, data_path):
    """Generate MNIST examples as dicts.
    Args:
      num_examples (int): The number of example.
      data_path (str): Path to the data files
      label_path (str): Path to the labels
    Yields:
      Generator yielding the next examples
    """

    mat = scipy.io.loadmat(data_path)

    X = mat["X"]
    y = mat["y"]

    # Using index as key since data is always loaded in same order.
    for index, (data, label) in enumerate(zip(X, y)):
      record = {"data": data, "label": label}
      yield index, record

