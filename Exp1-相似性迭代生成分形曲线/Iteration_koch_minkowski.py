import numpy as np
import matplotlib.pyplot as plt

def koch_generator(u, level):
    """
    迭代生成科赫曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    points = u.copy()
    for _ in range(level):
        new_points = []
        for i in range(len(points) - 1):
            p0 = points[i]
            p1 = points[i + 1]
            # 计算线段的长度和方向
            length = abs(p1 - p0)
            direction = (p1 - p0) / length
            # 生成新的点
            p2 = p0 + direction * length / 3
            p3 = p0 + direction * length / 3 * np.exp(1j * np.pi / 3)  # 旋转60度
            p4 = p0 + direction * 2 * length / 3
            new_points.extend([p0, p2, p3, p4])
        new_points.append(points[-1])  # 添加最后一个点
        points = np.array(new_points)
    return points

def minkowski_generator(u, level):
    """
    迭代生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    points = u.copy()
    for _ in range(level):
        new_points = []
        for i in range(len(points) - 1):
            p0 = points[i]
            p1 = points[i + 1]
            # 计算线段的长度和方向
            length = abs(p1 - p0)
            direction = (p1 - p0) / length
            # 生成新的点
            p2 = p0 + direction * length / 4
            p3 = p2 + direction * length / 4 * np.exp(1j * np.pi / 2)  # 旋转90度
            p4 = p3 + direction * length / 4
            p5 = p4 + direction * length / 4 * np.exp(1j * np.pi / 2)  # 旋转90度
            p6 = p5 + direction * length / 4
            p7 = p6 + direction * length / 4 * np.exp(1j * np.pi / 2)  # 旋转90度
            p8 = p7 + direction * length / 4
            p9 = p8 + direction * length / 4 * np.exp(1j * np.pi / 2)  # 旋转90度
            new_points.extend([p0, p2, p3, p4, p5, p6, p7, p8, p9])
        new_points.append(points[-1])  # 添加最后一个点
        points = np.array(new_points)
    return points

if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1], dtype=complex)

    # 绘制不同层级的科赫曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # 调用koch_generator生成点
        koch_points = koch_generator(init_u, level=i)
        axs[i//2, i%2].plot(
            np.real(koch_points), np.imag(koch_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Koch Curve Level {i}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()

    # 绘制不同层级的闵可夫斯基香肠曲线
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    for i in range(4):
        # 调用minkowski_generator生成点
        minkowski_points = minkowski_generator(init_u, level=i)
        axs[i//2, i%2].plot(
            np.real(minkowski_points), np.imag(minkowski_points), 'k-', lw=1
        )
        axs[i//2, i%2].set_title(f"Minkowski Sausage Level {i}")
        axs[i//2, i%2].axis('equal')
        axs[i//2, i%2].axis('off')
    plt.tight_layout()
    plt.show()
