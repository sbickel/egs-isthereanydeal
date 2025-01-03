# Epic Games Library to IsThereAnyDeal Importer
A simple tool to convert your Epic Games Store library into a format compatible with IsThereAnyDeal's collection import feature.

## Overview
This tool helps you import your Epic Games Store library into IsThereAnyDeal by converting the library format from Legendary (Epic Games Store launcher) to IsThereAnyDeal's collection format.

## Prerequisites
- Python 3.6 or higher
- Legendary launcher installed with your Epic Games library synchronized

## Usage
1. Export your Epic Games library from Legendary:
If you want to use the [Legendary cli](https://github.com/derrod/legendary?tab=readme-ov-file#usage), you can export your list of games via: 
```bash
legendary list-games --json > legendary_library.json
```
If you want to skip cli and have the [Legendary app](https://github.com/derrod/legendary/releases) installed, you can find `legendary_library.json` in:
- Mac: `~/Library/Application Support/heroic/store_cache`
- Windows: `%APPDATA%/heroic/legendaryConfig/legendary`

2. [Download this repo](https://github.com/marcodallagatta/egs-isthereanydeal/archive/refs/heads/main.zip) and unpack is somewhere on your computer.

3. Copy the json over to your extracted copy of this repo.

4. Run the script:
```bash
python3 ./egs-isthereanydeal.py
```

4. Import to IsThereAnyDeal:
   - Go to [IsThereAnyDeal's Collection import page](https://isthereanydeal.com/collection/import/)
   - Upload the generated `transformed_legendary_library.json`
   - Check the other settings to suit your needs
   - Click Import Collection

## Format Specification

**Input (Legendary)**:
```json
{
    "library": [
        {
            "app_name": "...",
            "extra": {
                "about": {
                    "description": "..."
                }
            }
        }
    ]
}
```

**Output (ITAD)**:
```json
{
    "version": "03",
    "data": [
        {
            "group": "epicmanualimport",
            "public": false,
            "games": [
                {
                    "id": "...",
                    "title": "...",
                    "platforms": 0,
                    "playtime": 0
                }
            ]
        }
    ]
}
```
