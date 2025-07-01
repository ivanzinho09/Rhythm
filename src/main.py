import json
import time
from enum import Enum

class Difficulty(Enum):
    EASY = 'easy'
    NORMAL = 'normal'
    HARD = 'hard'

WINDOWS = {
    Difficulty.EASY: 0.5,
    Difficulty.NORMAL: 0.3,
    Difficulty.HARD: 0.15,
}

class ScoringSystem:
    def __init__(self):
        self.score = 0
        self.combo = 0
        self.max_combo = 0

    def register_hit(self, accuracy: str):
        base = {'perfect': 100, 'good': 50, 'miss': 0}[accuracy]
        if accuracy == 'miss':
            self.combo = 0
        else:
            self.combo += 1
            self.max_combo = max(self.max_combo, self.combo)
        self.score += base * max(1, self.combo)

    def __repr__(self):
        return f"Score: {self.score} | Max Combo: {self.max_combo}"

def load_level(path: str):
    with open(path) as f:
        return json.load(f)

def play_level(level_data, difficulty: Difficulty):
    beats = level_data.get('beats', [])
    timing_window = WINDOWS[difficulty]
    scoring = ScoringSystem()
    print(f"Starting level '{level_data.get('name', 'Unknown')}' on {difficulty.value}")
    start_time = time.time()
    for beat in beats:
        target = start_time + beat
        while time.time() < target:
            time.sleep(0.01)
        input_time = time.time()
        input("Hit Enter in time with the beat!")
        delta = abs(input_time - target)
        if delta <= timing_window / 2:
            scoring.register_hit('perfect')
            print('Perfect!')
        elif delta <= timing_window:
            scoring.register_hit('good')
            print('Good!')
        else:
            scoring.register_hit('miss')
            print('Miss!')
    print(scoring)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Simple rhythm game prototype')
    parser.add_argument('level', help='Path to level file')
    parser.add_argument('--difficulty', choices=[d.value for d in Difficulty], default='normal')
    args = parser.parse_args()

    level_data = load_level(args.level)
    difficulty = Difficulty(args.difficulty)
    play_level(level_data, difficulty)
