import streamlit as st

def main():
    
    st.set_page_config(page_title="POC Projects Landing Page", layout="wide")
    st.sidebar.image("logo.png", use_column_width=True)
    st.sidebar.title("CEO Retreat")
    st.sidebar.write("""Welcome! \n\nThis part of the retreat is dedicated to exploring some of the existing 
                     technologies you can use right now and touching on some of the new innovations 
                     we will explore in the future.""")


    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Say What You Can See")
        st.image("poc_0.png", width=150)
        st.write("Learn the art of image prompting with the help of Google AI. Try to generate matching images with your own prompts.")
        st.markdown("[Play a simple game!](https://artsandculture.google.com/experiment/say-what-you-see/jwG3m7wQShZngw?hl=en)", unsafe_allow_html=True)

    with col2:
        st.subheader("Ghostwriter")
        st.image("poc_2.png", width=150)
        st.write("AI-powered author services with more options to steer the book generation for various content types to help initiate ideas")
        st.markdown("[Explore Project](https://hpg-ghostwriter-basic.streamlit.app/advanced)", unsafe_allow_html=True)

    #with col3:
        #st.subheader("Ghostwriter Advanced")
        #st.image("poc_2.png", width=150)
        #st.write("AI-powered author services with more options to steer the book generation for various content types to help initiate ideas.")
        #st.markdown("[Explore Project](https://hpg-ghostwriter-basic.streamlit.app/advanced)", unsafe_allow_html=True)

    # Add some space between rows
    st.write("")
    st.write("")

    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Notebook LM")
        st.image("notebook.png", width=150)
        st.write("Interact with any of your internal documents. Internal HR documents, travel policies, legal contracts, etc.")
        st.markdown("[Chat with your documents](https://notebooklm.google.com/)", unsafe_allow_html=True)

    with col4:
        st.subheader("Podcasts")
        st.image("illuminate.png", width=150)
        st.write("Generate short podcasts with your published content.")
        st.markdown("[Listen to summary AI podcasts](https://illuminate.google.com/home?pli=1)", unsafe_allow_html=True)

    # Add some space between rows
    st.write("")
    st.write("")

    # Second row
    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Build your own app")
        st.image("https://via.placeholder.com/150", width=150)
        st.write("Use AI to quickly build small custom applications for your teams to solve small, very specific problems.")
        st.markdown("[Let's Build!](https://artifacts.e2b.dev/)", unsafe_allow_html=True)

    with col6:
        st.subheader("Hey Gen")
        st.image("hey_gen.png", width=150)
        st.write("Create a custom avatar of yourself train your voice to generate custom content. (Hardware provided)")
        st.markdown("[Create your own custom avatar!](https://www.heygen.com/)", unsafe_allow_html=True)

    # Add some space between rows
    st.write("")
    st.write("")


    st.subheader("Additional Tools", divider=True)



if __name__ == "__main__":
    main()