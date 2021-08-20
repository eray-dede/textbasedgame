import random
import time

# GLOBAL
coach = {}
computer_team = {
    "name": " ",
    "team_roster": ["Curry", "Harden", "James", "Durant", "Davis"]
}

game_db = {
    "score_text": {"goal": "made it!", "missed": "have missed it!"},
    "available_teams": ["Slam Dunkers", "Sharp Shooters", "Flashy Passers", "Jelly Fams"],
    "player_pool": {"Mike James": 5, "Shane Larkin": 4, "Wade Baldwin": 3, "Kostas Sloukas": 2, "Pierra Henry": 1,
                     "Alexey Shved": 5, "Vasilije Micic": 4, "Nando De Colo": 3, "Nick Calathes": 2, "Jordan Loyd": 1,
                     "Vladimir Lucic": 5, "Shavon Shields": 4, "Will Clyburn": 3, "Krunoslav Simon": 2, "Dyshawn Pierre": 1,
                     "Nikola Mirotic": 5, "Sasha Vezenkov": 4, "Achille Polonara": 3, "Tornike Shengelia": 2, "Bojan Dublijevic": 1,
                     "Jan Vesely": 5, "Eddy Tavares": 4, "Nikola Milutinov": 3, "Brandon Davies": 2, "Jalen Reynolds": 1}
}


action1_text = ["He brings the ball to the opposition court", "He throws the ball into play"]
action2_text = ["He passes the ball to", "He gives the ball to", "He bounces it to", "He hands of ball to"]
action3_text = ["He surpasses his opponent", "He crosses the defender", "He splits the defence"]
action4_text = ["He shoots beyond the arc", "He shoots a mid-range shot", "He lays a layup", "He steps back and shoots"]

def match_engine():
    my_team_score = 0
    comp_team_score = 0
    match_time = 0
    print("There is the jump ball and here goes the game! ")
    while match_time < 10:
        score_or_not = random.randint(0,1)
        the_ball = random.randint(0,1)
        if the_ball == 0:
            copied_team_roster = list(computer_team["team_roster"])
            random_computer_player1 = random.choice(copied_team_roster)
            copied_team_roster.remove(random_computer_player1)
            random_computer_player2 = random.choice(copied_team_roster)
            time.sleep(2)
            print("The ball is taken by {}. {} {}. {} and {}".format(random_computer_player1, random.choice(action2_text), random_computer_player2, random.choice(action3_text), random.choice(action4_text)))
            time.sleep(2)
            if score_or_not == 1:
                time.sleep(2)
                print("{} {}".format(computer_team["name"], game_db["score_text"]["goal"]))
                comp_team_score += 1
                time.sleep(2)
                print("It is {} - {} ".format(comp_team_score, my_team_score))
                match_time += 1
            else :
                time.sleep(2)
                print("{} {} ".format(computer_team["name"], game_db["score_text"]["missed"]))
                time.sleep(2)
                print("It is {} - {} ".format(comp_team_score, my_team_score))
                match_time += 1
        else :
            copied_coach_roster = list(coach["team_roster"])
            random_coach_player1 = random.choice(copied_coach_roster)
            copied_coach_roster.remove(random_coach_player1)
            random_coach_player2 = random.choice(copied_coach_roster)
            time.sleep(2)
            print("The ball is taken by {}. {} {}. {} and {}".format(random_coach_player1, random.choice(action2_text), random_coach_player2 , random.choice(action3_text), random.choice(action4_text)))
            time.sleep(2)
            if score_or_not == 1:
                time.sleep(2)
                print("{} {} ".format(coach["team_name"], game_db["score_text"]["goal"]))
                my_team_score += 1
                time.sleep(2)
                print("It is {} - {} ".format(comp_team_score, my_team_score))
                match_time += 1
            else:
                time.sleep(2)
                print("{} {} ".format(coach["team_name"], game_db["score_text"]["missed"]))
                time.sleep(2)
                print("It is {} - {} ".format(comp_team_score, my_team_score))
                match_time += 1

    if my_team_score > comp_team_score:
        print("{} - {} {} win!".format(my_team_score, comp_team_score, coach["team_name"]))
    elif my_team_score < comp_team_score:
        print("{} - {} {} win!".format(my_team_score, comp_team_score, computer_team["name"]))
    else:
        print("{} - {} It's a tie".format(my_team_score, comp_team_score))


def get_coach_info():
    intro_text = """
        Hi {}, you have {} million dollars to choose 5 players for your street ball team.
        And you must choose 1 point guard,1 shooting guard,1 small forward,1 power forward and a center.
    """
    coach["name"] = input("Enter your coach name: ")
    coach["budget"] = 15
    coach["team_roster"] = []
    coach["team_name"] = input("Enter team name for your team: ")
    print(intro_text.format(coach["name"], coach["budget"]))

    computer_team["name"] = random.choice(game_db["available_teams"])

    print("Your match is against '" + computer_team["name"] + "' ")


def print_player_pool():
    for key,value in game_db["player_pool"].items():
        print("Name: {} Value: {} Dollars".format(key, value))


def print_starting_five():
    print("\n".join(coach["team_roster"]))
    print("Here is your starting 5,let's make a exhibition match!")


def select_starting_five():
    while len(coach["team_roster"]) < 5:
       bought_player = input("Write the name of the player that you want to buy:")
       if bought_player in coach["team_roster"]:
          print(bought_player + " is already in your team")
          continue
       if bought_player not in game_db["player_pool"]:
           print("The player that you write cannot be found on the transfer list")
           continue
       print("Player: {} Value: {} Dollars {}'s Budget: {} Dollars".format(bought_player, game_db["player_pool"][bought_player], coach["name"], coach["budget"]))
       ask_to_approve = input("Are you sure that you want to make this transfer? y or n ?")
       if ask_to_approve.lower() != "y":
           continue
       if coach["budget"] - game_db["player_pool"][bought_player] < 0 :
           print("Not enough resources to build the team.Please try to sell players.")
           ask_to_sell = input ("you have to sell players to not exceed the budget,enter the player that you want to sell: ")
           if ask_to_sell not in coach["team_roster"] :
                continue
           print("{} , Value: {} Dollars Sold".format(ask_to_sell,game_db["player_pool"][bought_player]))
           coach["team_roster"].remove(ask_to_sell)
           coach["budget"] += game_db["player_pool"][ask_to_sell]
           print("{} dollars is your new budget".format(coach["budget"]))
           print("you have {} players in your team.".format(str(len(coach["team_roster"]))))
           continue
       coach["budget"] -= game_db["player_pool"][bought_player]
       coach["team_roster"].append(bought_player)
       print("you have {} players in your team with remaining {} Dollars".format(str(len(coach["team_roster"])), coach["budget"]))


# staring point of the program
if __name__ == "__main__":
    get_coach_info()
    print_player_pool()
    select_starting_five()
    print_starting_five()
    match_engine()