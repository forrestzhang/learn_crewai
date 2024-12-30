from crewai.flow.flow import Flow, listen, start, router
from pydantic import BaseModel
import random

class ExampleState(BaseModel):
    sucess_flag: bool = False

class RouterFlow(Flow[ExampleState]):
    @start()
    def start_method(self):
        print("Starting the flow")
        random_boolean = random.choice([True, False])
        self.state.sucess_flag = random_boolean
    
    @router(start_method)
    def second_method(self):
        if self.state.sucess_flag:
            return "success"
        else:
            return "failure"
    
    @listen("success")
    def third_method(self):
        print(f"Third method running")

    @listen("failure")
    def fourth_method(self):
        print(f"Fourth method running")


flow = RouterFlow()
# flow.plot()
flow.kickoff()