#Server
from flask import Flask, request, render_template
from solver import minimise_dictionary, get_best_words, get_definition
app = Flask(__name__)


@app.route('/')
def hello():
    words = []
    definition = ''
    word = ''
    inputText = request.args.get("inputText","")
    if "inputText" in request.args:
        letters = sorted(list(request.args["inputText"].lower()))
        dictionary = minimise_dictionary(letters)
        words = get_best_words(dictionary)
        definition,word = get_definition(words[0])
    return render_template("index.html", words=words, definition=definition, word=word, inputText=inputText)

if __name__ == '__main__':
    app.run(debug=True)
