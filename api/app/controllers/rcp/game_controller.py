import random
from enum import Enum
from collections import Counter

from app.controllers import crud

def get_rcp_result(in_: dict[str, crud.result.RcpChoices]) -> dict[str, crud.result.RcpResults]:
    """じゃんけんの勝敗判定を行う関数

    Args:
        in_ (dict[str, crud.result.RcpChoices]): ユーザーと出した手を格納した辞書

    Returns:
        dict[str, crud.result.RcpResults]: ユーザーと勝敗を格納した辞書
    """
    if len(in_) <= 1:
        raise ValueError("in_ must have at least 2 items.")
    unique_results = list(Counter(in_.values()))
    if len(unique_results) != 2:
        return {n: crud.result.RcpResults.DRAW for n, _ in in_.items()}
    else:
        if crud.result.RcpChoices.ROCK in unique_results:
            if crud.result.RcpChoices.SCISSORS in unique_results:
                return {n: crud.result.RcpResults.WIN if r == crud.result.RcpChoices.ROCK else crud.result.RcpResults.LOSE for n, r in in_.items()}
            elif crud.result.RcpChoices.PAPER in unique_results:
                return {n: crud.result.RcpResults.WIN if r == crud.result.RcpChoices.PAPER else crud.result.RcpResults.LOSE for n, r in in_.items()}
        return {n: crud.result.RcpResults.WIN if r == crud.result.RcpChoices.SCISSORS else crud.result.RcpResults.LOSE for n, r in in_.items()}

def get_bot_choice() -> crud.result.RcpChoices:
    return random.choice(list(crud.result.RcpChoices))

def save_rcp_result(in_: dict[str, crud.result.RcpChoices], out_: dict[str, crud.result.RcpResults]) -> None:
    """結果を保存する関数

    Args:
        in_ (dict[str, crud.result.RcpResults]): ユーザーと勝敗を格納した辞書
    """
    game = crud.game.create_game(crud.game.GameCreate())
    for (n, c), (_, r) in zip(in_.items(), out_.items()):
        crud.result.create_result(crud.result.ResultCreate(
            game_id = game.id,
            choice = c,
            result = r,
            is_bot = True if n == "bot" else False
        ))