import os
import time
import json
import subprocess
from openai import OpenAI
from dotenv import load_dotenv

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
    # Note: This function is modified to work within Docker
    subprocess.run(['git', 'config', '--global', 'user.email', "you@example.com"])
    subprocess.run(['git', 'config', '--global', 'user.name', "Your Name"])
    subprocess.run(['git', 'init'])
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', f'created {filename}'])
    print(f"Changes committed locally for {filename}")
    # Uncomment the following line when you've set up Git credentials
    # subprocess.run(['git', 'push', '-u', 'origin', 'main'])

def countdown_timer(minutes):
    for remaining in range(minutes, 0, -1):
        print(f"⌛⌛⌛ Time remaining: {remaining} minutes", end='\r')
        time.sleep(60)  # Wait for 1 minute
    print("\nCountdown finished. Starting next project...")

# Main loop
while True:
    print("Starting a new cycle of project generation...")

    # Load the project data from the JSON file
    with open('projects.json', 'r') as file:
        all_projects = json.load(file)

    if not all_projects:
        print("No projects found in the JSON file. Waiting for 24 hours before checking again...")
        countdown_timer(24 * 60)
        continue

    # Process one project
    project_name, prompt = next(iter(all_projects.items()))
    
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
        del all_projects[project_name]

        # Update the JSON file
        with open('projects.json', 'w') as file:
            json.dump(all_projects, file, indent=4)
    else:
        print(f"🔴 Failed to generate code for {project_name}")

    # Wait for 24 hours before the next project
    print("🟡Waiting for 24 hours before the next project...")
    countdown_timer(24 * 60)