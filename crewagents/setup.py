from crewai import Crew
from crewagents.agents import agent_all
from crewagents.tasks import task_all

def run_crew(query, context):
    researcher, writer = agent_all().get_agents()
    tasks = task_all().create_tasks(query, context, researcher, writer)
    crew = Crew(agents=[researcher, writer], tasks=tasks, verbose=True)

    return crew.kickoff()