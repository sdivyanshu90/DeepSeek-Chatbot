import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from embedding import get_embedding_function
import re

CHROMA_PATH = "chroma"

PROMPT= """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context in a brief: {question}
"""

def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)



def remove_think_tags(response):
    return re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL)

def query_rag(query: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query, k=5)

    context = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT)
    prompt = prompt_template.format(context=context, question=query)
    # print(prompt)

    #model = Ollama(model="mistral")
    model = Ollama(model="deepseek-r1")
    #model = Ollama(model="llama3")
    response_text = model.invoke(prompt)
    response = remove_think_tags(response_text)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response


if __name__ == "__main__":
    main()