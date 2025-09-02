# Using unix time

We start off by using the time function provided by the operating system.

Here we are assuming, that your are on Linux, if that is not the case, then skip this branch.

## Run the code

Run the code with the following command

```shell
/usr/bin/time -p python main.py
```

which should give you and output like:

```shell
Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 3.62 seconds
real 4.26
user 5.24
sys 0.0
```

While the first 3 lines are familar to us, the latter 3 are new and we will thus take a closer look.

`real` is the actual time it took to run the command. It might be surprising that it indicates a different runtime
than the Python output. This is due to the fact that `time` timed the entire Python execution including things like
the startup time of the Python binary.

`sys` is the time spent in kernel level functions.

`user` records the time the CPU spent on the task. If you wonder how this can be a longer time than the total 
execution time, then try out the additional flag `--verbose`.

The verbose flag provides much more information, for example things like:
* `Percent of CPU this job got` which can be more than 100% when more than one CPU was involved. This also explains how `user` can be longer than `real`
* `Maximum resident set size (kbytes)` give the maximum memory utilization.
* `Major (requiring I/O) page faults` is also an interesting. It indicates that operating system had to load data from disk because it was not in RAM, which is slow.