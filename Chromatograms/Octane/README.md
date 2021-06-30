
# Octane

## Description

Octane dataset from a `.mat` file


## How to use it

You first need to create a git + dvc project (in practise this should be done already for your project). See [here](https://github.com/VisiumCH/metrohm-dvc-demo) for an introduction on how to set-up a new project.


Then you can run the following command at the root of your project.

```bash
dvc import --rev octane git@github.com:VisiumCH/metrohm-dvc-demo.git Chromatograms/Octane
```
### Accessing the data using Python
You can now directly access the latest version of the data in python.

```python
import tensorflow_datasets as tfds

ds_train, ds_info = tfds.load(
    "octane",
    split="train",
    shuffle_files=True,
    as_supervised=True,
    with_info=True,
    data_dir="Octane/data/tensorflow_datasets"
)

print(ds_info)
```

### Accessing the data using the DVC CLI
You can download the latest version of the data directly by using the DVC CLI.
```bash
dvc pull
```

## Data Maintenance
In case of questions about the data, please refer to the data responsible.

Data Responsible: Charles Gallay, cg@visium.ch
 data_dir="augmented_mnist/data/tensorflow_datasets"
