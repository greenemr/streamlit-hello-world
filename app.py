import streamlit as st

# Page configuration
st.set_page_config(page_title="Always-On Insights", layout="wide")

# Header navigation bar
st.markdown('<img src="https://github.com/greenemr/streamlit-hello-world/blob/main/AOI%20Header%201.png" width="100%">', unsafe_allow_html=True)

st.markdown("""
    <style>
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #F0EADC;
            padding: 10px 20px;
            border-bottom: 1px solid #dee2e6;
        }
        .nav-links a {
            margin-right: 15px;
            text-decoration: none;
            color: #007bff;
            font-weight: 500;
        }
        .nav-links a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="header">
        <div class="nav-links">
            <a href="#sales">Sales</a>
            <a href="#operations">Operations</a>
            <a href="#digital">Digital</a>
            <a href="#menu-mix">Menu Mix</a>
            <a href="#loyalty">Loyalty</a>
            <a href="#customer">Customer</a>
            <a href="#supply-chain">Supply Chain</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("Hello, Streamlit!")
st.write("Welcome to your hello world Streamlit app.")

# Add a text input widget
user_input = st.text_input("Enter your name:")

# Greet the user if they enter a name
if user_input:
    st.write(f"Hello, {user_input}! 👋")

# Add a button to display a message
if st.button("Click me!"):
    st.success("You clicked the button!")

# Sidebar
st.sidebar.title("Navigation")
st.sidebar.info("This sidebar can include links, help, or other info.")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit")
