import streamlit as st

def main():
    st.set_page_config(page_title="POC Projects Landing Page", layout="wide")

    st.title("Welcome to Our POC Projects")
    st.write("Explore our innovative proof of concept projects selected for this AI workshop.:")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.subheader("Say What You Can See")
        st.image("poc_0.png", width=150)
        st.write("Learn the art of image prompting with the help of Google AI. Try to generate matching images with your own prompts.")
        st.markdown("[Play a simple game!](https://artsandculture.google.com/experiment/say-what-you-see/jwG3m7wQShZngw?hl=en)", unsafe_allow_html=True)

    with col2:
        st.subheader("Ghostwriter Basic")
        st.image("poc_1.png", width=150)
        st.write("AI-powered author services for various content types to help initiate ideas.")
        st.markdown("[Explore Project](https://hpg-ghostwriter-basic.streamlit.app/)", unsafe_allow_html=True)

    with col3:
        st.subheader("Ghostwriter Advanced")
        st.image("poc_2.png", width=150)
        st.write("AI-powered author services with more options to steer the book generation for various content types to help initiate ideas.")
        st.markdown("[Explore Project](https://hpg-ghostwriter-basic.streamlit.app/advanced)", unsafe_allow_html=True)

    with col4:
        st.subheader("Notebook LM")
        st.image("notebook.png", width=150)
        st.write("Interact with any of your internal documents. Internal HR documents, travel policies, legal contracts, etc.")
        st.markdown("[Private](https://notebooklm.google.com/notebook/7befb094-a5a2-43f7-87cf-8d22b4ea1c99)", unsafe_allow_html=True)
        st.markdown("[Corporate](https://notebooklm.google.com/notebook/b5427c43-cdc8-4703-85f9-b0a4e6f20e78)", unsafe_allow_html=True)

    with col5:
        st.subheader("Hey Gen")
        st.image("hey_gen.png", width=150)
        st.write("Create a custom avatar of yourself train your voice to generate custom content. (Hardware provided)")
        st.markdown("[Create your own custom avatar!](https://www.heygen.com/)", unsafe_allow_html=True)

    # Add some space between rows
    st.write("")
    st.write("")

    # Second row
    col6, col7, col8, col9, col10 = st.columns(5)

    with col6:
        st.subheader("Talk with Data")
        st.image("https://via.placeholder.com/150", width=150)
        st.write("Interact with your data through natural language queries.")
        st.markdown("[Explore Project](https://external-url-for-project1.com)", unsafe_allow_html=True)

    with col7:
        st.subheader("Illuminate")
        st.image("illuminate.png", width=150)
        st.write("Generate short podcasts with your published content.")
        st.markdown("[Listen to summary  AI podcasts](https://illuminate.google.com/home?pli=1)", unsafe_allow_html=True)

    with col8:
        st.subheader("Build your own app")
        st.image("https://via.placeholder.com/150", width=150)
        st.write("Use AI to quickly build small custom applications for your teams to solve small, very specific problems.")
        st.markdown("[Explore Project](https://claude.ai/)", unsafe_allow_html=True)

    with col9:
        st.subheader("Novel Science Ideas")
        st.image("https://via.placeholder.com/150", width=150)
        st.write("Test the novelty of your scientific ideas and generate new ones.")
        st.markdown("[Explore Project](project9.py)", unsafe_allow_html=True)

    with col10:
        st.subheader("Oxford English Dictionary")
        st.image("oxford.png", width=150)
        st.write("Automate the process of using the correct words for your region in your manuscripts. Built using artefacts.")
        st.markdown("[Explore Project](https://oed-basic.streamlit.app/)", unsafe_allow_html=True)

st.subheader("Additional Tools", divider=True)


if __name__ == "__main__":
    main()