# Rhythm

A simple rhythm game prototype written in Python. The repository now includes placeholder directories for final art, music, and sound effects as well as a minimal game script that supports scoring, combo tracking, and difficulty settings.

## Game Roadmap

1. **Pre-production**
   - Define the core concept and gameplay goals.
   - Select tools and technologies for development.
   - Outline initial art and audio direction.

2. **Prototype**
   - Implement a minimal playable prototype focusing on the beat-matching mechanic.
   - Integrate placeholder assets for quick iteration.
   - Validate the fun factor through early testing.

3. **Production**
   - Create final art, music, and sound effects (see `assets/`).
   - Expand level content and refine game mechanics.
   - Implement scoring, combos, and difficulty settings.

4. **Testing**
   - Conduct internal playtesting to polish gameplay.
   - Fix bugs and optimize performance across target platforms.

5. **Launch**
   - Prepare marketing material and publish the game.
   - Gather player feedback and monitor stability.

6. **Post-launch**
   - Release updates with new songs and features.
   - Continue community engagement and support.

## Gameplay Loop

- Built around short rhythm mini-games similar to **Rhythm Heaven**.
- Each stage opens with a quick practice so players learn the rhythm.
- Tap or press buttons in sync with the beat during the main section.
- Accuracy is graded as *Perfect*, *Good*, or *Miss* and rolled into a final rank.
- Results show ranks like "Superb," "OK," or "Try Again," unlocking the next stage when cleared.

## Directory Overview

- `src/` – Contains the Python prototype. Run `python src/main.py levels/level1.json` to play.
- `assets/art/`, `assets/music/`, `assets/sfx/` – Placeholders for final game assets.
- `levels/` – JSON files describing beat timings and level metadata.
