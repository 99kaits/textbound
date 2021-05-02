import numpy as np

earth = open('scriptprocessed.txt').read()
bound = earth.split()


def make_pairs(arg):
    for i in range(len(arg) - 1):
        yield (arg[i], arg[i + 1])


def gentext():
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

    result: str = ' '.join(chain)

    return result
