## 🔄 How Modules Work Together

- **main.py** starts the program and calls **menu.py**
- **menu.py** talks to user and uses **birthday_service.py** for operations
- **birthday_service.py** uses:
  - **validators.py** to check inputs
  - **storage.py** to save/load data
  - **models/person.py** to create people
- **storage.py** reads/writes **birthdays.json**
- **formatters.py** helps **menu.py** show formatted and better output