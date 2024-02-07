# open the files in "./chipped_tags" and iterate through them as json

# DEV: Relocate this within the chipped data folder

import json
import os
from copy import copy
from pprint import pprint

DEFAULT_JSON_RECIPE_TEMPLATE = {
    "conditions": [
        {
            "type": "forge:mod_loaded",
            "modid": "chipped"
        }
    ],
    "type": "create:cutting",
    "ingredients": [
        {
            "tag": ""
        }
    ],
    "results": [
        {
            "item": "",
            "count": 1
        }
    ],
    "processingTime": 50
}

# get the path to the chipped_tags folder
path = os.path.join(os.path.dirname(__file__), "chipped_tags")

# iterate through the files in the chipped_tags folder
for filename in os.listdir(path):
    if filename.endswith(".json"):
        with open(os.path.join(path, filename), "r") as file:
            print()
            print("="*50)
            print(f"Reading file {filename}")

            print()
            data = json.load(file)
            pprint(data)

            print()
            chipped_values = data['values'][1:]
            pprint(chipped_values)

            # get the ingredient
            ingredient = f"chipped:{filename.split('.')[0]}"

            # create a dir for the ingredient if it doesn't exist
            if not os.path.exists(ingredient.split(':')[1]):
                os.makedirs(ingredient.split(':')[1])

            # get the result from the values
            for result in chipped_values:

                if ":" not in result: continue

                print()
                print(f"Creating recipe for {result}")

                # create a copy of the default json recipe template
                recipe = copy(DEFAULT_JSON_RECIPE_TEMPLATE)

                # set the ingredient and result
                recipe['ingredients'][0]['tag'] = ingredient
                recipe['results'][0]['item'] = result

                # print the recipe
                pprint(recipe)

                # write the recipe to a file
                with open(
                            f"{ingredient.split(':')[1]}/{result.split(':')[1] }.json", 
                            "w"
                        ) as file:
                    json.dump(recipe, file, indent=4)

                print()
                print(f"Recipe for {result} created")
                print("="*50)
                print()
