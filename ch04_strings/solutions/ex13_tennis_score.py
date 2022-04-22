# Examples program for the book "Python Challenges"
#
# Copyright 2020 by Michael Inden


def extract_points(score):
    values = score.strip().split(":")

    if len(values) != 2:
        raise ValueError("illegal format -- score has not" +
                         "format <points>:<points>, e.g. 7:6")

    score1 = int(values[0])
    score2 = int(values[1])

    # sanity check
    if score1 < 0 or score2 < 0:
        raise ValueError("points must be > 0")

    # verhindert sowohl z. B. 6:3 als auch 5:1
    if (score1 > 4 or score2 > 4) and abs(score1 - score2) > 2:
        raise ValueError("point difference must be < 3, " +
                         "otherwise invalid score")

    return score1, score2


def tennis_score(score, player1_name, player2_name):
    points = extract_points(score)

    score1 = points[0]
    score2 = points[1]

    if score1 >= 3 and score2 >= 3:
        return generate_info(score1, score2, player1_name, player2_name)
    elif score1 >= 4 or score2 >= 4:
        return "Game " + (player1_name if (score1 > score2) else player2_name)
    else:
        # Spezielle Namensgebung
        point_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

        return point_names[score1] + " " + point_names[score2]


def generate_info(score1, score2, player1_name, player2_name):
    score_difference = abs(score1 - score2)

    player_name = player1_name if (score1 > score2) else player2_name

    if score1 == score2:
        return "Deuce"
    if score_difference == 1:
        return "Advantage " + player_name
    if score_difference == 2:
        return "Game " + player_name

    raise ValueError("Unexpected difference: " + score_difference)


def main():
    print(tennis_score("3:1", "Micha", "Tim"))
    print(tennis_score("4:3", "Micha", "Tim"))
    print(tennis_score("5:3", "Micha", "Tim"))


if __name__ == "__main__":
    main()
