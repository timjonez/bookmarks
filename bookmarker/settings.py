from pydantic import BaseSettings


class SettingsClass(BaseSettings):
    # These are defaults that can be override with a .env file
    app_name: str = "Bookmarker"
    admin_email: str = "admin@bookmarker.com"
    secret_key: str = "this-is-a-secret"

    class Config:
        env_file = ".env"

settings = SettingsClass()
