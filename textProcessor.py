import pandas as pd
import math

class TextProcessor:

    def calculateTFIDF(self, docs):

        corpus = self.__getCorpusSet(docs)

        wordTuples = []
        wordDicts = []
        for doc in docs:
            wordTuple = self.__getWordTuple(doc, corpus)
            wordTuples.append(wordTuple)
            wordDicts.append(wordTuple[0])

        idf = self.__computeIDF(wordDicts)

        tfidfs = []
        for wordTuple in wordTuples:
            tf = self.__computeTF(wordTuple[0], wordTuple[1])
            tfidf = self.__computeTFIDF(tf, idf)
            tfidfs.append(tfidf)

        return tfidfs

    #returns a tuple of <word dict, bag of words> for the given doc
    #pass in the document and the corpus
    def __getWordTuple(self, doc, corpus):
        wordDict = dict.fromkeys(corpus, 0)
        for word in doc:
            wordDict[word] += 1

        return (wordDict, doc)


    def __computeTFIDF(self, tfDict, idfs):
        tfidf = {}
        for word, val in tfDict.items():
            tfidf[word] = val * idfs[word]
        return tfidf


    def __computeTF(self, wordDict, bow):
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bowCount)
        return tfDict

    def __computeIDF(self, docList):
        idfDict = {}
        N = len(docList)

        idfDict = dict.fromkeys(docList[0].keys(), 0)
        for doc in docList:
            for word, val in doc.items():
                if val > 0:
                    idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))

        return idfDict

    def __getCorpusSet(self, docs):
        corpus = set()
        for doc in docs:
            [corpus.add(word) for word in doc]
        return corpus