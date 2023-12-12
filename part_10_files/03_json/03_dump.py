import json
import datetime

my_dict = {
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg",
        "isFound": None,
        "isValid": False,
        "languages": ("Java", "Python"),
        "cities": ["Jerusalem", "Tel Aviv"],
        "current_date": (str(datetime.date.today()) + "TZ"),
        "my_obj": {
            "key_1": "value_1",
        }
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}

with open("data_to_load.json", "w+") as report:
    json.dump(my_dict, report)
