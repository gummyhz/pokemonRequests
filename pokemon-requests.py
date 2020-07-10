import requests
import json

# 1. Make a GET request to https://pokeapi.co/api/v2/pokemon?limit=151
#   This page has the first 151 pokemon
#   Take some time to explore the website, Think about how you can get the data
### Goal : get names & abilities of the 1st 151 pokemon ###
request = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151')

# 2. Make your response readable
request_json = request.json()

# 3. Create an empty list that you will put your data into
dataList = []
# 4. Loop through all of the 151 pokemon
for pokemon in request_json['results']:
    # 5. Get the name of the pokemon
    name = pokemon['name']
    # 6. Get the link to the additional info
    link = pokemon['url']
    # 7. Make a GET request to the link
    moreInfo = requests.get(link)
    # 8. Make your response readable
    moreInfo = moreInfo.json()
    # 9. Get the ability of the pokemon
    #    Hint: If you are having trouble finding the ability, explore the data in your browser.
    #    Trial and error is your friend.
    abilities = moreInfo['abilities']
    abilitiesList = []
    for ability in abilities:
        abilitiesList.append(ability['ability']['name'])

    # 10. Append a dictionary to the list with the name and the ability of the pokemon
    dataList.append({'name': name, 'abilities': abilitiesList})

# 11. Loop through your list and print the name of the pokemon and their ability
for item in dataList:
    print(item['name'], ":", item['abilities'])
