import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="My Awesome Personal Website",
        page_icon="🌟",
        layout="wide"
    )
    
    # Title and introduction
    st.title("My Awesome Personal Website")
    st.subheader("Welcome!")
    st.write("""
        Hi, I'm [Your Name]. This website is built with **Streamlit**, a Python library for creating interactive web apps.
        Here you can learn more about my work, projects, and interests.
    """)

    # About Me Section
    st.header("About Me")
    st.write("""
        I am a passionate developer/data scientist/engineer (choose your own path) with a keen interest in creating interactive tools and visualizations.
        My expertise includes Python, machine learning, and web development.
    """)

    # Projects Section
    st.header("Projects")
    st.write("Below are some of my notable projects:")
    
    # Create a simple layout with columns for project cards
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/250x150", caption="Project 1")
        st.write("Project 1 Description")
        st.markdown("[Learn more](#)")
    with col2:
        st.image("https://via.placeholder.com/250x150", caption="Project 2")
        st.write("Project 2 Description")
        st.markdown("[Learn more](#)")
    with col3:
        st.image("https://via.placeholder.com/250x150", caption="Project 3")
        st.write("Project 3 Description")
        st.markdown("[Learn more](#)")

    # Contact Section
    st.header("Contact")
    st.write("""
        Feel free to reach out to me at [your.email@example.com](mailto:your.email@example.com) or connect with me on [LinkedIn](#).
    """)

if __name__ == "__main__":
    main()

