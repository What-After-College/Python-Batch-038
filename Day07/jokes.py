import requests

url = "https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,religious,racist,sexist"

response = requests.get(url)

# print(response)

recieve_data = response.json()

# print(recieve_data)

# print(type(recieve_data))

for x in recieve_data.keys():
    if x == 'id' or x == 'flags' or x=='type' or x == 'error':
        continue
    print("{} : {}".format(x,recieve_data[x]))