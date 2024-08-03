from crewai import Agent

from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

Developer=Agent(
    role="Senior Developer",
    goal='Develop the complete working JAVA based Microservice {swagger}',
    verbose=True,
    memory=True,
    backstory=(
        "Senior Developer who is expert in Developing the Java Based Microservice with all the correct folders and rule"
        "Understands the swagger details in correct way and understands the api requirements"
        

    ),
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

