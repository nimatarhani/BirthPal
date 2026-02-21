from services import birthday_service as service
from menu import run_menu

def main():

    print("🎂 Welcome to BirthPal!")
    print("="*50)
    

    people = service.load_people()
    

    people = run_menu(people)
    
    print("\n👋 Program ended.")

if __name__ == "__main__":
    main()