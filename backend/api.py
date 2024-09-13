from colorama import AnsiToWin32
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from knowledge_insertion import sim_search

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/test")
def test():
    return {"message": "ok!", "status": 200}


@app.get("/question/{question}")
def question(question: str):
    print(f"Received question: {question}")

    sim_result = sim_search(question=question)

    print(sim_result)

    return {"message": sim_result}
