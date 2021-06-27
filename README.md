
# Using the Metrohm Data Repository


## Further Improvement Ideas

We could have a pure dvc repo to store raw data.

One dataset repo composed of multiple git submodule where each submodule is a dataset.

   - Each of the datasets would be composed of a dvc pipeline that takes as an input the raw data from the pure dcv repo.
   The output of the last layer would be the generation of the tfrecods with the tfds cli.


Each time one would like to use a dataset within a project one would simply add the corresponding git submodule as a dependency. The command `dvc run` would download and augment the data (basically generate the tfrecords). The output of the last step could be cached on a bucket as well for sharing and speed up the processing.
