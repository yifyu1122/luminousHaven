from model.player import Player
import system.breed as breed
import system.merge as merge
import system.explore as explore

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

commands = {
    "list": player.list_creatures,
    "resource": player.list_resources,
    "synthesize": player.synthesize_gem,
    "unlock_land": player.unlock_land,
    "exit": lambda: print("👋 遊戲結束！")
}

def handle_breed(parts):
    """處理繁殖指令"""
    try:
        parts = command.split()
        if len(parts) != 3:
            raise ValueError  
        idx1, idx2 = int(parts[1]), int(parts[2]) 
        breed.breed_creatures(idx1, idx2)
    except (ValueError, IndexError):
        print("❌ 指令格式錯誤！請使用 `breed A B`，例如 `breed 1 2`")

def handle_merge(parts):
    """處理合體指令"""
    try:
        if len(parts) != 3:
            raise ValueError
        idx1, idx2 = int(parts[1]), int(parts[2])
        merge.merge_creatures(idx1, idx2)
    except (ValueError, IndexError):
        print("❌ 指令格式錯誤！請使用 `merge A B`，例如 `merge 1 2`")

def handle_explore():
    """處理探索指令"""
    if player.unlocked_lands >= 1:
        print("\n🌍 你可以探索以下地點：")
        print("1. 探索螢露谷")
        print("2. 探索夢魘灣")
        print("3. 探索精靈部落")

        choice = input("\n👉 你想探索哪裡？（輸入 1 / 2 / 3）：").strip()

        if choice == "1":
            explore.explore("螢露谷")
        elif choice == "2":
            explore.explore("夢魘灣")
        elif choice == "3":
            player.village.enter() 
        else:
            print("❌ 無效選項，請輸入 1 / 2 / 3。")
    else:
        explore.explore("螢露谷")


while True:
    # === 指令區 ===
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
    parts = command.split()

    if not parts:
        print("❌ 請輸入有效指令")
        continue

    cmd = parts[0]

    if cmd == "exit":
        commands["exit"]()
        break
    elif cmd in commands:
        commands[cmd]()
    elif cmd == "breed":
        handle_breed(parts)
    elif cmd == "merge":
        handle_merge(parts)
    elif cmd == "explore":
        handle_explore()
    else:
        print("❌ 無效指令")