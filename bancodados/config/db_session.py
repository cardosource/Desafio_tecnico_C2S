from pathlib import Path
from typing import Optional
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine
from bancodados.models.model_base import ModelBase

__asyncEngine:Optional[AsyncEngine] = None
database_postgresql = "postgresql+asyncpg://postgres:xxx@localhost:5432/ficatecnica"
database_sqlite = "sqlite+aiosqlite:///"

def create_engine(sqlite: bool = False) -> AsyncEngine:
    global __asyncEngine
    if __asyncEngine:
        return
    if sqlite:
        arquivo_db = 'db/picoles.sqlite'
        diretorio = Path(arquivo_db).parent
        diretorio.mkdir(parents=True,exist_ok=True)       
        conn_str = f'{database_sqlite}{arquivo_db}'
        __asyncEngine =create_async_engine(url=conn_str)
    else:#postgree
        conn_str = database_postgresql
        __asyncEngine = create_async_engine(url=conn_str)
    return __asyncEngine

def create_session() -> AsyncSession:

    global __asyncEngine
    if not __asyncEngine:
        create_engine()
    __asyncSession = AsyncSession( __asyncEngine,expire_on_commit=False)
    session:AsyncSession =__asyncSession
    return session

async def create_tables() -> None:
    print('tabelas criadas')
    global __asyncEngine
    if not __asyncEngine:
        create_engine()
    
    import bancodados.models.__all_models
    
    async with __asyncEngine.begin() as conn:
        # Correção: passar a função, não o resultado
        await conn.run_sync(lambda sync_conn: ModelBase.metadata.drop_all(bind=sync_conn))
        await conn.run_sync(lambda sync_conn: ModelBase.metadata.create_all(bind=sync_conn))
