from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBIG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_home(self):
        with app.test_client() as client:
            res = client.get('/')
            
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)

            
            self.assertIn('board', session)
            self.assertIsNone(session.get('best_score'))
            self.assertIsNone(session.get('games_played'))

    def test_valid_word(self):
        """Test if word is valid by modifying the board in the session"""

        with app.test_client() as client:
            with client.session_transaction() as session:
                session['board'] = [["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"], 
                                 ["C", "A", "T", "T", "T"]]

        response = self.client.get('/check-word?user-guess=cat')
        self.assertEqual(response.json['result'], 'ok')       

    def test_invalid_word(self):
        """Test if word is in the dictionary"""
        with app.test_client() as client:
            # self.client.get('/')
        # self.client.get('/')
            response = self.client.get('/check-word?user-guess=impossible')
            self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is on the board"""

        self.client.get('/')
        response = self.client.get(
            '/check-word?user-guess=fsjdakfkldsfjdslkfjdlksf')
        self.assertEqual(response.json['result'], 'not-word')

    

    # def test_game_over(self):
    #     with app.test_client() as client:
    #         res = client.get('/game-over')
    #         html = res.get_data(as_text=True)

    #         self.assertEqual(res.status_code, 200)

            
