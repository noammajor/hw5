import json
import os



def names_of_registered_students(input_json_path, course_name):
    import json
    # Opening JSON file
    with open(input_json_path, 'r') as f:
         loaded_dict=json.load(f)
    # returns JSON object as
    # a dictionary
    values = [loaded_dict["student_name"] for key in loaded_dict.keys() if course_name in key["registered_courses"]]
    return values
    pass

def enrollment_numbers(input_json_path, output_file_path):
    with open(input_json_path, 'r') as f:
        loaded_dict=json.load(f)
        courses_dict = {}

        for student_id, info in loaded_dict.items():
            for course in info["registered_courses"]:
                if course in courses_dict:
                    courses_dict[course] += 1
                else:
                    courses_dict[course] = 1
        for key in sorted(courses_dict.items()):
            with open(output_file_path, 'w') as o:
                s1 = key + courses_dict[key]
                o.write(s1)

    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    pass



def courses_for_lecturers(json_directory_path, output_json_path):
    lecturers_dict = {}
    for pos_json in os.listdir(json_directory_path):
        if pos_json.endswith('.json'):
            with open(pos_json, 'r') as f:
                loaded_dict = json.load(f)
                for course_number, info in loaded_dict.items():
                    for lecturer in info["lecturers"].values():
                        if lecturer in lecturers_dict:
                            lecturers_dict[lecturer].append(info["course_name"])
                        else:
                            lecturers_dict[lecturer] = [info["course_name"]]
    with open(output_json_path, 'w') as o:
        json.dump(lecturers_dict, o, indent=4)




    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass



