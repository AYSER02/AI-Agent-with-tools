from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from tools import get_skills_by_category

llm = ChatOpenAI(temperature=0)

tools = [get_skills_by_category]

agent_executor = create_react_agent(llm, tools)

if __name__ == "__main__":
    while True:
        user_input = input("\nAsk a question (or 'exit'): ")
        if user_input.lower() == "exit":
            break

        response = agent_executor.invoke({"messages": [("user", user_input)]})
        print("\nAgent Response:")
        print(response["messages"][-1].content)
