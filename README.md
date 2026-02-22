[README.txt](https://github.com/user-attachments/files/25471141/README.txt)
# BirthPal 🎂
A simple command-line application to To manage and store people's names and dates of birth.

## 📋 Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features
- **Add new person** - Store name and birthday date
- **Delete person** - Remove by ID
- **View all** - Display complete birthday list
- **Persistent storage** - Automatic save/load with JSON file
- **Input validation** - Validates dates and names
- **User-friendly CLI** - Simple menu interface
- **Modular design** - Clean, maintainable code structure

## 🛠 Technologies Used
- **Python 3.8+** - Core programming language
- **JSON** - Data storage format
- **Type Hints** - Better code documentation
- **Datetime** - Date handling and validation
- **Object-Oriented Programming** - Clean class design
- **Modular Architecture** - Separated concerns (models, services, utils)
- **Unit Testing** - Test coverage for main modules

## 📦 Installation

### Prerequisites
- Python 3.8 or higher installed on your system

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/birthpal.git
Navigate to project directory

bash
cd birthpal
Run the program

bash
python main.py
No additional dependencies required! It uses only Python standard library.

🎮 Usage
Main Menu Options
text
[A] Add new person
[D] Delete person
[Q] Quit
Adding a Person
Press A and Enter

Enter the person's name

Enter birthday in YYYY-MM-DD format (e.g., 1990-05-15)

Person will be added with an auto-generated ID

Deleting a Person
Press D and Enter

Enter the ID of the person you want to delete

Confirm deletion

Viewing List
The list automatically displays after every action

Shows: ID. Name - Birthday

📁 Project Structure
text
birthpal/
│
├── models/
│   └── person.py          # Person class definition
│
├── services/
│   ├── storage.py         # JSON file handling
│   └── birthday_service.py # Core business logic
│
├── utils/
│   ├── validators.py      # Input validation functions
│   └── formatters.py      # Output formatting
│
├── tests/
│   ├── test_person.py     # Person class tests
│   ├── test_storage.py    # Storage tests
│   └── test_validators.py # Validator tests
│
├── data/
│   └── birthdays.json     # Auto-generated data file
│
├── menu.py                 # User interface
├── main.py                 # Entry point
└── README.md               # This file
💡 Examples
Adding a person
text
==================================================
The list is empty

[A] Add new person
[D] Delete person
[Q] Quit

Your choice: A

--- Add New Person ---
Enter name: John Doe
Enter birthday (YYYY-MM-DD): 1990-05-15
✅ Person added successfully.
Viewing the list
text
==================================================
1. John Doe - 1990-05-15
2. Jane Smith - 1985-08-22

[A] Add new person
[D] Delete person
[Q] Quit
Deleting a person
text
Your choice: D

--- Delete Person ---
Enter person ID to delete: 2
✅ Person 'Jane Smith' deleted successfully.
🧪 Running Tests
To run the tests:

bash
python -m unittest discover tests/
🤝 Contributing
Contributions are welcome! Feel free to:

Fork the repository

Create a new branch

Make your changes

Submit a pull request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
Nima tarhani

GitHub: @nimatarhani

⭐ Show your support
Give a ⭐️ if this project helped you!

Made with ❤️ for learning and sharing
## 🔄 How Modules Work Together

- **main.py** starts the program and calls **menu.py**
- **menu.py** talks to user and uses **birthday_service.py** for operations
- **birthday_service.py** uses:
  - **validators.py** to check inputs
  - **storage.py** to save/load data
  - **models/person.py** to create people
- **storage.py** reads/writes **birthdays.json**
- **formatters.py** helps **menu.py** show formatted and better output
