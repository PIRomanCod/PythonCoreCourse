import json
data = {
    "developer": {
        "name": "Володимир В.",
        "species": "програміст"
    }
}

with open("data_user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)


with open("data_user.json", "r", encoding="utf-8") as f:
    restore_data = json.load(f)
    print(restore_data)