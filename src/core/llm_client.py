import os
from pathlib import Path
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI
from google import genai
from ollama import Client as OllamaClient
from anthropic import Anthropic

# Read the env file
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Read configuration from .env file
PROVIDER = os.getenv("PROVIDER", "openai").lower()
MODEL = os.getenv("MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

Message = Dict[str, str]

def chat(messages: List[Message]) -> str:
    if not messages:
        raise ValueError("messages cannot be empty")
    if PROVIDER == "openai":
        return _call_openai(messages)

    if PROVIDER == "ollama":
        return _call_ollama(messages)

    if PROVIDER == "google":
        return _call_gemini(messages)

    else:
        raise NotImplementedError(f"Provider '{PROVIDER}' not supported yet")

def _call_openai(messages: List[Message]) -> str:
    """Call OpenAI API."""
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY not set in .env")

    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=MODEL, messages=messages
    )
    return response.choices[0].message.content

def _call_gemini(messages: List[Message]) -> str:
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY is not set in the .env file")

    client = genai.Client(api_key=GOOGLE_API_KEY)

    system_text = ""
    contents = []
    for msg in messages:
        if msg["role"] == "system":
            system_text = msg["content"]
        elif msg["role"] == "user":
            contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
        elif msg["role"] == "assistant":
            contents.append({"role": "model", "parts": [{"text": msg["content"]}]})

    config = genai.types.GenerateContentConfig(
        temperature=0,
        system_instruction=system_text if system_text else None,
    )
    response = client.models.generate_content(
        model=MODEL, contents=contents, config=config
    )
    return response.text

def _call_ollama(messages: List[Message]) -> str:
    """Call local Ollama API."""
    client = OllamaClient(host=OLLAMA_HOST)
    response = client.chat(model=MODEL, messages=messages)
    if not response.message or not response.message.content:
        raise RuntimeError("Ollama returned empty response. Is Ollama running?")
    return response.message.content

def call_anthropic(messages: List[Message]) -> str:
    """Call Anthropic API."""
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY is not set in .env")

    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    # Convert messages to Anthropic format
    anthro_messages = []
    for msg in messages:
        if msg["role"] == "system":
            anthro_messages.append({"role": "system", "content": msg["content"]})
        elif msg["role"] == "user":
            anthro_messages.append({"role": "user", "content": msg["content"]})
        elif msg["role"] == "assistant":
            anthro_messages.append({"role": "assistant", "content": msg["content"]})

    response = client.completions.create(
        model=MODEL,
        messages=anthro_messages,
        max_tokens_to_sample=1000,
        temperature=0.7,
    )
    return response.completion