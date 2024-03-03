def exercise_vocal_counts():
    word = str(input("Enter word: "))
    vocal_count = 0
    
    for letter in word:
        if letter in "aeiouAEIOU":
            vocal_count += 1
    print("Word: ", word)
    print("Vocal Count: ", vocal_count)
exercise_vocal_counts()