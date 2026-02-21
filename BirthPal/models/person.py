from datetime import date

class Person:
    
    def __init__(self, id: int, name: str, birthday: date):
        if id <= 0:
            raise ValueError("id must be more than 0")
        if not name or not name.strip():
            raise ValueError("name cannot be empty")

        self.id = id
        self.name = name.strip()
        self.birthday = birthday
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "birthday": self.birthday.isoformat()
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        person_id = data["id"]
        person_name = data["name"]
        birthday_str = data["birthday"]
        year, month, day = birthday_str.split("-")
        birthday_date = date(int(year), int(month), int(day))
        
        return cls(person_id, person_name, birthday_date)
    
    def __str__(self) -> str:
        return f"{self.id}. {self.name} - {self.birthday}"