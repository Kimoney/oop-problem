def score_board(players):
    scores = []
    for player in players:
        score = player['chickenwings'] * 5 + player['hamburgers'] * 3 + player['hotdogs'] * 2
        scores.append({'name': player['name'], 'score': score})    
# Sort scores by score in descending order, then by name in ascending order
    scores.sort(key=lambda x: (-x['score'], x['name']))
    return scores

# Test Case:
players = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "Big Bob", 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
]
players2 = [
    {'name': "Habanero Hillary", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11},
    {'name': "John Doe", 'chickenwings': 5, 'hamburgers': 17, 'hotdogs': 11}
]

results = score_board(players)
results2 = score_board(players2)
print(results)
print(results2)