# Memory Profiling

Being aware of the memory usage can lead to two scenarios:
* You can find ways to reduce memory usage by writing more efficient code.
* You can use more ram in order to save on CPU time, e.g. by using caching

## Disclaimer

Memory profiling is not as clear-cut as cpu usage.

One reason for that is that memory usage is affected by the timings of garbage collection which are not deterministic. Thus,
the results for individual lines should not be overrated. Instead, it should be used to find trends in your application.

As second disclaimer: The code example we have investigated so far is not really fun to memory profile. On the one hand,
it comes with a significant runtime overhead of up to two orders of magnitude. So, unless you are willing to wait 2 hours
for the result you will have to reduce the complexity by reducing the `width`. BUT, with reduced complexity, you also hardly
see any impact on the allocated memory.

Thus, another example was added that is actually fun to profile, i.e. you see things happening, called `fun_profiling.py`. It
is suggested to use this one.

## Installation

* `uv pip install memory_profiler`
* and if you want to speed up profiling `uv pip install psutils`

## Execution

There are two ways to employ the `memory_profiler`.

### Line by line profiling
First, you can annotate a function you are interested with the `profile` decorator, but do *not* import that one from the
`memory_profiler` package. The function will be injected by the memory profiler. Run with

First, you can annotate a function you are interested with the `profile` decorator from the `memory_profile` package. Run with

```shell
python -m memory_profiler main.py
```

and you will see an output similar to the one provided by line_profiler for every time the function is executed

The most interesting columns of the output are `Mem usage` and `Increment`. Where `Mem usage` showed the memory used 
by the process after this line and `Increment` indicates the change in memory usage.

At the time of this writing, there was a bug in the `memory_profiler` which lead to incorrect values shown in the `Increment` 
column. There would be discrepancies compared to the `Mem usage` column.

### Memory profiling over time

Instead of profiling individual functions, the `memory_profiler` also offers the option to track the overall memory usage
over time. 

The runtime impact here is much smaller compared to the decorator approach. It is recommended to remove the decorator because
it seems to mess with the result. See `fun_profiling_mprof.py`.

In order to run it use `mprof run fun_profiling_mprof.py` which will create an `mprofile_*.dat` file which you can view with `mprof plot`.
Should the plotting result in a warning, then use `mprof plot --out profile.png` which should create a file you can look at.

#### More details in the graph

One problem with the graph is that it does not properly show where a function starts and where it ends. Of course, in our
example it is relatively clear but in more complex examples you might want to see the contribution of a specific function
to the overall memory usage.

For that you can annotate the function in interest with `profile` decorator, but do *not* import it from the `memory_profiler`
package. This might lead to your IDE complaining, but the function will be injected at runtime by the memory profiler. See,
`fun_profiling_mprof_details.py`.

You are even able to mark specific pieces of code with a context manager `profile.timestamp`. Be aware that the provided
labels must not contain spaces!

As above, use `mprof run` and `mprof plot` again.