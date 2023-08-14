## App Habit Tracker
import requests
from datetime import datetime

## creez un token si un username in vederea crearii userului
TOKEN = "fkpdskf0925oi345nknlmsao2"
USERNAME = "roxanastoicae"
GRAPH_ID = "graph2"

pixela_endpoint = "https://pixe.la/v1/users"

## Creez un user pe PIXELA
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

## Verific userul creat/profilul
response = requests.post(url=pixela_endpoint,json=user_params)
print(response.text)

## Creez un grafic nou pe PIXELA pentru userul de mai sus; ## Create a new pixelation graph definition.
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
# ## creez configuratia grafului (ajutandu-ma de documentatie) https://docs.pixe.la/entry/post-graph
graph_config = {
    "id":GRAPH_ID,
    "name": "MyLearningGraph",
    "unit": "lessons",
    "type": "float",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)
## The browser result is: https://pixe.la/v1/users/roxanastoicae/graphs/graph2.html

today = datetime.now()
today = today.strftime("%Y%m%d") ### https://www.w3schools.com/python/python_datetime.asp

yesterday = datetime(year=2023,month=8,day=13)
yesterday = yesterday.strftime("%Y%m%d")

print("today is: ",today)
print("yesterday is: ",yesterday)

pixel_config = {
    "date": today,
    "quantity": input("How many lessons did you learn today?"),
}

## creez ENDPOINT ul (adica UNDE voi posta ce am de postat:
url_graph = f'{graph_endpoint}/{GRAPH_ID}'

response = requests.post(url=url_graph,json=pixel_config,headers=headers)
# print(response.text)

## update pixel:
url_pixel = f'{url_graph}/{pixel_config["date"]}'
pixel_update = {
    "quantity": "2"
}
# response = requests.put(url=url_pixel,json=pixel_update, headers=headers)
# print(response.text)