import streamlit as st
from llm import Chatbot

CHAT_HISTORY_KEY = "chat_history"

# --- CACHING SETUP ---
@st.cache_resource
def get_chatbot():
    return Chatbot(model_name="Qwen/Qwen2.5-1.5B-Instruct", use_gpu=False)

def initialize_session_state():
    if CHAT_HISTORY_KEY not in st.session_state:
        st.session_state[CHAT_HISTORY_KEY] = [
            {"role": "system", "content": "You are a helpful AI assistant. Your answers are concise and to the point."}
        ]

def display_chat_history():
    for message in st.session_state[CHAT_HISTORY_KEY]:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

def handle_user_input(chatbot_instance, temperature, max_history, max_tokens):
    if user_input := st.chat_input("Ask something..."):
        
        # 1. Append input user
        st.session_state[CHAT_HISTORY_KEY].append({"role": "user", "content": user_input})
        
        # 2. Remove History > max_history
        if len(st.session_state[CHAT_HISTORY_KEY]) > (max_history * 2) + 1:
            st.session_state[CHAT_HISTORY_KEY] = [st.session_state[CHAT_HISTORY_KEY][0]] + \
                                                st.session_state[CHAT_HISTORY_KEY][-(max_history * 2 + 1):]
        
        # 3. Show input user
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # 4. Generate output
        with st.spinner("AI thinking..."):
            with st.chat_message("assistant"):
                response = chatbot_instance.generate_response(
                    chat_history=st.session_state[CHAT_HISTORY_KEY],
                    temperature=temperature,
                    max_tokens=max_tokens
                )
                st.markdown(response)
        
        # 5. Append response
        st.session_state[CHAT_HISTORY_KEY].append({"role": "assistant", "content": response})

def main():
    st.set_page_config(page_title="Chatbot Basic", layout="wide")
    st.title("Chatbot Basic")

    # --- SIDEBAR ---
    with st.sidebar:
        st.header("⚙️ Config")
        temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
        max_history = st.selectbox("Chat memory", range(1, 11), index=2)
        max_tokens = st.selectbox("Max Tokens", [256, 512, 1024], index=1)
        st.divider()
        if st.button("Clear Chat"):
            st.session_state[CHAT_HISTORY_KEY] = [st.session_state[CHAT_HISTORY_KEY][0]]
            st.rerun()

    # --- MAIN FLOW ---
    # 1. Get Instance
    bot = get_chatbot()
    
    # 2. Create UI
    initialize_session_state()
    display_chat_history()
    
    # 3. Logic
    handle_user_input(bot, temperature, max_history, max_tokens)

if __name__ == "__main__":
    main()