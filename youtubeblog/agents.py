from crewai import Agent
from tools import tool

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"


llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))
###blog researcher


blogResearch=Agent(
    role=" blog Reseacher from youtube videos",
    goal="get the relevant video content from the topic{topic} from Yt channel",
    name="Researcher",
    verbose=True,
    memory=True,
    backstory=("Expert in understanding videos in AI Data Science , MAchine Learning And GEN AI and providing suggestion"),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

#writer agent

writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about the video {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)