import streamlit as st
import functions

todos = functions.get_todos("todos.txt")
st.title("My Todo App")
st.subheader("se")
st.write("this is app")
for todo in todos:
    st.checkbox(todo)


st.text_input(label="",placeholder="Enter a new todo")