from functools import reduce, partial, wraps
from itertools import islice
from typing import Callable, Iterable, TypeVar, Optional, Tuple
from functools import reduce as _reduce

# functionalProgramming.py
# Several small examples of functional programming in Python


T = TypeVar("T")
U = TypeVar("U")

# 1) Pure functions
def pure_add(x: int, y: int) -> int:
    return x + y

def pure_factorial(n: int) -> int:
    # pure recursive implementation (no side effects)
    return 1 if n <= 1 else n * pure_factorial(n - 1)


# 2) map / filter / reduce usage
numbers = list(range(1, 11))
squares = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_of_numbers = reduce(lambda a, b: a + b, numbers, 0)


# 3) Higher-order functions
def apply_twice(f: Callable[[T], T], x: T) -> T:
    return f(f(x))

def compose(f: Callable[[U], T], g: Callable[..., U]) -> Callable[..., T]:
    # compose f(g(...))
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed


# 4) Currying and partial application
def add_three(a: int, b: int, c: int) -> int:
    return a + b + c

add_one_and_two = partial(add_three, 1, 2)  # fixes first two args


# 5) Closure example
def make_multiplier(n: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * n
    return multiplier


# 6) Generators & lazy evaluation (infinite Fibonacci)
def fib() -> Iterable[int]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

first_10_fib = list(islice(fib(), 10))


# 7) Immutability example using tuples
def pairwise_sum(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(map(lambda x_y: x_y[0] + x_y[1], zip(a, b)))


# 8) Simple Maybe/Option monad (to avoid None checks)
class Maybe:
    def __init__(self, value):
        self._value = value

    def map(self, fn: Callable[[T], U]) -> 'Maybe':
        if self._value is None:
            return Maybe(None)
        return Maybe(fn(self._value))

    def bind(self, fn: Callable[[T], 'Maybe']) -> 'Maybe':
        if self._value is None:
            return Maybe(None)
        return fn(self._value)

    def get_or(self, default: U) -> U:
        return self._value if self._value is not None else default

    def __repr__(self):
        return f"Maybe({self._value!r})"


# 9) Function decorator to memoize (pure function optimization)
def memoize(f: Callable) -> Callable:
    cache = {}
    @wraps(f)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = f(*args)
        cache[args] = res
        return res
    return wrapper

@memoize
def memo_fib(n: int) -> int:
    if n < 2:
        return n
    return memo_fib(n - 1) + memo_fib(n - 2)


# Demonstration prints (purely functional examples, no side effects except prints)
if __name__ == "__main__":
    print("numbers:", numbers)
    print("squares (map):", squares)
    print("evens (filter):", evens)
    print("sum (reduce):", sum_of_numbers)
    print("pure_factorial(5):", pure_factorial(5))

    print("apply_twice(lambda x: x+3, 7):", apply_twice(lambda x: x + 3, 7))
    inc = make_multiplier(1)  # trivial multiplier
    times3 = make_multiplier(3)
    print("times3(7):", times3(7))

    print("compose example (square ∘ inc):", compose(lambda x: x * x, lambda y: y + 1)(3))

    print("add_one_and_two(5):", add_one_and_two(5))
    print("first_10_fib (generator):", first_10_fib)
    print("memo_fib(30):", memo_fib(30))

    a = (1, 2, 3)
    b = (10, 20, 30)
    print("pairwise_sum:", pairwise_sum(a, b))

    # Maybe usage
    def safe_div(x: float, y: float) -> Maybe:
        if y == 0:
            return Maybe(None)
        return Maybe(x / y)

    result = Maybe(10).bind(lambda v: safe_div(v, 2)).map(lambda v: v * 5)
    print("Maybe pipeline result:", result.get_or("no result"))

    # function composition via reduce (left-to-right pipeline)
    pipeline = [lambda x: x + 1, lambda x: x * 2, lambda x: x - 3]
    pipeline_fn = lambda x: _reduce(lambda acc, fn: fn(acc), pipeline, x)
    print("pipeline applied to 5:", pipeline_fn(5))