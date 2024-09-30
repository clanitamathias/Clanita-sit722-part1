import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://clanita_sit722_part1_8nso_user:SP8eRKsjZKxIzzx72MOboE9PYOIF7RSL@dpg-crt76s5ds78s73eccdog-a.oregon-postgres.render.com/clanita_sit722_part1_8nso")

settings = Settings()
