from flask import Flask, Response, request
import subprocess

app = Flask(__name__)

@app.route('/run-tests', methods=['GET'])
def run_tests():
    def generate():
        # Run the test script and stream its output
        process = subprocess.Popen(['python3', 'test_api.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in iter(process.stdout.readline, ''):
            yield line
        process.stdout.close()
        process.wait()

    return Response(generate(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
