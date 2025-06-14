import time
import random
import script.scriptVillage as scriptVillage
import script.shopLana as shopLana
import script.plantLuna as plantLuna
import script.magicNas as magicNas
import script.questHwasa as questHwasa

class Village:
    def __init__(self):
        self.money = 0
        self.gossip = 0
        self.unlocked_features = {
            "shop": False,  # 商店
            "greenhouse": False,  # 溫室
            "magic": False,  # 魔法學習
            "quests": False,  # 任務系統
        }
        self._player = None
        self._on_exit_callbacks = []
        
        # NPC 物件初始化為 None
        self.scriptVillage = None
        self.shopLana = None
        self.plantLuna = None
        self.magicNas = None
        self.questHwasa = None

    def set_player(self, player):
        """設置玩家引用，使用依賴注入模式"""
        self._player = player
        
        # 初始化所有 NPC 物件
        self.scriptVillage = scriptVillage(player)
        self.shopLana = shopLana(player)
        self.plantLuna = plantLuna(player)
        self.magicNas = magicNas(player)
        self.questHwasa = questHwasa(player)

    def register_exit_callback(self, callback):
        """註冊退出回調函數"""
        self._on_exit_callbacks.append(callback)

    def enter(self):
        """進入部落"""
        if not self._player:
            raise RuntimeError("Player not set. Call set_player() first.")

        print("\n🏞 **前往部落中...**")
        count = 1
        time.sleep(3)  # 模擬前往部落時間（縮短為 3 秒）

        if self.gossip == 0:
            print("🌟 你來到了一個神秘的部落，四周環繞著樹木和瀑布，空氣中彷彿充滿了魔法的氣息。")
            print("🌟 這裡的居民似乎是一群精靈，他們看起來對你充滿好奇。")
            print("🌟 你決定和他們交流，看看是否能獲得一些有用的資訊。")
        else:
            print("\n🏞 **精靈遺族部落**")

        while True:
            print("\n📜 **指令列表**：")
            print("`talk` - 與隨機部落精靈對話")
            if self.unlocked_features["shop"]:
                print("🛍 `shop` - 進入拉娜的寶石交易所")
            if self.unlocked_features["greenhouse"]:
                print("🌿 `greenhouse` - 進入露娜的溫室")
            if self.unlocked_features["magic"]:
                print("🔮 `magic` - 進入娜絲的魔法實驗室")
            if self.unlocked_features["quests"]:
                print("🏡 `quests` - 與村長華莎對話，接受任務")
            print("🔙 `exit` - 離開精靈遺族部落")

            command = input("\n請輸入指令：").strip().lower()

            if command.startswith("talk"):
                if self.gossip == 0:
                    scriptVillage.talk1()
                    self.gossip += 1
                    return
                else:
                    parts = command.split()
                    npc_name = parts[1] if len(parts) > 1 else None
                    self.talk(npc_name)

            elif command == "shop" and self.unlocked_features["shop"]:
                shopLana.shop(self._player)

            elif command == "greenhouse" and self.unlocked_features["greenhouse"]:
                plantLuna.plant(self._player)

            elif command == "magic" and self.unlocked_features["magic"]:
                magicNas.magic(self._player)

            elif command == "quests" and self.unlocked_features["quests"]:
                questHwasa.quest(self._player)

            elif command == "exit":
                print("👋 離開精靈遺族部落！")
                print(f"🛤️ 你結束探索部落... ⏳（ 總耗時 {count}:00）")
                time.sleep(3)  # 模擬探索時間

                for creature in self.player.inventory:
                    creature.energy += creature.energy_rate * count
                    print(f"🔋 {creature.name}（{creature.color}） 產生了 {creature.energy_rate * count} 點能量！")
                    creature.drop_gem()
                break

            else:
                print("❌ 無效指令，請重新輸入")

    def talk(self, npc_name=None):
        """隨機找一位精靈溝通，溝通後解鎖對應面板，如商店、農場等"""
        npcs = {
            "拉娜": ("商人", self.talk_to_lana),
            "露娜": ("園藝師", self.talk_to_luna),
            "娜絲": ("魔法師", self.talk_to_nas),
            "華莎": ("村長", self.talk_to_hwasa),
            "普通精靈": ("村民", self.talk_to_villager)
        }

        if npc_name is None:
            npc_name = random.choice(list(npcs.keys()))

        role, talk_func = npcs[npc_name]
        print(f"\n🧝 你遇見了一位精靈：{npc_name}（{role}）")
        talk_func()

        self.gossip += 1

    def talk_to_lana(self):
        """與拉娜對話，解鎖商店"""
        self.shopLana.shop()

    def talk_to_luna(self):
        """與露娜對話，解鎖溫室與種植系統"""
        self.plantLuna.plant()

    def talk_to_nas(self):
        """與娜絲對話，學習魔法並提升淨化等級"""
        self.magicNas.magic()

    def talk_to_hwasa(self):
        """與村長華莎對話，獲取任務與獎勵"""
        self.questHwasa.quest()

    def talk_to_villager(self):
        """與普通精靈對話，沒有特殊功能"""
        dialogue = [
            "藍眼精靈大叔：「當初便是過度採集才造成了大量汙染。還好七彩寶石能夠淨化土地。世間的淨化師已經不多了。」",
            "紅髮精靈少女：「你好呀人類!」",
            "白髮精靈：「身上穿點好東西，能抵抗污染的力量。」",
            "綠眼精靈：「食用魔法植物可以治百病!」",
            "沉默的精靈：「大部分的生物多多少少都有些汙染疾病在身上呢。你真幸運，能成為淨化師。」",
            "精靈小孩：「我長大要成為淨化師!」",
            "精靈少女：「傳說中，在一個叫海洋的地方有一種生物叫人魚，真想去海洋看看~」",
            "綠髮精靈少年：「故事書上寫人類已經絕種了，沒想到還有人類!」",
        ]
        print(random.choice(dialogue))
