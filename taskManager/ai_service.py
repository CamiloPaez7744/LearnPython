import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(task):
    if not client.api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
    try:
        prompt = f"Create a simple task: {task}"
    except Exception as e:
        print(f"Error creating simple tasks: {e}")
        return None
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()

def prioritize_tasks(tasks):
    if not client.api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        prompt = f"Prioritize the following tasks: {tasks}"
    except Exception as e:
        print(f"Error prioritizing tasks: {e}")
        return None
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def suggest_task_decomposition(task):
    if not client.api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
    try:
        prompt = f"""Suggest how to decompose the following task into subtasks: {task}
        response format:
        - Subtask 1
        - Subtask 2
        - Subtask 3
        always use bullet points
        """
    except Exception as e:
        print(f"Error suggesting task decomposition: {e}")
        return None

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an expert task manager who helps decompose complex tasks into manageable subtasks."
                    },
                    {
                        "content": prompt
                    },
                ],
                "verbosity": "medium",
                "max_completion_tokens": 100,
                "reasoning_effort": "minimal"
            }
        ]
    )

    content = response.choices[0].message.content.strip()
    
    subtasks = []
    
    if not content.startswith("-"):
        print("Unexpected response format for task decomposition.")
        return None
    for line in content.split("\n"):
        if line.startswith("-"):
            subtask = line[1:].strip()
            subtasks.append(subtask)

    return subtasks if subtasks else ["Error: No subtasks generated."]

def generate_task_summary(task):
    if not client.api_key:
        raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        prompt = f"Generate a summary for the following task: {task}"
    except Exception as e:
        print(f"Error generating task summary: {e}")
        return None

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()