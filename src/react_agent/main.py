import asyncio
from react_agent.graph import graph
from langchain_core.messages import HumanMessage

async def run_graph_agent():
    print("Welcome to the Graph Agent! Type 'exit' to quit.")
    
    while True:
        user_input = input("> ")  # Prompt for user input
        if user_input.lower() == 'exit':
            print("Exiting the Graph Agent. Goodbye!")
            break
        
        # Create a HumanMessage with the user input
        message = HumanMessage(content=user_input)
        
        # Invoke the graph with the user input
        response = await graph.ainvoke({"messages": [message]})
        
        # Print the agent's response
        if response and "messages" in response:
            print(f"Agent: {response['messages'][-1].content}")
        else:
            print("Agent: I didn't understand that.")

if __name__ == "__main__":
    asyncio.run(run_graph_agent())
