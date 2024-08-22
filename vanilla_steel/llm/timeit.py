import time
import functools

def timeit(func):
    """Decorator to print the execution time of the decorated function."""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # Start the timer
        value = func(*args, **kwargs)     # Execute the function
        end_time = time.perf_counter()    # End the timer
        run_time = end_time - start_time  # Calculate the duration
        print(f"Finished {func.__name__!r} in {run_time:.4f} seconds")
        return value
    return wrapper_timer