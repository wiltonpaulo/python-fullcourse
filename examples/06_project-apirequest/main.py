import requests

response = requests.get("https://gitlab.com/api/v4/users/wpsilva/projects")

# print(response.json())
# print(type(response.json()))
# print(response.json()[0])

my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}")
    print(f"Path: {project['http_url_to_repo']}")
    print("")
