from crewai.flow.flow import Flow, listen, start, and_

class AndFlow(Flow):
    @start()
    def start_method(self):
        print("Starting the flow")
        self.state["greeting"] = "Hello from start method"
    
    @listen(start_method)
    def second_method(self):
        print("Second method")
        self.state["joke"] = "What do computers eat? Microchips!"

    @listen(and_(start_method, second_method))
    def logger(self, result):
        print("--- Logger ---")
        print(f"logger: {self.state}")


flow = AndFlow()
flow.kickoff()