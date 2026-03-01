import numpy as np

def FizzBuzz(start, finish):
    nums = np.arange(start, finish + 1)
    result = nums.astype(object)

    mask3 = nums % 3 == 0
    mask5 = nums % 5 == 0

    result[mask3] = "fizz"
    result[mask5] = "buzz"
    result[mask3 & mask5] = "fizzbuzz"

    return result
