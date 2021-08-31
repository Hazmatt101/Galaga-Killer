import Flask


from src.scripts.python import clean_build_game
from src.scripts.python.mame_runner_util import MameRunnerUtil


MameRunnerUtil.get_admin()
clean_build_game.initialize()