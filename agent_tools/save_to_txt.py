from datetime import datetime

from langchain_core.tools import Tool


def save_to_txt(data: str, filename: str = "reserch.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_test = f"--- Research Output ---\n{timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_test)

    return f"Data successfully saved into {filename}"


save_tool = Tool(
    name="SaveResearch",
    func=save_to_txt,
    description="Saves the research output to a text file.",
)