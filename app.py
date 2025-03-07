import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="My Professional Website",
    page_icon="🚀",
    layout="wide"
)

# Inject custom CSS for a professional look
custom_css = """
<style>
/* General styling */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Sidebar customization */
.css-1d391kg {  /* Note: this class may change with Streamlit updates */
    background: linear-gradient(135deg, #2a2a72, #009ffd);
    color: white;
}
.sidebar .sidebar-content {
    background: linear-gradient(135deg, #2a2a72, #009ffd);
}

/* Main content area */
.main {
    background-color: #ffffff;
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

/* Headings */
h1, h2, h3 {
    color: #2a2a72;
}

/* Footer styling */
.footer {
    text-align: center;
    font-size: 0.9rem;
    color: #666;
    margin-top: 50px;
    padding: 1rem 0;
    border-top: 1px solid #eaeaea;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])

# Define the content for each page
def home():
    st.title("Welcome to My Professional Website")
    st.write("This site is built using **Streamlit** and showcases my work and professional achievements.")
    st.image("https://via.placeholder.com/1200x400?text=Professional+Banner", use_column_width=True)

def about():
    st.title("About Me")
    st.write("""
        I am a seasoned professional with expertise in my field.
        With years of experience in developing innovative solutions,
        I strive to combine technology and creativity to deliver outstanding results.
    """)
    st.image("https://via.placeholder.com/400x400?text=Your+Photo", width=300)

def projects():
    st.title("Projects")
    st.write("Below are some of my notable projects:")
    # Display projects in a 3-column layout
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://via.placeholder.com/350x200?text=Project+1", use_column_width=True)
        st.subheader("Project One")
        st.write("A brief description of project one, highlighting key features and innovations.")
        st.markdown("[Learn More](#)")
    with col2:
        st.image("https://via.placeholder.com/350x200?text=Project+2", use_column_width=True)
        st.subheader("Project Two")
        st.write("A brief description of project two, focusing on creative problem-solving and design.")
        st.markdown("[Learn More](#)")
    with col3:
        st.image("https://via.placeholder.com/350x200?text=Project+3", use_column_width=True)
        st.subheader("Project Three")
        st.write("A brief description of project three, showcasing technical expertise and leadership.")
        st.markdown("[Learn More](#)")

def contact():
    st.title("Contact")
    st.write("Feel free to reach out via the following channels:")
    st.markdown("""
    **Email:** [your.email@example.com](mailto:your.email@example.com)  
    **LinkedIn:** [LinkedIn Profile](https://www.linkedin.com)  
    **GitHub:** [GitHub Profile](https://github.com)
    """)
    
    st.subheader("Send a Message")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for your message! I will get back to you soon.")

# Render the selected page
if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Projects":
    projects()
elif page == "Contact":
    contact()

# Add a footer
st.markdown('<div class="footer">© 2025 My Professional Website. All rights reserved.</div>', unsafe_allow_html=True)

