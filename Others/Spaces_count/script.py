def exercise_spaces_count():
    spaces_count = 0
    phrase = str(input("Enter phrase: "))
    
    for space in phrase:
        if space == " ":
            spaces_count += 1
    print("Phrase: ", phrase)
    print("Spaces: ", spaces_count)
exercise_spaces_count()