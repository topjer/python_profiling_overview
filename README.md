# Introduction

This repository aims to show different ways to profile Python applications. It covers different tools with different
areas of application, e.g. runtime measurements, memory utilization on program level or on level of an individual
line.

## How to use the repository

This repository consists of different branches which each focuses on a single tool. 

Go through each branch and checkout the README for a description of the tool.

## About the code itself

The piece of code we are profiling can be used to determine the Julia set for a specified complex point. 

It was taken from the book "High Performance Python, 3rd Edition" by Micha Gorelick and Ian Ozsvald

## Normal run of the application

In this branch, we want to run the code itself to get a feeling for the runtime.

In order to run the application, just call:
```
python main.py
```
you should see an output similar to:
```
Length of x: 1000
Total elements: 1000000
calculate_z_serial_purepython took 3.61 seconds
```

If you want to see the plot, then modify the call found in `main.py`:

```python
calc_pure_python(desired_width=1000, max_iterations=300, save_output=True)
```

Now run the code again and a png file should have been created called `julia.png`.

### Going deeper

If you want to, you can modify the values found on line 12
```python
c_real, c_imag = -0.62772, -.42193
```

and run the code again. With each change, the created image will be different.

Note also how runtime will change. There clearly is a correlation between amount of white areas and runtime, which
should be no surprise because the white areas need more iterations.

Here some recommended values to explore:
```python
c_real, c_imag = -0.5125, -.5213
c_real, c_imag = -0.4, -.6
c_real, c_imag = 0.285, .01
c_real, c_imag = 0.35, .35
```