from app import create_app,db

from app.models import Task,User
from flask import redirect, url_for

app = create_app()

with app.app_context():
    db.create_all()
# Redirect '/' to login page
@app.route('/')
def index():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)