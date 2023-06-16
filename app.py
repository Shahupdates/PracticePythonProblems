from flask import Flask, Response
import os
import glob

app = Flask(__name__)

@app.route('/<difficulty>/problem<int:problem_number>.py')
def serve_file(difficulty, problem_number):
    if difficulty == 'easy':
        filename = f"problem{problem_number}.py"
    elif difficulty == 'medium':
        filename = f"problem{problem_number + 21}.py"
    elif difficulty == 'hard':
        filename = f"problem{problem_number + 42}.py"
    elif difficulty == 'extreme':
        filename = f"problem{problem_number + 63}.py"
    else:
        return 'Invalid difficulty level.'

    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, difficulty)  # Removed 'practicepythonproblems' here

    # Print the files in the directory
    print(f"Files in {folder_path}:")
    print(glob.glob(os.path.join(folder_path, '*.py')))

    full_path = os.path.join(folder_path, filename)

    try:
        with open(full_path, 'r') as file:
            content = file.read()
        return Response(content, mimetype='text/plain')
    except FileNotFoundError:
        return f"File not found at path: {full_path}"

@app.route('/')
def serve_index():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, 'index.html')
    try:
        with open(full_path, 'r') as file:
            content = file.read()
        return Response(content, mimetype='text/html')
    except FileNotFoundError:
        return "File not found."

if __name__ == '__main__':
    app.run(debug=True)
