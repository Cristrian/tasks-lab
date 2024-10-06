from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def update_task(task_id, name=None, description=None):
        task = Task.query.get(task_id)
        if not task:
            return None

        if name is not None:
            task.name = name
        if description is not None:
            task.description = description

        db.session.commit()
        return task