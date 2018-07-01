from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from cleaner import Cleaner
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

class TextProcessor:

    def create_tfidf_from_dataframe(self, df):

        X_train, X_test, y_train, y_test = train_test_split(df["content"], df.index, random_state=0)

        count_vect = CountVectorizer(min_df=3)
        X_train_counts = count_vect.fit_transform(X_train)

        tfidf_transformer = TfidfTransformer()
        X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

        clf = MultinomialNB().fit(X_train_tfidf, y_train)

        cleanedMessages = []
        cleaner = Cleaner()
        cleanedMessage = cleaner.cleanMessage("gavin in australia for working for ey")
        cleanedMessages.append(' '.join(cleanedMessage))

        print(cleanedMessages)

        print(clf.predict(count_vect.transform(cleanedMessages)))

    def make_prediction_from_model(self, model, prediction):


        cleanedMessages = []
        cleaner = Cleaner()
        cleanedMessage = cleaner.cleanMessage(prediction)
        cleanedMessages.append(' '.join(cleanedMessage))

        print(cleanedMessages)

        print(model.predict(count_vect.transform(cleanedMessages)))





