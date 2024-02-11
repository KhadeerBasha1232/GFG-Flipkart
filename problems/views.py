from django.shortcuts import render

# Create your views here.
# views.py
import os
import json
from django.shortcuts import render

def search_flipkart(request):
    folder_path = './flipkart_sub'  # Update this with the actual path
    solutions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            problem_name, submission_id = filename.rsplit('_', 1)
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    response_data = json.load(file)
                    if response_data.get('status') == "1" or response_data.get('status') == '0':
                        code = response_data.get('user_code')
                        lang = response_data.get("language")
                        status = "Correct" if response_data.get('status') == '1' else "Error"
                        solution = {
                            'problem_name': problem_name,
                            'lang':lang,
                            'status':status,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'flipkart_solution.html', {'solutions': solutions})


def search_microsoft(request):
    folder_path = './microsoft_sub'  # Update this with the actual path
    solutions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            problem_name, submission_id = filename.rsplit('_', 1)
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    response_data = json.load(file)
                    if response_data.get('status') == "1" or response_data.get('status') == '0':
                        code = response_data.get('user_code')
                        lang = response_data.get("language")
                        status = "Correct" if response_data.get('status') == '1' else "Error"
                        solution = {
                            'problem_name': problem_name,
                            'lang':lang,
                            'status':status,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'microsoft_solution.html', {'solutions': solutions})

def search_google(request):
    folder_path = './google_sub'  # Update this with the actual path
    solutions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            problem_name, submission_id = filename.rsplit('_', 1)
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    response_data = json.load(file)
                    if response_data.get('status') == "1" or response_data.get('status') == '0':
                        code = response_data.get('user_code')
                        lang = response_data.get("language")
                        status = "Correct" if response_data.get('status') == '1' else "Error"
                        solution = {
                            'problem_name': problem_name,
                            'lang':lang,
                            'status':status,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'google_solution.html', {'solutions': solutions})


def search_amazon(request):
    folder_path = './amazon_sub'  # Update this with the actual path
    solutions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            problem_name, submission_id = filename.rsplit('_', 1)
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    response_data = json.load(file)
                    if response_data.get('status') == "1" or response_data.get('status') == '0':
                        code = response_data.get('user_code')
                        lang = response_data.get("language")
                        status = "Correct" if response_data.get('status') == '1' else "Error"
                        solution = {
                            'problem_name': problem_name,
                            'lang':lang,
                            'status':status,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'amazon_solution.html', {'solutions': solutions})


def search_must(request):
    folder_path = './mustdo_sub'  # Update this with the actual path
    solutions = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            problem_name, submission_id = filename.rsplit('_', 1)
            with open(os.path.join(folder_path, filename), 'r') as file:
                try:
                    response_data = json.load(file)
                    if response_data.get('status') == "1" or response_data.get('status') == '0':
                        code = response_data.get('user_code')
                        lang = response_data.get("language")
                        status = "Correct" if response_data.get('status') == '1' else "Error"
                        solution = {
                            'problem_name': problem_name,
                            'lang':lang,
                            'status':status,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'must_solution.html', {'solutions': solutions})


def index(request):
    return render(request,"index.html")