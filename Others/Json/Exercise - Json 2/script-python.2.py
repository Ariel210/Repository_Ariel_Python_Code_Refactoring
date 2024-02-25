import json

def second_exercise_json():
    with open('Others/Json/Exercise - Json 2/script-2.json') as json_file_2:
        load_dates = json.load(json_file_2)
        dumps_dates = json.dumps(load_dates)
        
        print(load_dates)
        print(type(load_dates))
        print(f"Dumps Method: {dumps_dates}")
        
        print("\n")
        
        for key in load_dates['diccionary_information'].keys():
            print(f"Keys of the diccionary: {key}")
        for values in load_dates['diccionary_information'].values():
            print(f"Values of the diccionary: {values}")
second_exercise_json()