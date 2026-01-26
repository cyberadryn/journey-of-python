import requests

def get_pokemon():
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    response = requests.get(url)
    r = response.json()
    print(f"Name:" + r['name'])
    print(f"Weight:" + str(r['weight']))
    # return r.keys()


def main():
    status = get_pokemon()
    print(f"\nStatus code: {status}")


main()
