from flask import Flask, Response
import subprocess

app = Flask(__name__)

@app.route('/run-tests', methods=['GET'])
def run_tests():
    def generate():
        process = subprocess.Popen(
            ['pytest', '-s'],  # -s flag allows output to be captured and streamed
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        for line in iter(process.stdout.readline, b''):
            yield line.decode('utf-8')
        for line in iter(process.stderr.readline, b''):
            yield line.decode('utf-8')

    return Response(generate(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
