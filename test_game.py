import unittest
from unittest.mock import patch
from game import play_rps

class TestRockPaperScissors(unittest.TestCase):
    @patch('builtins.input', side_effect=['rock', 'no'])
    @patch('random.choice', return_value='rock')
    def test_tie_game(self, mock_choice, mock_input):
        with patch('builtins.print') as mock_print:
            play_rps()
            mock_print.assert_any_call("It's a tie!")

    @patch('builtins.input', side_effect=['rock', 'no'])
    @patch('random.choice', return_value='scissors')
    def test_user_wins(self, mock_choice, mock_input):
        with patch('builtins.print') as mock_print:
            play_rps()
            mock_print.assert_any_call("You win!")

    @patch('builtins.input', side_effect=['rock', 'no'])
    @patch('random.choice', return_value='paper')
    def test_user_loses(self, mock_choice, mock_input):
        with patch('builtins.print') as mock_print:
            play_rps()
            mock_print.assert_any_call("You lose!")

    @patch('builtins.input', side_effect=['invalid', 'rock', 'no'])
    @patch('random.choice', return_value='rock')
    def test_invalid_input(self, mock_choice, mock_input):
        with patch('builtins.print') as mock_print:
            play_rps()
            mock_print.assert_any_call("Invalid choice. Please try again.")

    @patch('builtins.input', side_effect=['rock', 'yes', 'paper', 'no'])
    @patch('random.choice', side_effect=['rock', 'rock'])
    def test_play_again(self, mock_choice, mock_input):
        with patch('builtins.print') as mock_print:
            play_rps()
            # Verify the game played twice
            self.assertEqual(mock_input.call_count, 4)

if __name__ == '__main__':
    unittest.main()