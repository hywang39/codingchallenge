"""
WSGI config for codingChallenge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "codingChallenge.settings")

#########################
from challenge import models

FOOD_ID_CATEGORY_PAIRNG = {'vf': 1, 'gr': 2, 'mi': 3, 'me': 4}


def load_data_from_json_foodentry():
    json = {
        "foods": [
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup, 6 spears",
                "food": "Asparagus"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Beans, green"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Bok choy/Chinese cabbage (Choi sum)"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Broccoli"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup, 4 sprouts",
                "food": "Brussels sprouts"
            },
            {
                "fgid": "vf",
                "fgcat_id": "2",
                "srvg_sz": "125 mL, &frac12; cup, 1 large",
                "food": "Carrots"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Chard"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Dandelion greens"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Endive"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Fiddleheads"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Kale/collards"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup, &frac12; leek",
                "food": "Leeks"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Lettuce, romaine"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Mesclun mix"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Mustard greens"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Okra"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Peas"
            },
            {
                "fgid": "vf",
                "fgcat_id": "2",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Pumpkin"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Seaweed"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Snow peas"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Spinach"
            },
            {
                "fgid": "vf",
                "fgcat_id": "2",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Squash"
            },
            {
                "fgid": "vf",
                "fgcat_id": "2",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Sweet potato"
            },
            {
                "fgid": "vf",
                "fgcat_id": "2",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Yam"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "3 fruits",
                "food": "Apricot, fresh"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Cantaloupe"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, &frac12; fruit",
                "food": "Mango"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 fruit",
                "food": "Nectarine"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "&frac12; fruit",
                "food": "Papaya"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium",
                "food": "Peach"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium",
                "food": "Apple"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "&frac12; fruit",
                "food": "Avocado"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Bamboo shoots"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium",
                "food": "Banana"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Beans, yellow"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Beets"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Berries"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, &frac12; pod",
                "food": "Bitter melon"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Cabbage"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, 4 flowerets",
                "food": "Cauliflower"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium stalk",
                "food": "Celery"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Chayote"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "20",
                "food": "Cherries"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 ear, 125 mL, &frac12; cup",
                "food": "Corn"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Cucumber"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "60 mL, &frac14; cup",
                "food": "Dried fruit"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Eggplant"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "2 medium",
                "food": "Fig, fresh"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "&frac12; fruit",
                "food": "Grapefruit"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "20 fruits",
                "food": "Grapes"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, 1 fruit",
                "food": "Guava"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Honeydew"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 large fruit",
                "food": "Kiwi"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Kohlrabi"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "250 mL, 1 cup raw",
                "food": "Lettuce (example: iceberg or butterhead)"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "10 fruits",
                "food": "Lychee"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Mixed Vegetables"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Mushrooms"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium",
                "food": "Orange"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 medium",
                "food": "Pear"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, 1 medium",
                "food": "Peppers, bell"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, 1 slice",
                "food": "Pineapple"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Plantain"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "1 fruit",
                "food": "Plum"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup, &frac12; medium",
                "food": "Potato"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Radishes"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Rhubarb"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Tomato"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Tomato sauce"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Turnip"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Vegetable juice, lower sodium"
            },
            {
                "fgid": "vf",
                "fgcat_id": "0",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Watermelon"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Zucchini"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup, &frac12; medium",
                "food": "Pepper, sweet, green"
            },
            {
                "fgid": "vf",
                "fgcat_id": "1",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Edamame (soy beans)"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Barley"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "&frac12; bagel, 45 g",
                "food": "Bagel, whole grain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "1 slice, 35 g",
                "food": "Bread, pumpernickel or rye"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "1 slice, 35 g",
                "food": "Bread, whole grain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Bulgur"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "30 g",
                "food": "Cereal, cold, whole grain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "150 g, 175 mL, &frac34; cup cooked",
                "food": "Cereal, hot, whole grain (example: oatmeal)"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "30 g",
                "food": "Crackers, rye wafer"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "&frac12;",
                "food": "Muffin, whole grain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Quinoa"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Rice, brown"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Pasta/noodles, whole grain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "&frac12; pita, 35 g",
                "food": "Pita, whole wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "&frac12; piece, 35 g",
                "food": "Tortilla, corn"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "&frac12; piece, 35 g",
                "food": "Tortilla, whole wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 medium, 35 g",
                "food": "Bannock"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 slice, 35 g",
                "food": "Baguette, French"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 slice, 35 g",
                "food": "Bread, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "30 g",
                "food": "Cereal, cold"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "150 g, 175 mL, &frac34; cup cooked",
                "food": "Cereal, hot, for example: cream of wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Congee"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 slice, 35 g",
                "food": "Cornbread"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Couscous"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "10, 30 g",
                "food": "Cracker, saltines"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "&frac12; muffin, 35 g",
                "food": "English muffin, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "&frac14; naan, 35 g",
                "food": "Naan"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 small, 35 g",
                "food": "Pancake"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Pasta/noodles, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "&frac12; pita, 35 g",
                "food": "Pita, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "125 mL, &frac12; cup",
                "food": "Polenta"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Rice, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "2 medium",
                "food": "Rice cake, plain"
            },
            {
                "fgid": "gr",
                "fgcat_id": "4",
                "srvg_sz": "1 roll, 35 g",
                "food": "Roll, white"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "30 g",
                "food": "Crackers, whole wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cup cooked",
                "food": "Rice, wild"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "1 roll, 35 g",
                "food": "Roll, whole wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "125 mL, &frac12; cooked",
                "food": "Couscous, whole wheat"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "500 mL, 2 cups",
                "food": "Popcorn, without added fat or salt"
            },
            {
                "fgid": "gr",
                "fgcat_id": "3",
                "srvg_sz": "&frac12; muffin, 35 g",
                "food": "English muffin, whole grain"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Buttermilk"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Fortified soy beverage (unsweetened)"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Milk, 1%, 2%, skim"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "125 mL, &frac12; cup undiluted",
                "food": "Milk, evaporated, canned"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Milk, goat, enriched"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Milk, lactose reduced"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "250 mL, 1 cup reconstitued",
                "food": "Milk, powdered"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "25 g, 75 mL, 1/3 cup",
                "food": "Milk, powdered"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "50 g, 1 &frac12; oz",
                "food": "Cheese, block (Cheddar, Mozzarella, Swiss, feta)"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "250 ml, 1 cup",
                "food": "Cheese, cottage or quark"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "50 g, 1 &frac12; oz",
                "food": "Cheese, goat"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "50 g, 1 &frac12; oz",
                "food": "Paneer"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "175 g, 175mL, &frac34; cup",
                "food": "Yogurt, plain"
            },
            {
                "fgid": "mi",
                "fgcat_id": "5",
                "srvg_sz": "250 mL, 1 cup",
                "food": "Milk, whole"
            },
            {
                "fgid": "mi",
                "fgcat_id": "6",
                "srvg_sz": "175 g, 175 mL, &frac34; cup",
                "food": "Kefir"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "175 mL, &frac34; cup",
                "food": "Beans, cooked and canned"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "2",
                "food": "Eggs"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "175 mL, &frac34; cup",
                "food": "Lentils"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "60 mL, &frac14; cup",
                "food": "Nuts, shelled"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "30 mL, 2 Tbsp",
                "food": "Peanut butter or nut butters"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "60 mL, &frac14; cup",
                "food": "Seeds, shelled"
            },
            {
                "fgid": "me",
                "fgcat_id": "7",
                "srvg_sz": "150 g, 175 mL, &frac34; cup",
                "food": "Tofu"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Beef"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Bison/Buffalo"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Chicken"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Deli meat, low-fat, lower sodium"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Duck"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Fish and shellfish, canned (example: crab, salmon, tuna)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Fish, fresh or frozen (example: herring, mackerel, trout, salmon, sardines, squid, tuna)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Game birds (example: ptarmigan, partridge, grouse, goose)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Game me (example: deer, moose, caribou, elk)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Goat"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Ham"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Lamb"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Organ meat (example: liver, kidney)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Pork"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Rabbit /Hare"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Shellfish, fresh or frozen (example: clams, crab, lobster, mussels, scallops, shrimp, prawns)"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Turkey"
            },
            {
                "fgid": "me",
                "fgcat_id": "8",
                "srvg_sz": "75 g (2&frac12; oz) / 125 mL (&frac12; cup)",
                "food": "Veal"
            }
        ]
    }

    if not models.FoodEntry.objects.filter().count():
        for foodentry in json['foods']:
            food = models.FoodEntry()
            food.food_detail_category_id = foodentry['fgcat_id']
            food.serving_size = foodentry['srvg_sz']
            food.food_name = foodentry['food']
            food.save()


def load_data_from_json_serving():
    json = {
        "servings to per to miy": [
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "2 to 3",
                "servings": "4"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "2 to 3",
                "servings": "4"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "4 to 8",
                "servings": "5"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "4 to 8",
                "servings": "5"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "9 to 13",
                "servings": "6"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "9 to 13",
                "servings": "6"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "14 to 18",
                "servings": "7"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "14 to 18",
                "servings": "8"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "19 to 30",
                "servings": "7 to 8"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "19 to 30",
                "servings": "8 to 10"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "31 to 50",
                "servings": "7 to 8"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "31 to 50",
                "servings": "8 to 10"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "51 to 70",
                "servings": "7"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "51 to 70",
                "servings": "7"
            },
            {
                "fgid": "vf",
                "gender": "Female",
                "ages": "71+",
                "servings": "7"
            },
            {
                "fgid": "vf",
                "gender": "Male",
                "ages": "71+",
                "servings": "7"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "2 to 3",
                "servings": "3"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "2 to 3",
                "servings": "3"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "4 to 8",
                "servings": "4"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "4 to 8",
                "servings": "4"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "9 to 13",
                "servings": "6"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "9 to 13",
                "servings": "6"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "14 to 18",
                "servings": "6"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "14 to 18",
                "servings": "7"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "19 to 30",
                "servings": "6 to 7"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "19 to 30",
                "servings": "8"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "31 to 50",
                "servings": "6 to 7"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "31 to 50",
                "servings": "8"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "51 to 70",
                "servings": "6"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "51 to 70",
                "servings": "7"
            },
            {
                "fgid": "gr",
                "gender": "Female",
                "ages": "71+",
                "servings": "6"
            },
            {
                "fgid": "gr",
                "gender": "Male",
                "ages": "71+",
                "servings": "7"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "2 to 3",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "2 to 3",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "4 to 8",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "4 to 8",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "9 to 13",
                "servings": "3 to 4"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "9 to 13",
                "servings": "3 to 4"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "14 to 18",
                "servings": "3 to 4"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "14 to 18",
                "servings": "3 to 4"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "19 to 30",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "19 to 30",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "31 to 50",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "31 to 50",
                "servings": "2"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "51 to 70",
                "servings": "3"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "51 to 70",
                "servings": "3"
            },
            {
                "fgid": "mi",
                "gender": "Female",
                "ages": "71+",
                "servings": "3"
            },
            {
                "fgid": "mi",
                "gender": "Male",
                "ages": "71+",
                "servings": "3"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "2 to 3",
                "servings": "1"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "2 to 3",
                "servings": "1"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "4 to 8",
                "servings": "1"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "4 to 8",
                "servings": "1"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "9 to 13",
                "servings": "1 to 2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "9 to 13",
                "servings": "1 to 2"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "14 to 18",
                "servings": "2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "14 to 18",
                "servings": "3"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "19 to 30",
                "servings": "2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "19 to 30",
                "servings": "3"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "31 to 50",
                "servings": "2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "31 to 50",
                "servings": "3"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "51 to 70",
                "servings": "2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "51 to 70",
                "servings": "3"
            },
            {
                "fgid": "me",
                "gender": "Female",
                "ages": "71+",
                "servings": "2"
            },
            {
                "fgid": "me",
                "gender": "Male",
                "ages": "71+",
                "servings": "3"
            }
        ]
    }

    if not models.Serving.objects.filter().count():
        for serving in json['servings to per to miy']:
            serv = models.Serving()
            serv.food_category_id = FOOD_ID_CATEGORY_PAIRNG[serving['fgid']]
            if ('+' in serving['ages']):
                serv.age_upper = 200
                serv.age_lower = 71
            else:
                age_bounds = serving['ages'].split(' to ')
                serv.age_lower = age_bounds[0]
                serv.age_upper = age_bounds[1]
            serv.serving_number = serving['servings']
            serv.gender = serving['gender']
            serv.save()


def load_data_from_json_food_category():
    json = {
        "foodgroups": [
            {
                "fgid": "vf",
                "foodgroup": "Vegetables and Fruit",
                "categories": [
                    {
                        "fgcat_id": "0",
                        "fgcat": "Non dark green or orange vegetable"
                    },
                    {
                        "fgcat_id": "1",
                        "fgcat": "Dark green vegetable"
                    },
                    {
                        "fgcat_id": "2",
                        "fgcat": "Orange vegetable"
                    }
                ]
            },
            {
                "fgid": "gr",
                "foodgroup": "Grains",
                "categories": [
                    {
                        "fgcat_id": "3",
                        "fgcat": "Whole grain"
                    },
                    {
                        "fgcat_id": "4",
                        "fgcat": "Non whole grain"
                    }
                ]
            },
            {
                "fgid": "mi",
                "foodgroup": "Milk and Alternatives",
                "categories": [
                    {
                        "fgcat_id": "5",
                        "fgcat": "Milk"
                    },
                    {
                        "fgcat_id": "6",
                        "fgcat": "Milk Alternatives"
                    }
                ]
            },
            {
                "fgid": "me",
                "foodgroup": "Meat and Alternatives",
                "categories": [
                    {
                        "fgcat_id": "7",
                        "fgcat": "Meat Alternatives"
                    },
                    {
                        "fgcat_id": "8",
                        "fgcat": "Meat, fish, poultry and shellfish"
                    }
                ]
            }
        ]
    }

    if not models.FoodCategory.objects.filter().count():
        for foodcat in json['foodgroups']:
            fc = models.FoodCategory()
            fc._id = FOOD_ID_CATEGORY_PAIRNG[foodcat['fgid']]
            fc.food_category_short_name = foodcat['fgid']
            fc.food_category_long_name = foodcat['foodgroup']
            fc.save()


def load_data_from_json_food_detail_category():
    json = {
        "foodgroups": [
            {
                "fgid": "vf",
                "foodgroup": "Vegetables and Fruit",
                "categories": [
                    {
                        "fgcat_id": "0",
                        "fgcat": "Non dark green or orange vegetable"
                    },
                    {
                        "fgcat_id": "1",
                        "fgcat": "Dark green vegetable"
                    },
                    {
                        "fgcat_id": "2",
                        "fgcat": "Orange vegetable"
                    }
                ]
            },
            {
                "fgid": "gr",
                "foodgroup": "Grains",
                "categories": [
                    {
                        "fgcat_id": "3",
                        "fgcat": "Whole grain"
                    },
                    {
                        "fgcat_id": "4",
                        "fgcat": "Non whole grain"
                    }
                ]
            },
            {
                "fgid": "mi",
                "foodgroup": "Milk and Alternatives",
                "categories": [
                    {
                        "fgcat_id": "5",
                        "fgcat": "Milk"
                    },
                    {
                        "fgcat_id": "6",
                        "fgcat": "Milk Alternatives"
                    }
                ]
            },
            {
                "fgid": "me",
                "foodgroup": "Meat and Alternatives",
                "categories": [
                    {
                        "fgcat_id": "7",
                        "fgcat": "Meat Alternatives"
                    },
                    {
                        "fgcat_id": "8",
                        "fgcat": "Meat, fish, poultry and shellfish"
                    }
                ]
            }
        ]
    }

    if not models.FoodDetailCategory.objects.filter().count():
        for foodcatdetail in json['foodgroups']:
            for foodcd in foodcatdetail['categories']:
                fcd = models.FoodDetailCategory()
                fcd._id = foodcd['fgcat_id']
                fcd.description = foodcd['fgcat']
                fcd.food_category_id = FOOD_ID_CATEGORY_PAIRNG[foodcatdetail['fgid']]
                fcd.save()


def load_data_from_json_directional_statements():
    json = {
        "directional_statements": [
            {
                "fgid": "vf",
                "dir_stmt": "Eat at least one dark green and one orange vegetable each day."
            },
            {
                "fgid": "vf",
                "dir_stmt": "Choose vegetables and fruit prepared with little or no added fat, sugar or salt."
            },
            {
                "fgid": "vf",
                "dir_stmt": "Have vegetables and fruit more often than juice."
            },
            {
                "fgid": "gr",
                "dir_stmt": "Make at least half of your grain products whole grain each day."
            },
            {
                "fgid": "gr",
                "dir_stmt": "Choose grain products that are lower in fat, sugar or salt."
            },
            {
                "fgid": "mi",
                "dir_stmt": "Drink skim, 1%, or 2% milk each day."
            },
            {
                "fgid": "mi",
                "dir_stmt": "Select lower fat milk alternatives."
            },
            {
                "fgid": "me",
                "dir_stmt": "Have meat alternatives such as beans, lentils and tofu often."
            },
            {
                "fgid": "me",
                "dir_stmt": "Eat at least two Food Guide Servings of fish each week."
            },
            {
                "fgid": "me",
                "dir_stmt": "Select lean meat and alternatives prepared with little or no added fat or salt."
            }
        ]
    }
    if not models.DirectionalStatement.objects.filter().count():
        for direcional_statement in json['directional_statements']:
            ds = models.DirectionalStatement()
            ds.food_category_id = FOOD_ID_CATEGORY_PAIRNG[direcional_statement['fgid']]
            ds.statement = direcional_statement['dir_stmt']
            ds.save()



load_data_from_json_food_category()
load_data_from_json_food_detail_category()
load_data_from_json_foodentry()
load_data_from_json_serving()
load_data_from_json_directional_statements()
############################
application = get_wsgi_application()
