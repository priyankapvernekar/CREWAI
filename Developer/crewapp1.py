from crewai import Crew,Process
from tasks import develop
from agents import Developer
import yaml
## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[Developer],
    tasks=[develop],
    process=Process.sequential,

)

def read_file_line_by_line():
    file_path = input("Enter the file path: ")
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file: {exc}")

# Usage
swagger_details=read_file_line_by_line()

## starting the task execution process wiht enhanced feedback

  
result=crew.kickoff(inputs={'swagger':swagger_details})
print(result)