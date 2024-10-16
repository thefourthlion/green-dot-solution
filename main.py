import os
import time
import json
import subprocess
import logging
from openai import OpenAI
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Set the working directory to the script's location
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv('OPEN_AI_KEY')
github_token = os.getenv('GITHUB_TOKEN')

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
        logging.info(f"Sending prompt to OpenAI API: {full_prompt}")
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": full_prompt}
            ]
        )
        logging.info("API response received.")
        code = extract_code_from_response(completion.choices[0].message.content)
        return code
    except Exception as e:
        logging.error(f"An error occurred during code generation: {e}")
        return None

def write_code_to_file(filename, code):
    try:
        with open(filename, 'w') as file:
            file.write(code)
        logging.info(f"Code written to file: {filename}")
    except Exception as e:
        logging.error(f"Error writing code to file {filename}: {e}")

def run_git_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        logging.info(f"Git command succeeded: {' '.join(command)}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Git command failed: {' '.join(command)}")
        logging.error(f"Error output: {e.stderr}")
        return None

def upload_to_github(filename):
    repo_url = f"https://{github_token}@github.com/thefourthlion/green-dots.git"
    
    run_git_command(['git', 'config', '--global', 'user.email', "your_email@example.com"])
    run_git_command(['git', 'config', '--global', 'user.name', "Your Name"])
    
    if not os.path.exists('.git'):
        run_git_command(['git', 'init'])
    
    run_git_command(['git', 'add', '.'])
    run_git_command(['git', 'commit', '-m', f'created {filename}'])
    
    push_result = run_git_command(['git', 'push', '--force', repo_url, 'main'])
    if push_result:
        logging.info(f"Successfully pushed {filename} to GitHub")
    else:
        logging.error(f"Failed to push {filename} to GitHub")

def countdown_timer(minutes):
    for remaining in range(minutes, 0, -1):
        logging.info(f"⌛⌛⌛ Time remaining: {remaining} minutes")
        time.sleep(60)  # Wait for 1 minute
    logging.info("Countdown finished. Starting next project...")

# Main loop
while True:
    logging.info("Starting a new cycle of project generation...")

    try:
        # Load the project data from the JSON file
        with open('projects.json', 'r') as file:
            all_projects = json.load(file)

        if not all_projects:
            logging.info("No projects found in the JSON file. Waiting for 24 hours before checking again...")
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
            logging.info(f"🟢 {project_name} Is Done")

            # Remove the completed project from the dictionary
            del all_projects[project_name]

            # Update the JSON file
            with open('projects.json', 'w') as file:
                json.dump(all_projects, file, indent=4)
            logging.info("Updated projects.json file")
        else:
            logging.error(f"🔴 Failed to generate code for {project_name}")

        # Wait for 24 hours before the next project
        logging.info("🟡Waiting for 24 hours before the next project...")
        countdown_timer(24 * 60)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        logging.info("Waiting for 1 hour before retrying...")
        time.sleep(3600)  # Wait for 1 hour before retrying