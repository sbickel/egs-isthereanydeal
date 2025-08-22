import json
import requests

def transform_library(input_file, output_file):
    # 1. Load JSON
    with open(input_file, 'r') as f:
        data = json.load(f)

    # 2. Normalize to a list of game objects
    if isinstance(data, dict) and 'library' in data:
        games = data['library']
    elif isinstance(data, list):
        games = data
    else:
        raise ValueError("Unexpected JSON structure: expected list or dict with 'library' key.")

    # 3. Build ITAD skeleton
    itad_format = {
        "version": "03",
        "data": [
            {
                "group": "epicmanualimport",
                "public": False,
                "games": []
            }
        ]
    }

    # 4. Pull list of all game titles from legendary library
    gamedb = []
    for game in games:
        gamedb.append(game.get('app_title'))
    
    # 5. Lookup Is There Any Deals ID's for each game

    url = 'https://api.isthereanydeal.com/lookup/id/title/v1'

    response = requests.post(url,json=gamedb)
    
    # 6. Transform each game
    # 6.1 Open ITAD Dict
    itaddata = response.json()

    # 6.2 Get GameID from ITAD Dict
    for game in games:
        for itadid in itaddata:
            if game.get('app_title') == itadid:
                game_id = itaddata[itadid]

    # 6.3 Add game data to json structure
        # Prefer the field your file actually uses:
        title = (
            game.get('app_title')
            or game.get('metadata', {}).get('title', '')
            or game.get('metadata', {}).get('description', '')
        )
        itad_format['data'][0]['games'].append({
            "id": game_id,
            "title": title,
            "platforms": 0,
            "playtime": 0
        })

    # 7. Write out
    with open(output_file, 'w') as f:
        json.dump(itad_format, f, indent=2)


if __name__ == '__main__':
    # Use the real output filename you want:
    transform_library('legendary_library.json', 'transformed_legendary_library.json')

