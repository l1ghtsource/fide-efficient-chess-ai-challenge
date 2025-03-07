# FIDE & Google Efficient Chess AI Challenge (Kaggle Silver Medal)

## Description

> Chess has long been a grand challenge for artificial intelligence, a proving ground for pushing the boundaries of algorithms and computational power. While advancements like AlphaZero and Stockfish engines have achieved superhuman performance, they often rely on vast resources inaccessible to most developers. This particular competition, however, introduces a fascinating twist by emphasizing efficiency and elegance in addition to raw strategic prowess. This competition aims to shift the focus from brute-force computation to elegant and efficient design. Forget massive pre-computed tables and endless search trees – we're leveling the playing field and focusing on efficiency and strategic thinking. You're challenged to devise innovative and efficient solutions to play chess against other agents, thereby further expanding the frontiers of AI research. Your exploration of novel, optimized techniques can address a growing complexity and scale of problems, like advancements in modeling and inference techniques and improvements upon traditional heuristic-based algorithms, beyond the realm of chess.

## Solution

My solution based entirely on the [Ethereal 13.00](https://github.com/AndyGrant/Ethereal) engine (ty @agethereal) with minor changes:

- removing everything when associated with nnue, tablebases, unnecessary uci functions
- 12-bit size transposition table
- disable huge pages (ty @jsday96)
- MAX_PLY = 128, MAX_MOVES = 256 (in types.h)
- -Os -s -flto compiler flags
- default 160ms delay, not increment

## What didn't work

- other uci options: ContemptDrawPenalty, ContemptComplexity 
- increment (idk why)

So, in just one evening, making minimal changes to the open source Ethereal engine could get you a silver medal. The solution weighs only 33.1 KB and does not use NNUE. Sadly, I didn't find enough time for this contest and didn't give the cfish engine the attention it deserved.
