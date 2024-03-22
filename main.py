from ui import UI
from word_manager import WordManager
from word_dict import ENGLISH


word_man = WordManager(ENGLISH)
screen = UI(word_man)

screen.draw()
screen.update_words()

screen.window.mainloop()