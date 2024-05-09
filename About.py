import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to SkinCancerAI! 👋")

# st.sidebar.success()

st.markdown(
    """
    Skin cancer is one the most dangerous types of cancer and is one of the primary causes of death worldwide.
    Melanoma is a type of cancer that can be deadly if not detected early. It accounts for 75% of skin cancer deaths. A solution which can evaluate images and alert the dermatologists about the presence of melanoma has the potential to reduce a lot of manual effort needed in diagnosis. \n 
    As college students committed to harnessing the power of technology for societal benefit, we've developed this platform to streamline the detection and classification of skin cancer. \n
    **👈 Select a demo from the sidebar** to check out our model  \n

    ### :blue[Types of Skin Cancer]
    - Melanocytic Nevi(NV)
    - Melanama(MEL)
    - Benign Keratosis-like Lesion(BKL)
    - Dermatofibroma(DF)
    - Basal Cell Carcinoma(BCC)
    - Actinic Keratoses(Akiec)
    - Vascular Lesions(Vasc)
    ### :blue[Harnessing Advanced Technology]

    Behind the scenes, SkinCancerAI utilizes advanced technologies like convolutional neural networks (CNNs) to analyze images 
    with precision. While the technology may sound complex, our goal is to make the process seamless for users,
    providing accurate results without the need for specialized knowledge. 💻   \n

    ### :blue[How it works?]
    To get started, simply upload an image of a skin lesion and let SkinCancerAI provide you with valuable insights. 
    Together, let's make a difference in the fight against skin cancer. Welcome to SkinCancerAI! 🌿




    
"""
,unsafe_allow_html=True)