import socket
from typing import Tuple

import numpy as np

from robot_joint_packet import RobotJointPacket
import struct


class UDPClient:
    def __init__(self, server_address: Tuple[str, int]):
        self.server_address = server_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_get_request(self):
        message = 'get'.encode()
        self.sock.sendto(message, self.server_address)

    def receive_packets(self, count: int):
        packets = []
        for _ in range(count):
            data, _ = self.sock.recvfrom(1024)  # Предполагается, что размер буфера 1024 байт достаточен
            format_string = '<Q6d'
            decoded_data = struct.unpack(format_string, data)
            timestamp, *angles = map(float, decoded_data)
            # Преобразовываем углы в радианы
            angles = [np.radians(angle) for angle in angles]
            packet = RobotJointPacket(timestamp, angles)
            packets.append(packet)
        return packets

    def close(self):
        self.sock.close()
