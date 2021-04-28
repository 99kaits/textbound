import numpy as np
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

earth = open('scriptprocessed.txt').read()
bound = earth.split()


def make_pairs(bound):
    for i in range(len(bound) - 1):
        yield (bound[i], bound[i + 1])


@app.route("/")
def generate():
    pairs = make_pairs(bound)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(bound)
    chain = [first_word]
    n_words = 30

    for i in range(n_words):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    result = ' '.join(chain)

    return (render_template('index.html', text=result))

if __name__ == "__main__":
    app.run(threaded=True)