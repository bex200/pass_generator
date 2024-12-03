
import requests
#* HTTP - запросы - запросы которых понимает сервер
#* SQL - запросы - понимает SQL
import json

BASE_URL = 'https://9d2f-95-59-159-206.ngrok-free.app'

def get_all_students():
    requests_to_server = requests.get(url=f'{BASE_URL}/students')
    #! СТАТУС ЗАПРОСА
    #! 404, 500, 502, 401, 200, 300
    if requests_to_server.status_code == 200:
        results = requests_to_server.json() #Превращаю непонятный для меня ответ из сервера в понятный формат JSON
        for each_result in results:
            print(
                f'ID: {each_result['id']}, Name: {each_result['name']}'
            )
    return "ALL DONE, GOOD JOB!"

# final = get_all_students()
# print(final)

def get_exact_student(student_id: int):
    requests_to_server = requests.get(url=f'{BASE_URL}/students/{student_id}')

    if requests_to_server.status_code == 200:
        student_info = requests_to_server.json()
        print(
            f'ID: {student_info['id']}',
            f'Name: {student_info['name']}',
            f'Age: {student_info['age']}',
            f'Grade: {student_info['grade']}',
        )
# get_exact_student(8)

def add_new_student(name, age, grade):
    student_data = {
        "name": name,
        "age": age,
        "grade": grade
    }
    response = requests.post(f"{BASE_URL}/create-student", json=student_data)
    if response.status_code == 201:
        print(response.json()['message'])
    else:
        print("Failed to add student!")

add_new_student('Batman', 21, 50)


# THESE ARE GET request - запросы для чтения