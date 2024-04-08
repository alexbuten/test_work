import numpy as np


def dh_transform(a, alpha, d, theta):
    # Вычисляем матрицу преобразования DH
    return np.array([
        [np.cos(theta), -np.sin(theta), 0, a],
        [np.sin(theta) * np.cos(alpha), np.cos(theta) * np.cos(alpha), -np.sin(alpha), -d * np.sin(alpha)],
        [np.sin(theta) * np.sin(alpha), np.cos(theta) * np.sin(alpha), np.cos(alpha), d * np.cos(alpha)],
        [0, 0, 0, 1]
    ])


def forward_kinematics(dh_params, joint_angles):
    T = np.eye(4)
    for i, angle in enumerate(joint_angles):
        a, d, alpha, _ = dh_params[i]
        T_i = dh_transform(a, alpha, d, angle)
        T = T @ T_i
    return T[:3, 3]  # Возвращаем только позицию x, y, z, без ориентации
