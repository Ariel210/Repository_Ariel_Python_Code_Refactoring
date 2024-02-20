def first_exercise_json():
    with open('Others\Json\script-1.json', 'r') as json_file:
        read_dates_json = json_file.read()
        print(read_dates_json)
first_exercise_json()