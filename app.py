from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/")
def say_hello():
    return "hello"

@app.get("/sum")
def sum_two(a: int, b: int) -> int:
    return a+b

@app.get("/number/{number}")
def print_num(number:int):
    return number * 2


@app.post('/user')
def print(user: str):
    return {'message': f'hello, {user}'}

@app.get('/booking/all')
def all_bookings():
    conn = psycopg2.connect(
        "postgresql://postgres:password@localhost:5432/exercises"
        )
    cursor = conn.cursor()
    cursor.execude(
        """
        SELECT *
        FROM cd.bookings
        """)
    return cursor.fetchall()
