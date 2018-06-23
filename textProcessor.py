import pandas as pd

class TextProcessor:

    def __init__(self):
        pass

    def createTFIDFMatrix(self, textTuples):

        corpusSet = self.__generateCorpusSet(textTuples)

        wordDicts = self.__generateWordDictionaries(textTuples, corpusSet)





    def __generateWordDictionaries(self, textTuples, corpusSet):
        wordDicts = []
        for textTuple in textTuples:
            wordDict = dict.fromkeys(corpusSet, 0)
            name, bow = textTuple

            for word in bow:
                wordDict[word] += 1

            wordDicts.append((name, wordDict))

        return wordDicts


    def __generateCorpusSet(self, textTuples):
        allWords = set()
        for textTuple in textTuples:
            name, bow = textTuple
            for word in bow:
                allWords.add(word)
        return allWords