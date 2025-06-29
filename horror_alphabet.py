#!/usr/bin/env python3
import random
import time
import os
import sys
import locale

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
        'title': 'DEATH GAME Q',
        'intro1': 'You stand before cursed alphabets...',
        'intro2': 'Choose wrong and death awaits...',
        'level': 'LEVEL',
        'score': 'Score',
        'danger': 'dangerous letters hidden',
        'choose': 'Choose your fate...',
        'history': 'Your choices',
        'input': 'Choose a letter (A-Z)',
        'invalid': 'Enter A-Z letter',
        'already': 'already chosen',
        'safe': 'SAFE!',
        'death_msg1': 'You chose',
        'death_msg2': 'It was... the letter of death...',
        'game_over': 'GAME OVER',
        'final_score': 'Final Score',
        'play_again': 'Play again? (y/n)',
        'quit': 'Goodbye...'
    },
    'ja': {
        'title': 'DEATH GAME Q',
        'intro1': '呪われたアルファベットの前に立っている...',
        'intro2': '間違った文字を選べば...死が待っている...',
        'level': 'レベル',
        'score': 'スコア',
        'danger': '個の危険な文字が隠れている',
        'choose': '運命を選べ...',
        'history': 'これまでの選択',
        'input': '文字を選んでください (A-Z)',
        'invalid': 'A-Zの文字を入力してください',
        'already': 'は既に選択済みです',
        'safe': 'セーフ！',
        'death_msg1': 'あなたは',
        'death_msg2': 'それは...死の文字だった...',
        'game_over': 'ゲームオーバー',
        'final_score': '最終スコア',
        'play_again': 'もう一度プレイしますか? (y/n)',
        'quit': 'さようなら...'
    }
}

def msg(key):
    return MESSAGES.get(LANG, MESSAGES['en']).get(key, key)

