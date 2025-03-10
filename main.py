from player import Player

# 定義可能的顏色
COLORS = ["紅", "橙", "黃", "綠", "藍", "紫", "粉"] 

def game_intro():
    """遊戲開場說明"""
    print("🌿 歡迎來到幻彩育境 Luminous Haven！🌿")
    print("你目前所在地：✨ **培育室** ✨")
    print("在這裡，你可以培育、繁殖並提升你的魔法生物。\n")

game_intro()

player = Player()

player.add_creature("星光螢火蟲", "紅")
player.add_creature("星光螢火蟲", "黃")
player.add_creature("夢魘貓", "紅")

while True:
    print("\n📜 **指令列表**：")
    print("🔍 `explore 地點` - 探索指定地點（如 `explore 螢露谷`，`explore 夢魘灣`）")    
    print("📜 `list` - 查看持有生物")
    print("📜 `resource` - 查看持有資源")
    print("❤️ `breed A B` - 讓第 A 和 B 隻生物繁殖（例如 `breed 1 2`）")
    print("🔥 `merge A B` - 讓第 A 和 B 隻生物合體（例如 `merge 1 2`）")
    print("🌱 `synthesize` - 合成七彩寶石")
    print("🏡 `unlock_land` - 使用七彩寶石解鎖新土地（擴充培育室）")
    print("❌ `exit` - 離開遊戲")

    command = input("\n請輸入指令：").strip().lower()

    if command == "list":
        player.list_creatures()
    elif command == "resource":
        player.list_resources()
    elif command == "unlock_land":
        player.unlock_land()
    elif command == "synthesize":
        player.synthesize_gem()
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

    elif command.startswith("explore"):
        try:
            parts = command.split()
            location = parts[1] if len(parts) > 1 else "螢露谷"  # 預設探索螢露谷
            player.explore(location)
        except IndexError:
            print("❌ 指令格式錯誤！請使用 `explore 螢露谷` 或 `explore 夢魘灣`")

    elif command == "exit":
        print("👋 遊戲結束！")
        break

    else:
        print("❌ 無效指令，請重新輸入")