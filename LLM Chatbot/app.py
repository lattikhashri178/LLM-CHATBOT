import streamlit as st

from langchain_ollama import ChatOllama

from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.messages import SystemMessage


# 1. Page configuration

st.set_page_config(
    page_title="Friend AI Chatbot",
    page_icon="💬"
)


# 2. Application title

st.title("💬 Friend AI Chatbot")

st.write("Your friendly personal AI assistant!")


# 3. Connect to local LLM

llm = ChatOllama(
    model="gemma3:1b",
    temperature=0.8
)


# 4. Create conversation memory

if "memory" not in st.session_state:

    st.session_state.memory = InMemoryChatMessageHistory()


# 5. Create sidebar

st.sidebar.title("Chat Settings")

st.sidebar.write("Talk with your personal AI assistant.")

if st.sidebar.button("Clear Conversation"):

    st.session_state.memory.clear()

    st.rerun()


# 6. Display previous messages

for message in st.session_state.memory.messages:

    if message.type == "human":

        with st.chat_message("user"):

            st.write(message.content)

    elif message.type == "ai":

        with st.chat_message("assistant"):

            st.write(message.content)


# 7. Get user input

user_input = st.chat_input("Type your message here...")


# 8. Generate AI response

if user_input:

    # Display user message

    with st.chat_message("user"):

        st.write(user_input)


    # Store user message in memory

    st.session_state.memory.add_user_message(user_input)


    # Create system instructions

    messages = [

        SystemMessage(

            content="You are a friendly personal AI assistant. "
                    "Answer questions in simple English. "
                    "Be helpful, polite and friendly."

        )

    ] + st.session_state.memory.messages


    # Generate response

    with st.chat_message("assistant"):

        with st.spinner("AI is thinking..."):

            response = llm.invoke(messages)

            st.write(response.content)


    # Store AI response in memory

    st.session_state.memory.add_ai_message(
        response.content
    )