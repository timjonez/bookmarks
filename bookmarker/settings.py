from pydantic import BaseSettings


class PublicSettings(BaseSettings):
    # These are defaults that can be override with a .env file
    title: str = "Bookmarker"
    openapi_url: str = "/openapi.json"
    version = "1.0.0"

class PrivateSettings(PublicSettings):
    admin_email: str = "admin@bookmarker.com"
    secret_key: str = "this-is-a-secret"
    salt_rounds = 10

    class Config:
        env_file = ".env"

settings = PrivateSettings()
pub_settings = PublicSettings()
