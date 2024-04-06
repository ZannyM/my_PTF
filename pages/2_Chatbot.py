import streamlit as st

from information import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
local_css("style/style.css")

st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

# _ _ _ _ _ _ _ _ _ Chat Bot _ _ _ _ _ _ _ _ _ _ _ _ _ #
# with st.chat_message(name="assistant"):
#     st.write("Hello <3")
st.title("My ChatBot-GPT clone")
#create an openai key

if "messages" not in st.session_state: #initialise chat history
    st.session_state.messages = []

#display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#react to user input
if prompt:= st.chat_input("What would you like to know?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user","content": prompt})

    response = f"My Bot: {prompt}"
    #display instant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role":"assistant","content": response})


