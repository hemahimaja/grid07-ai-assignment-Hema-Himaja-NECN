import json
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langgraph.graph import StateGraph
from typing import TypedDict

#load API
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

#define state
class GraphState(TypedDict):
    persona: str
    topic: str
    search_results: str
    post_content: str
    
#mock search tool
@tool
def mock_searxng_search(query:str) -> str:
    """Returns mock search results based on keywords."""
    
    if "crypto" in query.lower():
        return "Bitcoin hits new all-time high amid ETF approvals"
    elif "ai" in query.lower():
        return "OpenAI releases powerful new model impacting jobs"
    elif "markets" in query.lower():
        return "Stock markets rally as interest rates stabilize"
    else:
        return "Tech industry sees mixed developments"
    
#Node 1: Decide Topic
def decide_topic(state: GraphState):
    prompt=f"""
    you are a bot with this persona: {state['persona']}
    Decide a topic you want to post about today. 
    Return ONLY plain text.No quotes.
    """
    response = llm.invoke(prompt)
    topic = response.content.strip().replace("",'')
    
    return {"topic": topic}

#Node 2: web search
def web_search(state: GraphState):
    results = mock_searxng_search.invoke(state["topic"])
    return {"search_results": results}

#Node 3: draft Post
def draft_post(state: GraphState):
    prompt=f"""
    You are a bot with this persona: {state['persona']}
    Topic: {state['topic']}
    Context: {state['search_results']}
    Write a highly opinionated Twitter post (max 280 chars).
    Return ONLY plain text. No quotes.
    """
    response = llm.invoke(prompt)
    post = response.content.strip().replace("",'')
    return {"post_content": post}

#build graph
builder=StateGraph(GraphState)
builder.add_node("decide_topic", decide_topic)
builder.add_node("web_search", web_search)
builder.add_node("draft_post", draft_post)

builder.set_entry_point("decide_topic")

builder.add_edge("decide_topic","web_search")
builder.add_edge("web_search","draft_post")

graph=builder.compile()

#run Graph
if __name__=="__main__":
    persona="I believe AI will transform the world and solve problems."
    result=graph.invoke({"persona": persona})
    output={
        "bot_id":"Bot_A",
        "topic": result["topic"],
        "post_content": result["post_content"]
    }
    print(json.dumps(output, indent=2))