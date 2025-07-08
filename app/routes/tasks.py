from flask import Blueprint, render_template, redirect, session, url_for, request, flash,sessions
from app import db
from app.models import Task,User

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/view_tasks', methods=['GET'])
def view_tasks():
    if 'username' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))
    
    user = User.query.filter_by(username=session['username']).first()
    if not user:
        flash('User not found. Please log in again.', 'danger')
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.filter_by(user_id=user.id).all()
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'username' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))
    
    
    
    title = request.form.get('title')
    if title:
        user = User.query.filter_by(username=session['username']).first()
        if user:
            new_task = Task(title=title,user_id=user.id)
            db.session.add(new_task)
            db.session.commit()
            flash('Task added successfully!', 'success')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    user = User.query.filter_by(username=session['username']).first()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first()

    if task:
        if task.status == 'pending':
            task.status = 'working'
        elif task.status == 'working':
            task.status = 'done'
        else:
            task.status = 'pending'

    db.session.commit()
    flash(f'Task status updated to {task.status}!', 'success')

    return redirect(url_for('tasks.view_tasks') + '#task-section')

@tasks_bp.route('/clear', methods=['POST'])
def clear_tasks():
    user = User.query.filter_by(username=session['username']).first()

    Task.query.filter_by(user_id=user.id).delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    user = User.query.filter_by(username=session['username']).first()
    task = Task.query.filter_by(id=task_id, user_id=user.id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')

    return redirect(url_for('tasks.view_tasks')+ '#task-section')

@tasks_bp.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    user= User.query.filter_by(username = session['username']).first()
    task = Task.query.filter_by(id = task_id,user_id = user.id).first()

    if task:
        new_title = request.form.get('title', '').strip()
        if not new_title:
            flash('Task title cannot be empty.', 'warning')
        elif new_title == task.title:
            flash('No changes made to the task.', 'info')
        else:
            task.title = new_title
            db.session.commit()
            flash('Task updated successfully!', 'success')
    else:
        flash('Task not found.', 'danger')
    
    return redirect(url_for('tasks.view_tasks') + '#task-section')
