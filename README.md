
# Some notes

## Improvement Ideas

We could have a pure dvc repo to store raw data.

One dataset repo composed of multiple git submodule where each submodule is actually a dataset.

   - Each of the dataset would be composed of a dvc pipeline that takes as input the raw data from the pure dcv repo
   And the output of the last layer would be the generation of the tfrecods with the tfds cli.


Then each project which wants to use a dataset would simple add the corresponding git submodule as a dependency. And run `dvc run` in order to dl and augment the data (basically generate the tfrecords). The output the last step could be cached on a bucket as well for sharing.