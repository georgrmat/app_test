import streamlit as st

def set_custom_style():
    """
    Set custom dark theme using CSS.
    """
    style = """
    <style>
        body {
            color: black;
            background-color: #2E2E2E; /* Dark background color */
        }
        .st-cg {
            color: black !important;
        }
        .st-ei {
            background-color: #2E2E2E !important;
            color: black !important;
        }
        .css-hi9bvv {
            background-color: #2E2E2E !important;
            color: white !important;
        }
        .st-at {
            color: black !important;
        }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def home():
    st.title("Home Page")
    st.sidebar.write("Sidebar content for Home Page")
    st.write("Welcome to the Home Page!")

def page_one():
    st.title("Page 1")
    st.sidebar.write("Sidebar content for Page 1")
    num = st.sidebar.selectbox("choose", [1, 2, 3])
    
    def test():
        st.write(num)
        st.write("This is Page 1.")
    launch = st.sidebar.button("test")
    if launch:
        test()

def page_two():
    st.title("Page 2")
    st.sidebar.write("Sidebar content for Page 2")
    num = st.sidebar.selectbox("choose", [1, 2, 3])
    st.write(num)
    st.write("You are now on Page 2.")

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
    set_custom_style()
    main()
