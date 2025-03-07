import random
import time
from magicCreature import MagicCreature

class Player:
    def __init__(self):
        self.inventory = []
        self.resources = {
            "螢露蜜": 0,
            "螢露土": 0,
            "螢露水": 0
        }
        self.rainbow_energy = 0 

    def add_creature(self, creature):
        """新增魔法生物到持有列表"""
        self.inventory.append(creature)

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
        """顯示玩家持有的所有資源"""
        if not self.resources:
            print("❌ 你目前沒有任何資源！")
            return
        print("\n🔹 你的資源：")
        for resource, count in self.resources.items():
            print(f"   {resource}：{count}")

    def breed_creatures(self, index1, index2):
        """讓兩隻魔法生物繁殖，但需要「螢露蜜」「螢露土」「螢露水」各 1 個"""
        
        # 檢查是否擁有足夠的繁殖資源
        required_resources = ["螢露蜜", "螢露土", "螢露水"]
        missing_resources = [res for res in required_resources if self.resources.get(res, 0) < 1]
        
        if missing_resources:
            print(f"❌ 無法繁殖！缺少以下資源：{', '.join(missing_resources)}")
            return

        # 確保輸入的索引是有效的
        if index1 < 1 or index2 < 1 or index1 > len(self.inventory) or index2 > len(self.inventory):
            print("❌ 無效的生物編號！")
            return

        parent1 = self.inventory[index1 - 1]
        parent2 = self.inventory[index2 - 1]

        child = parent1.breed(parent2)
        
        if child:
            # 繁殖成功，扣除資源
            for res in required_resources:
                self.resources[res] -= 1
            
            self.inventory.append(child)
            print(f"🍼 {child.name}（{child.color}） 誕生了！你已消耗 1 份「螢露蜜」「螢露土」「螢露水」。")

            
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
        creature1.energy += creature2.energy * 0.2
        creature1.energy_rate += creature2.energy * 0.2  

        print(f"🔥 {creature2.name}（{creature2.color}） 被吞噬，從庫存中移除！")
        self.inventory.remove(creature2)  

        print(f"✅ {creature1.name}（{creature1.color}） 吞噬後獲得力量，能量提升至 {creature1.energy}，產能提升至 {creature1.energy_rate:.1f}！")
    def explore(self):
        """探索螢露谷，隨機獲得資源，有極低機率獲得星光螢火蟲"""
        print("🛤️ 你開始探索螢露谷... ⏳（需時 1:00）")
        time.sleep(3)  # 模擬探索時間（縮短為 3 秒）
        
        # 主要資源獎勵
        rewards = ["螢露蜜", "螢露土", "螢露水"]
        reward = random.choice(rewards)
        
        # 確保 `self.resources` 內有這個資源
        if reward in self.resources:
            self.resources[reward] += 1
        else:
            self.resources[reward] = 1  # 若沒有該資源則初始化

        print(f"🎉 你成功探索螢露谷，獲得了 **{reward}**！")

        # 極低機率（10%）獲得"綠", "藍", "紫"星光螢火蟲
        if random.random() < 0.1:
            rare_colors = ["綠", "藍", "紫"]
            new_color = random.choice(rare_colors)
            new_creature = MagicCreature("星光螢火蟲", new_color, 50, 10)
            self.add_creature(new_creature)
            print(f"✨ 你在探索中遇見了一隻 **{new_color} 色的星光螢火蟲**，並成功帶回培育室！✨")

        # 離開期間生物會產生能量
        for creature in self.inventory:
            creature.energy += creature.energy_rate
            print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate} 點能量！")
            
    def help(self):
        """顯示幫助信息"""
        print("\n📚 **幻彩育境** 指令列表：")
        print("📜 `list` - 查看持有生物")
        print("📜 `resource` -  查看持有資源")
        print("❤️ `breed A B` - 讓第 A 和 B 隻生物繁殖（例如 `breed 1 2`）")
        print("🔥 `merge A B` - 讓第 A 和 B 隻生物合體（例如 `merge 1 2`）")
        print("🔍 `explore` - 探索螢露谷")
        print("❌ `exit` - 離開遊戲")
