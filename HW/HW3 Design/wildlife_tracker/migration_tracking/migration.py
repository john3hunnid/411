from typing import Any

class Migration:
    def __init__(self, migration_id: int,
                 paths: dict[int, MigrationPath]
                 ):
        self.migration_id=migration_id
        self.paths=paths
    
    def cancel_migration(migration_id: int) -> None:
        pass
    
    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass
    
    def get_migration_by_id(migration_id: int) -> Migration:
        pass
    
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass

    def get_migration_paths() -> list[MigrationPath]:
        pass
    
    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass
    pass