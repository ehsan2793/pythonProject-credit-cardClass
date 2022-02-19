from higher_lower_data import data
import random
logo = """
██╗░░██╗██╗░██████╗░██╗░░██╗███████╗██████╗░  ░█████╗░██████╗░  ██╗░░░░░░█████╗░░██╗░░░░░░░██╗███████╗██████╗░
██║░░██║██║██╔════╝░██║░░██║██╔════╝██╔══██╗  ██╔══██╗██╔══██╗  ██║░░░░░██╔══██╗░██║░░██╗░░██║██╔════╝██╔══██╗
███████║██║██║░░██╗░███████║█████╗░░██████╔╝  ██║░░██║██████╔╝  ██║░░░░░██║░░██║░╚██╗████╗██╔╝█████╗░░██████╔╝
██╔══██║██║██║░░╚██╗██╔══██║██╔══╝░░██╔══██╗  ██║░░██║██╔══██╗  ██║░░░░░██║░░██║░░████╔═████║░██╔══╝░░██╔══██╗
██║░░██║██║╚██████╔╝██║░░██║███████╗██║░░██║  ╚█████╔╝██║░░██║  ███████╗╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██║░░██║
╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ░╚════╝░╚═╝░░╚═╝  ╚══════╝░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚═╝

"""
def format_data(data):
    data_name = data["name"]
    data_descr = data["description"]
    data_country = data["country"]
    return f"{data_name}, a {data_descr}, from {data_country}"
def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
end_of_game = False

data_b = random.choice(data)

while not end_of_game:
    data_a = data_b
    data_b = random.choice(data)
    if data_a == data_b:
        data_b = random.choice(data)

    print(f"compare A: {format_data(data_a)}.")
    print("VS.")
    print(f"compare B: {format_data(data_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = data_a["follower_count"]
    b_follower_count = data_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        end_of_game = True
        print(f"Sorry, that's wrong. Final score: {score}.")
