import random
from collections import Counter

def randomQuestion():
    questionsList = [
        "Who is most likely to survive the apocalypse? ",
        "Who is most likely to start a band? ",
        "Who is most likely to become president? ",
        "Who is most likely to eat the weirdest animal? ",
        "Who is most likely to become a famous athlete? ",
        "Who is most likely to make a video game? "
    ]

    random.shuffle(questionsList)
    return questionsList

def start():
    q_list = randomQuestion()
    p_list = [
        ["1", "Name1", 0],
        ["2", "Name2", 0],
        ["3", "Name3", 0],
        ["4", "Name4", 0],
        ["5", "Name5", 0],
        ["6", "Name6", 0],
        ["7", "Name7", 0],
        ["8", "Name8", 0],
        ["9", "Name9", 0],
        ["10", "Name10", 0],
        ["11", "Name11", 0],
        ["12", "Name12", 0],
        ["13", "Name13", 0]
    ]

    for q in q_list:
        print(q)
        votes = []
        for p in p_list:
            vote = input(f"{p[1]} which player number? ")
            votes.append(vote)
            counts = Counter(votes)
            winner = max(counts, key=counts.get)
            p_list[int(winner) -1][2] += 1
            
    overall_winner = max(p_list, key= lambda x: x[2])
    print(f"The Winner Is: {overall_winner[1]}")
        
if __name__ == '__main__':
    try:
        start()
    except ValueError as Err:
        print(Err)
