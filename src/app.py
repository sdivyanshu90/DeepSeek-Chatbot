import os
import streamlit as st
from query import query_rag
from docs import main as process_uploaded_file

st.set_page_config(page_title="RAGify: Smarter Q&A, Fewer Hallucinations") 
with st.sidebar:
    st.title('DeepSeek RAG Q&A Chatbot')

    uploaded_file = st.file_uploader("📄 Upload a PDF", type=["pdf"])

    if uploaded_file:
        # Save uploaded file to a known path
        save_path = os.path.join("uploaded_files", uploaded_file.name)
        os.makedirs("uploaded_files", exist_ok=True)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        # Process file for embedding
        with st.spinner("Indexing the PDF into the vector store..."):
            try:
                process_uploaded_file(data_path=save_path)
                st.success("✅ File indexed successfully!")
            except Exception as e:
                st.error(f"❌ Error indexing file: {str(e)}")

    if st.button("🧹 Reset Vector DB"):
        clear_database()
        st.success("Vector database cleared.")


# Function for generating LLM response
def generate_response(user_input):
    greeting_keywords = ["hello", "hi", "hey", "hola"]

    if any(greet in user_input.lower() for greet in greeting_keywords):
        return (
            "🌟 Hello and welcome to the DeepSeek Chatbot!\n\n"
            "I'm your AI-powered assistant built on Retrieval-Augmented Generation (RAG), here to help you navigate knowledge with ease.\n"
            "📚 Just drop in your question — whether it's from uploaded documents or your own curiosity — and I'll dig deep to get you a smart, grounded answer.\n\n"
            "Ask me anything to get started! 🚀"
        )

    return query_rag(user_input)

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Welcome, get ready to be mind blown by AI"}]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User-provided prompt
if input := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Getting your answer from intelligence.."):
            response = generate_response(input) 
            
            st.write(response) 
    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)