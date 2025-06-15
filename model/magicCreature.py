from config.gameConfig import COLOR_MIX_RULES, SPECIAL_DROPS
import random

class MagicCreature:
    def __init__(self, name, color, energy=50, energy_rate=10):
        self.name = name
        self.color = color  # 這隻生物的顏色
        self.energy = energy  # 當前能量
        self.energy_rate = energy_rate  # 產能速度
    
    def __str__(self):
        return f"{self.name}"
    
    def generate_energy(self):
        """生物自動產生能量，並檢查是否應該掉落寶石"""
        self.energy += self.energy_rate
        print(f"🔋 {self}） 能量 +{self.energy_rate}！目前能量：{self.energy}")
        self.drop_gem()
        
    def breed(self, partner, player):
        """與另一隻相同品種的生物繁殖"""
        if self.name != partner.name:
            print(f"❌ {self.name} 和 {partner.name} 不是同品種，無法繁殖！")
            return None

        # 取得雙親顏色組合（確保順序一致）
        color_pair = tuple(sorted([self.color, partner.color]))

        # 根據遺傳規則決定新顏色
        if color_pair in COLOR_MIX_RULES:
            possible_colors = COLOR_MIX_RULES[color_pair]
            new_color = random.choices(
                [c[0] for c in possible_colors], 
                weights=[c[1] for c in possible_colors]
            )[0]
        elif "透明" in color_pair:
            new_color = "透明" if random.random() < 0.5 else partner.color
        else:
            new_color = random.choice(color_pair)  # 沒對應規則時，隨機選擇雙親顏色


        new_creature = MagicCreature(self.name, new_color)
        print(f"🍼 {self.name}（{self.color}） 和 {partner.name}（{partner.color}）生出了一隻 {new_creature.color} 色的 {new_creature.name}！")
        return new_creature

    def drop_gem(self):
        """當生物能量超過 100，掉落對應顏色的寶石，並有機率掉落特殊物品"""
        drops = []
        while self.energy >= 100:
            gem_name = f"{self.color}寶石"         
            self.energy -= 100  # 扣除能量
            drops.append(gem_name)
            print(f"💎 {self.name}（{self.color}） 能量過剩，掉落了一顆 {gem_name}！")

            # **🔮 新增特殊掉落機率（20%）**
            if self.name in SPECIAL_DROPS and random.random() < 0.2:  # 20% 機率掉落
                special_item = SPECIAL_DROPS[self.name]
                drops.append(special_item)
                print(f"✨ {self.name} 除了寶石，還掉落了 **{special_item}**！")

        return drops
