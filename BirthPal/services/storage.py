import json

from models.person import Person

DATA_FILE = "data/birthdays.json"

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            people = []
            for item in data :
                person = Person.from_dict(item)
                people.append(person)
            return people

    except FileNotFoundError:
        return[]
    
    except json.JSONDecodeError:
        # فایل خراب شده، لیست خالی برگردون
        print(" The data file is corrupted. A new list will be created.")
        return []

    
    

def save_data(people):
    data_to_save = []
    for person in people:
        data_to_save.append(person.to_dict())
    data_to_save = []
    for person in people:
        data_to_save.append(person.to_dict())
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, indent=4, ensure_ascii=False)




def get_next_id(people):
    if not people:
        return 1
    
    max_id = 0
    for person in people:
        if person.id > max_id:
            max_id = person.id
    
    return max_id + 1