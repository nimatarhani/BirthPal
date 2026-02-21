from typing import List
from datetime import datetime
from models.person import Person

def validate_date (date_str : str) -> bool:
    if len(date_str) != 10:
        return False
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_name (name : str) -> bool:
    name = name.strip()
    if not name :
        return False
    return True

def validate_id_exists (person_id : int , people : list[Person]) -> bool :
    for person in people:
        if person.id == person_id :
            return True
    return False

def validate_choice (choice : str) -> bool:
    choice_upper = choice.upper()
    if choice_upper == "A"  or choice_upper == "D" :
        return True
    else :
        return False 
