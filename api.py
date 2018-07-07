from flask import Flask, jsonify, request
from provider import Provider

app = Flask(__name__)

@app.route('/trainchat')
def train_chat():
    provider = Provider()
    chat_id = request.args.get('chatId')
    provider.train_chat_model(chat_id)

@app.route('/makeprediction')
def make_prediction():
    provider = Provider()
    chat_id = request.args.get('chatId')
    message = request.args.get('message')
    prediction = provider.make_prediction_from_chat_model(chat_id, message)

    return jsonify(prediction)

@app.route('/createmoviesdf')
def create_movies_df():
    provider = Provider()
    provider.add_new_movies_df()

@app.route('/chatmoviescomparison')
def chat_movies_comparison():
    provider = Provider()
    chat_id = request.args.get('chatId')
    comparisons = provider.find_movie_comparisons_from_chat(chat_id)
    return jsonify(comparisons)