class HorrorAlphabetGame:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.alive = True
        self.chosen_letters = []  # 選択済みの文字を記録
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def slow_print(self, text, delay=0.03):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()
        
    def print_death_game_q_logo(self, is_death=False):
        if is_death:
            # 赤文字のDEATH GAME Q
            logo = f"""
\033[91m██████╗ ███████╗ █████╗ ████████╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ 
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗
██║  ██║█████╗  ███████║   ██║   ███████║    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║
██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║▄▄ ██║
██████╔╝███████╗██║  ██║   ██║   ██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══▀▀═╝ \033[0m"""
        else:
            # 通常のDEATH GAME Q
            logo = f"""
██████╗ ███████╗ █████╗ ████████╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ 
██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗
██║  ██║█████╗  ███████║   ██║   ███████║    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║
██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║▄▄ ██║
██████╔╝███████╗██║  ██║   ██║   ██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝
╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚══▀▀═╝ """
        print(logo)
        
    def horror_intro(self):
        self.clear_screen()
        self.print_death_game_q_logo()
        print("=" * 80)
        print(msg('intro1'))
        print(msg('intro2'))
        print("=" * 80)
        time.sleep(2)
        
    def generate_hazure(self, num_hazure):
        """ハズレ文字を生成"""
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        return random.sample(alphabet, num_hazure)
        
    def display_alphabet(self, hazure_letters=None):
        """アルファベットを横一列で表示"""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("\n" + "=" * 80)
        
        # 横一列で表示（スペース2つに変更）
        for letter in alphabet:
            if hazure_letters and letter in hazure_letters:
                print(f"{letter}💀", end=" ")  # 死の文字
            else:
                print(f"{letter}", end="  ")    # 通常表示
        print("\n")
        
    def display_level(self, hazure_letters):
        self.clear_screen()
        # シンプルなスコア表示
        print("=" * 80)
        print(f"SCORE: {self.score:,}".center(80))
        print("=" * 80)
        print(f"⚠️  {len(hazure_letters)} {msg('danger')}")
        
        self.display_alphabet()
        print(f"🎯 {msg('choose')}")
        
        # これまでの選択を下部に表示
        if self.chosen_letters:
            print("\n" + "-" * 80)
            print(f"📋 {msg('history')}: {' → '.join(self.chosen_letters)}")
            print("-" * 80)
        
    def death_scene(self, chosen_letter, hazure_letters):
        self.chosen_letters.append(chosen_letter)  # 死の文字も記録
        self.clear_screen()
        self.print_death_game_q_logo(is_death=True)
        print("💀" * 30)
        print(f"{msg('death_msg1')} '{chosen_letter}'...")
        time.sleep(1)
        print(msg('death_msg2'))
        time.sleep(1)
        
        # 最終的なアルファベット表示（死の文字を表示）
        self.display_alphabet(hazure_letters)
        
        print()
        print(f"\033[91m{msg('game_over')}\033[0m")  # 赤文字
        print("💀" * 30)
        print(f"🏆 FINAL SCORE: {self.score:,}".center(80))
        print("💀" * 30)
        if self.score > 50000:
            print("🎉 LEGENDARY SCORE! 伝説級！")
        elif self.score > 20000:
            print("🎉 AMAZING SCORE! 素晴らしい！")
        elif self.score > 10000:
            print("👏 GREAT SCORE! なかなかのスコア！")
        elif self.score > 1000:
            print("👍 GOOD SCORE! いいスコア！")
        
    def animate_score_increase(self, old_score, new_score, points):
        """スコア加算のアニメーション"""
        print(f"\n✅ SAFE!")
        print("=" * 80)
        
        # スコア加算アニメーション
        steps = 10
        for i in range(steps + 1):
            current = old_score + (points * i // steps)
            print(f"\rSCORE: {current:,} (+{points * i // steps:,})".center(80), end="", flush=True)
            time.sleep(0.05)
        
        print(f"\rSCORE: {new_score:,} (+{points:,})".center(80))
        print("=" * 80)
    
    def success_scene(self, chosen_letter):
        self.chosen_letters.append(chosen_letter)  # 成功した文字を記録
        
        # 残り文字数をチェック
        remaining = 26 - len(self.chosen_letters)
        old_score = self.score
        
        if remaining == 1:
            # 最後の1文字でボーナス
            points = 10000
            self.score += points
            self.animate_score_increase(old_score, self.score, points)
            print(f"🎉 PERFECT! 最後の1文字まで生き残った！")
            print(f"🔄 新しいゲームが始まります...")
            time.sleep(1.5)
            # リセットして継続
            self.chosen_letters = []
        else:
            # 通常のスコア加算（残り文字が少ないほど高得点）
            points = max(10, (27 - remaining) * 5)
            self.score += points
            self.animate_score_increase(old_score, self.score, points)
            # 待機時間なしで即座に次へ
        
    def generate_hazure(self, num_hazure):
        """ハズレ文字を生成（選択済み文字を除外）"""
        alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        available = [letter for letter in alphabet if letter not in self.chosen_letters]
        return random.sample(available, min(num_hazure, len(available)))
        
    def play_level(self):
        # 残り文字数に応じてハズレ数を調整
        remaining = 26 - len(self.chosen_letters)
        if remaining <= 1:
            return  # ゲーム終了
            
        # 残り文字が少ないほど危険度アップ
        if remaining > 20:
            num_hazure = 2
        elif remaining > 15:
            num_hazure = 3
        elif remaining > 10:
            num_hazure = 4
        elif remaining > 5:
            num_hazure = 5
        else:
            num_hazure = max(1, remaining // 2)
            
        hazure_letters = self.generate_hazure(num_hazure)
        
        self.display_level(hazure_letters)
        
        while True:
            try:
                choice = input("\n> ").upper().strip()
                if len(choice) != 1 or choice not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    print(f"❌ {msg('invalid')}")
                    continue
                if choice in self.chosen_letters:
                    print(f"❌ '{choice}' {msg('already')}")
                    continue
                break
            except KeyboardInterrupt:
                print(f"\n{msg('quit')}")
                sys.exit(0)
                
        if choice in hazure_letters:
            self.death_scene(choice, hazure_letters)
            self.alive = False
        else:
            self.success_scene(choice)
            
    def play(self):
        self.horror_intro()
        
        while self.alive:
            self.play_level()
            
        # ゲームオーバー後の選択（自動的にy）
        print(f"\n{msg('play_again')}: y")
        time.sleep(1)
        self.__init__()  # リセット
        self.play()

if __name__ == "__main__":
    game = HorrorAlphabetGame()
    game.play()
