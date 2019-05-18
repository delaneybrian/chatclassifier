from flask import Flask, jsonify, request
from provider import Provider
import sys

app = Flask(__name__)

@app.route('/trainchat')
def train_chat():
    try:
        app.logger.info('TRAINING CHAT')
        provider = Provider()
        chat_id = request.args.get('chatId')
        provider.train_chat_model(chat_id)
        return "True"
    except Exception as e:
        app.logger.info('Could Not Train Chat - {}'.format(e))
        return "False"

@app.route('/makeprediction')
def make_prediction():
    try:
        provider = Provider()
        chat_id = request.args.get('chatId')
        message = request.args.get('message')
        prediction = provider.make_prediction_from_chat_model(chat_id, message)
        return jsonify(prediction[0])
    except Exception as e:
        app.logger.info('Could Not Make Prediction - {}'.format(e))
        return "False"

@app.route('/createmoviesdf')
def create_movies_df():
    try:
        provider = Provider()
        provider.add_new_movies_df()
        return "True"
    except Exception as e:
        app.logger.info('Could Not Create Movies DF - {}'.format(e))
        return "False"

@app.route('/chatmoviescomparison')
def chat_movies_comparison():
    try:
        provider = Provider()
        chat_id = request.args.get('chatId')
        comparisons = provider.find_movie_comparisons_from_chat(chat_id)
        return jsonify(comparisons)
    except Exception as e:
        app.logger.info('Could Not Create Movies Comparison - {}'.format(e))
        return "False"