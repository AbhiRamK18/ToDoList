import tkinter as tk
from tkinter import messagebox
import os

# File to store tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from a file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for task in file:
                task = task.strip()
                if task:
                    listbox.insert(tk.END, task)

def save_tasks():
    """Save all tasks to a file."""
    tasks = listbox.get(0, tk.END)
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
                file.write(task + "\n")

def add_task():
    """Add a new task to the list."""
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("CAUTION", "OOPS...! \n I want a task to be entered.")

def delete_task():
    """Delete the selected task."""
    try:
        selected_index = listbox.curselection()[0]
        listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    """Clear all tasks."""
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)
        save_tasks()

# Create main window
root = tk.Tk()
root.title("Student To-Do List")
root.geometry("400x450")
root.resizable(False, False)
root.configure(bg="#8871EE")

# Title label
title_label = tk.Label(root, text="Student To-Do List", font=("Helvetica", 18, "bold"), bg="#8871EE")
title_label.pack(pady=10,padx=10)

# Entry frame
frame = tk.Frame(root, bg="#8871EE")
frame.pack(pady=5,padx=5)

entry = tk.Entry(frame, font=("Arial", 14), width=25)
entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(frame, text="Add Task", font=("Arial", 12), bg="#331A6E", fg="white", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox
listbox = tk.Listbox(root, font=("Arial", 14), width=35, height=12, selectbackground="#8871EE")
listbox.pack(pady=10)

# Buttons frame
btn_frame = tk.Frame(root, bg="#8871EE")
btn_frame.pack(pady=5)

delete_button = tk.Button(btn_frame, text="Delete", font=("Arial", 12), bg="#331A6E", fg="white", command=delete_task)
delete_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(btn_frame, text="Clear All", font=("Arial", 12), bg="#331A6E", fg="white", command=clear_all)
clear_button.grid(row=0, column=1, padx=10)

# Load existing tasks
load_tasks()

# Run the main loop
root.mainloop()
