from langchain.agents import initialize_agent, Tool
from langchain.memory import ConversationBufferWindowMemory

tools = [
    Tool(
        name="Log Analyzer",
        description="Analyze log entries for security threats",
        func=analyze_logs
    ),
    Tool(
        name="CVE Lookup",
        description="Look up CVE information and patches",
        func=cve_lookup
    ),
    Tool(
        name="Command Recommender",
        description="Recommend security commands and fixes",
        func=recommend_commands
    )
]

agent = initialize_agent(
    tools=tools,
    llm=openai_llm,
    agent_type="CONVERSATIONAL_REACT_DESCRIPTION",
    memory=ConversationBufferWindowMemory(k=10)
)