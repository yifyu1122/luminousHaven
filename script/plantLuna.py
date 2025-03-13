class plantLuna:
    def __init__(self, player):
        self.gossip = 0
        self.player = player
    def plant(self):
        if self.gossip == 0:
            print("\n**金髮精靈**：「你好呀，我是露娜負責培育魔法植物。」") 
            print("**露娜**：「說起來我們的工作挺相似的呢。」")    
            print("**露娜**：「魔法植物可以做為魔法生物的食糧，也可以用來治病。」") 
            print("**露娜**：「你有需要可以來我這裡購買。」")     
            print("\n**露娜**：「想學種植？當我的學徒可不容易，你要想清楚啊人類。」")
            print("**露娜**：「光是材料費便是一筆不小的開銷。」") 
            print("**露娜**：「等你集齊**10,000 精靈幣**，再來向我學習吧」")   
            self.gossip += 1
            
        print("\n🌿 **露娜**：「你需要什麼嗎？」")
        print("`1` - 購買魔法植物")
        print("`2` - 學習種植（需要 10,000 精靈幣）")
        print("`3` - 退出")

        choice = input("👉 請選擇：").strip()

        if choice == "1":
            self.shop_plants()
        elif choice == "2":
            self.learn_planting()
        else:
            print("🚪 你離開了露娜的商店。")

    def shop_plants(self):
        """購買魔法植物"""
        plants = {
            "月光草": 500,
            "星露藤": 800,
            "銀葉花": 1200,
            "夢幻蘑菇": 1500
        }

        print("\n🛍 **魔法植物商店**")
        print("🌱 你可以購買以下魔法植物：")
        for plant, price in plants.items():
            print(f" - {plant}：💰 {price} 精靈幣")

        choice = input("👉 請輸入你想購買的植物名稱（或輸入 `exit` 取消購買）：").strip()

        if choice in plants:
            price = plants[choice]
            if self.player.resources.get("精靈幣", 0) >= price:
                self.player.resources["精靈幣"] -= price
                self.player.resources[choice] = self.player.resources.get(choice, 0) + 1
                print(f"✅ 你購買了一株 **{choice}**！")
            else:
                print("❌ **露娜**：「你的精靈幣不夠，先去賺點錢吧！」")
        elif choice.lower() == "exit":
            print("🚪 你離開了商店。")
        else:
            print("❌ **露娜**：「我這裡沒有這種植物哦！」")

    def learn_planting(self):
        """學習種植技能"""
        if self.player.village.unlocked_features["greenhouse"]:
            print("🌿 **露娜**：「你已經學會種植了，不用再學啦！」")
            return

        if self.player.resources.get("精靈幣", 0) >= 10000:
            self.player.resources["精靈幣"] -= 10000
            self.player.village.unlocked_features["greenhouse"] = True
            print("✨ 你解鎖了 **種植技能**！現在你可以種植魔法植物了！")
        else:
            print("❌ **露娜**：「你的精靈幣不夠，先去賺點錢吧！」")