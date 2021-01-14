# Challenge: Battling Knights
## The Rules

### Knights and Arena

There are four knights who are about to do battle:
1. RED (R)
2. BLUE (B)
3. GREEN (G)
4. YELLOW (Y)

Their world consists of an 8x8 square "Arena" which looks suspiciously like a chess-board.
The Arena is surrounded by water on all sides.

The 64 tiles on the board are identified with (row, col) coordinates with (0,0) being the top left tile and (7,0) being the botten left tile (row 7 col 0).

Each knight starts in one corner of the board:
1. R (0,0) (top left)
2. B (7,0) (bottom left)
3. G (7,7) (bottom right)
4.  Y (0,7) (top right)

### Items

Around the board are the following four items:
1. Axe (A): +2 Attack
2. MagicStaff (M): +1 Attack, +1 Defence
3. Dagger (D): +1 Attack
4. Helmet (H): +1 Defence

They start in the following locations:
1. Axe (A) (2,2)
2. MagicStaff (M) (5,2)
3. Dagger (D) (2,5)
4. Helmet (H) (5,5)

If a Knight moves onto a tile with an item they are immediately equipped with that item, gaining the bonus.
A knight may only hold one item.
If a knight moves onto a tile which has two items on it then they pick up the best item in this order: (A, M, D, H).
Knights will pick up an item on a tile before fighting any enemies on that tile.
Knights that die in battle drop their item (if they have one).
Knights that drown throw their item to the bank before sinking down to Davy Jones' Locker - the item is left on the last valid tile.

### Movement

Each knight moves one tile at a time in one of four directions:
1. North (N) (UP)
2. East (E) (RIGHT)
3. South (S) (DOWN)
4. West (W) (LEFT)

If a knight moves off the board then they are swept away and drown immediately.
Further moves do not apply to DROWNED knights.
The final position of a DROWNED knight is null.

### Fighting

Each knight has a base attack and defence score of 1:
* Attack (1)
* Defence (1)

If one knight moves onto the tile of another knight then they will attack.
The knight already on the tile will defend.

The outcome of a fight it determined as follows:
* The attacker takes their base attack score and adds any item modifiers.
* The attacker adds 0.5 to their attack score (for the element of surprise).
* The defender takes their base defence score and adds any item modifiers.
* The attacker's final attack score is compared to the defender's final defence score.
* The higher score wins, the losing knight dies.

DEAD knights drop any equipped items immediately.
Further moves do not apply to DEAD knights.
The final position of a DEAD knight is the tile that they die on.

A DEAD or DROWNED knight has attack 0 and defence 0.

### Game

The initial state of the board looks like this:
 _ _ _ _ _ _ _ _
|R|_|_|_|_|_|_|Y|
|_|_|_|_|_|_|_|_|
|_|_|A|_|_|D|_|_|
|_|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|_|
|_|_|M|_|_|H|_|_|
|_|_|_|_|_|_|_|_|
|B|_|_|_|_|_|_|G|

You are supplied a list of movements in the following format:
  GAME-START
  <Kinght>:<Direction>
  <Kinght>:<Direction>
  <Kinght>:<Direction>
  .
  .
  .
  GAME-END

For example:
  GAME-START
  R:S
  R:S
  B:E
  G:N
  Y:N
  GAME-END

After these four movements the board would look like this (lowercase denotes a DEAD or DROWNED knight):
_ _ _ _ _ _ _ (y)
|_|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|_|
|R|_|A|_|_|D|_|_|
|_|_|_|_|_|_|_|_|
|_|_|_|_|_|_|_|_|
|_|_|M|_|_|H|_|_|
|_|_|_|_|_|_|_|G|
|_|B|_|_|_|_|_|_|

### Instructions

Your code should open a file called `moves.txt` and, if the contents are a valid set of moves, determine the final state of the board.
The output should be a JSON file called `final_state.json` with the following information:
* Position of the knights
* Status of the kights (LIVE, DEAD, DROWNED)
* Attack of each knight (including weapons but not surprise bonus)
* Defence of each knight (including weapons)
* Position of the items (and whether they are held by a knight or not)

The format should be as follows:
{
"red": [<R position>,<R status>,<R item (null if no item)>,R Attack,<R Defence>],
"blue": [<B position>,<B status>,<B item (null if no item)>,B Attack,<B Defence>],
"green": [<G position>,<G status>,<G item (null if no item)>,G Attack,<G Defence>],
"yellow": [<Y position>,<Y status>,<Y item (null if no item)>,Y Attack,<Y Defence>],
"magic_staff": [<M position>,<M equipped>],
"helmet": [<H position>,<H equipped>],
"dagger": [<D position>,<D equipped>],
"axe": [<A position>,<A equipped>],
}

The output for the final board in the example above should therefore be:
{
"red": [[2,0],"LIVE",null,1,1],
"blue": [[7,1],"LIVE",null,1,1],
"green": [[6,7],"LIVE",null,1,1],
"yellow": [null,"DROWNED",null,0,0],
"magic_staff": [[5,2],false],
"helmet": [[5,5],false],
"dagger": [[2,5],false],
"axe": [[2,2],false]
}

Please include a README with your final solution detailing how to use the code you write to determine the output of an instruction.
