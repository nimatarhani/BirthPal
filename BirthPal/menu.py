

from typing import List
from models.person import Person
from services import birthday_service as service
from utils import validators, formatters  

def run_menu(people: List[Person]) -> List[Person]:

    while True:

        print("\n" + "="*50)
        print(formatters.format_person_list(people)) 
        

        print(formatters.format_menu())
        

        choice = input("Your choice: ").strip()
        

        if not validators.validate_choice(choice):
            print("Invalid choice! Please enter A, D, or Q.")
            continue
        

        if choice.upper() == "A":
            people = handle_add(people)
        elif choice.upper() == "D":
            people = handle_delete(people)
        elif choice.upper() == "Q":
            print("Goodbye!")
            break
    
    return people


def handle_add(people: List[Person]) -> List[Person]:

    print("\n--- Add New Person ---")
    

    name = input("Enter name: ").strip()
    

    birthday = input("Enter birthday (YYYY-MM-DD): ").strip()
    

    success, message, new_person = service.add_person(name, birthday, people)
    
    if success:

        people.append(new_person)

        service.save_people(people)
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
    
    return people


def handle_delete(people: List[Person]) -> List[Person]:

    print("\n--- Delete Person ---")
    

    if not people:
        print("The list is empty. Nothing to delete.")
        return people
    

    try:
        person_id = int(input("Enter person ID to delete: ").strip())
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return people
    

    success, message, deleted_person = service.delete_person(person_id, people)
    
    if success:
        service.save_people(people)
        print(f"✅ {message}")
    else:
        print(f"❌ {message}")
    
    return people