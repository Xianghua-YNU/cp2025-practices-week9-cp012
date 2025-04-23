import matplotlib.pyplot as plt
import math


def apply_rules(axio, rule, iteration):
    """
    生成L-System字符串
    :param axiom: 初始字符串（如"F"或"0"）
    :param rules: 规则字典，如{"F": "F+F--F+F"} 或 {"1": "11", "0": "1[0]0"}
    :param iterations: 迭代次数
    :return: 经过多轮迭代后的最终字符串
    """
    result = axio
    for _ in range(iteration):
        new_string = ""
        for char in result:
            new_string += rule.get(char, char)
        result = new_string
    return result


def draw_l_system(instructions, angle, step, start_pos=(0, 0), start_angle=90, savefile=None):
    """
    根据L-System指令绘图
    :param instructions: 指令字符串（如"F+F--F+F"）
    :param angle: 每次转向的角度（度）
    :param step: 每步前进的长度
    :param start_pos: 起始坐标 (x, y)
    :param start_angle: 起始角度（0表示向右，90表示向上）
    :param savefile: 若指定则保存为图片文件，否则直接显示
    """
    x, y = start_pos
    current_angle = start_angle
    stack = []
    x_coords = [x]
    y_coords = [y]

    for char in instructions:
        if char == 'F':
            rad_angle = math.radians(current_angle)
            new_x = x + step * math.cos(rad_angle)
            new_y = y + step * math.sin(rad_angle)
            x, y = new_x, new_y
            x_coords.append(x)
            y_coords.append(y)
        elif char == '+':
            current_angle += angle
        elif char == '-':
            current_angle -= angle
        elif char == '[':
            stack.append((x, y, current_angle))
        elif char == ']':
            x, y, current_angle = stack.pop()
            x_coords.append(x)
            y_coords.append(y)

    plt.plot(x_coords, y_coords)
    plt.axis('equal')
    if savefile:
        plt.savefig(savefile)
    else:
        plt.show()
    plt.close()


if __name__ == "__main__":
    """
    主程序示例：分别生成并绘制科赫曲线和分形二叉树
    学生可根据下方示例，调整参数体验不同分形效果
    """
    # 1. 生成并绘制科赫曲线
    axiom = "F"  # 公理
    rules = {"F": "F+F--F+F"}  # 规则
    iterations = 3  # 迭代次数
    angle = 60  # 每次转角
    step = 10  # 步长
    instr = apply_rules(axiom, rules, iterations)  # 生成指令字符串
    draw_l_system(instr, angle, step)  # 绘图并保存

    # 2. 生成并绘制分形二叉树
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    iterations = 5
    angle = 45
    step = 10
    # 调整起始位置
    instr = apply_rules(axiom, rules, iterations)
    draw_l_system(instr, angle, step)
