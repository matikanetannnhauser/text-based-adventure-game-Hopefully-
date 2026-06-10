import importlib.machinery
import importlib.util
from pathlib import Path

GAME_FILE = Path("darksouls textbased adventure game")

loader = importlib.machinery.SourceFileLoader("dark_game", str(GAME_FILE))
spec = importlib.util.spec_from_loader("dark_game", loader)
module = importlib.util.module_from_spec(spec)
loader.exec_module(module)


def test_rooms_have_encounters():
    assert "encounter" in module.rooms["Cemetery of Ash"]
    assert module.rooms["Cemetery of Ash"]["encounter"] == "Skeleton"


def test_battle_round_reduces_hp():
    result = module.run_turn_based_battle("Skeleton", 20, 10, "attack")
    assert result["player_hp"] < 20
    assert result["enemy_hp"] < 10
