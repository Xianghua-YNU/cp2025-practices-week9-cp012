import numpy as np
import matplotlib.pyplot as plt


def generate_mandelbrot(width=800, height=800, max_iter=100):
    """
    生成Mandelbrot集数据
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素)
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间

    实现步骤:
    1. 创建x(-2.0到1.0)和y(-1.5到1.5)的线性空间
    2. 生成复数网格C
    3. 初始化Z和B数组
    4. 迭代计算逃逸时间
    """
    # 创建x和y的线性空间，定义Mandelbrot集的计算区域
    x = np.linspace(-2.0, 1.0, width)  # x轴范围：[-2, 1]
    y = np.linspace(-1.5, 1.5, height)  # y轴范围：[-1.5, 1.5]

    # 使用np.meshgrid生成网格，将x和y组合成二维坐标
    X, Y = np.meshgrid(x, y)

    # 构建复数矩阵C = x + iy，这里C代表参数c的网格
    C = X + 1j * Y  # 1j是Python中的虚数单位i

    # 初始化Z和B数组
    Z = np.zeros_like(C)  # Z初始化为0，因为Mandelbrot集从z0=0开始迭代
    B = np.zeros_like(C, dtype=int)  # B记录每个点的逃逸时间（迭代次数）

    # 迭代计算逃逸时间
    for j in range(max_iter):
        mask = np.abs(Z) <= 2  # 创建布尔掩码，标记尚未逃逸的点（|Z| <= 2）
        Z[mask] = Z[mask] ** 2 + C[mask]  # 对未逃逸的点应用迭代公式z = z^2 + c
        B += mask  # 未逃逸的点迭代次数加1（True值为1，False值为0）

    # 返回转置后的结果，使数组方向与图像坐标系匹配
    return B.T


def generate_julia(c, width=800, height=800, max_iter=100):
    """
    生成Julia集数据
    :param c: Julia集参数(复数)
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素)
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间

    实现步骤:
    1. 创建x和y的线性空间(-2.0到2.0)
    2. 生成复数网格Z0
    3. 初始化记录数组
    4. 迭代计算逃逸时间
    """
    # 创建x和y的线性空间，定义Julia集的计算区域
    x = np.linspace(-2.0, 2.0, width)  # x轴范围：[-2, 2]
    y = np.linspace(-2.0, 2.0, height)  # y轴范围：[-2, 2]

    # 使用np.meshgrid生成网格，将x和y组合成二维坐标
    X, Y = np.meshgrid(x, y)

    # 构建复数矩阵Z0 = x + iy，这里Z0代表初始值z0的网格
    Z = X + 1j * Y  # Z初始化为网格点本身

    # 初始化记录数组
    B = np.zeros_like(Z, dtype=int)  # B记录每个点的逃逸时间（迭代次数）

    # 迭代计算逃逸时间
    for j in range(max_iter):
        mask = np.abs(Z) <= 2  # 创建布尔掩码，标记尚未逃逸的点（|Z| <= 2）
        Z[mask] = Z[mask] ** 2 + c  # 对未逃逸的点应用迭代公式z = z^2 + c，c固定
        B += mask  # 未逃逸的点迭代次数加1

    # 返回转置后的结果，使数组方向与图像坐标系匹配
    return B.T


def plot_fractal(data, title, filename=None, cmap='magma'):
    """
    绘制分形图像
    :param data: 分形数据(2D数组)
    :param title: 图像标题
    :param filename: 保存文件名(可选)
    :param cmap: 颜色映射
    """
    plt.figure(figsize=(10, 10))  # 设置图像大小为10x10英寸
    plt.imshow(data, cmap=cmap, origin='lower')  # 显示数据，origin='lower'确保坐标原点在左下角
    plt.title(title)  # 设置图像标题
    plt.axis('off')  # 关闭坐标轴显示

    if filename:
        plt.savefig(filename, bbox_inches='tight', dpi=150)  # 保存图像，dpi控制分辨率
    plt.show()  # 显示图像


if __name__ == "__main__":
    # 示例参数
    width, height = 800, 800  # 图像分辨率800x800像素
    max_iter = 100  # 最大迭代次数

    # 生成并绘制Mandelbrot集
    mandelbrot = generate_mandelbrot(width, height, max_iter)
    plot_fractal(mandelbrot, "Mandelbrot Set", "mandelbrot.png")

    # 生成并绘制Julia集(多个c值)
    julia_c_values = [
        -0.8 + 0.156j,  # 经典Julia集，生成连通的复杂图案
        -0.4 + 0.6j,  # 树枝状Julia集，呈现分支结构
        0.285 + 0.01j  # 复杂结构Julia集，细节丰富
    ]

    for i, c in enumerate(julia_c_values):
        julia = generate_julia(c, width, height, max_iter)
        plot_fractal(julia, f"Julia Set (c = {c:.3f})", f"julia_{i + 1}.png")
