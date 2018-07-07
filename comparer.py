from repository import Repository
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics.pairwise import cosine_similarity
from cleaner import Cleaner
from movieFactory import MovieFactory
from transformer import Transformer
import pandas as pd
import pickle
import os

class Comparer:

    def create_all_movies_df(self):
        repository = Repository()
        cleaner = Cleaner()
        transformer = Transformer()
        movieFactory = MovieFactory()

        allRawMovies = repository.getAllMovies()

        movieMatrixs = []
        for rawMovie in allRawMovies:
            movie = movieFactory.createMovie(rawMovie)
            cleanedMovie = cleaner.cleanMovie(movie)
            movieMatrix = transformer.transformMovieMatrixAsDF(cleanedMovie)
            movieMatrixs.append(movieMatrix)

        moviesdf = pd.concat(movieMatrixs)

        self.__replace_save_movies_df(moviesdf)

    def __replace_save_movies_df(self, moviesdf):

        file_path = os.path.dirname(os.path.realpath(__file__)) + '/MoviesDfs/moviesdf.pickle'

        if os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, 'wb') as handle:
            pickle.dump(moviesdf, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def create_chat_movie_df(self, chat_df):

        movies_df_file_path = os.path.dirname(os.path.realpath(__file__)) + '/MoviesDfs/moviesdf.pickle'

        with open(movies_df_file_path, 'rb') as handle:
            movies_df = pickle.load(handle)

        chat_movies_df = pd.concat([chat_df, movies_df])

        return chat_movies_df

    def generate_comparison(self, chat_movie_df, chat_df):

        chat_movie_df['individual'] = chat_movie_df.index
        chat_movie_df.reset_index(drop=True, inplace=True)

        contents = chat_movie_df['content']

        count_vectorizer = CountVectorizer(min_df=3)
        tfidf_transformer = TfidfTransformer()

        counts = count_vectorizer.fit_transform(contents)
        tfidf = tfidf_transformer.fit_transform(counts)

        similarity = cosine_similarity(tfidf)

        num_chatters = len(chat_df)
        total_individuals = len(chat_movie_df)

        most_similar = {}
        for x in range(0, num_chatters):
            x_similarity = similarity[x]

            sim_position = 0
            sim_value = 0
            for y in range(num_chatters, total_individuals):
                if(x_similarity[y] > sim_value):
                    sim_position = y
                    sim_value = x_similarity[y]

            movie_individual = chat_movie_df['individual'].at[sim_position]
            chat_individual = chat_movie_df['individual'].at[x]
            similarity_value = sim_value

            most_similar[chat_individual] = (movie_individual, similarity_value)

        return most_similar
