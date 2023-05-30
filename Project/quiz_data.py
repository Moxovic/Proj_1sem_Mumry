import requests

response = requests.get(url="https://opentdb.com/api.php?amount=45&category=22&difficulty=medium&type=multiple")
question_data = (response.json()["results"])
print(question_data)
