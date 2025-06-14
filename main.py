from player import Player

def game_intro():
    """遊戲開場說明"""
    print("🌿 歡迎來到幻彩育境 Luminous Haven！🌿")
    print("你目前所在地：✨ **培育室** ✨")
    print("在這裡，你可以培育、繁殖並提升你的魔法生物。\n")

game_intro()

player = Player()

player.initialize_village()

player.add_creature("星光螢火蟲", "紅")
player.add_creature("星光螢火蟲", "黃")
player.add_creature("夢魘貓", "藍")

while True:
    print("\n📜 **指令列表**：")
    print("🔍 `explore` - 探索獲取資源")    
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
            if player.unlocked_lands >= 1:
                print("\n🌍 你可以探索以下地點：")
                print("1. 探索螢露谷")
                print("2. 探索夢魘灣")
                print("3. 探索精靈部落")

                choice = input("\n👉 你想探索哪裡？（輸入 1 / 2 / 3）：").strip()

                if choice == "1":
                    player.explore("螢露谷")
                elif choice == "2":
                    player.explore("夢魘灣")
                elif choice == "3":
                    player.village.enter() 
                else:
                    print("❌ 無效選項，請輸入 1 / 2 / 3。")
            else:
                player.explore("螢露谷")
        except Exception as e:
            print("❌ 指令格式錯誤！請使用 `explore `")

    elif command == "exit":
        print("👋 遊戲結束！")
        break

    else:
        print("❌ 無效指令，請重新輸入")