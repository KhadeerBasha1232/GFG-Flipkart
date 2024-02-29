import threading
from django.shortcuts import redirect, render

# Create your views here.
# views.py
import os
import json
from django.shortcuts import render


running_threads_count = 0
threads_lock = threading.Lock()



# views.py

from django.http import JsonResponse

def get_running_threads_count(request):
    global running_threads_count
    return JsonResponse({'count': running_threads_count})


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




from .run import runner




from functools import partial


def run_and_store_results(request, url, sid, delay, success_list, error_list):
    global running_threads_count

    with threads_lock:
        running_threads_count += 1
    success, error = runner(url, sid, delay)
    success_list.extend(success)
    error_list.extend(error)
    with threads_lock:
            running_threads_count -= 1


def auto(request):
    if request.method == "POST":
        # Extracting form data
        url = request.POST.get('url')
        sid = request.POST.get('sid', '')  # Default to empty string if not provided
        delay = request.POST.get('delay')
        
        try:
            delay = int(delay)  # Ensure delay is an integer
        except ValueError:
            delay = 0

        # Lists to store success and error results
        success_list = []
        error_list = []

        # Create a thread to run the task asynchronously
        task_thread = threading.Thread(target=partial(run_and_store_results, request, url, sid, delay, success_list, error_list))
        task_thread.start()

        # Continue processing without waiting for the thread to finish

        # Render the template (without waiting for the thread to complete)
        return render(request, 'success.html')

    else:
        # Handle GET request
        return render(request, "auto_form.html")

