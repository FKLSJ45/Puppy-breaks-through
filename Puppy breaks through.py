import time

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def level_one():
    delay_print("欢迎来到第一关！")
    delay_print("你发现自己置身在一片森林中。")

    while True:
        choice = input("你要往左边走还是往右边走？（左/右）：")
        if choice.lower() == "左":
            delay_print("你选择了往左边走。")
            return "left"
        elif choice.lower() == "右":
            delay_print("你选择了往右边走。")
            return "right"
        else:
            delay_print("无效的选择，请重新输入。")

def level_two():
    delay_print("\n恭喜你通过第一关！")
    delay_print("现在你来到了一片广阔的草原。")

    while True:
        choice = input("你要继续前进还是停下来休息？（前进/休息）：")
        if choice.lower() == "前进":
            delay_print("你选择继续前进。")
            return "forward"
        elif choice.lower() == "休息":
            delay_print("你选择停下来休息。")
            return "rest"
        else:
            delay_print("无效的选择，请重新输入。")

def level_three():
    delay_print("\n恭喜你通过第二关！")
    delay_print("你来到了一个神秘的洞穴。")

    while True:
        choice = input("你要进入洞穴还是绕过洞穴？（进入/绕过）：")
        if choice.lower() == "进入":
            delay_print("你选择进入洞穴。")
            return "enter"
        elif choice.lower() == "绕过":
            delay_print("你选择绕过洞穴。")
            return "bypass"
        else:
            delay_print("无效的选择，请重新输入。")

def level_four():
    delay_print("\n恭喜你通过第三关！")
    delay_print("你来到了一片花海，周围都是五彩斑斓的花朵。")

    while True:
        choice = input("你要尝试闻一下花的香味还是继续前进？（闻花/前进）：")
        if choice.lower() == "闻花":
            delay_print("你弯下身子，闻了一下花的香味。")
            return "smell"
        elif choice.lower() == "前进":
            delay_print("你选择继续前进。")
            return "forward"
        else:
            delay_print("无效的选择，请重新输入。")

def final_level():
    delay_print("\n恭喜你通过第四关！")
    delay_print("你终于找到了通往自由的出口。")

    while True:
        choice = input("你要走出出口，重新回到自由的世界吗？（是/否）：")
        if choice.lower() == "是":
            delay_print("你选择了重新回到自由的世界。")
            delay_print("恭喜你，你成功完成了所有关卡，获得了自由！")
            break
        elif choice.lower() == "否":
            delay_print("你选择不离开这个美丽的地方。")
            delay_print("好吧，你可以继续留在这里，享受生活。")
            break
        else:
            delay_print("无效的选择，请重新输入。")

def play_game():
    delay_print("欢迎来到狗视角的闯关游戏！")
    delay_print("你是一只可爱的小狗，正在寻找自由的出口。")
    
    level_one_choice = level_one()

    if level_one_choice == "left":
        level_two_choice = level_two()

        if level_two_choice == "forward":
            level_three_choice = level_three()

            if level_three_choice == "enter":
                level_four_choice = level_four()

                if level_four_choice == "smell":
                    final_level()
                else:
                    delay_print("你迷路了，游戏结束。")
            else:
                delay_print("你迷路了，游戏结束。")
        else:
            delay_print("你迷路了，游戏结束。")
    else:
        delay_print("你迷路了，游戏结束。")

if __name__ == "__main__":
    play_game()
