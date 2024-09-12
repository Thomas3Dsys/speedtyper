from tkinter import *
import time

SENTENCE= "decide through sing unit example west has write his him the out list be hind minute change body full study fly"      
word_count = len(SENTENCE.split(" "))
start = 0.0
end = 0.0
done_flag = False
word_cursor = 0
cursor = 0 # character cursor

print(f"Testing typing of {word_count} words")

      

def key_pressed(event):
    """ 
        When the user types the next correct letter, increment the cursor. 
        Next highlight the text up to the cursor position.
        Start the timer when the first matching character is typed.
        Call the done method when the cursor is at the end of the sentence
        """
    global cursor, done, start, word_cursor, current_word

    if done_flag == True:
        return

    
    try:
        if win.focus_get()._name != "!text2" : 
            print("Type in the input box")
            return
    except: # not focus
        print("Type in the input box")
        return

    print(cursor)
    
    if(cursor == len(SENTENCE)-1):
        highlight_to(text,f"1.{len(SENTENCE)}")
        done()
        return
    
    if(cursor == 1):
        print("Start Timer")
        start = time.time()
    
    next_char = SENTENCE[cursor]
    if(event.char == next_char):
        if event.char == " ":
            if current_word  == entry.get("1.0", END).replace(" ","").replace("\n", ""):
                entry.delete("1.0", END)
                entry.pack()
                cursor += 1
                highlight_to(text,f"1.{cursor}")
                word_cursor = word_cursor + 1
                current_word = SENTENCE.split(" ")[word_cursor]
        else:
            cursor += 1
            highlight_to(text,f"1.{cursor}")
               
        

        
def done():
    """Stop the timer and calculate the words per minute typed and display to the user.
    """
    global win,done_flag
    done_flag = True
    print("Stop Timer")
    end = time.time()
    elapsed = end-start
    wpm = word_count / (elapsed / 60)
    msg = f"You typed {word_count} words in {'{0:.2f}'.format(elapsed)} seconds for a Words per minute of {'{0:.2f}'.format(wpm)}"
    print(msg)
    done_label=Label(win, width=80, height=15, font=('Calibri 12'), fg="#223333", text=msg)
    done_label.pack()
    entry.delete("1.0", END)
    entry.pack()
    text.configure(bg='#33ee33')
    text.pack()
  


def highlight_to(text, position):
    text.tag_add("start", "1.0",position)

win=Tk()
win.geometry("700x400")

text=Text(win, width=80, height=6, font=('Calibri 24'), bg="#CCCCCC")
text.insert(INSERT, SENTENCE)

text.tag_configure("start", background="OliveDrab1", foreground="black")
text.configure(state="disabled")
text.pack()

entry=Text(win, width=20, height=1, font=('Calibri 24'), bg="#dddddd")

entry.pack(pady = 10)


done_label=Label(win, font=('Calibri 14'), fg="#4444aa", text="Begin Typing to start the timer.")
done_label.pack()


current_word = SENTENCE.split(" ")[0]
win.bind("<Key>",key_pressed)#handles the user input

win.mainloop()
