from fastapi import FastAPI

from knowledge_insertion import sim_search

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/question/{question}")
def question(question: str):
    answer = sim_search(question)
    return {"answer": answer}
