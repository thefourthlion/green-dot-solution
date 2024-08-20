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

def generate_code(prompt):
    try:
        # Modify the prompt to specify that only the code should be returned
        full_prompt = f"Please generate the Python code only. No additional text or explanations. {prompt}"
        print(f"Sending prompt to OpenAI API: {full_prompt}")
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        print("API response received.")
        code = completion.choices[0].message.content
        return code
    except Exception as e:
        print(f"An error occurred during code generation: {e}")
        return None

# Function to write code to a file
def write_code_to_file(filename, code):
    with open(filename, 'w') as file:
        file.write(code)

# Function to upload to GitHub
def upload_to_github(filename):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'created {filename}'])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])

# Load the project data from the JSON file
with open('projects.json', 'r') as file:  # Ensure this path is correct
    projects = json.load(file)

# Iterate over each project
for project_name, prompt in list(projects.items()):
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
        del projects[project_name]

        # Update the JSON file
        with open('projects.json', 'w') as file:
            json.dump(projects, file, indent=4)
    else:
        print(f"🔴 Failed to generate code for {project_name}")

    # Wait 30 seconds before moving to the next project
    time.sleep(30)
