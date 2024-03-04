from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id: Optional[int] = None
    nome: str
    ano_lancamento: int
    total_premios: int