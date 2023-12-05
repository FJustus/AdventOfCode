def main():
    games = open("input.txt").read()
    #games = "A X\nA Y\nA Z\nB X\nB Y\nB Z\nC X\nC Y\nC Z"

    part = 2

    plays = {"A":1, "B":2, "C":3}
    responses = {"X":1, "Y":2, "Z":3}

    games = games.split("\n")
    points = 0

    for game in games:
        play, response = game.split(" ")
        play = plays[play]
        
        if part == 1:
            response = responses[response]
        else:
            # X = loss, Z = win
            match play, response:
                case _, "Y":
                    response = play
                case 1, "X":
                    response = 3
                case 1, "Z":
                    response = 2 
                case 2, "X":
                    response = 1
                case 2, "Z":
                    response = 3
                case 3, "X":
                    response = 2
                case 3, "Z":
                    response = 1 
        # 1 = Rock, 2 = Paper, 3 = Scissors
        points += response
        

        if play == response:
            points += 3
        elif (play+1)%3==response%3:
            points += 6
        """ 
        # also works but is not fancy enough
        match play, response:
            case (1, 1) | (2, 2) | (3, 3):
                points += 3
            case (1, 2) | (2, 3) | (3, 1):
                points += 6
        """

    print(f"Part {part}: sum= {points}")


main()