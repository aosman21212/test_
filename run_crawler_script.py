from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_command', methods=['POST'])
def run_command():
    result = subprocess.run(["/home/bab/Desktop/alico/BABNLU-Services/.venv/bin/python", 
                             "/home/bab/Desktop/alico/BABNLU-Services/scripts/extract_synonyms.py",
                             "--model_file",
                             "/home/bab/Desktop/alico/BABNLU-Services/data/bins/semsim_02.bin",
                             "--save_folder",
                             "/home/bab/Desktop/alico/BABNLU-Services/temps",
                             "--seed",
                             "محمد",
                             "--tag_name",
                             "PERSON"],
                            capture_output=True,
                            text=True,
                            cwd="/home/bab/Desktop/alico/BABNLU-Services/")
    
    result_output = result.stdout
    return jsonify(result=result_output)

if __name__ == '__main__':
    app.run(debug=True)
