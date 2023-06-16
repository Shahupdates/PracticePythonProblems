from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Route to serve the problem files
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

    folder_path = os.path.join('practicepythonproblems', difficulty)
    try:
        with open(os.path.join(folder_path, filename), 'r') as file:
            content = file.read()
        return render_template_string('<pre>{{content}}</pre>', content=content)
    except FileNotFoundError:
        return 'File not found.'

# Route handler for the root URL ("/")
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
