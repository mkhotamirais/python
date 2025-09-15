# Function
# Function: block code yang hanya akan dijalankan saat dipanggil, bisa menerima parameter dan mengembalikan nilai
def fn1(): print("fn1 dipanggil")
# fn1()                               # memanggil function

# Jumlah parameter dan argumen harus sama agar tidak error
def fn2(x, y): return x + y
# print(fn2(5, 4))                       # memanggil function dengan parameter

# Jika tidak tahu jumlah argumen, bisa menggunakan arbitrary arguments *args (tuple) atau **kwargs (dictionary)
def fn3(*args): return sum(args)
def fn4(**kwargs): return kwargs
# print(fn3(1, 2, 3, 4, 5))              # memanggil function dengan arbitrary arguments
# print(fn4(a=1, b=2, c=3))              # memanggil function dengan arbitrary keyword arguments

# Default parameter
def fn5(x, y, z=10): return x + y + z
# print(fn5(1, 2))                       # memanggil function dengan default parameter, harus diakhir

# Positional-Only Arguments (hanya bisa diisi parameter selain key value) and Keyword-Only Arguments (hanya bisa diisi parameter key value)
def fn6(a, b, /, x, y, z): return a + b + x + y + z
# print(fn6(1, 2, 3, 4, z=5))                # memanggil function dengan positional-only arguments
def fn7(a, b, *, x, y, z): return a + b + x + y + z
# print(fn7(1, 2, x=3, y=4, z=5))            # memanggil function dengan keyword-only arguments
def fn8(a, b, /, *, x, y, z): return a + b + x + y + z
# print(fn8(1, 2, x=3, y=4, z=5))            # memanggil function dengan positional-only arguments dan keyword-only arguments

# Recursion
def fn9(n):
    if n == 1: return 1
    return n * fn9(n - 1)
# print(fn9(4))                              # memanggil function dengan recursion 4! 4 permutasi


# Closure Concept in Python
# untuk memahami decorator dan lambda, kita perlu memahami closure terlebih dahulu.
# Closure adalah situasi dimana sebuah fungsi memiliki akses ke variabel di luar fungsi tersebut.
# Umumnya terjadi pada kondisi dimana fungsi di dalam fungsi lainnya.
# Variabel yang valuenya closure function akan memiliki argumen sesuai dengan yang dimiliki inner function.

def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func
var_closure = outer_func(10)
# print(var_closure(5))

# Decorator
def dec1(fn):
    def inner(): return fn().upper()
    return inner
@dec1
def fn10(): return "ahmad"
# print(fn10())

def dec2(fn):
    def inner(x): return fn(x).upper()
    return inner
@dec2
def fn11(x): return x
# print(fn11("ahmad"))

def dec3(fn):
    def inner(*args, **kwargs): return fn(*args, **kwargs).upper()
    return inner
@dec3
def fn12(x): return f"Hello {x}"
# print(fn12("ahmad"))

# Decorator with arguments
def dec4(n):
    def innerDec(fn):
        def inner():
            if(n == "upper"): return fn().upper()
            if(n == "lower"): return fn().lower()
        return inner
    return innerDec

@dec4("upper")
def fn13(): return "ahmad"
# print(fn13())

@dec4("lower")
def fn14(): return "AHMAD"
# print(fn14())

# Multiple Decorators
def dec5(fn):
    def inner(): return fn().upper()
    return inner
def dec6(fn):
    def inner(): return f"Hello {fn()}, have a great day!"
    return inner

@dec5
@dec6
def fn15(): return "ahmad"
# print(fn15())

# Preserving Function Metadata and Preserve Function Name with functools.wrap
import functools
def dec7(fn):
    # @functools.wraps(fn)
    def inner(): return fn()
    return inner

@dec7
def fn16(): return "ahmad"
# print(fn16.__name__) # mengembalikan "inner" jika tidak menggunakan @functools.wraps. Mengembalikan nama fungsi "fn16" jika menggunakan @functools.wraps


# Lambda Function

# lambda arguments: expression # lambda function dapat mengambil berapapun argumen tapi hanya punya satu expression
fn17 = lambda x, y: x + y
# print(fn17(1, 2))

# penulisan tanpa lambda
def fn18_a():
    def inner(x, y): return x + y
    return inner
fn18 = fn18_a()
# print(fn18(1, 2))

def fn19(x):
    return lambda y: x + y
fn20 = fn19(1)
# print(fn20(2))

