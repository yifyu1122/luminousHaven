import random
import player
#寶石沒掉 產速太快
# 定義顏色遺傳規則
COLOR_MIX_RULES = {
    ("紅", "黃"): [("橙", 60), ("紅", 15), ("黃", 15),("粉", 10)],
    ("紅", "藍"): [("紫", 60), ("紅", 15), ("藍", 15),("粉", 10)],
    ("黃", "藍"): [("綠", 70), ("黃", 15), ("藍", 15)],
    ("橙", "紫"): [("粉", 60), ("橙", 20), ("紫", 20)],
    ("紅", "綠"): [("黃", 40), ("橙", 40), ("紅", 20)],
    ("藍", "綠"): [("綠", 70), ("藍", 20), ("粉", 10)],
    ("紅", "橙"): [("橙", 50), ("紅", 30), ("黃", 20)],
    ("紅", "紫"): [("粉", 30), ("紫", 40), ("紅", 30)],
    ("黃", "綠"): [("黃", 50), ("綠", 50), ("橙", 20)],
    ("藍", "紫"): [("紫", 50), ("藍", 30), ("粉", 20)],
    ("橙", "黃"): [("橙", 50), ("黃", 30), ("紅", 20)],
    ("橙", "綠"): [("橙", 40), ("綠", 40), ("黃", 20)],
    ("橙", "藍"): [("綠", 40), ("橙", 40), ("藍", 20)],
    ("黃", "紫"): [("粉", 30), ("黃", 40), ("紫", 30)],
    ("綠", "紫"): [("綠", 40), ("紫", 40),("粉", 20)],
}

class MagicCreature:
    def __init__(self, name, color, energy, energy_rate, player):
        self.name = name
        self.color = color  # 這隻生物的顏色
        self.energy = energy  # 當前能量
        self.energy_rate = energy_rate  # 產能速度
        self.player = player
    
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
            new_color = random.choices([c[0] for c in possible_colors], weights=[c[1] for c in possible_colors])[0]
        elif "粉" in color_pair:
            new_color = "粉" if random.random() < 0.5 else partner.color
        else:
            new_color = random.choice(color_pair)  # 沒對應規則時，隨機選擇雙親顏色

        # **✅ 修正：新增 `player` 參數**
        new_creature = MagicCreature(self.name, new_color, 50, 10, player)
        print(f"🍼 {self.name}（{self.color}） 和 {partner.name}（{partner.color}）生出了一隻 {new_creature.color} 色的 {new_creature.name}！")
        return new_creature



    def drop_gem(self):
        """當生物能量超過 100，掉落對應顏色的寶石"""
        while self.energy >= 100:
            gem_name = f"{self.color}寶石"
            print(f"💎 {self.name}（{self.color}） 能量過剩，掉落了一顆 {gem_name}！")
            self.energy -= 100  # 扣除能量

            # ✅ 確保 `self.player.resources` 是來自 `Player` 類的
            self.player.resources[gem_name] = self.player.resources.get(gem_name, 0) + 1
            print(f"🌟 你現在擁有 {self.player.resources[gem_name]} 顆 {gem_name}！")


    


