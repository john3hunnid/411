from typing import Any

class Migration:
    def __init__(self, migration_id: int,
                 paths: dict[int, MigrationPath],
                 status: str = "Scheduled"
                 ):
        self.migration_id=migration_id
        self.paths=paths
        self.status=status
    
    def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass
    
    def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass
    
    def cancel_migration(migration_id: int) -> None:
        pass

    pass