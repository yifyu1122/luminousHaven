import random
import time
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
        """讓兩隻魔法生物繁殖"""
        if index1 < 1 or index2 < 1 or index1 > len(self.inventory) or index2 > len(self.inventory):
            print("❌ 無效的生物編號！")
            return

        parent1 = self.inventory[index1 - 1]
        parent2 = self.inventory[index2 - 1]

        child = parent1.breed(parent2)
        if child:
            self.inventory.append(child)
            
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
        creature1.energy += creature2.energy
        creature1.energy_rate *= 1.2  # 產能速度提升 1.2 倍

        print(f"🔥 {creature2.name}（{creature2.color}） 被吞噬，從庫存中移除！")
        self.inventory.remove(creature2)  # 移除副體生物

        print(f"✅ {creature1.name}（{creature1.color}） 吞噬後獲得力量，能量提升至 {creature1.energy}，產能提升至 {creature1.energy_rate:.1f}！")
    def explore(self):
        """探索螢露谷，隨機獲得資源"""
        print("🛤️ 你開始探索螢露谷... ⏳（需時 1:00）")
        time.sleep(3)  # 模擬探索時間（縮短為 3 秒）
        
        rewards = ["螢露蜜", "螢露土", "螢露水"]
        reward = random.choice(rewards)
        print(f"🎉 你成功探索螢露谷，獲得了 **{reward}**！")
        self.resources[reward] += 1
        #離開期間生物有產生能量
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
