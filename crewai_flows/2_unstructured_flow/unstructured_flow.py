from crewai.flow.flow import Flow, listen, start

class UnstructuredFlow(Flow):
    
    @start()
    def first_method(self):
        print("Starting the flow")
        print(f"State before first_method:\n{self.state}")
        self.state["message"] = "Hello from structured flow"
        self.state["counter"] = 0
    
    @listen(first_method)
    def second_method(self):
        print(f"State before second_method:\n{self.state}")
        self.state["counter"] += 1
        self.state["message"] += " - updated"
        
    @listen(second_method)
    def third_method(self):
        print(f"State before third_method:\n{self.state}")
        self.state["counter"] += 1
        self.state["message"] += " - updated again"

        print(f"State after third_method: {self.state}")
        
flow = UnstructuredFlow()
flow.kickoff()

print(f"Final state: {flow.state}")