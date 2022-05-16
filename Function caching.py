import time
from functools import lru_cache


@lru_cache(maxsize=2)
# When we used the decorator you can see that the same value is printed again without any time delay.
# Maximum number of values you will cache is stored in your memory.
def any_function(n):
    time.sleep(n)
    print("Executed.")


if __name__ == '__main__':
    print("Executing Function 1.")
    any_function(3)
    print("Executing Function 1 again...")
    any_function(3)
    print("Executing Function 2.")
    any_function(4)
# When the same function is called several times,then it would be stored in "cache memory" to optimise the work.
# We have to store the function(s) in the "cache memory" using a decorator called "lru_cache" from module "functools".
