import os
import time
import json
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv('OPEN_AI_KEY')

# Initialize the OpenAI client
client = OpenAI(api_key=api_key)

def extract_code_from_response(response):
    """
    Extract the Python code from the AI's response.
    Assumes the code is wrapped in triple backticks (```).
    """
    start = response.find("```")
    if start != -1:
        end = response.find("```", start + 3)
        if end != -1:
            code = response[start + 3:end].strip()
            if code.startswith("python"):
                code = code[len("python"):].strip()
            return code
    return response

def generate_code(prompt):
    try:
        full_prompt = f"Please generate the Python code only. No additional text or explanations. {prompt}"
        print(f"Sending prompt to OpenAI API: {full_prompt}")
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        print("API response received.")
        code = extract_code_from_response(completion.choices[0].message.content)
        return code
    except Exception as e:
        print(f"An error occurred during code generation: {e}")
        return None

def write_code_to_file(filename, code):
    with open(filename, 'w') as file:
        file.write(code)

def upload_to_github(filename):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'created {filename}'])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])

# Main loop to run every 24 hours
while True:
    print("Starting a new cycle of project generation...")

    # Load the project data from the JSON file
    with open('projects.json', 'r') as file:
        all_projects = json.load(file)

    # Create a copy of the projects to work on in this cycle
    projects_to_process = all_projects.copy()

    if not projects_to_process:
        print("No projects found in the JSON file. Waiting for 24 hours before checking again...")
        time.sleep(24 * 60 * 60)  # 24 hours in seconds
        continue

    # Iterate over each project
    for project_name, prompt in list(projects_to_process.items()):
        # Create the filename
        filename = f"{project_name}.py"

        # Generate the code using OpenAI API
        code = generate_code(prompt)

        if code:
            # Write the code to the file
            write_code_to_file(filename, code)

            # Upload the file to GitHub
            upload_to_github(filename)

            # Print completion message
            print(f"🟢 {project_name} Is Done")

            # Remove the completed project from the dictionary
            del projects_to_process[project_name]
        else:
            print(f"🔴 Failed to generate code for {project_name}")

        # Wait 30 seconds before moving to the next project
        time.sleep(30)

    # After processing all projects, wait for 24 hours
    print("🟡🟡🟡Cycle completed. Waiting for 24 hours before the next cycle...")
    time.sleep(24 * 60 * 60)  # 24 hours in seconds