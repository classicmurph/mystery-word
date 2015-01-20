#Test each step

import mystery_word_tdd as mw

def test_random_word_assignment():
    assert type(mw.random_word_assignment()) == str

def test_game_intro():
    assert mw.game_intro("word", 8) == "The word has 4 letters. You have 8 guesses."

def test_change_count_guess():
    assert mw.change_count_guess(8) == 7

def test_correct_guess():
    assert (mw.correct_guess(guess)) == ["guess"]

def test_display_correct_guesses():
    assert type(mw.display_correct_guesses("guess")) == str

# def test_get_guess():
#     assert mw.get_guess() == "input"

def test_game_over():
    assert mw.game_over() == "You lose. The word was " + random_word +".'"

def test_guess_list():
    assert type(mw.guess_list) == list
