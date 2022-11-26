def merge_sort(unsorted_list):
    '''Takes an unsorted list and sorts it in ascending order using the recursive merge sort algorithm'''
    number_of_items = len(unsorted_list)

    #Stopping condition
    if number_of_items <= 1:
        return unsorted_list
    else:
        #Slit list into two halves
        middle_index = number_of_items // 2
        unsorted_first_half = unsorted_list[0 : middle_index]
        unsorted_second_half = unsorted_list[middle_index : number_of_items]

        #Sort each half by recursively calling merge_sort() on them
        sorted_first_half = merge_sort(unsorted_first_half)
        sorted_second_half = merge_sort(unsorted_second_half)
        
        #Merge the two halves
        length_of_first_half = len(sorted_first_half)
        length_of_second_half = len(sorted_second_half)
        
        first_half_index = 0
        second_half_index = 0

        sorted_list = []

        while first_half_index < length_of_first_half and second_half_index < length_of_second_half:
            if sorted_first_half[first_half_index] <= sorted_second_half[second_half_index]:
                sorted_list.append(sorted_first_half[first_half_index])
                first_half_index += 1
                continue
            else:
                sorted_list.append(sorted_second_half[second_half_index])
                second_half_index += 1
                continue
        
        while first_half_index < length_of_first_half:
            sorted_list.append(sorted_first_half[first_half_index])
            first_half_index += 1

        while second_half_index < length_of_second_half:
            sorted_list.append(sorted_second_half[second_half_index])
            second_half_index += 1

        return sorted_list

def quick_sort(unsorted_list):
    '''Takes an unsorted list and sorts the items in ascending order using the recursive quick sort algorithm.'''
    number_of_items = len(unsorted_list)

    #Stopping condition
    if number_of_items <= 1:
        return unsorted_list
    else:
        #Choose the pivot near the middle of the list
        pivot_index = (number_of_items - 1) // 2

        #Divide the unsorted list into three sublists
        greater_than = []
        equal_to = []
        less_than = []

        for item in unsorted_list:
            if item > unsorted_list[pivot_index]:
                greater_than.append(item)
            elif item < unsorted_list[pivot_index]:
                less_than.append(item)
            else:
                equal_to.append(item)
        
        #Recursively call quick_sort() on each of the three sublists
        return quick_sort(less_than) + equal_to + quick_sort(greater_than)

def bubble_sort(unsorted_list):
    '''Takes an unsorted list and sorts the items in ascending order using the bubble sort algorithm.'''
    last_sorted_index = len(unsorted_list)

    #Assume the list is not sorted
    sorted = False

    while sorted != True:
        #Once sorting has begun, set the sorted flag to True in order to break out of the loop at the next iteration unless a swap is made
        sorted = True
        for index in range(last_sorted_index - 1):
            #If a number in the list is greater than the number on its right, swap the two numbers and set the sorted flag to False to trigger another iteration of the loop
            if unsorted_list[index] > unsorted_list[index + 1]:
                sorted = False
                unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1], unsorted_list[index]
        #At every iteration, the largest unsorted number is moved to the right of the list. The rightmost portion of the list is sorted and does not need to be revisited
        last_sorted_index -= 1

    return unsorted_list

def is_sorted(sorted_list):
    '''Takes in a list and traverses the list comparing adjacent elements to ensure each element less than the following one.'''
    length_of_list = len(sorted_list)

    for index in range(length_of_list - 1):
        if sorted_list[index] > sorted_list[index + 1]:
            return False

    return True

        