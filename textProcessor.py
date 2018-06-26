import pandas as pd
import math

class TextProcessor:

    def __init__(self):
        pass

    def createTFIDFMatrix(self, textTuples):

        corpusSet = self.__generateCorpusSet(textTuples)

        #tuple of name, wordDict, bow for each document
        wordDicts = self.__generateWordDictionaries(textTuples, corpusSet)

        tfs = self.__computeTFs(wordDicts)

        idf = self.__computeIDF(wordDicts)

        tfidfTuples = []
        for tf in tfs:
            name, tfdict = tf
            tfidf = self.__computeTFIDF(tfdict, idf)
            tfidfTuples.append((name, tfidf))

        tfidfs = []
        names = []
        for a in tfidfTuples:
            tfidfs.append(a[1])
            names.append(a[0])

        return pd.DataFrame.from_records(tfidfs, index=names)



    def __computeTFIDF(self, tf, idf):
        tfidf = {}
        for word, val in tf.items():
            tfidf[word] = val * idf[word]
        return tfidf


    def __computeTFs(self, wordDicts):
        tfs = []
        for wordDict in wordDicts:
            name, doc, bow = wordDict
            tfDict = {}
            bowCount = len(bow)
            for word, count in doc.items():
                tfDict[word] = count / float(bowCount)
            tfs.append((name, tfDict))

        return tfs


    def __computeIDF(self, wordDicts):

        docList = []
        for wordDict in wordDicts:
            name, doc, bow = wordDict
            docList.append(doc)

        idfDict = {}
        N = len(docList)

        #counts the number of documents that contain a word w
        idfDict = dict.fromkeys(docList[0].keys(), 0)
        for doc in docList:
            for word, val in doc.items():
                if val > 0:
                    idfDict[word] += 1

        #divide N by denominator above, take log of that
        for word, val in idfDict.items():
            idfDict[word] = math.log(N / float(val))

        return idfDict



    def __generateWordDictionaries(self, textTuples, corpusSet):
        wordDicts = []
        for textTuple in textTuples:
            wordDict = dict.fromkeys(corpusSet, 0)
            name, bow = textTuple

            for word in bow:
                wordDict[word] += 1

            wordDicts.append((name, wordDict, bow))

        return wordDicts


    def __generateCorpusSet(self, textTuples):
        allWords = set()
        for textTuple in textTuples:
            name, bow = textTuple
            for word in bow:
                allWords.add(word)
        return allWords