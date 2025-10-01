import os
import httpx
from typing import List, Dict, Any

MODEL_API_URL = os.getenv("MODEL_API_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
MODEL_API_KEY = os.getenv("MODEL_API_KEY")

class ModelClient:
    async def generate(self, messages: List[Dict[str, str]]) -> str:
        payload: Dict[str, Any] = {
            "model": MODEL_NAME,
            "messages": messages,
            "max_tokens" : 2000,
            "top_p" : 1,
            "top_k" : 40,
            "presence_penalty" : 0,
            "frequency_penalty" : 0,
            "temperature" : 0.0,
        }

        headers = {
            "Authorization": f"Bearer {MODEL_API_KEY}",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            resp = await client.post(MODEL_API_URL, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()

        return data["choices"][0]["message"]["content"].strip()