dft = [10, 10, 100, 10] # default (range, low, high, row)

## Non-unique random list (1d, 2d)
from random import randrange
def nu_rand1d(info=dft[:-1]):
    r, low, high = info # r: range
    return [randrange(low, high) for _ in range(r)]

def nu_rand2d(info=dft):
    *info_1d, rows = info
    return [nu_rand1d(info_1d) for _ in range(rows)]

# Unique random list (1d, 2d)
from random import sample
def u_rand1d(info=dft[:-1]):
    r, low, high = info # r: range
    return sample(range(low, high), r) # unique sample

def u_rand2d(info=dft):
    *info_1d, rows = info
    return [u_rand1d(info_1d) for _ in range(rows)]

# Unique random string list
def randstr(length):
    alphanum = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    return sample(alphanum, length)

## Test
# rdict = {"nu_rand1d": nu_rand1d, "nu_rand2d": nu_rand2d, "u_rand1d": u_rand1d, "u_rand2d": u_rand2d}
# cases = {"1d": [5, 15, 25], "2d": [8, 11, 30, 5]}
# def rdict_test():
#     c1d, c2d = cases.values() # get test cases
#     for name, func in rdict.items() # loop thru functions:
#         print(f"{name} -----------------------------------------")
#         if "1d" in name:
#             print(f"default: {func()}", 
#                   f"rand: {func(c1d)}", sep = "\n")
#         elif "2d" in name:
#             print(f"default:")
#             for row in func(): 
#                 print(row)
                
#             print(f"rand:")
#             for row in func(c2d): 
#                 print(row)
#         print()
# rdict_test()