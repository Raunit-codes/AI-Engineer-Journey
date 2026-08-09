
def add_task(tasks, description):
    new_id = len(tasks)+1
    task = {"id": new_id,"task": description,"done": False }
    tasks.append(task)

def list_tasks(tasks):
    for task in tasks:
        print(task)

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
def remove_task(tasks, task_id):
    for task in tasks:
        if task["id"]==task_id:
            tasks.remove(task)
            break