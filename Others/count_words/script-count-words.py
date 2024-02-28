def exercise_count_words():
    count_words = 0
    
    while count_words < 5:
        count_words += 1
        word = str(input("Enter Word: "))
        print(f"Count words...{count_words}")
        print(f"Word: {word}")
exercise_count_words()