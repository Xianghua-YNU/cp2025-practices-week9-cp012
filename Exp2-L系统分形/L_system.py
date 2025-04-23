import matplotlib.pyplot as plt
import math


def apply_rules(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        new_str = []
        for c in current:
            new_str.append(rules.get(c, c))
        current = ''.join(new_str)
    return current


def draw_l_system(instructions, angle, step, start_pos=(0, 0), start_angle=0, savefile=None):
    x, y = start_pos
    current_angle = start_angle
    stack = []

    plt.figure()
    for cmd in instructions:
        if cmd == '+':
            current_angle += angle
        elif cmd == '-':
            current_angle -= angle
        elif cmd == '[':
            stack.append((x, y, current_angle))
        elif cmd == ']':
            if stack:
                x, y, current_angle = stack.pop()
        else:
            rad = math.radians(current_angle)
            dx = step * math.cos(rad)
            dy = step * math.sin(rad)
            new_x = x + dx
            new_y = y + dy
            plt.plot([x, new_x], [y, new_y], color='black', linewidth=1)
            x, y = new_x, new_y

    plt.axis('equal')
    plt.axis('off')
    if savefile:
        plt.savefig(savefile, bbox_inches='tight')
        plt.close()
    else:
        plt.show()


if __name__ == "__main__":
    # Koch curve example
    axiom = "F"
    rules = {"F": "F+F--F+F"}
    iterations = 3
    angle = 60
    step = 10
    instr = apply_rules(axiom, rules, iterations)
    draw_l_system(instr, angle, step, savefile="l_system_koch.png")

    # Fractal tree example
    axiom = "0"
    rules = {"1": "11", "0": "1[0]0"}
    iterations = 5
    angle = 45
    step = 10
    instr = apply_rules(axiom, rules, iterations)
    draw_l_system(instr, angle, step, savefile="fractal_tree.png")
