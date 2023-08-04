from judini.agent import Agent

api_key = ""
agent_id = ""

agent = Agent(api_key, agent_id)

prompt = ""
response = agent.completion(prompt)
print(response)

