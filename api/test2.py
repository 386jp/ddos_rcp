
def get_rcp_result(user_1: str, user_2: str) -> str:
    if user_1 == user_2:
        return "DRAW"
    elif user_1 == "ROCK":
        if user_2 == "SCISSORS":
            return "user_1 WIN"
        elif user_2 == "PAPER":
            return "user_2 WIN"
    elif user_1 == "SCISSORS":
        if user_2 == "ROCK":
            return "user_2 WIN"
        elif user_2 == "PAPER":
            return "user_1 WIN"
    elif user_1 == "PAPER":
        if user_2 == "ROCK":
            return "user_1 WIN"
        elif user_2 == "SCISSORS":
            return "user_2 WIN"
    return "DRAW"

if __name__ == "__main__":
    print(get_rcp_result("ROCK", "SCISSORS"))