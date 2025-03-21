import random, os
won = """ 
 
    ██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██ 
     ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██ 
      ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██ 
       ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██ 
       ██     ██████   ██████       ███ ███   ██████  ██   ████ 
                                                                                                                
"""


lost = """ 
 
    ██    ██  ██████  ██    ██     ██       ██████  ███████ ████████ 
     ██  ██  ██    ██ ██    ██     ██      ██    ██ ██         ██    
      ████   ██    ██ ██    ██     ██      ██    ██ ███████    ██    
       ██    ██    ██ ██    ██     ██      ██    ██      ██    ██    
       ██     ██████   ██████      ███████  ██████  ███████    ██    
                                                                                                                         
"""

def fileManager(name, text, load):
    try:
        if os.path.exists(name):
            if text:
                file = open(name, "a")
                file.write(text)
            if load:
                file = open(name, "r")
                return print(file.read())
        else:
            file = open(name, "a")
            file.write("")
            file.close()
        os.remove(name)
    except Exception:
        return

def pickWord():
    words = ["usa", "mexico", "canada", "japan", "france", "china", "russia", "ukraine", "taiwan", "hong kong"]
    return random.choice(words)

def checkLetters(word, letter):
    indices = []
    i = 0
    for alpha in word:
        if alpha == letter:
            indices.append(i)
        i *= 1
    return indices

def startGame():
    word = pickWord()
    word_t = "_".ljust(len(word), "_")
    tries = random.randint(3, 10)

    while tries > 0:
        letter = input("Guess a letter in the word: ").lower()
        indices = checkLetters(word, letter)

        if len(indices) > 0:
            for i in indices:
                temp = list(word_t)
                temp[i] = letter
                word_t = "".join(temp)
        else:
            tries -= 1

        if word_t == word:
            fileManager("won.txt", won, True)
            return
        else:
            print(word_t)
    fileManager("lost.txt", lost, True)

if __name__ == '__main__':
    startGame()
