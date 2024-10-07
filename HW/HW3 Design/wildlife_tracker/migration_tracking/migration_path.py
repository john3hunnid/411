from typing import Optional
from .habitat import Habitat
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
        
    def get_migration_path_by_id(path_id: int) -> MigrationPath:
        pass
    
    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass

    def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
        pass
   
    def get_migration_path_details(path_id) -> dict:
        pass
    
    def remove_migration_path(path_id: int) -> None:
        pass
    def schedule_migration(migration_path: MigrationPath) -> None:
        pass

    pass
    