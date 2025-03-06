import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry
import json


# Initialize the main window
root = tk.Tk()
root.title("Advanced To-Do List")
root.geometry("600x700")
root.configure(bg="#f0f0f0")  # Light gray background

# Custom Fonts
title_font = ("Arial", 18, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")

# Variables
tasks = tk.Listbox(root, width=70, height=15, bg="white", selectmode=tk.SINGLE, font=label_font)
task_entry = tk.Entry(root, width=50, font=label_font)
priority_var = tk.StringVar(value="Low")  # Default priority
due_date_var = tk.StringVar()

# Scrollbar for Task List
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks.yview)

# Load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            saved_tasks = json.load(file)
            for task in saved_tasks:
                tasks.insert(tk.END, task)
    except FileNotFoundError:
        pass  # No tasks file exists yet

# Save tasks to file
def save_tasks():
    tasks_list = [tasks.get(i) for i in range(tasks.size())]
    with open("tasks.json", "w") as file:
        json.dump(tasks_list, file)

# Add Task with Animation
def add_task():
    task_title = task_entry.get().strip()
    priority = priority_var.get()
    due_date = due_date_var.get()

    if not task_title:
        messagebox.showwarning("Warning", "Task title cannot be empty!")
        return

    if not due_date:
        messagebox.showwarning("Warning", "Please select a due date!")
        return

    # Format task string
    formatted_task = f"[{priority}] {task_title} (Due: {due_date})"
    tasks.insert(tk.END, formatted_task)
    task_entry.delete(0, tk.END)

    # Animation: Fade in the new task
    tasks.itemconfig(tasks.size() - 1, {'bg': 'lightgreen'})
    root.after(500, lambda: tasks.itemconfig(tasks.size() - 1, {'bg': 'white'}))

    save_tasks()

# Remove Task with Animation
def remove_task():
    try:
        selected_index = tasks.curselection()[0]
        tasks.itemconfig(selected_index, {'bg': 'lightcoral'})  # Highlight before removal
        root.after(500, lambda: tasks.delete(selected_index))  # Delayed removal
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove!")

# Mark Task as Done with Animation
def mark_task_done():
    try:
        selected_index = tasks.curselection()[0]
        task = tasks.get(selected_index)
        if "(Done)" not in task:
            tasks.itemconfig(selected_index, {'bg': 'lightblue'})  # Highlight before marking
            root.after(500, lambda: tasks.delete(selected_index))
            tasks.insert(selected_index, f"{task} (Done)")
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done!")

# Edit Task
def edit_task():
    try:
        selected_index = tasks.curselection()[0]
        current_task = tasks.get(selected_index)

        # Extract task details
        parts = current_task.split(" (Due: ")
        task_title = parts[0].split("] ")[1]
        priority = parts[0].split("] ")[0][1:]
        due_date = parts[1].split(")")[0]

        # Open dialog for editing
        new_title = simpledialog.askstring("Edit Task", "Enter new task title:", initialvalue=task_title)
        if new_title:
            new_priority = simpledialog.askstring("Edit Priority", "Enter new priority (High, Medium, Low):", initialvalue=priority)
            new_due_date = simpledialog.askstring("Edit Due Date", "Enter new due date (YYYY-MM-DD):", initialvalue=due_date)

            if new_priority not in ["High", "Medium", "Low"]:
                messagebox.showwarning("Invalid Priority", "Priority must be High, Medium, or Low.")
                return

            # Update task
            updated_task = f"[{new_priority}] {new_title} (Due: {new_due_date})"
            tasks.delete(selected_index)
            tasks.insert(selected_index, updated_task)
            save_tasks()

    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to edit!")

# GUI Layout
label = tk.Label(root, text="To-Do List", font=title_font, bg="#f0f0f0", fg="black")
label.pack(pady=10)

# Task Entry
task_entry_label = tk.Label(root, text="Task Title:", font=label_font, bg="#f0f0f0", fg="black")
task_entry_label.pack()
task_entry.pack(pady=5)

# Priority Dropdown
priority_label = tk.Label(root, text="Priority:", font=label_font, bg="#f0f0f0", fg="black")
priority_label.pack()
priority_menu = tk.OptionMenu(root, priority_var, "High", "Medium", "Low")
priority_menu.config(font=label_font, bg="white", fg="black")
priority_menu.pack()

# Due Date Picker
due_date_label = tk.Label(root, text="Due Date:", font=label_font, bg="#f0f0f0", fg="black")
due_date_label.pack()
due_date_picker = DateEntry(root, textvariable=due_date_var, date_pattern="yyyy-mm-dd", font=label_font)
due_date_picker.pack(pady=5)

# Buttons with Hover Effects
def on_enter(e):
    e.widget['bg'] = '#d3d3d3'

def on_leave(e):
    e.widget['bg'] = 'SystemButtonFace'

add_button = tk.Button(root, text="Add Task", command=add_task, font=button_font, bg="lightgreen", fg="black")
add_button.pack(pady=5)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

remove_button = tk.Button(root, text="Remove Task", command=remove_task, font=button_font, bg="lightcoral", fg="black")
remove_button.pack(pady=5)
remove_button.bind("<Enter>", on_enter)
remove_button.bind("<Leave>", on_leave)

mark_button = tk.Button(root, text="Mark as Done", command=mark_task_done, font=button_font, bg="lightblue", fg="black")
mark_button.pack(pady=5)
mark_button.bind("<Enter>", on_enter)
mark_button.bind("<Leave>", on_leave)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, font=button_font, bg="lightyellow", fg="black")
edit_button.pack(pady=5)
edit_button.bind("<Enter>", on_enter)
edit_button.bind("<Leave>", on_leave)

# Task List with Scrollbar
tasks_label = tk.Label(root, text="Your Tasks:", font=title_font, bg="#f0f0f0", fg="black")
tasks_label.pack(pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tasks.pack(pady=10)

# Load tasks on startup
load_tasks()

# Run the application
root.mainloop()