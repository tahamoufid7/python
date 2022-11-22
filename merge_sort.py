def merge_sort(unsorted_list):
    number_of_items = len(unsorted_list)

    if number_of_items <= 1:
        return unsorted_list
    else:
        #Slit list into two halves
        middle_index = number_of_items // 2
        unsorted_first_half = unsorted_list[0 : middle_index]
        unsorted_second_half = unsorted_list[middle_index : number_of_items]

        #Sort each half
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



        