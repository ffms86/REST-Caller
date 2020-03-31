import main_caller
import requests

try:
    response = main_caller.caller_get("htps://jsonplaceholder.typicode.com/todos/1", "", "", "")
    print(response.content)
except requests.exceptions.InvalidSchema as bad_url:
    print(bad_url)
