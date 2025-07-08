## ✅ Flask To-Do App

A simple multi-user To-Do web application built with Flask and SQLAlchemy. Users can register, log in, and manage their personal task list.

## 📸 UI Preview

![App Screenshot](./Screenshot%202025-07-08%20202752.png)

---

# 🚀 Features

- 🔐 User Registration & Login
- 📝 Add, Edit, Delete tasks
- 🔄 Toggle task status: Pending → Working → Done
- 👤 Tasks are user-specific
- 💡 Flash messages for user feedback
- 🧼 Responsive and minimal UI

---

# 🛠 Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Database**: SQLite
- **Frontend**: HTML, CSS, Jinja2
- **Session Handling**: Flask sessions
- **Authentication**: Basic login system

---

# 🔧 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/flask-todo-app.git
   cd flask-todo-app
# Create and activate virtual environment
  ```bash
  python -m venv venv
  source venv/bin/activate     # macOS/Linux
  venv\Scripts\activate        # Windows
```

# Install dependencies
```
  pip install -r requirements.txt
```

# Run the app
```
  python run.py
  Open http://127.0.0.1:5000 in your browser.
```

# Project Structure
```
todo_app/
|
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│       ├── auth.py
│       └── tasks.py
│   ├── templates/
│       ├── login.html
│       ├── register.html
│       └── tasks.html
│   └── static/
│       └── style.css
│
├── requirements.txt
├── .gitignore
└── run.py
```

# Future Improvements
🔐 Password hashing
📨 Email verification (optional)
🗂️ Task categories or tags
📱 Mobile responsive UI
☁️ Deployment (Render/Railway)

# 🤝 Contributing
Feel free to fork and enhance this project.

MIT License © Tejash Gawas




