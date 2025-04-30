import numpy as np
import matplotlib.pyplot as plt

# 科赫曲线生成函数
def koch_generator(u, level):
    """
    迭代生成科赫曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # 如果迭代层数为0或负数，直接返回初始线段
    if level <= 0:
        return u
    
    # 科赫曲线的旋转角度为60度
    theta = np.pi / 3  
    for _ in range(level):
        new_u = []  # 用于存储新的点序列
        for i in range(len(u) - 1):  # 遍历每条线段
            start = u[i]  # 线段的起点
            end = u[i + 1]  # 线段的终点
            
            # 计算科赫曲线的四个新点
            p1 = start  # 第一个点：起点
            p2 = start + (end - start) / 3  # 第二个点：起点向终点方向的三分之一处
            p3 = p2 + (end - start) / 3 * np.exp(1j * theta)  # 第三个点：旋转60度
            p4 = start + 2 * (end - start) / 3  # 第四个点：起点向终点方向的三分之二处
            p5 = end  # 第五个点：终点
            
            # 将新的点加入到新的点序列中
            new_u.extend([p1, p2, p3, p4, p5])
        
        # 更新点序列
        u = np.array(new_u)
    
    return u

# 闵可夫斯基香肠曲线生成函数
def minkowski_generator(u, level):
    """
    迭代生成闵可夫斯基香肠曲线的点序列。

    参数:
        u: 初始线段的端点数组（复数表示）
        level: 迭代层数

    返回:
        numpy.ndarray: 生成的所有点（复数数组）
    """
    # 如果迭代层数为0或负数，直接返回初始线段
    if level <= 0:
        return u
    
    # 闵可夫斯基香肠曲线的旋转角度为90度
    theta = np.pi / 2  
    for _ in range(level):
        new_u = []  # 用于存储新的点序列
        for i in range(len(u) - 1):  # 遍历每条线段
            start = u[i]  # 线段的起点
            end = u[i + 1]  # 线段的终点
            
            # 计算闵可夫斯基香肠曲线的八个新点
            p1 = start  # 第一个点：起点
            p2 = start + (end - start) / 4  # 第二个点：起点向终点方向的四分之一处
            p3 = p2 + (end - start) / 4 * np.exp(1j * theta)  # 第三个点：旋转90度
            p4 = p3 + (end - start) / 4  # 第四个点：沿着旋转后的方向前进四分之一
            p5 = p4 + (end - start) / 4 * np.exp(1j * theta)  # 第五个点：再次旋转90度
            p6 = p5 + (end - start) / 4  # 第六个点：沿着旋转后的方向前进四分之一
            p7 = p6 + (end - start) / 4 * np.exp(-1j * theta)  # 第七个点：旋转-90度
            p8 = p7 + (end - start) / 4  # 第八个点：沿着旋转后的方向前进四分之一
            p9 = p8 + (end - start) / 4 * np.exp(-1j * theta)  # 第九个点：再次旋转-90度
            p10 = end  # 第十个点：终点
            
            # 将新的点加入到新的点序列中
            new_u.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10])
        
        # 更新点序列
        u = np.array(new_u)
    
    return u

if __name__ == "__main__":
    # 初始线段
    init_u = np.array([0, 1], dtype=complex)
    
    # 创建2x2子图布局
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    
    # 生成不同层级的科赫曲线
    for i in range(4):
        # 调用koch_generator生成点
        koch_points = koch_generator(init_u, i)
        # 绘制曲线
        axs[i // 2, i % 2].plot(koch_points.real, koch_points.imag, 'k-', lw=1)
        # 设置标题
        axs[i // 2, i % 2].set_title(f"Koch Curve Level {i}")
        # 设置图形比例
        axs[i // 2, i % 2].axis('equal')
        # 隐藏坐标轴
        axs[i // 2, i % 2].axis('off')
    
    # 显示图形
    plt.tight_layout()
    plt.show()

    # 创建2x2子图布局
    fig, axs = plt.subplots(2, 2, figsize=(10, 10))
    # 生成不同层级的闵可夫斯基香肠
    for i in range(4):
        # 调用minkowski_generator生成点
        minkowski_points = minkowski_generator(init_u, i)
        # 绘制曲线
        axs[i // 2, i % 2].plot(minkowski_points.real, minkowski_points.imag, 'k-', lw=1)
        # 设置标题
        axs[i // 2, i % 2].set_title(f"Minkowski Sausage Level {i}")
        # 设置图形比例
        axs[i // 2, i % 2].axis('equal')
        # 隐藏坐标轴
        axs[i // 2, i % 2].axis('off')
    
    # 显示图形
    plt.tight_layout()
    plt.show()
