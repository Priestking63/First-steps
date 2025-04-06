from fastapi import Depends, FastAPI, HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel


app = FastAPI()

class PostResponse(BaseModel):
    id : int
    text: str
    topic: str

    class Config:
        orm_mode = True

def get_db():
    conn = psycopg2.connect(
    "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml",
    cursor_factory=RealDictCursor
   )
    return conn

@app.get('/post/{id}',response_model=PostResponse)
def post_id(id:int, db = Depends(get_db))->PostResponse:
    with db.cursor() as cursor:
        cursor.execute(
             f"""SELECT id, text, topic
                 FROM post
                 WHERE id = {id}
              """)
        result = cursor.fetchone()
        if not result:
            raise HTTPException(404)
        else:
            return PostResponse(**result)
    