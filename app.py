import streamlit as st
import random

def home():
    st.title("Home Page")
    with st.sidebar:
        st.write("Home Page Sidebar")
        selected_page = st.selectbox("Select Page", ["Home", "Page 1", "Page 2"])
        st.write(f"Selected Page: {selected_page}")

    st.write("Welcome to the Home Page!")

def page_one():
    st.title("Page 1")
    with st.sidebar:
        st.write("Page 1 Sidebar")
        selected_page = st.selectbox("Select Page", ["Home", "Page 1", "Page 2"])
        st.write(f"Selected Page: {selected_page}")

    st.write("This is Page 1.")
    st.write("Random Number in Page 1:", random.randint(1, 100))

def page_two():
    st.title("Page 2")
    with st.sidebar:
        st.write("Page 2 Sidebar")
        selected_page = st.selectbox("Select Page", ["Home", "Page 1", "Page 2"])
        st.write(f"Selected Page: {selected_page}")

    st.write("You are now on Page 2.")
    st.write("Random Number in Page 2:", random.randint(1, 100))

def main():
    pages = ["Home", "Page 1", "Page 2"]
    choice = st.sidebar.selectbox("Select Page", pages)

    if choice == "Home":
        home()
    elif choice == "Page 1":
        page_one()
    elif choice == "Page 2":
        page_two()

if __name__ == "__main__":
    main()
