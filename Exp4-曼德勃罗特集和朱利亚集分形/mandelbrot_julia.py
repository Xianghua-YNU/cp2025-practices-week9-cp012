import numpy as np
import matplotlib.pyplot as plt


def generate_mandelbrot(width=800, height=800, max_iter=100):
    """
    生成Mandelbrot集数据
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素)
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间
    """
    # 创建x坐标：从-2.0到1.0，步长根据宽度决定
    x = np.linspace(-2.0, 1.0, width)
    # 创建y坐标：从-1.5到1.5，步长根据高度决定
    y = np.linspace(-1.5, 1.5, height)
    # 使用meshgrid生成坐标网格
    x_grid, y_grid = np.meshgrid(x, y)
    # 构建复数矩阵C = x + i*y（注意虚部在前，这里需要转置吗？）
    # 默认情况下，x_grid和y_grid是按列优先的，因此需要转置
    x_grid, y_grid = x_grid.T, y_grid.T
    C = x_grid + 1j * y_grid

    # 初始化记录数组B和当前值Z
    B = np.zeros(C.shape, dtype=np.uint16)
    Z = np.zeros(C.shape, dtype=np.complex128)

    for j in range(max_iter):
        # 找到哪些点还在范围内（abs(Z) <= 2）
        mask = np.abs(Z) <= 2
        # 这些点继续迭代
        B[mask] += 1
        Z[mask] = Z[mask] ** 2 + C[mask]

    return B.T  # 转置以便imshow正确显示


def generate_julia(c, width=800, height=800, max_iter=100):
    """
    生成Julia集数据
    :param c: 固定复数参数c
    :param width: 图像宽度(像素)
    :param height: 图像高度(像素)
    :param max_iter: 最大迭代次数
    :return: 2D numpy数组，包含每个点的逃逸时间
    """
    # 创建x和y的范围（这里使用对称的-2.0到2.0范围）
    x = np.linspace(-2.0, 2.0, width)
    y = np.linspace(-2.0, 2.0, height)
    # 生成网格坐标
    x_grid, y_grid = np.meshgrid(x, y)
    x_grid, y_grid = x_grid.T, y_grid.T
    Z0 = x_grid + 1j * y_grid

    # 初始化数组
    B = np.zeros(Z0.shape, dtype=np.uint16)
    Z = Z0.copy()

    for j in range(max_iter):
        # 找到仍未逃逸的点（绝对值小于等于2）
        mask = np.abs(Z) <= 2
        # 更新迭代次数
        B[mask] += 1
        # 当前点迭代处理
        Z[mask] = Z[mask] ** 2 + c

    return B.T  # 转置以保证正确显示


def plot_fractal(data, title, filename=None, cmap='magma'):
    """
    绘制分形图像
    :param data: 分形数据(2D数组)
    :param title: 图像标题
    :param filename: 保存文件名(可选)
    :param cmap: 颜色映射，默认'magma'
    """
    plt.figure(figsize=(10, 10))
    # 使用imshow显示图像，origin='lower'让坐标原点在左下角
    plt.imshow(data, cmap=cmap, origin='lower')
    plt.title(title)
    plt.axis('off')  # 关闭坐标轴

    if filename:
        plt.savefig(filename, bbox_inches='tight', dpi=150)
    plt.show()


if __name__ == "__main__":
    # 设置参数
    width, height = 800, 800
    max_iter = 100

    # 生成并绘制Mandelbrot集
    print("正在生成Mandelbrot集...")
    mandelbrot = generate_mandelbrot(width, height, max_iter)
    plot_fractal(mandelbrot, "Mandelbrot Set", "mandelbrot.png")
    print("Mandelbrot集绘制完成，已保存为mandelbrot.png\n")

    # 定义Julia集的c参数
    julia_c_values = [
        -0.8 + 0.156j,  # 经典的“满月”Julia集
        -0.4 + 0.6j,  # 产生树枝状分形的c值
        0.285 + 0.01j  # 产生复杂结构的c值
    ]

    # 生成和绘制每个c对应的Julia集
    for idx, c in enumerate(julia_c_values):
        print(f"正在生成Julia集（c = {c})...")
        julia = generate_julia(c, width, height, max_iter)
        plot_fractal(julia, f"Julia Set (c = {c:.3f} + {c.imag:.3f}i)", f"julia_{idx + 1}.png")
        print(f"Julia集 {idx + 1} 绘制完成，已保存为julia_{idx + 1}.png\n")
