from typing import List, Optional, Tuple
from datetime import datetime
from models.person import Person
from services import storage
from utils import validators

def load_people()-> list[Person]:
    return storage.load_data()

def save_people(people: list[Person]) -> None:

    storage.save_data(people)

def add_person(name : str ,birthday_str : str , people: list) -> tuple[bool , str , Optional[Person]] :
    if not validators.validate_name(name):
        return False, "Invalid name. Name cannot be empty.", None
    if not validators.validate_date(birthday_str):
        return False, "Invalid date. Please use YYYY-MM-DD format.", None
    try:
        birthday = datetime.strptime(birthday_str, "%Y-%m-%d").date()
    except ValueError:
        return False, "Invalid date.", None
    
    new_id = storage.get_next_id(people)
    new_person = Person(new_id, name, birthday)
    return True, "Person added successfully.", new_person

def delete_person(person_id : int , people : list[Person])-> tuple[bool , str, Optional[Person]] :
    if not validators.validate_id_exists(person_id, people):
        return False, f"Person with ID {person_id} not found.", None
    
    for i, person in enumerate(people):
        if person.id == person_id:

            deleted_person = people.pop(i)
            return True, f"Person '{deleted_person.name}' deleted successfully.", deleted_person
    
    return False, "Error occurred while deleting.", None


