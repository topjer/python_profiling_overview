# cProfile

Is a built-in, deterministic [profiler for Python](https://docs.python.org/3/library/profile.html#module-cProfile).

## Profiling vs benchmarking

There is an important difference between profiling and benchmarking.

Profiling tells you how much time is spent in the individual parts of your code, i.e. how much time is spent in a 
specific function in relation to other functions. So it can be used to make statements like: "20% of the runtime is 
spent in function X".

Benchmarking is when you want to determine the exact time a program ran.

cProfile can be used for profiling purposes but should not be used for benchmarking purposes because it creates overhead
and increases overall runtime.

## Execution

Run

```shell
python -m cProfile -s cumulative main.py | head -20
```

The output of `cProfile` can be quite lengthy, thus we added the flag `-s cumulative` which sorts the output in
descending order by cumulative time, i.e. the total time spent within a function.

The pipe to `head -20` is there to only show the first 20 lines of the output.

The following columns of the output are of interest:
* `ncalls` number of times the function is called.
* `tottime` actual time spent in the function (excluding subcalls)
* `cumtime` time spent in the function including subcalls

### Notes

* Note the runtime overhead introduced by cProfile. Compare to runtimes in master branch
* A single call to the `abs` function is negligible but because we call it over 34 million times we do spent a noticeable amount of time in it.

## Generate output

If you want to further explore the output of `cProfile` you can export the results into a dedicated file and use another tool for the
investigation.

```shell
python -m cProfile -o out.prof main.py
```

In order to open the profile output, you can use a tool like
* [snakeviz](https://jiffyclub.github.io/snakeviz/)
* [tuna](https://github.com/nschloe/tuna)

While snakeviz provides more features than tuna, the latter claims that the results are more reliable than snakeviz. Still it
is worth trying out both tools for yourself. See whether you can find any inconsistencies in the output of snakeviz.

So we will focus on Tuna for now.

Install it with
```shell
uv pip install tuna
```

and look at the previously generated output with

```shell
tuna out.prof
```

Now your browser should open up and show the call stack as a bunch of boxes where the size of the box indicates
the overall time spent in this function. This helps you to visualize where all the time is spent during the 
execution of your program.
Unfortunately, tuna does not display the number of function calls.