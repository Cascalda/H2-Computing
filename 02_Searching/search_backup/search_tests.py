from search_backup.randlst_gen import nu_rand1d as randlst

# >>> Quicksearching -----------------------------------------------------------------------------------------
def find(lst, item):
    return [i for (i, x) in enumerate(lst) if x == item]

# >>> Linear Search ------------------------------------------------------------------------------------------
from random import choice
def linear_search_Test(searches):
    # Make random list and choose a random item from it
    lst = randlst([20, 10, 100])
    item = choice(lst)
    print(f"item: {item}",
          f"lst: {lst}", 
          f"sorted: {sorted(lst)}", 
          sep = "\n", end = "\n\n")
    
    # Run through all the linear search functions
    for name, search in searches.items():
        
        # Sort the list if it is ordered linear search
        if name == "ordered_linear_search":
            lst.sort()
            
        item_at = search(lst, item)
        ans = find(lst, item)
        valid = (item_at == ans)
        print(f">>> {name}: {item_at}", 
              f"Expected: {ans}", 
              f"{valid}", 
              sep = " | ") # ans
        
# >>> Binary Search ------------------------------------------------------------------------------------------
def binary_search_Test(searches):
    # Make SORTED random list and choose a random item from it
    lst = sorted(randlst([20, 10, 100]))
    item = choice(lst)
    print(f"item: {item}",
          f"sorted: {lst}", 
          sep = "\n", end = "\n\n")
    
    # Run through all the binary search functions
    for name, search_function in searches.items():
        item_at = search_function(lst, item)
        ans = find(lst, item)
        valid = (item_at in ans)
        print(f">>> {name}: {item_at}", 
              f"Expected: {ans}", 
              f"{valid}", 
              sep = " | ") # ans
        
# >>> Hash Table Search --------------------------------------------------------------------------------------
from search_backup.randlst_gen import randstr
from random import randint
def hash_table_Test(HT):
    print(f">>> HashTable:")
    # Make keys and values
    r = randint(8, 15)
    keys = randlst([r, 10, 100])
    values = randstr(len(keys))
    print(f"Keys to enter: {keys}",
          f"Values to enter: {values}",
          f"Key-value pair: {list(zip(keys, values))}",   # display one list with key-value pair
          sep = "\n", end = "\n\n")
    
    # Initiate Hash Table
    H = HT(len(keys) - 2)
    
    # Put the key-value pair into Hash Table
    print("Put:")
    for i, (key, value) in enumerate(zip(keys, values)):
        print(f"Key: {key}",
              f"Status: {H.put(key, value)}",
              f"Load factor: {H.load_factor()}", 
              sep = " | ")
    print()
    print(f"Keys entered: {H._keys}",
          f"Values entered: {H._values}", 
          sep = "\n", end = "\n\n")
    
    # Get the values in Hash Table for each corresponding key
    print("Get:")
    for key in keys:
        print(f"Key: {key}",
              f"({H.get(key)})",
              sep = " | ")