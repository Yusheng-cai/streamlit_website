import streamlit as st

# Configure the page
st.set_page_config(
    page_title="My Professional Website",
    page_icon="🚀",
    layout="wide"
)

# Create a theme toggle at the top of the page
dark_mode = st.checkbox("Dark Mode", value=False)

# Inject custom CSS based on theme selection
if dark_mode:
    custom_css = """
    <style>
    body {
        background-color: #121212;
        color: #ffffff;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background-color: #121212;
    }
    /* Additional dark mode styling */
    .stButton>button {
        background-color: #333333;
        color: #ffffff;
    }
    </style>
    """
else:
    custom_css = """
    <style>
    body {
        background-color: #ffffff;
        color: #000000;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background-color: #ffffff;
    }
    /* Additional light mode styling */
    .stButton>button {
        background-color: #f0f0f0;
        color: #000000;
    }
    </style>
    """
st.markdown(custom_css, unsafe_allow_html=True)

# Create a top navigation menu using Streamlit tabs
tabs = st.tabs(["Home", "Research", "Software"])

with tabs[0]:
    st.title("Welcome to My Professional Website")
    st.write("This is the Home page. Introduce yourself, share your background, and welcome your visitors!")
    st.image("https://via.placeholder.com/1200x400?text=Professional+Banner", use_column_width=True)

with tabs[1]:
    st.title("Research")
    st.write("Explore my research projects, publications, and innovative ideas. More details will be added soon.")
    st.image("https://via.placeholder.com/800x400?text=Research+Banner", use_column_width=True)

with tabs[2]:
    st.title("Software")
    st.write("Discover my software projects, demos, and code repositories. Check out my latest work below.")
    # Example project layout in columns
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/350x200?text=Project+1", use_column_width=True)
        st.subheader("Project One")
        st.write("A brief description of Project One.")
        st.markdown("[Learn More](#)")
    with col2:
        st.image("https://via.placeholder.com/350x200?text=Project+2", use_column_width=True)
        st.subheader("Project Two")
        st.write("A brief description of Project Two.")
        st.markdown("[Learn More](#)")
    with col3:
        st.image("https://via.placeholder.com/350x200?text=Project+3", use_column_width=True)
        st.subheader("Project Three")
        st.write("A brief description of Project Three.")
        st.markdown("[Learn More](#)")

# Optionally add a footer
st.markdown('<div style="text-align:center; margin-top:50px; font-size:0.9rem;">© 2025 My Professional Website. All rights reserved.</div>', unsafe_allow_html=True)

