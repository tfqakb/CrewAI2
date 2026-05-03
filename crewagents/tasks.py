from crewai import Task

class task_all:
    def __init__(self):
        pass

    def create_tasks(self, query, context, researcher, writer)-> list:

        self.task1 = Task(description=f"""
                          Analyze the following context and extract key insights.
                          Context: {context}, Question: {query}""", agent=researcher)
        
        self.task2 = Task(description=f"""
            Write a clear and relevant insights based on research. 
                          Avoid hallucinations. Use only provided context.""", agent=writer)
        
        return [self.task1, self.task2]