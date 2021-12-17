from flask import Flask, redirect, render_template,session, request, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)

boggle_game = Boggle()
boggle_board = boggle_game.make_board()

@app.route('/')
def home():
    if session.get('board'):
        board = session['board']
    else:    
        session['board'] = boggle_board
        board = session['board']

    return render_template('home.html',board=board)

@app.route('/check-word')
def check_word():
    
    word = request.args['user-guess']
    board = session['board']
    response = boggle_game.check_valid_word(board, word)


    return jsonify({'results': response})
    
    
@app.route('/game-over', methods=['POST'])
def update_user_data():
    # import pdb
    # pdb.set_trace()

    if session.get('best_score') and session['best_score'] < request.json['score']:
        session['best_score'] = request.json['score']
        best_score = session['best_score']
    elif session.get('best_score') and session['best_score'] > request.json['score']:
        best_score = session['best_score']
    else:
        session['best_score'] = request.json['score']
        best_score = session['best_score']

    if session.get('plays'):
        session['plays'] += 1
        played = session['plays']
    else:
        session['plays'] = 1
        played = session['plays']
    
    session['board'] = boggle_game.make_board()
    new_board = session['board']
    
    # import pdb
    # pdb.set_trace()

    return jsonify({'games_played':played, 'best_score':best_score, 'new_board' : new_board})
    

