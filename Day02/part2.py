with open('Day02/input.txt') as f:
    data = [value.rstrip().split(' ') for value in f.readlines()]

translate_to_rps = {'A': 'rock', 'B': 'paper', 'C': 'scissors',
                    'X': 'loss', 'Y': 'draw', 'Z': 'win'}
actions = ["rock", "paper", "scissors"]
action_points = {"rock": 1, "paper": 2, "scissors": 3}
outcome_points = {"win": 6, "draw": 3, "loss": 0}


def translateForHumans(data):
    result = []

    for line in data:
        opponent_action = translate_to_rps[line[0]]
        your_action = getAction(opponent_action, translate_to_rps[line[1]])
        result.append([opponent_action, your_action])

    return result


def getWinner(opponent_action, your_action):
    if opponent_action == your_action:
        return "draw"
    if your_action == getWinningAction(opponent_action):
        return "win"
    else:
        return "loss"


def getScore(outcome, action):
    return outcome_points[outcome] + action_points[action]


def getAction(opponent_action, prefered_outcome):
    if prefered_outcome == "draw":
        return opponent_action
    if prefered_outcome == "win":
        return getWinningAction(opponent_action)
    return getWinningAction(getWinningAction(opponent_action))


def getWinningAction(action):
    return actions[(actions.index(action)+1) % len(actions)]


data = translateForHumans(data)
print(sum([getScore(getWinner(*game), game[1]) for game in data]))
