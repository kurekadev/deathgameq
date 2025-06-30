#!/usr/bin/env python3
import random
import time
import os
import sys
import locale
import json

# 多言語対応
def get_system_language():
    try:
        lang = locale.getdefaultlocale()[0]
        if lang:
            return lang[:2].lower()
    except:
        pass
    return 'en'

# 言語設定
LANG = get_system_language()

MESSAGES = {
    'en': {
        'title': 'Q WERT',
        'intro1': 'Ancient treasure letters await discovery...',
        'intro2': 'Choose wisely to claim the golden alphabet...',
        'score': 'Score',
        'high_score': 'High Score',
        'danger': 'trap letters hidden',
        'choose': 'Choose your treasure...',
        'history': 'Your discoveries',
        'safe': 'TREASURE FOUND!',
        'death_msg1': 'You chose',
        'death_msg2': 'It was... a cursed trap letter...',
        'death_letters': 'Trap letters were',
        'game_over': 'GAME OVER',
        'new_high_score': 'NEW HIGH SCORE!',
        'combo': 'COMBO',
        'perfect': 'PERFECT TREASURE HUNT!',
        'quit': 'Farewell, treasure hunter...'
    },
    'ja': {
        'title': 'Q WERT',
        'intro1': '古代の宝物文字が発見を待っている...',
        'intro2': '賢く選んで黄金のアルファベットを手に入れよう...',
        'score': 'スコア',
        'high_score': 'ハイスコア',
        'danger': '個の罠文字が隠れている',
        'choose': '宝物を選べ...',
        'history': 'これまでの発見',
        'safe': '宝物発見！',
        'death_msg1': 'あなたは',
        'death_msg2': 'を選んだ...\nそれは...呪われた罠の文字だった...',
        'death_letters': '罠の文字は',
        'game_over': 'ゲームオーバー',
        'new_high_score': '新記録達成！',
        'combo': 'コンボ',
        'perfect': 'パーフェクト宝探し！',
        'quit': 'さらば、トレジャーハンター...'
    }
}

def msg(key):
    return MESSAGES.get(LANG, MESSAGES['en']).get(key, key)

# ハイスコア管理
def load_high_score():
    try:
        with open('high_score.json', 'r') as f:
            data = json.load(f)
            return data.get('high_score', 0)
    except:
        return 0

def save_high_score(score):
    try:
        with open('high_score.json', 'w') as f:
            json.dump({'high_score': score}, f)
    except:
        pass

