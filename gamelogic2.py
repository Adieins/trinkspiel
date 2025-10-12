# game.py
import random

# list of standard tasks with placeholders
tasks = [
    "{player} takes 2 sips!",
    "{player}, attempt a back flip or drink 5 sips!",
    "Everybody take one sip for every deceased pet (RIP)",
    "{player}, name as many members of {other_player}'s family as you can. They take 1 sip for each one!",
    "The player with the smallest underwear (least amount of fabric) has to take a sip!",
    "Vote: Who would win a fist fight, {player} or {other_player}? Everybody who voted for the player with the least amount of votes takes a sip!",
    "Vote: Who is the biggest keyboard warrior? The winner gives out 5 sips!",
    "Vote: Who is the biggest alcoholic? The winner gives out 4 sips!",
    "{player}, you're only allowed to speak in questions until your next turn. Take a sip for everytime you break the rule!",
    "{player}, point to whoever you think has committed the most crimes. If the group agrees with you, give out 3 sips. If the group disagrees, take 3 sips instead!",
    "{player}, name as many flowers as you can within 10 seconds and give out a sip for each one!",
    "Take turns naming {player}'s problems. The first person to fail or repeat something has to take 2 sips. {other_player}, you start!",
    "{other_players}: If {player} died, what loot would they drop? The group votes on the best answer and the winner gives out 4 sips!",
    "Vote: Who is most likely to go to jail for tax evasion? The player with the most votes gives back to the community by giving out 4 sips!",
    "{player}, name {other_player}'s most problematic ex or take 2 sips!",
    "Take turns naming countries and their capitals. The first player to fail or repeat something takes 3 sips. {player}, you start!",
    "Take turns naming horror movies. The first player to fail or repeat something takes 3 sips. {player}, you start!",
    "{player} and {other_player}, name the first thing you would do as president. The group then votes on which policy they prefer. The winner gives out 3 sips!",
    "{player}, name your favourite conspiracy theory. If more than half the group share your belief, give out 3 sips. Otherwise take 3!",
    "{other_players}, share one your most embarrassing memories each. {player} decides which is worse. The chosen player takes 3 sips to numb the pain!",
    "{player}, name one of {other_player}'s pet peeves. If you're right, give out 3 sips, if you're wrong take them.",
    "Take turns naming cigarette brands. The first player to fail or repeat something takes 3 sips. {player}, you start!",
    "{player}, pick a word of your choice. {other_player} has to spell it. If they succeed, {other_player} can give out 3 sips, otherwise they take them!",
    "The player with the least amount of drink in their cup gives out 3 sips!",
    "Vote: Who is the most edible player? The winner gives out 4 sips!",
    "Vote: Would you rather have sex with a goat but nobody knows OR not have sex with a goat but everybody thinks you did? The group with the least votes takes 3 sips each!",
    "{player}: You're charged with murder. Who would you pick as your lawyer between {other_players}?",
    "Vote: Are you a mountain person or a beach person? The group with the least votes takes 3 sips each!"
]

def replace_placeholders(task_template, players):
    """replaces placeholders in a task with actual player names"""
    if not players:
        return "no players available"

    p1 = random.choice(players)

    # for {other_player}

    others = [p for p in players if p != p1]
    if others:
        p2 = random.choice(others)
    else:
        p2 = p1 # fall back in case of 1 player

    # for {other_players}

    if len(others) >= 2:
        p_group = random.sample(others, 2)
        p_group_str = ", ".join(p_group)
    elif len(others) == 1:
        p_group_str = others[0]
    else:
        p_group_str = p1 # fall back in case of 1 player

    task = (
        task_template
        .replace("{player}", p1)
        .replace("{other_player}", p2)
        .replace("{other_players}", p_group_str)
    )
    return task

def collect_custom_tasks(player_list):
    """each player can add one custom task at the beginning of the game"""
    custom_tasks = []
    for player in player_list:
        new_task = input(f"{player}, please submit your task: ")
        custom_tasks.append(new_task)
    return custom_tasks

def create_game_tasks(custom_tasks, total=30):
    """
    Builds a list of 'total' unique task templates.
    All custom tasks are guaranteed to be included.
    """
    if len(custom_tasks) > total:
        raise ValueError("too many custom tasks! maximum amount: 30")

    # erase doubles from custom tasks
    unique_custom = list(dict.fromkeys(custom_tasks))

    # add tasks from standard tasks that aren't in the customs
    available_standard = [t for t in tasks if t not in unique_custom]

    # randomly choose tasks until 30 is reached (no repetitions)
    needed = total - len(unique_custom)
    if needed > len(available_standard):
        raise ValueError("not enough standard-tasks to create 30 unique tasks")

    selected_standard = random.sample(available_standard, needed)

    # add everything together and shuffle
    game_tasks = unique_custom + selected_standard
    random.shuffle(game_tasks)
    return game_tasks

# start game
if __name__ == "__main__":
    players = input("submit player names, separated by comma: ").split(",")
    players = [p.strip() for p in players if p.strip()]

    if not players:
        print("no players submitted, game finished")
    else:
        # collect custom tasks
        custom_tasks = collect_custom_tasks(players)

        # generate game tasks
        game_tasks = create_game_tasks(custom_tasks, total=30)

        # show tasks one after the other
        for i, task_template in enumerate(game_tasks, start=1):
            task = replace_placeholders(task_template, players)
            print(f"round {i}: {tasks}")
