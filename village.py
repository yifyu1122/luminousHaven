import time
import player
import script.scriptVillage as scriptVillage

class Village:
    def __init__(self):
        self.money = 0
        self.gossip = 0
        
    def enter(self):
        print("\n🏞 **前往部落中...**")
        count=1
        time.sleep(3)  # 模擬前往部落時間（縮短為 3 秒）
        if self.gossip == 0:
            print("🌟 你來到了一個神秘的部落，四周環繞著樹木和瀑布，空氣中彷彿充滿了魔法的氣息。")
            print("🌟 這裡的居民似乎是一群精靈，他們看起來非常友善。")
            print("🌟 你決定和他們交流，看看是否能獲得一些有用的資訊。")
        else:
            print("\n🏞 **精靈遺族部落**")       
        while True:
            print("\n📜 **指令列表**：")
            print("`talk` - 與隨機部落精靈對話")
            print("🔙 `exit` - 離開精靈遺族部落")
            command = input("\n請輸入指令：").strip().lower()
            if command == "talk":
                self.talk()
                count+=1
            elif command == "exit":
                print("👋 離開精靈遺族部落！")
                print(f"🛤️ 你結束探索部落... ⏳（ 總耗時 {count}:00）")
                time.sleep(3)  # 模擬探索時間（縮短為 3 秒）
                for creature in player.inventory:
                    creature.energy += creature.energy_rate*count
                    print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate*count} 點能量！")
                    creature.drop_gem()
            else:
                print("❌ 無效指令，請輸入 `talk` 或 `exit`")
    def talk(self):
        if self.gossip == 0:
           scriptVillage.talk1() 
           self.gossip += 1
        elif(self.gossip>=1):
           """隨機找一位精靈溝通，溝通後解鎖對應面板，如商店、農場等"""