## Things to try

### Normal run of the application

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

