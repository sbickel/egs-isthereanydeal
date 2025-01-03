import json

def transform_library(legendary_file, itad_file):
    # Read legendary library
    with open(legendary_file, 'r') as f:
        legendary_data = json.load(f)

    # Create ITAD format
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

    # Transform each game
    for game in legendary_data['library']:
        game_entry = {
            "id": game['app_name'],
            "title": game['extra']['about']['description'],
            "platforms": 0,
            "playtime": 0
        }
        itad_format['data'][0]['games'].append(game_entry)

    # Save transformed file
    with open('transformed_legendary_library.json', 'w') as f:
        json.dump(itad_format, f, indent=2)

# Use the function
transform_library('legendary_library.json', 'collection.json')