class HorrorAlphabetGame:
    def __init__(self):
        self.score = 0
        self.high_score = load_high_score()
        self.alive = True
        self.chosen_letters = []
        self.combo = 0
        self.stage = 1
        self.max_stage = 5
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_logo(self, is_death=False):
        color = "\033[91m" if is_death else "\033[96m"  # 赤 or シアン
        reset = "\033[0m"
        
        logo = f"""{color}
 ██████╗     ██╗    ██╗███████╗██████╗ ████████╗
██╔═══██╗    ██║    ██║██╔════╝██╔══██╗╚══██╔══╝
██║   ██║    ██║ █╗ ██║█████╗  ██████╔╝   ██║   
██║▄▄ ██║    ██║███╗██║██╔══╝  ██╔══██╗   ██║   
╚██████╔╝    ╚███╔███╔╝███████╗██║  ██║   ██║   
 ╚══▀▀═╝      ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   {reset}"""
        print(logo)
        
    def horror_intro(self):
        self.clear_screen()
        self.print_logo()
        print(msg('intro1'))
        print(msg('intro2'))
        print(f"\n{msg('high_score')}: {self.high_score:,}")
        print("\n\033[92mPRESS ENTER TO START\033[0m")
        
        try:
            input()
        except KeyboardInterrupt:
            print(f"\n{msg('quit')}")
            sys.exit(0)
        
    def generate_hazure(self, choices, num_hazure):
        """QWERTの中からハズレを生成"""
        return random.sample(choices, min(num_hazure, len(choices)))
        
    def get_qwert_choices(self):
        """QWERTの5文字を返す"""
        return list("QWERT")
        
    def display_and_get_choice(self, choices, hazure_letters):
        """選択肢を表示して入力を取得"""
        self.clear_screen()
        
        print(f"STAGE {self.stage} | SCORE: {self.score:,} | COMBO: {self.combo}")
        print(f"⚠️  {len(hazure_letters)} {msg('danger')}")
        print("")
        
        # QWERTを横に並べて表示
        print("  " + "   ".join(choices))
        
        print("")
        print("文字を入力してください:")
        
        # 選択履歴
        if self.chosen_letters:
            print("\n" + "-" * 40)
            recent = self.chosen_letters[-5:]
            print(f"{msg('history')}: {' → '.join(recent)}")
        
        # 入力取得
        while True:
            try:
                choice = input("\n> ").strip()
                
                # 全角小文字・ひらがなを半角大文字に変換
                conversion_map = {
                    'ｑ': 'Q', 'ｗ': 'W', 'ｅ': 'E', 'ｒ': 'R', 'ｔ': 'T',
                    'q': 'Q', 'w': 'W', 'e': 'E', 'r': 'R', 't': 'T',
                    'く': 'Q', 'う': 'W', 'え': 'E', 'り': 'R', 'て': 'T'
                }
                
                if choice in conversion_map:
                    choice = conversion_map[choice]
                else:
                    choice = choice.upper()
                
                if choice in choices:
                    return choice
                
                print("❌ Q, W, E, R, T のいずれかを入力してください（全角小文字・ひらがなも可）")
                
            except KeyboardInterrupt:
                print(f"\n{msg('quit')}")
                sys.exit(0)
            except:
                print("❌ 無効な入力です")
    
    def success_effect(self, chosen_letter):
        """成功時のエフェクト"""
        self.combo += 1
        
        # 爽快感のあるエフェクト
        effects = [
            "✨ TREASURE! ✨",
            "🔥 GREAT FIND! 🔥", 
            "⚡ AMAZING! ⚡",
            "💫 PERFECT! 💫",
            "🌟 LEGENDARY! 🌟"
        ]
        
        effect = effects[min(self.combo - 1, len(effects) - 1)]
        
        print(f"\n{effect}")
        print(f"COMBO x{self.combo}")
        
        # スコア計算（ステージとコンボボーナス付き）
        base_points = 100 * self.stage  # ステージが上がるほど高得点
        combo_bonus = self.combo * 50
        total_points = base_points + combo_bonus
        
        self.score += total_points
        
        # スコアアニメーション
        print(f"+{total_points} points!")
        time.sleep(1.5)
        
    def death_scene(self, chosen_letter, hazure_letters):
        self.clear_screen()
        self.print_logo(is_death=True)
        
        print(f"{msg('death_msg1')} '{chosen_letter}'{msg('death_msg2')}")
        time.sleep(2)
        
        print(f"\n{msg('death_letters')}: {', '.join(hazure_letters)}")
        print(f"\nGAME OVER")
        
        # ハイスコア更新
        if self.score > self.high_score:
            print(f"🎉 {msg('new_high_score')} 🎉")
            self.high_score = self.score
            save_high_score(self.high_score)
        
        print(f"FINAL SCORE: {self.score:,}")
        print(f"HIGH SCORE: {self.high_score:,}")
        print(f"REACHED STAGE: {self.stage}")
        print(f"MAX COMBO: {self.combo}")
        
        # 評価
        if self.stage > 5:
            print("🏆 TREASURE MASTER!")
        elif self.stage == 5:
            print("🥇 EXPERT HUNTER!")
        elif self.stage >= 3:
            print("🥈 SKILLED EXPLORER!")
        elif self.stage >= 2:
            print("🥉 BRAVE ADVENTURER!")
        else:
            print("🔰 NOVICE SEEKER!")
        
    def show_game_over_options(self):
        print("\nENTER: もう一度プレイ | X: 終了")
        
        while True:
            try:
                choice = input().strip().upper()
                if choice == '' or choice == 'Y':
                    return True
                elif choice == 'X':
                    return False
            except KeyboardInterrupt:
                return False
        
    def play_round(self):
        """1ステージをプレイ"""
        # ステージクリアチェック
        if self.stage > self.max_stage:
            # 全ステージクリア！
            self.score += 5000
            print(f"\n🎉 {msg('perfect')} 🎉")
            print("+5000 BONUS!")
            time.sleep(2)
            
            # 新しいゲーム開始
            self.stage = 1
            self.chosen_letters = []
            return True
            
        # QWERTの5文字を取得
        choices = self.get_qwert_choices()
        
        # ハズレの数を決定
        if self.stage <= 4:
            num_hazure = 1  # 1-4ステージは1個のハズレ
        else:
            num_hazure = 4  # 5ステージ目は4個のハズレ
            
        hazure_letters = self.generate_hazure(choices, num_hazure)
        
        # 選択肢表示と入力取得
        choice = self.display_and_get_choice(choices, hazure_letters)
        
        if choice in hazure_letters:
            self.death_scene(choice, hazure_letters)
            self.alive = False
            return False
        else:
            self.chosen_letters.append(choice)
            self.success_effect(choice)
            self.stage += 1  # 次のステージへ
            return True
            
    def play(self):
        self.horror_intro()
        
        while self.alive:
            if not self.play_round():
                break
                
        # ゲームオーバー後の選択
        if self.show_game_over_options():
            self.__init__()  # リセット
            self.play()
        else:
            print(f"\n{msg('quit')}")
            sys.exit(0)

if __name__ == "__main__":
    game = HorrorAlphabetGame()
    game.play()
