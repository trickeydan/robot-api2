"""Dummy (testing) implementations of robot backends."""

from .motor import DummyMotorBoard, DummyMotorChannel
from .game_state import DummyGameState
from .power import DummyPowerBoard
from .servo import DummyServoAssembly
from .robot import DummyRobot

__all__ = [
    "DummyMotorBoard",
    "DummyMotorChannel",
    "DummyGameState",
    "DummyPowerBoard",
    "DummyServoAssembly",
    "DummyRobot",
]
