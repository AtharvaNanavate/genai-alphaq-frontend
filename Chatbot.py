import streamlit as st
import pieces_os_client as pos_client
from api import *

# Initialize variables
pieces_os_version = None
asset_ids = {}  # Asset ids for any list or search
assets_are_models = False
current_asset = {}
parser = None
query = ""



# Initialize the WebSocket Manager if it doesn't exist in the session state
# if "ws_manager" not in st.session_state:
#     st.session_state.ws_manager = WebSocketManager()

# Streamlit UI
st.markdown(""" <style>.centered-title {text-align: center; font-size : 80px; color: #202c38; }</style> """, unsafe_allow_html=True)
st.markdown(""" <style> .stApp { color: #202c38; background-color: white !important;}</style> """, unsafe_allow_html=True)
st.markdown("<h1 class ='centered-title'>Barclays Know</h1>", unsafe_allow_html=True)
st.image("image.png", caption="Barclays Know", width=300)
st.markdown(
    """
    <style>
    .element-container {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize chat history for Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Ask me Anything - Barclays Know"}]

# Display chat messages from history on the app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process and store Query and Response
# def pieces_copilot_function(query):
#     with st.chat_message("user"):  # Displaying the User Message
#         st.markdown(query)
#     try:
#         # Storing the User Message
#         st.session_state.messages.append({"role": "user", "content": query})
#         with st.chat_message("assistant"):
#             # Call the WebSocketManager to generate a response using the single, hardcoded model
#             response = st.write_stream(st.session_state.ws_manager.message_generator(query))
#         st.session_state.messages.append({"role": "assistant", "content": response})
#     except Exception as e:
#         print(f"Error occurred while asking the question: {e}")

# Custom CSS to style the chat input
st.markdown(
    """
    <style>
    .st-emotion-cache-128upt6.ea3mdgi6{
        background-color: #202c38 !important;}
    .st-ae.st-b1.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b5.st-b6.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-b8.st-b9.st-ba.st-bv.st-bc.st-bd.st-be.st-bw.st-bx.st-by.st-bz.st-c2 : focus{ {
        background-color: white !important;
        color: grey !important;
        font-size: 40px !important;
        padding: 1px !important;
        
        
    }
    .st-ae.st-b1.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b5.st-b6.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-b8.st-b9.st-ba.st-bv.st-bc.st-bd.st-be.st-bw.st-bx.st-by.st-bz.st-c2 {
        transition : none !important;
        transform: none !important;  

    }

  
    .st-ae.st-b1.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b5.st-b6.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-b8.st-b9.st-ba.st-bv.st-bc.st-bd.st-be.st-bw.st-bx.st-by.st-bz.st-c2 :hover , 
    .st-ae.st-b1.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b5.st-b6.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-b8.st-b9.st-ba.st-bv.st-bc.st-bd.st-be.st-bw.st-bx.st-by.st-bz.st-c2 : focus , 
    .st-ae.st-b1.st-bf.st-bg.st-bh.st-bi.st-bj.st-bk.st-bl.st-bm.st-b5.st-b6.st-bn.st-bo.st-bp.st-bq.st-br.st-bs.st-bt.st-bu.st-b8.st-b9.st-ba.st-bv.st-bc.st-bd.st-be.st-bw.st-bx.st-by.st-bz.st-c2 : active {
    font-size: 40px !important;
    transition: none !important;
    transform: none !important;
   
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the chat input
query = st.chat_input("Ask a question to the Barclays Know")

# # Calling the Function when Input is Provided
# if query:
#     if st.session_state.ws_manager.loading:
#         st.warning('Hold on there is already a response generating', icon="⚠️")
#     else:
#         pieces_copilot_function(query)

sample_responses = [
    "Hi there! How can I assist you today?",
    "I don't have access to your actual model, but I can provide some sample responses for testing.",
    "Sure, I'd be happy to help. What would you like to know?",
    "Unfortunately, I don't have the capability to generate dynamic responses at the moment. But I can still chat with you!",
    "Hmm, I don't have enough information to provide a meaningful response. Could you please rephrase your question?"
]

# Process and store Query and Response
def mock_chatbot_response(query):
    with st.chat_message("user"):
        st.markdown(query)

    try:
        # Storing the User Message
        st.session_state.messages.append({"role": "user", "content": query})

        # Generate a mock response
        mock_response = st.write(st.selectbox("Responses", sample_responses))

        # Store the Assistant's Response
        st.session_state.messages.append({"role": "assistant", "content": mock_response})
    except Exception as e:
        print(f"Error occurred while asking the question: {e}")

# Call the mock chatbot function when input is provided
if query:
    mock_chatbot_response(query)