# Task Manager 📋

An intelligent task management system in Python with AI integration via OpenAI for automatic decomposition of complex tasks.

## 📖 Description

Task Manager is a command-line application that allows you to manage tasks efficiently. The application includes traditional task management functionalities and advanced AI-powered features to help you break down complex tasks into more manageable subtasks.

### Key Features

- ✅ **Basic task management**: Create, list, complete, and delete tasks
- 🤖 **AI assistance**: Automatic decomposition of complex tasks using GPT-4
- 💾 **Data persistence**: Automatic storage in JSON format
- 🎯 **Priority system**: Organize your tasks by priority (Low, Medium, High)
- ✨ **Intuitive interface**: Easy-to-use interactive menu
- 🧪 **Fully tested**: Complete unit test suite with pytest

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- OpenAI account with API key (for AI functionalities)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/CamiloPaez7744/LearnPython.git
cd taskManager
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**

Create a `.env` file in the project root with your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## 📋 Usage

### Run the application

```bash
python main.py
```

### Main Menu

When you run the application, you'll see the following menu:

```
--- Intelligent Task Manager ---
1. Add Task
2. Add Task with AI Assistance
3. List Tasks
4. Complete Task
5. Delete Task
6. Exit
```

### Features

#### 1️⃣ Add Task Manually
Allows you to add a task by manually specifying the description and priority.

```
Option: 1
Enter task description: Complete monthly report
Enter task priority (Low, Medium, High): High
```

#### 2️⃣ Add Task with AI Assistance
AI automatically decomposes a complex task into smaller subtasks.

```
Option: 2
Enter task description: Develop a complete web application
```

AI will generate subtasks such as:
- Design system architecture
- Create database
- Develop backend
- Implement frontend
- Perform testing
- Deploy application

#### 3️⃣ List Tasks
Displays all tasks with their status, ID, description, and priority.

```
[ ] (ID: 1) Complete monthly report - Priority: High
[✓] (ID: 2) Review emails - Priority: Medium
```

#### 4️⃣ Complete Task
Marks a task as completed using its ID.

```
Option: 4
Enter task ID to complete: 1
Task completed: [✓] (ID: 1) Complete monthly report - Priority: High
```

#### 5️⃣ Delete Task
Permanently deletes a task from the system.

```
Option: 5
Enter task ID to delete: 1
```

## 🏗️ Project Structure

```
taskManager/
├── main.py                 # Application entry point
├── task_manager.py         # Main task management logic
├── ai_service.py          # OpenAI API integration
├── tasks.json             # Data persistence file
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
├── .env                   # Environment variables (not included in git)
└── tests/
    └── test_task_manager.py  # Unit tests
```

## 🧪 Testing

The project includes a complete unit test suite using pytest.

### Run tests

```bash
pytest tests/
```

### Run with coverage

```bash
pytest --cov=. tests/
```

### Included test cases

- ✅ Add and retrieve tasks
- ✅ Complete tasks and verify persistence
- ✅ Delete tasks
- ✅ Automatic ID increment
- ✅ Handle corrupt or missing files
- ✅ Correct JSON file format

## 📦 Main Dependencies

- **openai** (2.6.0): Official OpenAI client for GPT-4 integration
- **python-dotenv** (1.1.1): Environment variable management
- **pytest** (implicit): Testing framework
- **pydantic** (2.12.3): Data validation
- **requests** (2.32.5): HTTP client

See `requirements.txt` for the complete list of dependencies.

## 🔧 System Components

### TaskManager
Main class that manages all CRUD operations for tasks:
- `add_task(description, priority)`: Creates a new task
- `list_tasks()`: Displays all tasks
- `complete_task(task_id)`: Marks a task as completed
- `delete_task(task_id)`: Deletes a task
- `save_tasks()`: Saves tasks to JSON
- `load_tasks()`: Loads tasks from JSON

### Task
Class representing an individual task:
- `id`: Unique identifier
- `description`: Task description
- `priority`: Priority (Low, Medium, High)
- `completed`: Completion status (boolean)

### AI Service
OpenAI integration service:
- `suggest_task_decomposition(task)`: Decomposes complex tasks
- `create_simple_tasks(task)`: Simplifies tasks
- `prioritize_tasks(tasks)`: Suggests prioritization
- `generate_task_summary(task)`: Generates summaries

## 🔐 Security

- API keys are stored in environment variables (`.env` file)
- The `.env` file should be included in `.gitignore`
- Never share your OpenAI API key publicly

## 🤝 Contributing

Contributions are welcome. To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Important Notes

- Make sure you have sufficient credits in your OpenAI account
- GPT-4 model has associated usage costs
- Tasks are automatically saved to `tasks.json`
- The application automatically handles corrupt file errors

## 🐛 Troubleshooting

### Error: "OpenAI API key is not set"
**Solution:** Verify that your `.env` file exists and contains your API key correctly:
```env
OPENAI_API_KEY=your_api_key_here
```

### Error: "No module named 'openai'"
**Solution:** Install the dependencies:
```bash
pip install -r requirements.txt
```

### Tasks don't persist between runs
**Solution:** Verify that the `tasks.json` file exists and has write permissions.

## 📄 License

This project is part of the [LearnPython](https://github.com/CamiloPaez7744/LearnPython) learning repository.

## 👤 Author

**Camilo Paez**
- GitHub: [@CamiloPaez7744](https://github.com/CamiloPaez7744)

## 🙏 Acknowledgments

- OpenAI for providing the GPT-4 API
- The Python community for excellent libraries

---

⭐ If you found this project useful, consider giving it a star on GitHub!