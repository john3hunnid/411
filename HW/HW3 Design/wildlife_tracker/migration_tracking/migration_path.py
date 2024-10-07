from typing import Optional
from ..habitat_management.habitat import Habitat
class MigrationPath:
    def __init__ (self,
                  species: str, 
                  start_location: Habitat, 
                  start_date: str,
                  destination: Habitat, 
                  duration: Optional[int],
                  path_id:int):
        self.species=species
        self.start_location=start_location
        self.start_date=start_date
        self.destination=destination
        self.duration=duration
        self.path_id=path_id

    def get_migration_path_details(path_id) -> dict:
        pass
    pass
    