from ds_backup.randlst_gen import u_rand1d as randlst

# >>> Linked List --------------------------------------------------------------------------------------------
# Linear (Singly-Linked)
from random import randint
def LLL_Test(LinearLinkedList):
    # Create random lists
    r = randint(15, 20)
    test = randlst([r, 10, 100])
    a, b = len(test) // 3, -3
    notinlst, inlst, after_empty = test[:a], test[a:b], test[b:]
    print(f"test: {test}",
          f"notinlst: {notinlst}",
          f"inlst: {inlst}",
          f"after_empty: {after_empty}",
          sep = "\n", end = "\n\n")
    
    # Create empty LLL 
    LLL = LinearLinkedList()
    print(">>> LLL:")
    
    # Put items from inlst into LLL, and sort LLL
    for num in inlst:
        LLL.insert(num)
        
    if hasattr(LLL, 'sort_it'):
        LLL.sort_it()
        
    print(f"Size: {LLL.size_of()}",
          f"Data (  ):      ",
          f"      ",
          f"LLL: {LLL.display()}",
          f"{LLL.display() == sorted(inlst)}", 
          sep = " | ", end = "\n\n")
    
    ## Test notinlst
    print("Not In List:")
    for num in notinlst:
        print(f"Size: {LLL.size_of()}",
              f"Data ({num}): {LLL.search(num)}",
              f"{LLL.delete(num)}",
              f"LLL: {LLL.display()}",
              sep = " | ")
    print()
    
    # Test inlst
    print("In List:")
    for num in inlst:
        print(f"Size: {LLL.size_of()}",
              f"Data ({num}): {LLL.search(num)}",
              f"{LLL.delete(num)}",
              f"LLL: {LLL.display()}",
              sep = " | ")
    print()
    
    # Test after_empty
    print("Empty:")
    for num in after_empty:
        print(f"Size: {LLL.size_of()}",
                  f"Data ({num}): {LLL.search(num)}",
                  f"{LLL.delete(num)}",
                  f"LLL: {LLL.display()}",
                  sep = " | ")
    
# >>> Stack --------------------------------------------------------------------------------------------------
def Stack_Test(Stack):
    # Create random list
    lst = randlst()
    print(f"List: {lst}", end = "\n\n")
    
    # Create Empty Stack
    S = Stack()
    print(">>> Stack:")
    print(f"Stack: {S.display()}", 
          f"Size: {S.size()}", 
          f"Top: {S.peek()}",
          sep = " | ", end = "\n\n")
    
    # Put items into stack
    for item in lst: 
        S.push(item)
    print(f"Top: {S.peek()}", 
          f"Stack: {S.display()}",
          sep = " | ", end = "\n\n")
    
    # Remove items from stack
    for _ in range(len(lst)): 
        print(f"Popped: {S.pop()}", 
              f"Top: {S.peek()}", 
              f"Size: {S.size()}", 
              f"Stack: {S.display()}",
              sep = " | ")

# >>> Queue --------------------------------------------------------------------------------------------------
# Linear
def LinearQueue_Test(LinearQueue):
    # Create random list
    lst = randlst()
    print(f"List: {lst}")
    
    # Create Empty LQ
    LQ = LinearQueue()
    print(">>> LQ:")
    print(f"LQ: {LQ.display()}",
          f"Size: {LQ.size()}",
          f"Front: {LQ.peek()}",
          sep = " | ", end = "\n\n")
    
    # Put items into LQ
    for item in lst: 
        LQ.enqueue(item)
    print(f"Front: {LQ.peek()}",
          f"LQ: {LQ.display()}",
          sep = " | ", end = "\n\n")
    
    # Remove items from LQ
    for _ in range(len(lst)): 
        print(f"Deq: {LQ.dequeue()}", 
              f"Front: {LQ.peek()}",
              f"Size: {LQ.size()}", 
              f"LQ: {LQ.display()}",
              sep = " | ")
        
# Circular
def CircularQueue_Test(CircularQueue):
    # Create random list
    nums = randlst() 
    print(f"List: {nums}", 
          sep = " | ", end = "\n\n")
    
    # Create Empty CQ with length less than lst
    len_CQ = len(nums) - 1
    CQ = CircularQueue(len_CQ)
    print(">>> CQ")
    print(f"Max_size: {CQ.max_size_of()}")
    print()
    
    # Headers and ALignment
    temp_headers = ["Status", "Size", "Head", "Tail", "Circular Queue"]
    headers = " | ".join(temp_headers)
    align_data = [len(_) for _ in temp_headers]
    
    # General display format
    def display(status):
        # Display data
        temp_display_data = [status, CQ.size_of(), CQ.head_at(), CQ.tail_at(), CQ.display()]
        display_data = [str(_) for _ in temp_display_data]
        
        # Make the headers / data on one line
        temp_line_data = []
        for display, align in zip(display_data, align_data):
            centered_display = display.center(align)
            temp_line_data.append(centered_display)
        line_data = " | ".join(temp_line_data)
        return line_data
    
    # Start
    print("---START", headers,
         sep = "\n")
    print(display(CQ.dequeue()))
    print()
        
    # Fill CQ completely
    print("---ENQUEUE", headers,
         sep = "\n")
    for num in nums:
        print(display(CQ.enqueue(num)))
    print()
    
    # Remove half of CQ
    mid = len_CQ // 2
    print("---DEQUEUE", headers,
         sep = "\n")
    for _ in range(mid):
        print(display(CQ.dequeue()))
    print()
    
    # Fill CQ back to full
    print("---ENQUEUE", headers,
         sep = "\n")
    for i in range(mid, len_CQ):
        print(display(CQ.enqueue(nums[i])))
    print()
    
    # Remove all in CQ
    print("---DEQUEUE", headers,
         sep = "\n")
    for _ in range(len_CQ):
        print(display(CQ.dequeue()))
    print()
    
    # End
    print("---END", headers,
         sep = "\n")
    print(display(CQ.dequeue()))
    
# >>> Binary Search Tree -------------------------------------------------------------------------------------
from random import randint, sample
def BinarySearchTree_Test(BinarySearchTree):
    # Create random list
    r = randint(5, 10)
    lst = randlst([r, 10, 100])
    print(f"List: {lst}", 
          f"Sorted: {sorted(lst)}",
          sep = "\n", end = "\n\n")
    
    # Create empty BST
    BST = BinarySearchTree()
    print(">>> BST:")
    
    # Put items into bst
    for item in lst:
        BST.put(item)
    print("AFTER INSERTION:",
          f"Size: {BST.size()} | {BST.size() == len(lst)}",
          f"Height: {BST.height()} | idk how to display this",
          f"Min: {BST.min_of()} | {BST.min_of() == min(lst)}",
          f"Max: {BST.max_of()} | {BST.max_of() == max(lst)}",
          sep = "\n", end = "\n\n")
    
    items = sample(lst, 5) + randlst([5, 10, 100]) # 5 confirm in list, 5 might be in list
    found = [BST.find(_) for _ in items]
    zipped = list(zip(items, found))
    inlst, notinlst = zipped[:5], zipped[5:] 
    print(f"Sampled from lst: {inlst} | {all(found[:5])}",
          f"Random: {notinlst}",
          sep = "\n", end = "\n\n")
    lst.sort()
    print(f"Inord: {BST.in_order()} | {lst == BST.in_order()}",
          f"Preord: {BST.pre_order()}",
          f"Postord: {BST.post_order()}",
          sep = "\n")