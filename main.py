from dotenv import load_dotenv
from pydantic import base_model
from langchain_openai import chatopenai
from langchain_anthropic import chatanthropic   

load_dotenv()
llm=chatopenai(model="gpt-4o-mini")
llm2=chatanthropic(model="claude-3-5-sonnent-20240924"
                   )