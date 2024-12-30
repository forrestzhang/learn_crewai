from crewai.flow.flow import Flow, listen, start
from litellm import completion
from dotenv import load_dotenv


load_dotenv()

"""
response = completion(
    model="ollama/qwen2.5:14b", 
    messages=[{ "content": "respond in 20 words. who are you?","role": "user"}], 
    api_base="http://localhost:11434"
)
print(response)
"""

class ExampleFlow(Flow):

    model = "ollama/qwen2.5:14b"

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