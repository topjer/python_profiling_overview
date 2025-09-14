# Honourable mentions

This branch is dedicated to tools we want to investigate less deeply compared to the other ones, thus they do not get 
a dedicated branch.
Still, they seem worthwhile to be aware of.

# Scalene

Scalene is a combined CPU and memory profiler with an alleged low runtime overhead that 

It can be installed with `uv pip install scalene` and executed with `scalene main.py`.

Now your browser should open, showing the report.

The `TIME` column shows - as the name suggest - the runtime of you application, but splits it up into 3 categories:
* 'Python' refers to time spent executing Python instructions. This number can be affected by you.
* 'Native' refers to time spent in libraries. It will be hard to impact this time unless you reduce the number of calls
    to the library
* 'System' refers to time spent on operating system calls. Again, unlikely to optimize something here, but it can indicate
    I/O issues, which also count in this category.

The `MEMORY` column shows the peak memory usage per line.

Comments:
* You can restrict profiling to specific regions by using the decorator `@profile`. (You do not have to import this one, it will
    be injected at runtime.)
* Scalene offers to feature to get AI recommendations for single lines or entire sections of code
  * Be careful with this feature. The created recommendations can appear sensible but might be outdated. Always be skeptical.
* It is also possible to get an output only to the command line instead of in the browser. For that, use `--cli`

# PySpy

This tool inspects a running python process and reports in a `top`-like fashion. It is a sampling profiler and as such 
comes with very little overhead that can profile subprocesses and natively compiled extensions.

Install via `uv pip install py-spy`.

Run with:
* `py-spy top -- python main.py`
* `py-spy record -o profile.svg -- python main.py`

Can also be used to investigate running processes, but elevated rights are needed for that.

# Viztracer

(This might be the most complex tool compared to all the tools so far and we won't be able to do it justice. Thus we just
cover the bar minimum and leave the exploration to you.)

Viztracer can be used to record trace information of your application, i.e. the timing of every individual function call
that does not require code modifications. Concurrency and multiprocessing are also supported.

Install via `uv pip install viztracer`

Run with:
* `viztracer [...].py` -> a JSON will be generated
* view results with `vizviewer [...].json`

Recording the trace can lead to the creation of huge files. By default only a limited number of objects is tracked. 
If this limit is surpassed a "Circular Buffer is Full" error can occur and only the latest objects are stored.

To avoid, plenty of filtering options are provided, e.g. ignore all function calls that take less than X ms/ns etc.  