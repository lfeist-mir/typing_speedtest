from tkinter import Tk, Label, Entry, Button,END
from word_manager import WordManager


class UI():
    '''
    This class model the UI.
    '''
    def __init__(self, word_manager:WordManager):
        self.score = 0
        self.countdown_on = False
        self.word_manager = word_manager
        # Main window
        self.window = Tk()
        self.window.title("Typing test")
        self.window.config(width=500, height=500, padx=100, pady=100)
        
        # Label title
        self.label_title = Label(
            self.window, 
            text="Type as fast as possible.",
            font=("Courier",24)
        )
        
        # 3 words, one past, one current and one future
        self.past_word = Label(self.window, text="past_word", font=('Arial',20),width=12)
        self.current_word = Label(self.window, text="current_word", font=('Arial',20), background='aquamarine1',width=12)
        self.future_word = Label(self.window, text="future_word", font=('Arial',20),width=12)
        
        # Entry where peaple type
        self.word_entry = Entry(
            self.window,
            width=15,
            font = ("courier",26),
            justify='center'
        )
        self.word_entry.bind("<KeyRelease>", self.check_entry)
        
        
        # Label for countdown
        self.countdown_label = Label(
            self.window,
            text = "0 s",
            width=12
        )
        
        # Label for score
        self.score_label = Label(
            self.window,
            text = f"Score: {self.score}",
            width=12
        )
        
        # Button for test
        self.countdown_button = Button(
            self.window,
            text="Start",
            command= self.start_timer
        )
        
    def draw(self):
        self.label_title.grid(row=0, column=0, columns=3)
        
        self.past_word.grid(row=1, column=0)
        self.current_word.grid(row=1, column=1)
        self.future_word.grid(row=1, column=2)
        
        self.word_entry.grid(row=2, column=1)
        
        self.countdown_label.grid(row=3, column=0)
        self.score_label.grid(row=3, column=1)
        self.countdown_button.grid(row=3, column=2)
        
    def update_words(self):
        self.word_manager.update_words()
        self.past_word.config(text=self.word_manager.past_word)
        self.current_word.config(text=self.word_manager.current_word)
        self.future_word.config(text=self.word_manager.future_word)
        
    def check_entry(self, event):
        if self.word_manager.check_word(self.word_entry.get()):
            self.update_words()
            self.word_entry.delete(0,END)
            if self.countdown_on :
                self.score += 1
                self.score_label.config(text = f"Score: {self.score}")
            
            
    def start_timer(self):
        self.countdown_on = True
        
        self.word_entry.delete(0,END)
        self.score = 0
        self.score_label.config(text = f"Score: {self.score}")
        self.count_down(60)
        
        
        
    def count_down(self,count):
        self.countdown_label.config(text=f"{str(count)} s")
        if count > 0:
            self.window.after(1000, self.count_down, count-1)
        else:
            self.countdown_on = False
            
        