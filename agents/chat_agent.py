from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

def run_agent(docs, question):
    prompt_template = """Use the following context to answer the question.
    If you don't know the answer, just say "I don't know." Don't try to make up an answer.

    Context:
    {context}

    Question:
    {question}
    """

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = load_qa_chain(llm=llm, chain_type="stuff", prompt=prompt)
    result = chain.run(input_documents=docs, question=question)

    return result
