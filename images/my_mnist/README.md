# My MNIST

## Description

This dataset is a copy of the famous MNIST dataset.


## How to use it!

In order to and use this dataset within a already created git + dvc project, run this command at the root of the project.

```bash
dvc import git@github.com:VisiumCH/metrohm-dvc-demo.git images/my_mnist
```

In your python code you can now use the Dataset this way.

```python
import my_mnist
import tensorflow_datasets as tfds

(ds_train, ds_test), ds_info = tfds.load(
    "my_mnist",
    split=["train", "test"],
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
)

print(ds_info)
```