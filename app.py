from flask import Flask, render_template, jsonify
import threading
import os
import check_target_script

app = Flask(__name__)
LOG_FILE = "target_pokemon_bot.log"

def run_bot():
    try:
        check_target_script.check_target()
    except Exception as e:
        with open(LOG_FILE, "a") as log:
            log.write(f"Error: {str(e)}\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-bot', methods=['POST'])
def run_bot_endpoint():
    thread = threading.Thread(target=run_bot)
    thread.start()
    return jsonify({'status': 'Bot started'})

@app.route('/logs')
def logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return f"<pre>{f.read()}</pre>"
    return "<pre>No logs found.</pre>"

if __name__ == '__main__':
    app.run(debug=True)
