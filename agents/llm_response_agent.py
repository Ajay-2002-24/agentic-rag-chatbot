# agents/llm_response_agent.py
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.schema import Document

def llm_response_agent(mcp_message):
    context = mcp_message["payload"]["retrieved_context"]
    query = mcp_message["payload"]["query"]

    docs = [Document(page_content=chunk) for chunk in context]
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")
    answer = chain.run(input_documents=docs, question=query)

    return answer
