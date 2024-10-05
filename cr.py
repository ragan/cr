import os
import subprocess
import json
import re
import sys
import threading
import itertools
import time

# Read the diff file content from standard input if no file is provided
if len(sys.argv) < 2:
    diff_content = sys.stdin.read()
else:
    diff_file = sys.argv[1]
    with open(diff_file, "r") as f:
        diff_content = f.read()

prompt = (
    "\n Review this diff, provide suggestions for improvement, coding best practices, "
    "improve readability, and maintainability. Check for adherence to SOLID, KISS, and DRY principles. Show any code smells and anti-patterns. "
    "Provide code examples for your suggestion. Respond in markdown format. If the file "
    "does not have any code or does not need any changes, say 'No changes needed'."
)

def spinner():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stderr.write(f'\rOllama is working... {c}')
        sys.stderr.flush()
        time.sleep(0.1)
    sys.stderr.write('\rDone!            \n')

done = False
spinner_thread = threading.Thread(target=spinner)
spinner_thread.start()

try:
    # Process the diff content
    ollama_output = subprocess.getoutput(
        f"ollama run qwen2.5-coder 'Code: {diff_content} {prompt}'"
    )
finally:
    done = True
    spinner_thread.join()

# Function to remove ANSI escape sequences
def remove_ansi_escape_sequences(text):
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

# Clean the ollama output
clean_output = remove_ansi_escape_sequences(ollama_output)

print("Ollama Output:")
print(clean_output)

