import json

def second_exercise_json():
    with open('Others/Json/Exercise - Json 2/script-2.json') as json_file_2:
        load_dates = json.load(json_file_2)
        
        print(load_dates)
        print(type(load_dates))
second_exercise_json()