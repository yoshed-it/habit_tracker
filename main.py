import requests
import datetime as dt


now_time = dt.datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

# URL="https://pixe.la/v1/users/yoshed-it/graphs/graph1.html"

TOKEN = "max_ignores_me505"
USERNAME = "yoshed-it"

user_params = {
    "token" : "max_ignores_me505",
    "username": "yoshed-it",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint =(f"{pixela_endpoint}/{user_params['username']}/graphs")

graph_config = {
    "id" : "graph1",
    "name" : "coding_graph",
    "unit" : "minutes",
    "type" : "int",
    "color" : "shibafu"
}
headers = {
    "X-USER-TOKEN" : TOKEN
    
}

pixel_config = {
    "date" : now_time,
    "quantity" : "1"    
}

response = requests.post(f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}", json=pixel_config, headers=headers)


print(response.text)


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)



