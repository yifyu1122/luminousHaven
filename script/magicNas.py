from .baseNPC import BaseNPC
import time

class MagicNas(BaseNPC):
    """娜絲的魔法塔，提供學習魔法和淨化土地的功能"""
    def __init__(self, player):
        super().__init__(player, name="娜絲", role="魔法師")

    def get_initial_dialogue(self):
        return [
            "\n**白髮精靈**：「你好呀~人類我是魔法師娜絲。」",
            "**娜絲**：「如果你想學習真正的魔法，得先證明你值得。」",
            "**娜絲**：「學魔法可不是免費的，需要 **5000 精靈幣** 和一些魔法資源。」"
        ]

    def get_repeat_dialogue(self):
        return ["\n🔮 **娜絲**：「需要我教你魔法嗎？」"]

    def handle_interaction(self):
        """處理魔法塔互動"""
        # 顯示對話
        if self.gossip == 0:
            for line in self.get_initial_dialogue():
                print(line)
        else:
            for line in self.get_repeat_dialogue():
                print(line)

        # 顯示選單
        print("\n🔹 **選擇行動** 🔹")
        print("`1` - 學習魔法（提升淨化等級，需要 5000 精靈幣 + 魔法資源）")
        print("`2` - 詢問娜絲關於污染的事")
        print("`3` - 退出")

        choice = input("\n👉 你的選擇是？（輸入數字 1 / 2 / 3）：").strip()

        if choice == "1":
            self.learn_magic()
        elif choice == "2":
            self.ask_about_pollution()
        else:
            print("🚪 你離開了娜絲的魔法塔。")
            
        self.gossip += 1

    def magic(self):
        """原有的魔法功能保持不變，但現在透過 handle_interaction 調用"""
        self.handle_interaction()

    def learn_magic(self):
        """學習魔法，提高淨化等級"""
        required_coins = 5000
        required_resources = ["星輝之粉", "夢魘貓毛"]

        if self.player.village.unlocked_features["magic"]:
            print("🔮 **娜絲**：「你已經學會魔法了！現在只能透過 **實戰** 來提升能力。」")
            return
        
        # 檢查是否有足夠的精靈幣
        if self.player.resources.get("精靈幣", 0) < required_coins:
            print("❌ **娜絲**：「你的精靈幣不夠，先去賺點錢吧！」")
            return

        # 檢查是否有足夠的魔法資源
        missing_resources = [res for res in required_resources if self.player.resources.get(res, 0) < 1]
        if missing_resources:
            print(f"❌ **娜絲**：「你的魔法資源不足，需要：{', '.join(missing_resources)}」")
            return
        
        # 消耗資源並提升淨化等級
        self.player.resources["精靈幣"] -= required_coins
        for res in required_resources:
            self.player.resources[res] -= 1

        self.player.village.unlocked_features["magic"] = True
        self.player.purification_level += 1
        print(f"✨ 你學會了魔法！你的 **淨化等級提升至 {self.player.purification_level}**！")

    def ask_about_pollution(self):
        """詢問娜絲關於污染的事"""
        print("\n🔮 **娜絲**：「污染是這個世界最大的危機。當土地被探索過度，它會變得不穩定。」")
        time.sleep(1)
        print("🌫 **娜絲**：「如果土地污染程度達到一定程度，就會無法再探索，除非進行淨化。」")
        time.sleep(1)
        print("💎 **娜絲**：「你可以使用 **七彩寶石** 來淨化土地，不過污染次數越高，需要的寶石數量也會增加。」")
        print("\n🔮 **娜絲**：「如果你學會了魔法，就可以幫助土地恢復原本的活力。」")

