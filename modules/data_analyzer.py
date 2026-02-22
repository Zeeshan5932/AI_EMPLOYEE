import pandas as pd


def handle_data(task):
    task_type = task.get("type")

    if task_type == "analyze_csv":
        file_path = task.get("file")

        try:
            df = pd.read_csv(file_path)
            summary = df.describe().to_string()
            return summary

        except Exception as e:
            return f"Failed to analyze data: {str(e)}"

    return "Data analysis task not supported."