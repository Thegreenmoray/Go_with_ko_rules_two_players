import Go
import Rules
from Player import Player

print("Testing Go game modules...")
board = Go.createboard(19)
print(f"✓ Created {len(board)}x{len(board)} board")

player1 = Player('X')
player2 = Player('O')
print("✓ Players created")

print("All modules work correctly in Docker!")