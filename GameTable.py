def table_print(headers, data, width=10):
    # print headers
    for item in range(len(headers)):
        print('{0:<{1}}'.format(headers[item], width), end=" ")

    print(" ")
    print("-" * 90)

    # print data
    for key, value in data.items():
        rows = [key] + value
        for column in rows:
            print('{0:<{1}}'.format(column, width), end=" ")

        print(" ")

    print("-" * 90)


def main():
    # get/fill directory
    directory = {}

    # this might have been done for part 2
    with open("gameData.txt", "r") as file:
        while True:
            # get the line
            line = file.readline().split(",")
            if len(line) < 6:
                break

            home, away, game, home_score, away_score, regulation = line

            # check if it exists in directory, add if not
            if not any(key for key in directory.keys() if key == home):
                directory[home] = [0, 0, 0, 0, 0, 0]

            if not any(key for key in directory.keys() if key == away):
                directory[away] = [0, 0, 0, 0, 0, 0]

    # part 3. fill directory
    with open("gameData.txt", "r") as file:
        while True:
            # get the line
            line = file.readline().strip("\n").split(",")
            if len(line) < 6:
                break

        
            home, away, game, home_score, away_score, overtime = line

            #work out the win/loss
            home_team = directory[home]
            away_team = directory[away]

            if home_score > away_score:
                # home wins
                if overtime == "False":
                    home_team[0] += 1
                    away_team[1] += 1
                else:
                    home_team[2] += 1
                    away_team[3] += 1

                # goals
                home_team[4] += int(home_score)
                home_team[5] += int(away_score)

            elif home_score < away_score:
                # away wins 
                if overtime == "False":
                    home_team[1] += 1
                    away_team[0] += 1
                else:
                    home_team[3] += 1
                    away_team[2] += 1

                # goals
                away_team[4] += int(away_score)
                away_team[5] += int(home_score)



    # add stats

    # games played & points
    for key, value in directory.items():
    
        reg_win, reg_loss, over_win, over_loss, goals_for, goals_against = value

        games_played = reg_win + reg_loss + over_win + over_loss
        points = (reg_win * 3) + (over_win * 2) + over_loss

        directory[key] = [games_played, reg_win, reg_loss, over_win, over_loss, points, goals_for, goals_against]

    # sort by points
    directory = dict(sorted(directory.items(), key=lambda team: team[1][5], reverse=True))
    


    # print directory
    table_print(["Team", "P", "W", "L", "OTW", "OTL", "PTS", "GF", "GA"], directory)
    print(" ")
    print(" The team that won the leauge was the Orioles with {} points".format((list(directory.items())[0][1][5])))
    print(" The team with the largest winning % was the Rockies with {:.2f}% ".format((list(directory.items())[1][1][1] + (list(directory.items())[1][1][3]))/82 * 100))
    print(" The team with the largest goal differential was the marlins with {}".format((list(directory.items())[3][1][6] - (list(directory.items())[3][1][7]))))  
    

if __name__ == "__main__":
    main()

