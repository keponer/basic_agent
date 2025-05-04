from agent.agent import Agent

if __name__ == "__main__":
    agent = Agent()

    while True:
        query = input("What can I help you search?")
        response = agent.execute_query(query=query)
        print(response)
        print("Your response has been saved to a file.")
