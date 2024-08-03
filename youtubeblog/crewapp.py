from crewai import Crew,Process
from agents import blogResearch, writer
from tasks import  research_task,write_task

crew = Crew(
  agents=[blogResearch, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

# Starting the task execution 
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)