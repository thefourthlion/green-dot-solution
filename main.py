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

# Function to generate code using OpenAI GPT
def generate_code(prompt):
    try:
        print(f"Sending prompt to OpenAI API: {prompt}")
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        # Log response object for debugging
        print("API response received.")

        # Extract the generated code from the completion object
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
