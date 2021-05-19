from typing import List, Union, Optional, Dict, Any
from pydantic import BaseSettings, validator, AnyHttpUrl


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"  # for api versioning

    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME = "ITSNP Blog"

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        P_User = values.get('POSTGRES_USER')
        P_Password = values.get('POSTGRES_PASSWORD')
        P_Server = values.get('POSTGRES_SERVER')
        P_Port = values.get('POSTGRES_PORT')
        P_Db = values.get('POSTGRES_DB')

        return f"postgresql://{P_User}:{P_Password}@{P_Server}:{P_Port}/{P_Db}"

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
