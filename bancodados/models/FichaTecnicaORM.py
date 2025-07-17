import sqlalchemy as sa
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bancodados.models.model_base import ModelBase



class ModelFichaTecnica(ModelBase):
    __tablename__: str = 'ficha_tecnica'

    ficha_id: Mapped[int] = mapped_column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: Mapped[datetime] = mapped_column(sa.DateTime, default=datetime.now, index=True)

    marca: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    modelo: Mapped[str] = mapped_column(sa.String(200), nullable=False)
    cor: Mapped[str] = mapped_column(sa.String(90), nullable=False)
    ano: Mapped[str] = mapped_column(sa.BigInteger, nullable=False)
    crm: Mapped[str] = mapped_column(sa.String(100), unique=True, nullable=False)
    combustivel: Mapped[str] = mapped_column(sa.String(89), nullable=False)
    km: Mapped[float] = mapped_column(sa.Float, nullable=False)
    motor: Mapped[float] = mapped_column(sa.Float,  nullable=False)
   

    def __repr__(self) -> str:
        return f'<Marca: {self.marca}>'
