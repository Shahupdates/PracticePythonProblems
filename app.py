from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Route to serve the problem files
@app.route('/<difficulty>/<filename>')
def serve_file(difficulty, filename):
    folder_path = os.path.join('practicepythonproblems', difficulty)
    return send_from_directory(folder_path, filename)

# Route handler for the root URL ("/")
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run()
