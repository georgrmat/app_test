import streamlit as st

def home():
    st.title("Home Page")
    st.sidebar.write("Sidebar content for Home Page")
    st.write("Welcome to the Home Page!")

def page_one():
    def test():
        st.title("Page 1")
        st.sidebar.write("Sidebar content for Page 1")
        num = st.sidebar.selectbox("choose", [1, 2, 3])
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
    main()
