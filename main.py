from fastapi import FastAPI

app = FastAPI()

# int, str, bool
# dict, set, list, tuple -> collction (자료형)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str) -> dict[str, str]:
    return {"message": f"Hello {name}"}
