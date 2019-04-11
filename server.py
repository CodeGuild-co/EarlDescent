#Server
from flask import Flask, request, render_template
from solver import minimise_dictionary, get_best_words
app = Flask(__name__)


@app.route('/')
def hello():
    words = []
    inputText = request.args.get("inputText", "")
    if inputText:
        letters = sorted(list(inputText.lower()))
        dictionary = minimise_dictionary(letters)
        words = get_best_words(dictionary)       
    return render_template("index.html", words=words, inputText=inputText)

if __name__ == '__main__':
    app.run(debug=True)
