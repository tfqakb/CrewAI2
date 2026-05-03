from crewai import Agent
from langchain_groq import ChatGroq

llm = ChatGroq(model="gpt-4o", temperature=0.7)

class agent_all:
    def __init__(self):
        pass

    def get_agents(self):
        self.researcher = Agent(role="Research Analyst", goal = "Analyze retrieved documents and extract key" \
        " insights, trends.", backstory="A research analyst with expertise in data analysis", 
        llm=llm, verbose=True)

        self.writer = Agent(role="Content Writer", goal="Generate clear and concise content based on the insights" \
        "extracted", backstory="A content writer expert in explainging complex topics", llm=llm, verbose=True)
