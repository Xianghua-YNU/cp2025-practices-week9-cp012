import matplotlib.pyplot as plt
import math


def apply_rules(axiom, rules, iterations):
    """
    L-System 字符串生成器
    :param axiom: 初始字符串
    :param rules: 字典，符号重写规则
    :param iterations: 迭代次数
    :return: 迭代后生成的字符串
    """
    current = axiom
    for _ in range(iterations):
        next_seq = []
        for char in current:
            # 如果字符在规则字典中，使用规则替换；否则保持原样
            next_seq.append(rules.get(char, char))
        current = ''.join(next_seq)
    return current


def draw_l_system(commands, angle_deg, step, initial_pos=(0, 0), initial_angle=90, tree_mode=False, savefile=None):
    """
    L-System 绘图函数
    :param commands: 命令字符串
    :param angle_deg: 每次转向的角度（度）
    :param step: 步长
    :param initial_pos: 初始位置
    :param initial_angle: 初始方向（度）
    :param tree_mode: 是否使用分形树模式（影响 [ 和 ] 的行为）
    :param savefile: 如果指定，将绘图保存到该文件
    """
    x, y = initial_pos
    current_angle = initial_angle
    stack = []
    fig, ax = plt.subplots()
    try:
        for cmd in commands:
            if cmd in ('F', '0', '1'):
                # 计算新的位置
                nx = x + step * math.cos(math.radians(current_angle))
                ny = y + step * math.sin(math.radians(current_angle))
                # 绘制线段
                ax.plot([x, nx], [y, ny], color='green' if tree_mode else 'blue', linewidth=1.2 if tree_mode else 1)
                x, y = nx, ny
            elif cmd == 'f':
                # 移动但不绘制
                x += step * math.cos(math.radians(current_angle))
                y += step * math.sin(math.radians(current_angle))
            elif cmd == '+':
                # 顺时针旋转
                current_angle += angle_deg
            elif cmd == '-':
                # 逆时针旋转
                current_angle -= angle_deg
            elif cmd == '[':
                # 保存当前状态
                stack.append((x, y, current_angle))
                if tree_mode:
                    current_angle += angle_deg
            elif cmd == ']':
                if not stack:
                    raise ValueError("Stack is empty when trying to pop. Check the L-System commands.")
                # 恢复之前保存的状态
                x, y, current_angle = stack.pop()
                if tree_mode:
                    current_angle -= angle_deg
        # 设置坐标轴比例和隐藏坐标轴
        ax.set_aspect('equal')
        ax.axis('off')
        if savefile:
            # 保存绘图
            plt.savefig(savefile, bbox_inches='tight', pad_inches=0.1, dpi=150)
            plt.close()
        else:
            # 显示绘图
            plt.show()
    except Exception as e:
        print(f"An error occurred while drawing the L-System: {e}")


def main():
    # Koch 曲线参数
    koch_axiom = "F"
    koch_rules = {'F': 'F+F--F+F'}
    koch_angle = 60
    koch_iter = 4
    koch_step = 5
    koch_cmds = apply_rules(koch_axiom, koch_rules, koch_iter)
    plt.figure(figsize=(10, 3))
    draw_l_system(koch_cmds, koch_angle, koch_step, initial_pos=(0, 0), initial_angle=0)
    plt.title("L-System Koch Curve")
    plt.axis('equal')
    plt.axis('off')
    plt.show()

    # 分形树参数
    tree_axiom = "0"
    tree_rules = {'1': '11', '0': '1[0]0'}
    tree_angle = 45
    tree_iter = 7
    tree_step = 7
    tree_cmds = apply_rules(tree_axiom, tree_rules, tree_iter)
    plt.figure(figsize=(7, 7))
    draw_l_system(tree_cmds, tree_angle, tree_step, initial_pos=(0, 0), initial_angle=90, tree_mode=True)
    plt.title("L-System Fractal Tree")
    plt.axis('equal')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
