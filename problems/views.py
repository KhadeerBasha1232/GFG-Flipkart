from django.shortcuts import render

# Create your views here.
# views.py
import os
import json
from django.shortcuts import render

def search_solution(request):
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

                        solution = {
                            'problem_name': problem_name,
                            'code': code,
                        }

                        solutions.append(solution)

                except json.JSONDecodeError:
                    print(f"Error decoding JSON in file: {filename}")
                except KeyError:
                    print(f"KeyError in file: {filename}")
    return render(request, 'search_solution.html', {'solutions': solutions})
