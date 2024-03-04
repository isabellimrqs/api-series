from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, Any, List
import uvicorn
from models import Serie
from time import sleep
from fastapi.encoders import jsonable_encoder

app = FastAPI()

def fake_db():
    try:
        print('abrindo conexão com banco de dados')
        sleep(1)
    finally:
        print('fechando conexão com banco de dados')
        sleep(1)

series = {
    1: {"nome": "friends", 
        "ano_lancamento": 1994, 
        "total_premios": 24 },
    2: {
        "nome": "the good place", 
        "ano_lancamento": 2016, 
        "total_premios": 4 
    },
    3: {
        "nome": "the last of us", 
        "ano_lancamento": 2023, 
        "total_premios": 16 
    },
    4: {
        "nome": "the office", 
        "ano_lancamento": 2005, 
        "total_premios": 20 
    },
    5: {
        "nome": "how i met yout mother", 
        "ano_lancamento": 2005, 
        "total_premios": 10 
    },
    6: {
        "nome": "gilmore girls", 
        "ano_lancamento": 2000, 
        "total_premios": 5 
    },
    7: {
        "nome": "brooklyn 99", 
        "ano_lancamento": 2013, 
        "total_premios": 6 
    },
    8: {
        "nome": "greys anatomy", 
        "ano_lancamento": 2005, 
        "total_premios": 36 
    },
    9: {
        "nome": "prison break", 
        "ano_lancamento": 2005, 
        "total_premios": 3 
    },
    10: {
        "nome": "breaking bad", 
        "ano_lancamento": 2008, 
        "total_premios": 28 
    },

}

@app.get("/")
async def home():
    return {"Total de séries na API": len(series)}

@app.get('/all_series' )
async def get_series(db: Any = Depends(fake_db)):
    return series

@app.get("/serie/{id_serie}")
async def get_serie(id_serie: int):
    if id_serie in series:
        return series[id_serie]
    else: 
        return {"Erro": "ID inexistente"}

@app.post("/serie")
async def post_serie(serie: Optional[Serie] = None):
    if serie.id not in series:
        next_id = len(series) + 1
        series[next_id] = serie
        del serie.id
        return serie
    
@app.delete("/serie/{id_serie}")
async def del_serie(id_serie: int, serie: Serie):
    if id_serie in series:
        del series[id_serie]
        return {"Deletada a série {id_serie}"}
    
@app.put('/serie/{id_serie}')
async def put_serie(id_serie: int, serie: Serie):
    if id_serie in series:
        series[id_serie] = serie
        serie.id = id_serie
        return serie
    else:
        return{"Erro": "Não existe uma série com esse ID"}
    
@app.patch("/serie/{id_serie}")
async def patch_serie(id_serie: int, serie: Serie):
    stored_item_data = series[id_serie]
    stored_item_model = Serie(**stored_item_data)
    update_data = serie.dict(exclude_unset=True)
    updated_item = stored_item_model.model_copy(update=update_data)
    series[id_serie] = jsonable_encoder(updated_item)
    return updated_item
    
    
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
