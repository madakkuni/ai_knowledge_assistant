from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    app_name: str
    app_version: str
    app_description: str
    environment: str
    api_prefix: str

    # Logging
    log_directory: str = "logs"
    log_level: str = "INFO"

    # Azure OpenAI
    azure_openai_api_key: str
    azure_openai_endpoint: str
    azure_openai_api_version: str

    azure_openai_chat_deployment: str
    azure_openai_embedding_deployment: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


settings = Settings()