from repository import Repository
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

        chat_movies_df = pd.concat([movies_df, chat_df])

        return chat_movies_df

    