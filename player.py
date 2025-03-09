import random
import time
from magicCreature import MagicCreature

class Player:
    def __init__(self):
        self.inventory = []
        self.resources = {
            "螢露蜜": 0,
            "螢露土": 0,
            "螢露水": 0,
            "夢魘果實": 0,
            "夢魘之塵": 0,
            "夢魘精華": 0,
            "星輝露滴": 0,
            "惡夢碎片": 0, 
            "七彩寶石": 0,
            "紅寶石": 0,
            "橙寶石": 0,
            "黃寶石": 0,
            "綠寶石": 0,
            "藍寶石": 0,
            "紫寶石": 0,
            "粉寶石": 0,
        }
        # 培育室最大容量
        self.max_creatures = 10
        self.unlocked_lands = 0

    def add_creature(self, creature_name, color):
        """新增魔法生物到持有列表"""
        if len(self.inventory) >= self.max_creatures:
            print("❌ 培育室已滿，無法新增生物！請先釋放或合併現有生物。")
            return
        
        # 確保所有生物名稱統一（去除空格、固定格式）
        normalized_name = creature_name.strip()

        new_creature = MagicCreature(normalized_name, color, 50, 10, self)
        self.inventory.append(new_creature)
        print(f"✅ {new_creature.name}（{new_creature.color}） 加入培育室！目前數量：{len(self.inventory)}/{self.max_creatures}")
    
    def synthesize_gem(self):
        """合成七彩寶石，需要集齊 7 種顏色的寶石"""
        required_gems = ["紅寶石", "橙寶石", "黃寶石", "綠寶石", "藍寶石", "紫寶石", "粉寶石"]

        # 檢查是否擁有每種寶石至少 1 顆
        if all(self.resources.get(gem, 0) > 0 for gem in required_gems):
            print("🌈 你集齊了七種顏色的寶石，並成功合成了一顆 **七彩寶石**！")

            # 消耗 1 顆每種顏色的寶石
            for gem in required_gems:
                self.resources[gem] -= 1
            
            # 增加 1 顆七彩寶石
            self.resources["七彩寶石"] = self.resources.get("七彩寶石", 0) + 1
        else:
            print("❌ 你的寶石顏色尚未集齊，無法合成七彩寶石！")

    def unlock_land(self):
        """使用七彩寶石解鎖新的土地，擴建培育室，並在首次解鎖時獲得夢魘貓（黃）"""
        if self.resources.get("七彩寶石", 0) < 1:
            print("❌ 七彩寶石不足！需要 1 顆七彩寶石來解鎖新土地。")
            return

        self.resources["七彩寶石"] -= 1
        self.unlocked_lands += 1
        self.max_creatures += 5  # 每次解鎖增加 5 個可容納生物數量
        print(f"🌿 你使用 1 顆七彩寶石，成功淨化了一塊被污染的土地！")
        print(f"🏡 你的培育室擴建完成，可容納生物數量增加至 {self.max_creatures}！")

        # 第一次解鎖土地時，獲得夢魘貓（黃）並解鎖新地圖
        if self.unlocked_lands == 1:
            new_creature = MagicCreature("夢魘貓", "黃", 50, 10)
            self.add_creature(new_creature, "黃")
            print("✨ 你發現了一隻 **夢魘貓（黃）**，並成功將牠帶回培育室！")
            print("🌙 你解鎖了一個新的探索地點：**夢魘灣**！")

        else:
            print(f"🌍 你已成功淨化 {self.unlocked_lands} 塊土地！繼續探索吧！")

    def list_creatures(self):
        """顯示玩家持有的所有魔法生物"""
        if not self.inventory:
            print("❌ 你目前沒有任何魔法生物！")
            return
        print("\n🔹 你的魔法生物：")
        for i, creature in enumerate(self.inventory):
            print(f"{i + 1}. {creature.name}（{creature.color}）")
            #顯示生物能量狀態
            print(f"   能量：{creature.energy} | 產能速度：{creature.energy_rate}")
    
    def list_resources(self):
        """顯示玩家持有的所有資源（不顯示數量為 0 的項目）"""
        # 過濾掉數量為 0 的資源
        owned_resources = {res: count for res, count in self.resources.items() if count > 0}

        if not owned_resources:
            print("❌ 你目前沒有任何資源！")
            return

        print("\n🔹 你的資源：")
        for resource, count in owned_resources.items():
            print(f"   {resource}：{count}")


    def breed_creatures(self, index1, index2):
        """讓兩隻魔法生物繁殖，依照品種需求不同資源"""

        # 確保輸入的索引是有效的
        if index1 < 1 or index2 < 1 or index1 > len(self.inventory) or index2 > len(self.inventory):
            print("❌ 無效的生物編號！")
            return

        parent1 = self.inventory[index1 - 1]
        parent2 = self.inventory[index2 - 1]

        # **確保名稱統一後再比對**
        parent1_name = parent1.name.strip()
        parent2_name = parent2.name.strip()

        print(f"🐣 嘗試繁殖：{parent1_name}（{parent1.color}） 和 {parent2_name}（{parent2.color}）")

        if parent1_name != parent2_name:
            print(f"❌ {parent1_name} 和 {parent2_name} 不是同品種，無法繁殖！")
            return

        # **根據品種決定繁殖所需資源**
        if parent1_name == "星光螢火蟲":
            required_resources = ["螢露蜜", "螢露土", "螢露水"]
        elif parent1_name == "夢魘貓":
            required_resources = ["夢魘果實", "夢魘之塵", "夢魘精華"]
        else:
            print(f"❌ {parent1_name} 目前無法繁殖！")
            return

        # **檢查是否擁有足夠的繁殖資源**
        missing_resources = [res for res in required_resources if self.resources.get(res, 0) < 1]
        
        if missing_resources:
            print(f"❌ 無法繁殖！缺少以下資源：{', '.join(missing_resources)}")
            return

        # **✅ 修正：傳入 `self` 作為 `player` 參數**
        child = parent1.breed(parent2, self)

        if child:
            # 繁殖成功，扣除資源
            for res in required_resources:
                self.resources[res] -= 1
            
            self.inventory.append(child)
            print(f"🍼 {child.name}（{child.color}） 誕生了！你已消耗 1 份「{'、'.join(required_resources)}」。")




    def merge_creatures(self, index1, index2): 
        """讓兩隻魔法生物合體，提升主體能量，但不直接進化"""
        
        # 確保輸入的索引是有效的
        if index1 < 1 or index2 < 1 or index1 > len(self.inventory) or index2 > len(self.inventory):
            print("❌ 無效的生物編號！")
            return

        if index1 == index2:
            print("❌ 不能自己跟自己合體！")
            return

        # 取得兩隻生物
        creature1 = self.inventory[index1 - 1]
        creature2 = self.inventory[index2 - 1]

        # 確保品種相同
        if creature1.name != creature2.name:
            print(f"❌ {creature1.name} 和 {creature2.name} 不是同品種，無法合體！")
            return

        # 確保顏色相同
        if creature1.color != creature2.color:
            print(f"❌ {creature1.name}（{creature1.color}） 和 {creature2.name}（{creature2.color}） 顏色不同，無法合體！")
            return

        # 執行合體強化
        print(f"⚡ {creature1.name}（{creature1.color}） 吞噬了 {creature2.name}（{creature2.color}）！")
        
        # 增加能量 #
        creature1.energy += min(creature2.energy * 0.2, 10)
        creature1.energy_rate += min(creature2.energy * 0.2, 10)  

        print(f"🔥 {creature2.name}（{creature2.color}） 被吞噬，從庫存中移除！")
        self.inventory.remove(creature2)  

        print(f"✅ {creature1.name}（{creature1.color}） 吞噬後獲得力量，能量提升至 {creature1.energy}，產能提升至 {creature1.energy_rate:.1f}！")
        
    def merge_gems(self):
        """當玩家集齊 7 種顏色的寶石時，合成七彩寶石"""
        required_gems = ["紅寶石", "橙寶石", "黃寶石", "綠寶石", "藍寶石", "紫寶石", "粉寶石"]

        # 檢查是否擁有每種寶石至少 1 顆
        if all(self.resources.get(gem, 0) > 0 for gem in required_gems):
            print("🌈 你集齊了七種顏色的寶石，並成功合成了一顆 **七彩寶石**！")

            # 消耗 1 顆每種顏色的寶石
            for gem in required_gems:
                self.resources[gem] -= 1
            
            # 增加 1 顆七彩寶石
            self.resources["七彩寶石"] = self.resources.get("七彩寶石", 0) + 1
        else:
            print("❌ 你的寶石顏色尚未集齊，無法合成七彩寶石！")
    
    def explore(self, location="螢露谷"):
        """探索螢露谷或夢魘灣，獲得不同的資源或魔法生物"""
        
        if location not in ["螢露谷", "夢魘灣"]:
            print("❌ 無效的探索地點！請選擇 `螢露谷` 或 `夢魘灣`")
            return

        # 夢魘灣只有當玩家解鎖第一塊土地後才可探索
        if location == "夢魘灣" and self.unlocked_lands < 1:
            print("❌ 你尚未解鎖「夢魘灣」！請先使用七彩寶石解鎖土地。")
            return

        print(f"🛤️ 你開始探索 {location}... ⏳（需時 1:00）")
        time.sleep(3)  # 模擬探索時間（縮短為 3 秒）

        # 探索獎勵
        if location == "螢露谷":
            rewards = ["螢露蜜", "螢露土", "螢露水"]
            special_creature_name = "星光螢火蟲"
            special_creature_colors = ["綠", "藍", "紫"]
            special_creature_chance = 0.3
        elif location == "夢魘灣":
            rewards = ["夢魘果實", "夢魘之塵", "夢魘精華"]
            special_creature_name = "夢魘貓"
            special_creature_colors = ["綠", "藍", "紫"]
            special_creature_chance = 0.3

        # **保底獎勵**
        base_reward = random.choice(rewards)
        self.resources[base_reward] += 1
        print(f"🎉 你成功探索 {location}，獲得了 **{base_reward}**！")

        # 額外獎勵
        if random.random() < 0.5:  # 50% 機率獲得額外資源
            extra_reward = random.choice(rewards)
            self.resources[extra_reward] += 1
            print(f"✨ 額外獎勵：你獲得了 **{extra_reward}**！")

        # 可能遇到特殊生物
        if random.random() < special_creature_chance:
            new_color = random.choice(special_creature_colors)
            # 確保名稱統一
            normalized_creature_name = special_creature_name.strip()
            self.add_creature(normalized_creature_name, new_color)
            print(f"✨ 你在探索中遇見了一隻 **{new_color} 色的 {normalized_creature_name}**，並成功帶回培育室！✨")

        # 離開期間生物會產生能量
        for creature in self.inventory:
            creature.energy += creature.energy_rate
            print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate} 點能量！")
            creature.drop_gem()

            
            
