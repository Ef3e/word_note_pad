import json
from tkinter import ttk
from tkinter import messagebox
import time
import tkinter as tk
import random

sayi = 0
values = ["a-z","z-a","normal"]
for a in values:
    values[sayi] = a.upper()
    sayi += 1
window = tk.Tk()
window.title("Words")
window.geometry("350x270+300+150")
window.configure(bg="#ECEE66")
window.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")
# these codes work to destroy all windows
def close_all_windows():
    #if messagebox.askokcancel("Exit", "Are you sure about exit from application"):
    window.destroy()

window.protocol("WM_DELETE_WINDOW", close_all_windows)
#---------------------------------------

# |we disable manual resizable|
window.resizable(width=False,height=False)

# |this button works to add a new word|
add_word_button = tk.Button(window,text="Add New Word",font="bold 10",height=2)
add_word_button.place(x=5,y=65)
# -----------------------------------

# |this button will show information of the word which we select|
show_info_button = tk.Button(window,text="Show Word",font="bold 10",height=2,width=11)
show_info_button.place(x=5,y=115)
# ------------------------------------

but1 = tk.Button(window,bg="#ECEE66",width=10,text="TRUE = ")
but2 = tk.Button(window,bg="#ECEE66",width=10,text="FALSE = ")

but1.place(x=110,y=230)
but2.place(x=220,y=230)
# |this button will set of the word which we select|
delete_button = tk.Button(window,text="Delete",font="bold 10",height=2,width=11)
delete_button.place(x=5,y=165)
# ------------------------------------
#
try_button = tk.Button(window,text="Try Yourself")
try_button.place(x=15,y=220)

#
# |The all words will appear in this box|
words_listbox = tk.Listbox(window,width=30,height=13,font="sans 10 bold")
words_listbox.place(x=110,y=5)
bar = ttk.Scrollbar(window,command=words_listbox.yview)
bar.pack(side="right", fill="y")
# --------------------------------------
wrong_answers = []
# |this button will sort the words by selected|
sort_button = tk.Button(window,text=" Sort ",font="bold 8")
sort_button.place(x=35,y=30)
sort_combo = ttk.Combobox(window,values=values,width=8)
sort_combo.place(x=20,y=5)
# --------------------------------------

# this function works to select a word
def select(arg):
    return arg.selection_get()
#---------------------------------------

words = []
words_names = []

type_words = ["NOUNS","ADJECTIVES","PRONOUNS","VERBS",
              "ADVERBS","PREPOSİTİONS","CONJUNCTIONS","INTERJACTIONS","PATTERN"]

class word():
    def __init__(self,word,turkish_mean,description,word_type,sentence,date):
        self.word = word
        self.mean = turkish_mean.lower()
        self.description = description
        self.type = word_type
        self.date = date
        self.sentence = sentence
        words.append(self)
        words_names.append(self.word)
        
try:    
    with open("words.json","r",encoding="utf-8") as f:
        read = json.load(f)  
    for u in read[0]["Words"]:
        word(u["Word"],u["Turkish_mean"],u["Description"],u["Type"],u["Sentence"],u["Date"])
    for a in words_names: 
        words_listbox.insert(len(words_names)-1,a)
except:
    ...
# |this function works to delete the word which we select|

def delete_func():
    take = sort_combo.get()
    selected = select(words_listbox)
    words_listbox.delete(0,tk.END)
    index = words_names.index(selected) 
    words.pop(index)
    words_names.remove(selected)
    second_names = words_names.copy()
    sayi = 0
    try:
        with open("words.json","r",encoding="utf-8") as a:
            read = json.load(a)
        read[0]["Words"].pop(index)
        with open("words.json","w",encoding="utf-8") as f:
            json.dump(read,f,ensure_ascii=False,indent=4)
    except:
        ...   
    if take == "A-Z":
        second_names.sort(reverse=False)
    if take == "Z-A":
        second_names.sort(reverse=True)
    if take == "NORMAL":
        second_names = words_names       
    for u in second_names:
        words_listbox.insert(sayi,u)
        sayi += 1

