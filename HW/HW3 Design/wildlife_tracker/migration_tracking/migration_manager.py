from typing import Optional


class MigrationManager:
    def __init__(self)->None:
        migrations: dict[int, Migration]={}

    def get_migration_paths() -> list[MigrationPath]:
        pass
    def get_migrations_by_current_location(current_location: str) -> list[Migration]:
        pass

    def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
        pass

    def get_migrations_by_start_date(start_date: str) -> list[Migration]:
        pass

    def get_migrations_by_status(status: str) -> list[Migration]:
        pass
    
    def get_migration_by_id(migration_id: int) -> Migration:
        pass
    
    def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
        pass
    
    def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
        pass