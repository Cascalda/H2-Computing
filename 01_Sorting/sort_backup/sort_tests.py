from sort_backup.randlst_gen import nu_rand1d as randlst
def sort_Test(sorts):
    # Create random nums, and valid sort
    nums = randlst()
    valid = sorted(nums)
    print(f"nums: {nums}",
          f"Valid: {valid}", 
          sep = "\n", end = "\n\n")
    
    # Sort the nums
    for func_name, sort in sorts.items():
        result = sort(nums.copy())
        print(f">>> {func_name}: {result}",
              f"{result == valid}",
              sep = " | ")
        
    