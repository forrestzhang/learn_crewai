from crewai.flow.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv


load_dotenv()

class ExampleFlow(Flow):

    model = "deepseek/deepseek-chat"

    @start()
    def generate_city(self):
        print("Starting the flow")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world"
                }
            ]
        )

        random_city = response["choices"][0]["message"]["content"]
        print(f"Random city: {random_city}")
        return random_city
    
    @listen(generate_city)
    def generate_fun_fact(self, random_city: str):
        print(f"Received random city: {random_city}")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Return a fun fact about {random_city}"
                }
            ]
        )

        fun_fact = response["choices"][0]["message"]["content"]
        print(f"Fun fact: {fun_fact}")
        return fun_fact


flow = ExampleFlow()
result = flow.kickoff()

print(f"The city is {result}")