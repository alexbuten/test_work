from udp_client import UDPClient
from kinematics import forward_kinematics
import numpy as np
import time


def main(server_ip, server_port):
    # Параметры DH для каждого сустава (a, d, alpha, theta)
    dh_params = [
        (0, 0.21, np.pi / 2, 0),
        (0.8, 0.193, 0, 0),
        (-0.598, 0.16, 0, 0),
        (0, 0.25, np.pi / 2, 0),
        (0, 0.25, -np.pi / 2, 0),
        (0, 0.25, 0, 0)
    ]

    client = UDPClient((server_ip, server_port))

    try:

        # Отправляем запрос 'get' на сервер
        client.send_get_request()
        # Получаем 5 пакетов от сервера
        packets = client.receive_packets(5)

        # Для каждого пакета вычисляем прямую кинематику и выводим результаты
        for packet in packets:
            position = forward_kinematics(dh_params, packet.joint_angles)
            print(f'Пакет #{packet.timestamp}: Позиция эндэффектора - {position}')

    finally:
        client.close()


if __name__ == "__main__":
    main("localhost", 8088)  # Пример использования: IP-адрес сервера и порт
