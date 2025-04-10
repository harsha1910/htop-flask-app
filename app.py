from flask import Flask
import subprocess
import os
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Full Name
    full_name = "Your Full Name"  # <<< Replace with your real name

    # System username (using getpass to avoid permission errors)
    username = getpass.getuser()

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top output (capture output of 'top' command)
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    # Prepare HTML response
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

