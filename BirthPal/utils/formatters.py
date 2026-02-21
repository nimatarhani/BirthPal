from typing import List
from models.person import Person

def format_person_list(people : list[Person]) -> str :
    if not people :
        return "list is empty"
    
    result = ""
    for person in people:
        result += str(person) + "\n"
    return result

def format_person(person:Person) -> str:
    return str(person)

def format_menu() -> str:

    menu = """
[A] Add new person
[D] Delete new person
[Q] exit
"""
    return menu

def format_success_message(action : str , name: str) -> str :
    if action == "add":
        return f"person named {name} added successfully"
    elif action == "delete":
        return f"person named {name} deleted successfully"
    else :
        return "Operation completed successfully"