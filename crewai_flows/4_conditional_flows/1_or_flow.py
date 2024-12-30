from crewai.flow.flow import Flow, listen, start, or_

class OrFlow(Flow):
    @start()
    def start_method(self):
        print("Starting the flow")
        return "Hello from start flow"
    
    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Hello from second method"
    
    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"logger: {result}")


flow = OrFlow()
flow.plot()
flow.kickoff()