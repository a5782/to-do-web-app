import streamlit as st
import functions

todos = functions.get_todos("todos.txt")

def add_todo():
     todo = st.session_state['new_todo'] + '\n'
     todos.append(todo)
     functions.write_todos("todos.txt",todos)



st.title("My Aravind Todo App")
st.subheader("i created")
st.write("this is app")
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos("todos.txt",todos)
        del st.session_state[todo]




st.text_input(label=" ",placeholder="Enter a new todo",on_change = add_todo,key="new_todo")


st.session_state