from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def say_hello():
    return "hello"

@app.get("/sum")
def sum_two(a: int, b: int) -> int:
    return a+b