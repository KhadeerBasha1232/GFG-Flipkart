import json
import time
from urllib.parse import urlparse
import requests
import pymysql.cursors

def get_cookies_from_api(session_id):
    api_url = f'https://api.softpage.tech/api/cookies/{session_id}'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            response_data = response.json()
            cookies = json.loads(response_data.get('cookies', '[]'))
            print("suuccessfully fetched cookies :- "+session_id)
            return cookies
        else:
            print(f"Failed to fetch cookies from the API. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching cookies: {e}")
        return None

def convert_cookies_to_dictionary(cookies_list):
    cookies_dict = {}
    for cookie in cookies_list:
        name = cookie.get('name')
        value = cookie.get('value')
        if name and value:
            cookies_dict[name] = value
    return cookies_dict

def extract_slug_from_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Get the path components
    path_components = parsed_url.path.split('/')

    # Find the index of 'track' in the path
    track_index = path_components.index('track') if 'track' in path_components else -1

    # Check if 'track' is present and there is a component after it
    if track_index != -1 and track_index < len(path_components) - 1:
        # Return the component after 'track' as the slug
        return path_components[track_index + 1]

    # Return None if 'track' is not found or there is no component after it
    return None


# Assuming you have a MySQL connection already established
# Make sure to replace the connection details with your own


def get_code_from_database(problem_name,connection, max_retries=5, retry_delay=3 ):
    retries = 0
    while retries < max_retries:
        try:
            with connection.cursor() as cursor:
                # Use parameterized query to avoid SQL injection
                sql = "SELECT code, user_code, language FROM gfg_codes WHERE name = %s"
                cursor.execute(sql, (problem_name,))
                result = cursor.fetchone()
                return result
        except pymysql.MySQLError as e:
            print(f"Error in database query: {e}")
            retries += 1
            if retries < max_retries:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"Maximum retries reached. Unable to fetch data from the database.")
                return None

def submit_problems(main_response, track_slug, cookies,delay ,connection):
    results = main_response.get("results", {})
    problems = results.get("problems", {}).get("results", [])
    track = track_slug
    batch_id = results.get("batch_id")
    track_id = results.get("track_id")

    submitted_problems = []
    non_submitted_problems = []
    for problem in problems:
        time.sleep(delay)
        slug = problem.get("slug")
        problem_name = problem.get("problem_name")
        print(f"Processing problem: {problem_name} - {slug}")
        if slug:
            api_url = f'https://practiceapiorigin.geeksforgeeks.org/api/latest/problems/{slug}/submit/compile/'

            # Search for code, user_code, and language based on problem_name
            code_info = get_code_from_database(problem_name,connection)

            if code_info:
                # Include the retrieved information in the payload
                payload = {
                    "source": "https://www.geeksforgeeks.org",
                    "request_type": "solutionCheck",
                    "userCode": code_info['user_code'],
                    "code": code_info['code'],
                    "language": code_info['language'],
                    "track": track,
                    "batch_id": batch_id,
                    "track_id": track_id
                }

                try:
                    response = requests.post(api_url, json=payload, cookies=cookies)

                    if response.status_code == 200:
                        print(f"Successfully submitted: {problem_name}")
                        submitted_problems.append((problem_name, "Submitted successfully"))
                    else:
                        print(f"Failed to submit {problem_name}. Status code: {response.status_code}")
                        non_submitted_problems.append((problem_name, f"Failed. Status code: {response.status_code}"))

                except Exception as e:
                    print(f"Error submitting {problem_name}: {e}")
                    non_submitted_problems.append((problem_name, f"Error: {e}"))

            else:
                non_submitted_problems.append((problem_name, "No code found in the database"))
        else:
            print("No slug Found")

    return submitted_problems, non_submitted_problems

def runner(url, session_id, delay):
    # Establish a new connection for each invocation of the runner function
    connection = pymysql.connect(
        host='13.232.45.191',
        port=3306,
        user='khadeer',
        password='khadeer12',
        database='gfg',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=100
    )

    try:
        cookies = get_cookies_from_api(session_id)
        success = []
        error = []
        if cookies is not None:
            cookies_dict = convert_cookies_to_dictionary(cookies)
            track_slug = extract_slug_from_url(url)
            url = f"https://practiceapi.geeksforgeeks.org/api/latest/tracks/{track_slug}/batch/cts-1/"
            response = requests.get(url, cookies=cookies_dict)
            main_response = response.json()
            success, error = submit_problems(main_response, track_slug, cookies_dict, delay, connection)
            return success, error
        else:
            print("Failed to fetch cookies.")
            return success, error
    finally:
        # Close the connection at the end of the function
        connection.close()