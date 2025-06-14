import random
import time
from model.magicCreature import MagicCreature

from model.resourceManager import ResourceManager

class Player:
    def __init__(self):
        self.inventory = []
        self.resources = ResourceManager()
        # 培育室最大容量
        self.max_creatures = 10
        self.unlocked_lands = 1
        self.exploration_count = {"螢露谷": 0, "夢魘灣": 0} 
        self.polluted_lands = {"螢露谷": False, "夢魘灣": False}  
        self.purification_level = 1

    def _handle_village_exit(self, count):
        """處理離開村莊時的事件"""
        for creature in self.inventory:
            creature.energy += creature.energy_rate * count
            print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate * count} 點能量！")
            for creature in self.inventory:
                drops = creature.drop_gem()
                for item in drops:
                    self.resources.add(item)
                    print(f"🌟 你現在擁有 {self.resources.get(item)} 個 {item}！")



    def add_creature(self, creature_name, color):
        """新增魔法生物到持有列表"""
        if len(self.inventory) >= self.max_creatures:
            self.list_creatures()
            print("❌ 培育室已滿，無法新增生物！請先釋放或合併現有生物。")           
            print("💡 提示：你可以使用 `merge A B` 來融合兩隻相同品種的生物，釋放空間！")
            return
        
        # 確保所有生物名稱統一（去除空格、固定格式）
        normalized_name = creature_name.strip()

        new_creature = MagicCreature(normalized_name, color, 50, 10)
        self.inventory.append(new_creature)
        print(f"✅ {new_creature.name}（{new_creature.color}） 加入培育室！目前數量：{len(self.inventory)}/{self.max_creatures}")
    
    def synthesize_gem(self):
        """合成七彩寶石，需要集齊 7 種顏色的寶石"""
        required_gems = ["紅寶石", "橙寶石", "黃寶石", "綠寶石", "藍寶石", "紫寶石", "透明寶石"]

        # 檢查是否擁有每種寶石至少 1 顆
        if all(self.resources.get(gem, 0) > 0 for gem in required_gems):
            print("🌈 你集齊了七種顏色的寶石，並成功合成了一顆 **七彩寶石**！")

            # 消耗 1 顆每種顏色的寶石
            for gem in required_gems:
                self.resources.consume(gem)
            
            self.resources.add("七彩寶石")
        else:
            print("❌ 你的寶石顏色尚未集齊，無法合成七彩寶石！")

    def unlock_land(self):
        """使用七彩寶石解鎖新的土地，擴建培育室，並在首次解鎖時獲得夢魘貓（黃）"""
        if self.resources.get("七彩寶石") < 1:
            print("❌ 七彩寶石不足！需要 1 顆七彩寶石來解鎖新土地。")
            return

        self.resources.consume("七彩寶石")
        self.unlocked_lands += 1
        self.max_creatures += 5  # 每次解鎖增加 5 個可容納生物數量
        print(f"🌿 你使用 1 顆七彩寶石，成功淨化了一塊被污染的土地！")
        print(f"🏡 你的培育室擴建完成，可容納生物數量增加至 {self.max_creatures}！")

        # 第一次解鎖土地時，獲得夢魘貓（紅）並解鎖新地圖
        if self.unlocked_lands == 1:
            self.add_creature("夢魘貓", "紅")
            print("✨ 你發現了一隻 **夢魘貓（紅）**，並成功將牠帶回培育室！")
            print("🌙 你解鎖了一個新的探索地點：**夢魘灣**！")
            print("🌙 你解鎖了一個新的探索地點：**精靈遺族的部落**！")
        
            
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
    

    


    def purify_land(self, location):
        """使用七彩寶石來淨化被汙染的土地"""
        if location not in self.polluted_lands:
            print("❌ 無效的地點！")
            return
        
        if not self.polluted_lands[location]:
            print(f"✅ {location} 沒有被汙染，無需淨化。")
            return

        # 需要對應等級的七彩寶石
        required_purification = self.pollution_levels[location]
        
        if self.resources.get("七彩寶石") < required_purification:
            print(f"❌ 七彩寶石不足！需要 {required_purification} 顆七彩寶石來淨化 {location}。")
            return
        
        # 消耗七彩寶石
        self.resources["七彩寶石"] -= required_purification
        self.polluted_lands[location] = False
        print(f"🌱 你使用 {required_purification} 顆七彩寶石成功淨化 {location}，可以再次探索！")
     
            
