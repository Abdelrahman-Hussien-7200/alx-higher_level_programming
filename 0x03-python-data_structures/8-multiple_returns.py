#!/usr/bin/python3

def multiple_returns(sentence):
    le = len(sentence)
    if sentence == "":
        return 0, None
    c = sentence[0]
    tu = (le, c)
    return tu
