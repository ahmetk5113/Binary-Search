def binary_search():
    ordered_list = [0,1,2,3,4,5,6,7,8,9]

    lower_bound = 0
    upper_bound = 10
    
    item_f = int(input("please enter the number you want to find (1-10): "))
    t = True
    while t:
        if ordered_list[index] == item_f:
            print(f"number {item_f} is found at index position {index}")
            t = False
        elif item_f > ordered_list[index]:
            lower_bound = index + 1
        elif item_f < ordered_list[index]:
            upper_bound = index - 1
        index = int((lower_bound + upper_bound) / 2)
    if t == False:
        print("number found")
    else:
        pass
        
binary_search()


