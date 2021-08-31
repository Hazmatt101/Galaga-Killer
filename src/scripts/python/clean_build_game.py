from mame_runner_util import MameRunnerUtil


def initialize():
    MameRunnerUtil.change_permissions_recursive()
