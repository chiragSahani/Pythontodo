
# 📋 To-Do List Application

![Python](https://img.shields.io/badge/Python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange) ![License](https://img.shields.io/badge/License-MIT-green)

An advanced **To-Do List Application** built using Python's `tkinter` library. This application allows users to manage their tasks with features like task prioritization, due dates, editing, and persistence. The user interface is enhanced with animations, hover effects, and a modern design.

---

## 🌟 Features

- **Add Tasks**: Add tasks with a title, priority (High, Medium, Low), and due date.
- **View Tasks**: Display tasks in a scrollable list with formatting based on priority.
- **Mark as Done**: Mark tasks as completed by appending "(Done)".
- **Delete Tasks**: Remove tasks from the list with an animation effect.
- **Edit Tasks**: Modify existing tasks (title, priority, due date).
- **Persistence**: Save tasks to a `.json` file and load them when the app starts.
- **Animations**: Smooth animations for adding, removing, and marking tasks.
- **Hover Effects**: Interactive buttons with hover effects for better usability.
- **Scrollbar**: Scrollable task list for handling large numbers of tasks.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- `tkcalendar` library for the date picker

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/advanced-to-do-list.git
   cd advanced-to-do-list
   ```

2. Install the required dependencies:
   ```bash
   pip install tkcalendar
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## 🚀 Usage

1. **Add a Task**:
   - Enter the task title in the input field.
   - Select the priority (High, Medium, Low) from the dropdown menu.
   - Choose a due date using the calendar widget.
   - Click the "Add Task" button.

2. **Remove a Task**:
   - Select a task from the list.
   - Click the "Remove Task" button.

3. **Mark as Done**:
   - Select a task from the list.
   - Click the "Mark as Done" button.

4. **Edit a Task**:
   - Select a task from the list.
   - Click the "Edit Task" button.
   - Update the task title, priority, or due date in the dialog boxes.

5. **Persistence**:
   - Tasks are automatically saved to a `tasks.json` file when added, removed, marked as done, or edited.
   - On startup, the app loads tasks from the file.

---

## 🎨 UI Enhancements

- **Animations**: Tasks fade in when added and highlight before being removed or marked as done.
- **Hover Effects**: Buttons change color when hovered over for better interactivity.
- **Styling**: Modern fonts, colors, and a clean layout for a polished look.

---

## 📂 File Structure

```
advanced-to-do-list/
├── main.py               # Main application code
├── tasks.json            # File to store tasks persistently
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature or fix"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---





## 🙏 Acknowledgments

- Built using Python's `tkinter` library for the GUI.
- Thanks to the `tkcalendar` library for providing a user-friendly date picker.
- Inspired by beginner-friendly Python projects to help developers enhance their skills.

---


