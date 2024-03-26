class Player:

    def __init__(self, name, chicken_wings, hamburgers, hot_dogs):
        self.name = name
        self.score = (chicken_wings*5)+(hamburgers*3)+(hot_dogs*2)


def score_board(players):
    scores = list()

    for player_details in players:
        player = Player(player_details["name"], player_details["chicken_wings"], player_details["hamburgers"], player_details["hot_dogs"])
        scores.append({"name": player.name, "score": player.score})

    scores.sort(key=lambda x: (-x["score"], x["name"]))

    return scores