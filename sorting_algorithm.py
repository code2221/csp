import random
import string
import time

def random_string(length):
    new_string = ""
    for i in range(length):
        new_string += random.choice(string.ascii_letters)
    return new_string

def mutate_string(rand_string):
    new_string = ""
    indexes = [random.randrange(0,len(rand_string)) for n in range(0,len(rand_string)//100)]
    for i in range(len(rand_string)):
        if i in indexes:
            new_string += random.choice(string.ascii_letters)
        else:
            new_string += rand_string[i]
    return new_string

def mutated_list(count, length):
    string_list = []
    string_list.append(random_string(length))
    for i in range(1,count):
        string_list.append(mutate_string(string_list[-1]))
    return string_list

def bubble_swap_sort(list, verbose = False):
    sorted = False
    while not sorted:
        if verbose:
            print(list)
        sorted = True
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sorted = False
    return list

def binary_search(sorted_list, target): 
    minimum = 0
    maximum = len(sorted_list)-1
    while minimum<maximum: 
        index = (minimum+maximum)//2
        guess = sorted_list[index]
        if target == guess:
            return index
        elif target < guess:
            maximum = index-1
        else:
            minimum = index+1
    if target < sorted_list[minimum]:
        return minimum-0.5
    elif target >sorted_list[maximum]:
        return maximum+0.5
    else:
        return minimum+0.5
    
def insertion_sort(list, verbose = False):
    if verbose:
        print(list)
    sorted_list = [list[0]]
    for item in list[1:]:
        if verbose:
            print(sorted_list)
        index = binary_search(sorted_list,item)
        sorted_list = sorted_list[:int(index//1)+1]+[item]+sorted_list[int(index//1)+1:]
    return sorted_list

def insertion_sort_fast(lst, verbose=False):
    sorted_list = [lst[0]]
    for item in lst[1:]:
        low = 0
        high = len(sorted_list)
        while low < high:
            mid = (low + high) // 2
            if sorted_list[mid] < item:
                low = mid + 1
            else:
                high = mid
        sorted_list.insert(low, item)
    return sorted_list

def merge(list1,list2):
    index1 = 0
    index2 = 0
    list = []
    while index1 < len(list1) and index2<len(list2):
        if list1[index1] < list2[index2]:
            list.append(list1[index1])
            index1+=1
        else:
            list.append(list2[index2])
            index2+=1
    list += list1[index1:]+list2[index2:]
    return list

def merge_sort(list, verbose = False):
    lists = [[item] for item in list]
    while len(lists) > 1:
        n = 0
        while n < len(lists)-1:
            if verbose:
                print(lists)
            lists[n] = merge(lists[n],lists[n+1])
            lists = lists[:n+1]+lists[n+2:]
            n += 1
    return lists[0]

def time_sorting_function(func, count, complexity):
    print("Generating data to be sorted")
    list = mutated_list(count, complexity)
    print("Starting Sorting Algorithm")
    start_time = time.perf_counter()
    sorted_list = func(list)
    end_time = time.perf_counter()
    elapsed_time = end_time-start_time
    print(f"Time to completion: {elapsed_time:.6f} seconds")

counts = [100, 500, 1000, 2500, 5000, 10000]
complexity = 2000

for c in counts:
    print(f"\nCount = {c}")
    time_sorting_function(bubble_swap_sort, c, complexity)
    time_sorting_function(insertion_sort, c, complexity)
    time_sorting_function(merge_sort, c, complexity)
    time_sorting_function(sorted, c, complexity)
    time_sorting_function(insertion_sort_fast, c, complexity)


