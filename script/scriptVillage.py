import time
import player
class ScriptVillage:
    def __init__(self):
        self.likeness = 0 
        self.humor = 0
    def talk1(self):
        print("\n🧝 你注意到一位紅髮的精靈少女正在樹蔭下玩耍。")
        time.sleep(1)
        print("👀 她一轉頭，看見了你，眼睛瞬間睜大，然後——")
        time.sleep(1)

        print("\n🧝 **紅髮精靈**：「麻麻！有怪物！」👀💨\n")
        time.sleep(1)

        print("你還來不及反應，她已經撒腿跑了。")
        print("🧝‍♂️ 周圍的精靈們聞聲而動，有的立刻後退，有的則握緊了手中的法杖，神情戒備。")

        while(1):
            print("\n🔹 **選擇行動** 🔹")
            print("`1` - 「我才不是怪物！」（強烈反駁）")
            print("`2` - 默默站在原地，觀察情勢。")
            print("`3` - 尷尬地逃離現場。")
            print("`4` - 試圖交出一顆七彩寶石。")

            choice = input("\n👉 你的選擇是？（輸入數字 1 / 2 / 3 / 4 ）：").strip()

            if choice == "1":
                print("\n🗣️ 你大聲反駁：「我才不是怪物！」\n")
                time.sleep(1)
                print("👀 精靈們對你的反應感到驚訝，有些開始竊竊私語……")
                print("💬 其中一位長者走上前來：「冷靜些。我們只是好奇你是誰。你聽得懂我們的語言嗎？」")
                break
            elif choice == "2":
                print("\n😐 你選擇沉默不語，靜靜觀察精靈們的反應。\n")
                time.sleep(1)
                print("🌿 精靈們依然盯著你，但有些人開始低聲討論，似乎在評估你的來歷。")
                print("💬 一位銀髮精靈走上前，溫和地問道：「你是從哪裡來的？你聽得懂我們的語言嗎？」")
                break
            elif choice == "3":
                print("\n🏃 你選擇尷尬地跑走。\n")
                time.sleep(1)
                print("💨 你迅速轉身離開，但你感覺到背後投來更多疑惑的目光……")
                print("💭 （這樣跑走真的好嗎……？）")
                time.sleep(1)
                print("🌿 很快精靈便將你圍了起來。")
                print("💬 一位銀髮精靈走上前，溫和地問道：「你是從哪裡來的？你聽得懂我們的語言嗎？」")
                break
            elif choice == "4":
                if player.resources["七彩寶石"] > 0:
                    print("\n💎 你拿出一顆七彩寶石，試圖交給精靈們。\n")
                    time.sleep(1)
                    player.resources["七彩寶石"] -= 1
                    print("🌟 精靈們看到七彩寶石，眼睛瞬間放光，議論紛紛。")
                    print("💬 一位精靈長者走上前來，神情複雜：「這是……七彩寶石？」")
                    time.sleep(1)
                    print("🌫️ 然而，並非所有精靈都表現出興奮，反而有些人開始竊竊私語，似乎在懷疑什麼……")
                    print("💬 另一位長老低聲說：「這種寶石已經很久沒有出現了……」")
                    print("⚖️ 你的選擇似乎引起了更大的關注，但精靈們並沒有立刻完全信任你。")
                    print("💬 一位銀髮精靈走上前，溫和地問道：「你是從哪裡來的？你聽得懂我們的語言嗎？」")
                    break
                else:
                    print("\n❌ 你手上並沒有七彩寶石！")
            else:
                print("\n❌ 無效的選擇，精靈們依然看著你，等著你的回應……")
      
        while(1):
            print("\n🔹 **選擇行動** 🔹")
            print("`1` - 「聽得懂。」")
            print("`2` - 點頭")
            print("`3` - 「I'm fine. Thank you, and you?」")
            
            choice = input("\n👉 你的選擇是？（輸入數字 1 / 2 / 3 ）：").strip()

            if choice == "1":
                print("\n💬 你回答：「聽得懂。」")
                print("\n💬🧝‍♂️ 銀髮精靈點點頭：「那就好。我們有很多話想問你……」")
            elif choice == "2":
                print("\n🤔 你只是點頭，沒有說話。")
                print("\n💬🧝‍♂️ 精靈們交換了幾個眼神，似乎對你的沉默感到困惑。")
                print("💬 一個綠髮精靈說：「他聽不懂人話。」")
            elif choice == "3":
                print("\n 你試圖用英文回應：「I'm fine. Thank you, and you?」")
                print("\n💬🤨 精靈們一臉問號，場面變得更加尷尬……")
                print("💬 一個綠髮精靈說：「他聽不懂人話。」")
                if self.humor < 2:
                    print("\n🤣 你的幽默感+1！")
                    self.humor+=1
            else:
                print("\n❌ 無效的選擇，請輸入數字 1 / 2 / 3。")
                
            print ("\n🧝‍♂️ 銀髮精靈：「你是從哪裡來的？你為什麼會來到我們的部落？」")
            print ("🧝‍♂️ 銀髮精靈：「我們從未見過你這樣的生物。」")
            while True:
                print("\n🔹 **選擇行動** 🔹")
                print("`1` - 「我是一名在培育室進行物種復甦的科學家。」")
                print("`2` - 「嗚嗚嗚嗚我不知道我迷路了我要找麻麻~」")

                choice = input("\n👉 你的選擇是？（輸入數字 1 / 2 ）：").strip()    

                if choice == "1":
                    print("\n💬 你回答：「我是一名在培育室進行物種復甦的科學家。在淨化土地的過程中意外發現了這個地方。」")
                    time.sleep(1)
                    print("🧝‍♂️ 銀髮精靈沉默了下，似乎是在消化你剛才說的話。")
                    time.sleep(1)
                    print("你：「在我的研究下，我發現了製造七彩寶石的方法，並且學會了如何使用寶石淨化土地。」")
                    time.sleep(1)

                    print("\n🧝‍♂️ 銀髮精靈點點頭：「這樣啊……也許這就是我們祖先曾經提到過的技術。」")
                    print("✨ 精靈們的敵意稍微減少，開始把你視為來訪的研究者。")

                    # **設定自由探索模式**
                    player.likeness += 1
                    print("\n🔓 你現在可以自由探索精靈部落！\n")

                    # **解鎖新探索點**
                    player.unlocked_locations.append("精靈部落")
                    break

                elif choice == "2":
                    print("\n💬 你回答：「嗚嗚嗚嗚我不知道我迷路了我要找麻麻~」")
                    time.sleep(1)
                    print("\n🧝‍♂️ 銀髮精靈溫柔的拍了拍你的背：「冷靜一點，你家在哪裡？我帶你去找媽媽。」")
                    time.sleep(1)
                    print("\n🧝‍♂️ 你嗚嗚嗚嗚沒辦法回答。眾精靈氾起了母愛。")
                    
                    # **提高精靈對玩家的好感**
                    player.likeness += 2
                    print("\n💕 眾精靈對你的好感 +2，決定讓你自由行動。\n")

                    # **設定自由探索模式**
                    player.unlocked_locations.append("精靈部落")
                    break

            print("\n✨ **你現在可以自由探索精靈部落，尋找新的線索與資源！**")
