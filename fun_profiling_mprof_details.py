import numpy as np
from time import sleep

@profile
def random_number_average(seconds: int):
    sample_size = int(seconds * 10_000_000)
    # timestamp lables must not contain spaces
    with profile.timestamp("array_creation"):
        arr1 = np.random.randint(low=0, high=100, size=sample_size)
    sleep(seconds)
    return arr1.mean()

def main():
    res1 = random_number_average(0.5)
    res2 = random_number_average(1)
    res3 = random_number_average(0.8)
    print(f"Averages: {res1}, {res2}, {res3}")

if __name__ == "__main__":
    main()
