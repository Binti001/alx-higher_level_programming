#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:

        letter = None
        size = (len(sentence))
    else:

        size = (len(sentence))
        letter = sentence[0]
    tup = (size, letter)

    return tup
