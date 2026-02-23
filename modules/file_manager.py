import os

current_directory = os.getcwd()


def handle_file(task):
    global current_directory

    task_type = task.get("type")

    if task_type == "create_folder":
        name = task.get("name")
        path = os.path.join(current_directory, name)

        os.makedirs(path, exist_ok=True)
        return f"Folder {name} created."

    elif task_type == "create_file":
        name = task.get("name")
        path = os.path.join(current_directory, name)

        with open(path, "w") as f:
            f.write("")

        return f"File {name} created."

    elif task_type == "change_directory":
        folder = task.get("name")
        path = os.path.join(current_directory, folder)

        if os.path.exists(path):
            current_directory = path
            return f"Changed directory to {folder}"
        else:
            return "Folder not found."

    return "File task not supported."