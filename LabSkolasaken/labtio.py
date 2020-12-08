from stockfish import Stockfish
stockfish = Stockfish("\Users\Sami\Documents\stockfish_12_win_x64-1")

{
    "Write Debug Log": "false",
    "Contempt": 0,
    "Min Split Depth": 0,
    "Threads": 1,
    "Ponder": "false",
    "Hash": 16,
    "MultiPV": 1,
    "Skill Level": 20,
    "Move Overhead": 30,
    "Minimum Thinking Time": 20,
    "Slow Mover": 80,
    "UCI_Chess960": "false",
}

stockfish.get_best_move()
stockfish.get_board_visual()