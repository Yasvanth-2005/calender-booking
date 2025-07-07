import os
import shutil
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent

source_path = "/etc/secrets/service_account.json"
destination_folder = "credentials"
destination_path = os.path.join(destination_folder, "service_account.json")

os.makedirs(destination_folder, exist_ok=True)

if os.path.exists(source_path):
    shutil.copy(source_path, destination_path)
    print(f"✅ Copied service_account.json to {destination_path}")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

@app.post("/chat")
def chat(message: Message):
    return {"response": run_agent(message.message)}
