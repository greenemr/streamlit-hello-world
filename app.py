import streamlit as st

# Set the title of the app
st.title("Hello, Streamlit!")

# Add a simple text to the app
st.write("Welcome to your hello world Streamlit app.")

# Add a text input widget
user_input = st.text_input("Enter your name:")

# Greet the user if they enter a name
if user_input:
    st.write(f"Hello, {user_input}! 👋")

# Add a button to display a message
if st.button("Click me!"):
    st.success("You clicked the button!")
