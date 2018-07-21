from flask import Flask, jsonify, request
from provider import Provider

app = Flask(__name__)

@app.route('/trainchat')
def train_chat():
    try:
        provider = Provider()
        chat_id = request.args.get('chatId')
        provider.train_chat_model(chat_id)
        return "True"
    except:
        print("Could Not Train Chat")

@app.route('/makeprediction')
def make_prediction():
    try:
        provider = Provider()
        chat_id = request.args.get('chatId')
        message = request.args.get('message')
        prediction = provider.make_prediction_from_chat_model(chat_id, message)
        return jsonify(prediction[0])
    except:
        print("Could Not Make Prediction")
        return "False"

@app.route('/createmoviesdf')
def create_movies_df():
    try:
        provider = Provider()
        provider.add_new_movies_df()
        return "True"
    except:
        print("Could Not Create Movies DF")
        return "False"

@app.route('/chatmoviescomparison')
def chat_movies_comparison():
    try:
        provider = Provider()
        chat_id = request.args.get('chatId')
        comparisons = provider.find_movie_comparisons_from_chat(chat_id)
        return jsonify(comparisons)
    except:
        print("Could Not Create Movies Comparison")
        return "False"