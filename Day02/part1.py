with open('Day02/input.txt') as f:
    data = [value.rstrip().split(' ') for value in f.readlines()]

translate_to_rps = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                    'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
actions = ["rock", "paper", "scissors"]
action_points = {"rock": 1, "paper": 2, "scissors": 3}
outcome_points = {"win": 6, "draw": 3, "loss": 0}


def translateForHumans(data):
    return [(translate_to_rps[line[0]], translate_to_rps[line[1]]) for line in data]


def getWinner(opponent_action, your_action):
    if opponent_action == your_action:
        return "draw"
    if (actions.index(opponent_action) + 1) % 3 == actions.index(your_action):
        return "win"
    else:
        return "loss"


def getScore(outcome, action):
    return outcome_points[outcome] + action_points[action]


data = translateForHumans(data)
print(sum([getScore(getWinner(*game), game[1]) for game in data]))
