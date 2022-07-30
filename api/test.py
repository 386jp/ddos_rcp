from enum import Enum
from collections import Counter

class RcpChoices(str, Enum):
    ROCK = "ROCK"
    SCISSORS = "SCISSORS"
    PAPER = "PAPER"

class RcpResults(str, Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    DRAW = "DRAW"

def get_rcp_result(in_: dict[str, RcpChoices]) -> dict[str, RcpResults]:
    """じゃんけんの勝敗判定を行う関数

    Args:
        in_ (dict[str, RcpChoices]): ユーザーと出した手を格納した辞書

    Returns:
        dict[str, RcpResults]: ユーザーと勝敗を格納した辞書
    """
    unique_results = list(Counter(in_.values()))
    if len(unique_results) != 2:
        return {n: RcpResults.DRAW for n, _ in in_.items()}
    else:
        if RcpChoices.ROCK in unique_results:
            if RcpChoices.SCISSORS in unique_results:
                return {n: RcpResults.WIN if r == RcpChoices.ROCK else RcpResults.LOSE for n, r in in_.items()}
            elif RcpChoices.PAPER in unique_results:
                return {n: RcpResults.WIN if r == RcpChoices.PAPER else RcpResults.LOSE for n, r in in_.items()}
        return {n: RcpResults.WIN if r == RcpChoices.SCISSORS else RcpResults.LOSE for n, r in in_.items()}

if __name__ == "__main__":
    print(get_rcp_result({"1": RcpChoices.PAPER, "2": RcpChoices.SCISSORS, "3": RcpChoices.PAPER}))