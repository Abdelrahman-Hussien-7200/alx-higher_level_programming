#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return(0, None)
    n = len(sentence)
    return (n, sentence[0])
