import time
import random

class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return damage

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        return damage

def delay_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def fight(player, dinosaur):
    delay_print(f"{player.name}遭遇了{dinosaur.name}！")
    while player.health > 0 and dinosaur.health > 0:
        player_damage = player.attack(dinosaur)
        dinosaur_damage = dinosaur.attack(player)
        delay_print(f"{player.name}对{dinosaur.name}造成了{player_damage}点伤害，{dinosaur.name}剩余{dinosaur.health}生命值。")
        delay_print(f"{dinosaur.name}对{player.name}造成了{dinosaur_damage}点伤害，{player.name}剩余{player.health}生命值。")
        if dinosaur.health <= 0:
            delay_print(f"{player.name}战胜了{dinosaur.name}！")
            break
        elif player.health <= 0:
            delay_print(f"{player.name}被{dinosaur.name}击败，游戏结束。")
            exit()

def main():
    player_name = input("请输入你的名字：")
    player = Player(player_name)

    delay_print(f"欢迎来到恐龙世界，{player_name}！")
    delay_print("你将在这个游戏中探索恐龙世界，与恐龙互动。")

    dinosaurs = [
        Dinosaur("暴龙", health=80, attack_power=30),
        Dinosaur("剑龙", health=100, attack_power=25),
        Dinosaur("三角龙", health=70, attack_power=35)
    ]

    while player.health > 0:
        dinosaur = random.choice(dinosaurs)
        fight(player, dinosaur)
        play_again = input("是否继续探险？(是/否): ").strip().lower()
        if play_again != "是":
            delay_print(f"谢谢参与恐龙世界游戏！再见。")
            exit()

if __name__ == "__main__":
    main()
