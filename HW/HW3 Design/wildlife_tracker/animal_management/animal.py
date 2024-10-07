from typing import Any, Optional
import List
class Animal:
    def __init__(self, animal_id: int,age: Optional[int],health_status: Optional[str])->None:
        self.animal_id=animal_id
        self.age=age
        self.health_status=health_status
    pass

def get_animal_details(animal_id) -> dict[str, Any]:
    pass
