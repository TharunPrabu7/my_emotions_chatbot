from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    userInput = request.form['userInput']
    bot_response = generate_bot_response(userInput)
    return jsonify({'bot_response': bot_response})

def generate_bot_response(userInput):
    if userInput.lower() == 'hi':
        return 'Hello'
    else:
        return "Send Hi you stupid fuck."

if __name__ == '__main__':
    app.run(debug=True)
