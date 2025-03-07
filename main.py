import time
import random
from player import Player
from magicCreature import MagicCreature

# 定義可能的顏色
COLORS = ["紅", "橙", "黃", "綠", "藍", "紫", "粉"] 




def game_intro():
    """遊戲開場說明"""
    print("🌿 歡迎來到幻彩育境 Luminous Haven！🌿")
    print("你目前所在地：✨ **培育室** ✨")
    print("在這裡，你可以培育、繁殖並提升你的魔法生物。")
    print("\n🗺️ **探索選項**：")
    print("🚀 你可以前往 **螢露谷**（適合培育星光螢火蟲）")
    print("🔍 探索可獲得：食物 / 土地 / 水")
    print("⏳ 探索耗時：1:00")
    print("\n🔹 輸入 `explore` 來開始探索，或輸入 `help` 查看其他指令。\n")

# 遊戲開始時呼叫開場說明
game_intro()

# 創建玩家
player = Player()

# 預設給玩家一些初始生物23
player.add_creature(MagicCreature("星光螢火蟲", "紅" , 50, 10))
player.add_creature(MagicCreature("星光螢火蟲", "黃", 50, 10))
player.add_creature(MagicCreature("夢魘貓", "藍", 50, 10))

# 指令介面
while True:
    print("\n指令列表：")
    print("📜 `list` - 查看持有生物")
    print("📜 `resource` -  查看持有資源")
    print("❤️ `breed A B` - 讓第 A 和 B 隻生物繁殖（例如 `breed 1 2`）")
    print("🔥 `merge A B` - 讓第 A 和 B 隻生物合體（例如 `merge 1 2`）")
    print("🔍 `explore` - 探索螢露谷")
    print("❌ `exit` - 離開遊戲")

    command = input("\n請輸入指令：").strip().lower() 

    if command == "list":
        player.list_creatures()
    elif command == "resource":
        player.list_resources()

    elif command.startswith("breed"):
        try:
            parts = command.split()
            if len(parts) != 3:
                raise ValueError  

            idx1, idx2 = int(parts[1]), int(parts[2]) 
            player.breed_creatures(idx1, idx2)
        except (ValueError, IndexError):
            print("❌ 指令格式錯誤！請使用 `breed A B`，例如 `breed 1 2`")

    elif command.startswith("merge"):
        try:
            parts = command.split()
            if len(parts) != 3:
                raise ValueError 

            idx1, idx2 = int(parts[1]), int(parts[2]) 
            player.merge_creatures(idx1, idx2)
        except (ValueError, IndexError):
            print("❌ 指令格式錯誤！請使用 `merge A B`，例如 `merge 1 2`")
    elif command == "explore":
        player.explore()
 

    elif command == "exit":
        print("👋 遊戲結束！")
        break

    else:
        print("❌ 無效指令，請輸入 `list`, `resource`, `breed`, `merge`, `explore` 或 `exit`")