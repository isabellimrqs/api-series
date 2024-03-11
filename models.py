from typing import Optional
from pydantic import BaseModel

class Serie(BaseModel):
    id: Optional[int] = None
    nome: str |  None = None
    ano_lancamento: int |  None = None
    total_premios: int |  None = None

