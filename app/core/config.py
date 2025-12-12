from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Trade Opportunities API"
    env: str = "development"
    debug: bool = False

    auth_header: str = "Authorization"
    auth_scheme: str = "Bearer"

    rate_limit_requests: int = 10
    rate_limit_window_seconds: int = 3600

    api_token: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
