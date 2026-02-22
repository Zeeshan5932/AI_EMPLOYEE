import os

def handle_file(task):
    task_type = task.get("type")

    if task_type == "create_folder":
        name = task.get("name")

        try:
            os.makedirs(name, exist_ok=True)
            return f"Folder {name} created."
        except:
            return "Failed to create folder."

    return "File task not supported."