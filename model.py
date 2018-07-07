from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from cleaner import Cleaner
from sklearn.model_selection import train_test_split, cross_val_score
import pickle
import os

class Model:

    def create_chat_model_from_dataframe(self, df, modelId):

        pipeline = Pipeline([
            ('vect', CountVectorizer(min_df=3)),
            ('tfidf', TfidfTransformer()),
            ('mnb', MultinomialNB())
        ])

        X_train, X_test, y_train, y_test = train_test_split(df["content"], df.index, random_state=0)

        pipeline.fit(X_train, y_train)

        dir_path = os.path.dirname(os.path.realpath(__file__)) + '/ChatModels/'

        with open(dir_path + str(modelId) +'.pickle', 'wb') as handle:
            pickle.dump(pipeline, handle, protocol=pickle.HIGHEST_PROTOCOL)

        #print(cross_val_score(pipeline, X_train, y_train, cv=3, scoring="accuracy"))

    def make_prediction_from_model(self, modelId, message):

        with open(str(modelId) +'.pickle', 'rb') as handle:
            pipeline = pickle.load(handle)

        cleanedMessages = []
        cleaner = Cleaner()
        cleanedMessage = cleaner.cleanMessage(message)
        cleanedMessages.append(' '.join(cleanedMessage))

        return pipeline.predict(cleanedMessages)




