from pyxavi.config import Config
from pyxavi.janitor import Janitor
from pyxavi.debugger import full_stack
from pyxavi.terminal_color import TerminalColor
from diferencial.runners.runner_protocol import RunnerProtocol
from definitions import ROOT_DIR
import logging


class Diferencial(RunnerProtocol):
    '''
    Main Runner of the Echo bot
    '''

    def __init__(
        self, config: Config = None, logger: logging = None, params: dict = None
    ) -> None:
        self._config = config
        self._logger = logger

    def run(self) -> None:
        '''
        Full run
        - Gets historical data
        - Gets today's data
        - Calculates difference
        - Publishes

        Set the behaviour in the config.yaml
        '''
        self._logger.info(f"{TerminalColor.MAGENTA}Main Diferencial run{TerminalColor.END}")
        
        # self._logger.info(
        #     f"{TerminalColor.YELLOW}Getting data{TerminalColor.END}"
        # )

        # Get historical data

        # Get today's data

        # Calculate difference

        # Format a status message

        # Publish the status message


if __name__ == '__main__':
    Diferencial().run()
