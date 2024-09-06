from pydantic_settings import SettingsConfigDict, BaseSettings

class Setting(BaseSettings):
    
    HOST: str
    PORT: str
    USER: str
    PASSWORD: str
    DATEBASE: str
    
    @property
    def DATABASE_URL_ASYNC_PSYCOPG(self):
        
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self. DATEBASE}"
    
    
    model_config = SettingsConfigDict(env_file=".env")
        
settings = Setting()    
    