# |we gave a command to delete button by "configure" function|
delete_button.configure(command=delete_func)
#------------------------------------------
def show_wrong_answers():
    if len(wrong_answers) > 0:
        wrong_answer_window = tk.Toplevel(window)
        wrong_answer_window.title("Words")
        wrong_answer_window.geometry("350x180+300+150")
        wrong_answer_window.configure(bg="#ECEE66")
        wrong_answer_window.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")
        listbox = tk.Listbox(wrong_answer_window,width=53,height=8)
        listbox.place(x=5,y=5)
        listb = ttk.Scrollbar(wrong_answer_window,command=listbox.yview)
        listb.pack(side="right", fill="y")

        bt = tk.Button(wrong_answer_window,text=("show"))
        bt.place(x=140,y=140)
        sayi = 0
        listbox.delete(0,tk.END)
        for u in wrong_answers:
            listbox.insert(sayi,u["word"])
        def show():
            selected = listbox.selection_get()
            for u in wrong_answers:
                if u["word"] == selected:
                    try:
                        ww = tk.Toplevel(wrong_answer_window)
                        ww.title("Words")
                        ww.geometry("350x80+670+150")
                        ww.configure(bg="#ECEE66")
                        ww.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")
                        lab1 = tk.Label(ww,text="word",bg="#ECEE66").place(x=30,y=5)
                        lab2 = tk.Label(ww,text="turkish mean",bg="#ECEE66").place(x=130,y=5)
                        lab3 = tk.Label(ww,text="your answer",bg="#ECEE66").place(x=250,y=5)
                        entr1 = tk.Entry(ww,width=15,justify=tk.CENTER)
                        entr1.insert(0,u["word"])
                        entr1.place(x=0,y=30)
                        entr2 = tk.Entry(ww,width=15,justify=tk.CENTER)
                        entr2.insert(0,u["Turkish mean"])
                        entr2.place(x=120,y=30)
                        entr3 = tk.Entry(ww,width=15,justify=tk.CENTER)
                        entr3.insert(0,u["given answer"])
                        entr3.place(x=240,y=30)
                    except:
                        pass
                    break                
        bt.configure(command=show)
but2.configure(command=(show_wrong_answers))
def show_info_word():
    try:
        info_window = tk.Toplevel(window)
        info_window.resizable(height=False,width=False)
        info_window.configure(bg="#ECEE66")
        info_window.geometry("370x190+680+150")
        info_window.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")

        seletc_word = select(words_listbox)
        seleted_index = words_names.index(seletc_word)
        main_word = words[seleted_index]
        
        word_entry = tk.Entry(info_window,justify=tk.CENTER,font="sans 10 bold",bg="#ECEE67",fg="red",width=47)
        word_entry.place(x=30,y=15)
        word_entry.insert(0,main_word.word)
        
        turkish_mean_entry = tk.Entry(info_window,justify=tk.CENTER,font="sans 10 bold",bg="#ECEE67",fg="red",width=47)
        turkish_mean_entry.place(x=30,y=40)
        turkish_mean_entry.insert(0,main_word.mean)
        
        example_sentence_entry = tk.Entry(info_window,bg="#ECEE67",fg="red",justify=tk.CENTER,font="sans 10 bold",width=47)
        example_sentence_entry.place(x=30,y=65)
        example_sentence_entry.insert(0,main_word.sentence)
        
        description_entry = tk.Entry(info_window,justify=tk.CENTER,font="sans 10 bold",bg="#ECEE67",fg="red",width=47)
        description_entry.place(x=30,y=90)
        description_entry.insert(0,main_word.description)
        
        type_combobox = ttk.Combobox(info_window,justify=tk.CENTER,font="sans 12 bold",values=type_words,width=12)
        type_combobox.place(x=30,y=115)
        type_combobox.insert(0,main_word.type)

        save_button = tk.Button(info_window,text="Save",font="sans 12 bold",width=12)
        save_button.place(x=230,y=110)
        def save_it():
            try:
                with open("words.json","r",encoding="utf-8") as f:
                    read = json.load(f)
                features = {"Word":word_entry.get(),"Turkish_mean":turkish_mean_entry.get(),"Type":type_combobox.get(),
                    "Description":description_entry.get(),"Sentence":example_sentence_entry.get(),"Date":time.strftime("%x")}
                read[0]["Words"][seleted_index] = features
                with open("words.json","w",encoding="utf-8") as f:
                    read = json.dump(read,f,ensure_ascii=False,indent=4)
                info_window.destroy()
                words[seleted_index] = word(features["Word"],features["Turkish_mean"],features["Description"],features["Type"],features["Sentence"],features["Date"])
                for u in words_names:
                    if u == seletc_word:
                        indexx = words_names.index(seletc_word)
                        words_names[indexx] = features["Word"]
                        break
                words_listbox.delete(0,tk.END)
                words_names.pop(-1)
                for a in words_names: 
                    words_listbox.insert(len(words_names)-1,a)
            except:
                pass
        save_button.configure(command=save_it)
        info_window.mainloop()
    except:
        info_window.destroy()
