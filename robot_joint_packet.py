from dataclasses import dataclass
from typing import List


@dataclass
class RobotJointPacket:
    timestamp: int
    joint_angles: List[float]  # Список углов поворота суставов
