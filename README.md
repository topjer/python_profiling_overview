# Line Profiler

The line profiler is a great tool to further drill down on functions of which why know that they are costly. It is for 
example a great next step after having used cProfile to get a feeling for which function is the most expensive.

## Installation

In order to install it, use:
```shell
uv pip install line_profiler
```

## Usage

Before you can analyse, you have to annotate the functions you want to profile with the `@profile` decorator. Check `main.py`
to see the necessary changes.

Start an analysis via
```shell
kernprof -l -v main.py
```

Where `-l` indicates line-wise profiling and `-v` means to provide verbose output.

Profiling your code should lead to a noticeable increase in runtime. Here the profiling overhead becomes very apparent. During
my execution runtime went up from 3 seconds to 36 seconds.

### Output

You should receive output similar to:

```shell
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    55                                           @profile
    56                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    57                                               """Calculate output list using Julia update rule"""
    58         1       2260.4   2260.4      0.0      output = [0] * len(zs)
    59   1000001     295758.2      0.3      0.8      for i in range(len(zs)):
    60   1000000     254799.3      0.3      0.7          n = 0
    61   1000000     290054.1      0.3      0.8          z = zs[i]
    62   1000000     271560.4      0.3      0.8          c = cs[i]
    63  34219980   14814403.7      0.4     41.1          while abs(z) < 2 and n < maxiter:
    64  33219980   10761730.5      0.3     29.9              z = z * z + c
    65  33219980    9022288.2      0.3     25.1              n += 1
    66   1000000     296971.9      0.3      0.8          output[i] = n
    67         1          0.8      0.8      0.0      return output
```

As we can see, most time was spent on the while loop which was roughly 34 million times.

### timeit

Now is the time where you might want to further test the runtimes of individual statements, e.g. to see which statement
in the while condition is more expensive. Is it `abs(z) < 2` or `n < maxiter`?

For that purpose, we can use [timeit](https://docs.python.org/3/library/timeit.html#)

There are many ways to invoke `timeit` in we will look at the more esoteric ones.

#### Command line

We start with the [command line interface](https://docs.python.org/3/library/timeit.html#command-line-interface).

As a basic example, execute this in your shell:
```shell
$ python -m timeit "x = 1 + 1"
50000000 loops, best of 5: 8.25 nsec per loop
```

What has happened is that the statement `x = 1 + 1` was executed 50 million times, the overall time was measured and the
time for each execution was determined. If we want to see whether variable resolutions have some kind of impact, we can
first define variables and then use them. For that purpose, the flag `-s` can be provided to define setup statements which
are only executed *once*.

```shell
$ python -m timeit -s "a = 1; b = 1" "x = a + b"
20000000 loops, best of 5: 13.2 nsec per loop
```

As we can see, there is a significant "overhead" to variable resolution.

To see the impact of the setup statement, try running the following:

```shell
$ python -m timeit "a = 1; b = 1; x = a + b"
```

#### IPython

Another way of invoking - that is particularly handy if you work with jupyter notebooks a lot is via IPython.

Which you can install via
```shell
$ uv pip install ipython
```

and then start it with `ipython` in you shell. You are now in an interactive python interpreter. Now you can try something
like:
```shell
In [1]: z = 0+0j

In [2]: %timeit abs(z) < 2
44.8 ns ± 0.119 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
```

You might have already noticed, but `timeit` is a tool to be used for benchmarking and not for profiling purposes.
It can be used to determine the "cost" of individual pieces of code or to compare two different implementations. As such
it works complementary the line profiler which tells you which lines are expensive.