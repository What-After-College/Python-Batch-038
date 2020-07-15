import requests
import json
import matplotlib.pyplot as plt

def get_pokemon_data(name="Raichu"):

    url = "https://api.pokemontcg.io/v1/cards?name={}".format(name)    
    response = requests.get(url)
    return response.json()

pokemon_name = input("Enter the name of Pokemon: ")
# print(get_pokemon_data(pokemon_name))

pokemon_data = get_pokemon_data(pokemon_name)

url_data = requests.get(pokemon_data["cards"][0]["imageUrl"])
with open('./poke.png','wb') as f:
    for item in url_data.iter_content(1024):
        f.write(item)

image_data = plt.imread('./poke.png')
plt.imshow(image_data)
plt.show()



