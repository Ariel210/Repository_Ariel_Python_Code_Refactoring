def exercise_bubbleSort_method():
    numbers_list = [20,53,45,2,12,4,8]
    
    print("1st Number list : ", numbers_list)
    number = 0
    
    for caracter in numbers_list:
        number += 1
        
    for i in range(number-1):
        for j in range(0, number-i-1):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1],numbers_list[j]
    
    print("The number list is: ", numbers_list)
exercise_bubbleSort_method()