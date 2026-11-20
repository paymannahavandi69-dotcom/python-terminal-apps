import streamlit as st
import json
import os

# 1. Title
st.title("Todo List")

# 2. Session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# 3. Add form
with st.form("add_form"):
    st.subheader("Add Task")
    new_task = st.text_input("New task:")
    submit = st.form_submit_button("Add")
    
    if submit and new_task:
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.success(f"Task '{new_task}' added!")

# 4. Show tasks
st.divider()
st.subheader("Your Tasks")

if len(st.session_state.tasks) == 0:
    st.info("No tasks yet!")
else:
    for i in range(len(st.session_state.tasks)):
        task = st.session_state.tasks[i]
        col1, col2, col3 = st.columns([5, 1, 1])
        
        with col1:
            if task["done"]:
                st.write(f"✓ {task['text']}")
            else:
                st.write(f"○ {task['text']}")
        
        with col2:
            if st.button("✓", key=f"done_{i}"):
                st.session_state.tasks[i]["done"] = True
                st.rerun()
        
        with col3:
            if st.button("🗑", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()

# 5. Save to file
st.divider()
if st.button("Save to File"):
    try:
        with open("tasks.json", "w") as f:
            json.dump(st.session_state.tasks, f, ensure_ascii=False)
        st.success("Tasks saved!")
    except Exception as e:
        st.error(f"Error: {e}")