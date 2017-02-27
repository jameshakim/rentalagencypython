import rental_main

items = {
    "6ft ladder": {
        "quantity": 1,
        "rent": 10,
        "value": 70
    },
    "12ft ladder": {
        "quantity": 2,
        "rent": 15,
        "value": 100
    },
    "drill": {
        "quantity": 4,
        "rent": 20,
        "value": 150
    },
    "chainsaw": {
        "quantity": 3,
        "rent": 45,
        "value": 350
    },
    "table saw": {
        "quantity": 1,
        "rent": 50,
        "value": 400
    }
}

rental_main.dump_data(items)
