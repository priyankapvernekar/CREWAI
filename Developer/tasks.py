
from crewai import Task
from agents import Developer

# Research task
develop = Task(
  description=(
    "Identify all the api's ,response , out put from the given swagger{swagger}.create the folder structure in the local and then add all the program/code according to that folder structure which is followed by developers when they develop the JAVA microservice"
    "develop the complete working java based microservice with correct folder structure with controller Model service classes "
    "Add the exception class with custom exception if required"
    
  ),
  expected_output='A completely working JAVA based microservice with correct folder structure as per JAVA guidelines ',
  agent=Developer,
)

# Writing task with language model configuration
