from random import choice

class WordManager():
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.past_word = ""
        self.current_word = ""
        self.future_word = choice(self.word_dict)
    
    def update_words(self):
        self.past_word = self.current_word
        self.current_word = self.future_word
        self.future_word = choice(self.word_dict)
        
    def check_word(self, word):
        return self.current_word == word