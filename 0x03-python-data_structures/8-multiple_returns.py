#!/usr/bin/python3
def multiple_returns(sentence):
        if sentence == '':
                return (None)
        if sentence:
                return (len(sentence), sentence[0])