show_info_button.configure(command=show_info_word)
# |this function works to add new word to json|
def add_word_func():
    word_window = tk.Toplevel(window)
    word_window.resizable(height=False,width=False)
    word_window.configure(bg="#ECEE66")
    word_window.geometry("370x190+680+150")
    word_window.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")
    # | we gave two argument for this function |
    # | first argument determines the entry    |
    # | second argument is that entry's text   |
    def entries(selected_entry,text):
        # |this function will destroy the text in the entry which we click|
        a= text
        def delete(e):
            get = selected_entry.get()
            if get == a:            
                selected_entry.delete(0,"end")
        selected_entry.insert(0,text)
        if selected_entry.get() == text:
            selected_entry.bind("<FocusIn>",delete)
    # we will take the word name from this entry 
    word_entry = tk.Entry(word_window,justify=tk.CENTER,font="bold 10",width=28)
    word_entry.place(x=30,y=15)
    entries(word_entry,"Word")
    #-----------------------------------

    # we will take the turkish meaning from this entry 
    turkish_mean_entry = tk.Entry(word_window,justify=tk.CENTER,font="bold 10",width=28)
    turkish_mean_entry.place(x=30,y=40)
    entries(turkish_mean_entry,"Turkish Mean")
    #------------------------------------

    # we will take the example sentece from this entry 
    example_sentence_entry = tk.Entry(word_window,justify=tk.CENTER,font="bold 10",width=28)
    example_sentence_entry.place(x=30,y=65)
    entries(example_sentence_entry,"Example Sentence")
    #-------------------------------------

    # we will take the description from this entry 
    description_entry = tk.Entry(word_window,justify=tk.CENTER,font="bold 10",width=28)
    description_entry.place(x=30,y=90)
    entries(description_entry,"Description")
    #---------------------------------------
    

    type_label = tk.Label(word_window,text="Type Of Word",bg=word_window["bg"],font="bold 12")
    type_label.place(x=240,y=15)

    type_combobox = ttk.Combobox(word_window,justify=tk.CENTER,font="bold 10",values=type_words,width=12)
    type_combobox.place(x=240,y=40)

    save_button = tk.Button(word_window,text="SAVE",height=2,width=13)
    save_button.place(x=240,y=70)
    # |this function will work when we click save button|
    def save_func():
        features = {"Word":word_entry.get(),"Turkish_mean":turkish_mean_entry.get(),"Type":type_combobox.get(),
                    "Description":description_entry.get(),"Sentence":example_sentence_entry.get(),"Date":time.strftime("%x")}
        try:
            with open("words.json","r",encoding="utf-8") as f:
                read = json.load(f)
            read[0]["Words"].append(features)
            with open("words.json","w",encoding="utf-8") as f:
                json.dump(read,f,ensure_ascii=False,indent=4)
        except:
            with open("words.json","w",encoding="utf-8") as f:
                json.dump([{"Words":[features]}],f,ensure_ascii=False,indent=4)
        word(features["Word"],features["Turkish_mean"],features["Description"],features["Type"],features["Sentence"],features["Date"])
        words_listbox.insert(len(words_names),features["Word"])
        word_window.destroy()
    save_button.configure(command=save_func)
    word_window.mainloop()

# |and we append a command to add_word_button by "configure" function|
add_word_button.configure(command=add_word_func)
def try_func():
    wrong_answers.clear()
    global true_answers
    global false_answers
    global random_word
    try_window = tk.Toplevel(window)
    try_window.resizable(height=False,width=False)
    try_window.configure(bg="#ECEE66")
    try_window.geometry("200x130+680+150")
    try_window.iconbitmap("C:\\Users\\efeek\\Desktop\\pyhton\\a.ico")
    words_copy = words.copy()
    random_word = random.choice(words_copy)
    words_copy.remove(random_word)
    
    lab1 = tk.Label(try_window,text="|Turkish mean|",bg="#ECEE66").place(x=60,y=45)
    lab2 = tk.Label(try_window,text="TRUE = ",bg="#ECEE66",width=9)
    lab3 = tk.Label(try_window,text="FALSE =",bg="#ECEE66",width=9)
    lab2.place(x=5,y=100)
    lab3.place(x=125,y=100)
    english_word = tk.Entry(try_window,justify=tk.CENTER)
    english_word.insert(0,random_word.word)
    english_word.place(x=40,y=10)
    
    answer_entry = tk.Entry(try_window)
    answer_entry.place(x=40,y=70)
    
    check = tk.Button(try_window,text="check")
    check.place(x=75,y=100)
    true_answers = 0 
    false_answers = 0
    def check_answer():
        global wrong_answers
        global true_answers
        global false_answers        
        global random_word
        answer_get = answer_entry.get()
        answer_entry.delete(0,tk.END)
        if answer_get.lower() == random_word.mean.lower:
            true_answers +=  1
            lab2.configure(text=f"TRUE = {true_answers}")
        else:
            false_answers += 1
            lab3.configure(text=f"FALSE = {false_answers}")
            wrong_answers.append({"word":random_word.word,"Turkish mean":random_word.mean,"given answer":answer_get})    
        but1.configure(text=f"TRUE = {true_answers}")
        but2.configure(text=f"FALSE = {false_answers}")
        if len(words_copy) == 0:
            try_window.destroy()
        else:    
            english_word.delete(0,tk.END)
            random_word = random.choice(words_copy)
            words_copy.remove(random_word)
            english_word.insert(0,random_word.word)
    check.configure(command=check_answer)

    try_window.mainloop()

try_button.configure(command=try_func)

def sort_function():
    words_listbox.delete(0,tk.END)
    second_names = words_names.copy()
    sort_type = sort_combo.get()
    sayi = 0
    if sort_type == "A-Z":
        second_names.sort(reverse=False)
    if sort_type == "Z-A":
        second_names.sort(reverse=True)
    if sort_type == "NORMAL":
        second_names = words_names   
    for u in second_names:
        words_listbox.insert(sayi,u)
        sayi+=1
sort_button.configure(command=sort_function)
window.mainloop()
