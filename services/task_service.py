from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
    
    @staticmethod
    def update_task(task_id, name=None, description=None):
        return TaskRepository.update_task(task_id, name, description)