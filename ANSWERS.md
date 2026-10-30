# AI Lab – Tips & Answers (Viva Guide)

This file explains every practical in this folder, what to say if the teacher asks
"explain your code", the expected output, and the questions teachers commonly ask.

---

## Quick index

| Lab | File | Topic | Type of AI technique |
|---|---|---|---|
| 1 | `LAB1.py` | Vacuum cleaner agent | Simple reflex agent |
| 2 | `LAB2.py` | Grid navigation agent | Model-based reflex agent |
| 3 | `LAB3.py` | 8-puzzle | Informed search (A*) |
| 4 | `LAB4.py` | Tower of Hanoi | Iterative problem solving |
| 5 | `LAB5.py` | Blocks world | Uninformed search (BFS) |
| 6 | `LAB6.py` | N-Queens | Backtracking (CSP) |
| 7 | `LAB7.py` | Chatbot | Rule-based system |
| 8 | `LAB8.py` | Tic-tac-toe | Adversarial search (Minimax) |

---

## LAB 1 – Vacuum Cleaner Agent

### What the program does
There are two rooms, `A` and `B`. Each room can be `Dirty` or `Clean`. The agent
sucks if the current room is dirty, otherwise it moves to the other room. It stops
when both rooms are clean.

### Expected output
```
Suck dirt in room A
Room A is clean
Move to room B
Suck dirt in room B
Both rooms are clean
```

### Key code points
- `state` is a dictionary storing the condition of each room.
- `act(room)` is the condition–action rule (the "brain" of the agent).
- The `while "Dirty" in state.values()` loop keeps the agent working until no room is dirty.
- The function returns the new room, so the agent remembers where it is.

### Type of agent
**Simple reflex agent** – it decides only from the current percept (is this room dirty?),
using if–else condition–action rules. It does not plan ahead.

### PEAS
| Part | Answer |
|---|---|
| Performance | Clean rooms, few actions/moves, no unnecessary sucking |
| Environment | Two rooms, dirt in each room |
| Actuators | Suction motor, wheels (move left/right) |
| Sensors | Dirt sensor, location sensor |

### Likely questions

**Q. Why is this called an intelligent agent?**
Because it perceives its environment (room state) and acts on it to achieve a goal
(clean both rooms), without a human doing each step.

**Q. Is the environment fully observable?**
Yes in this program – the agent can see the state of both rooms through the `state`
dictionary.

**Q. Is it deterministic?**
Yes. The same room and same dirt state always produce the same action.

**Q. How many actions are performed?**
Three: suck A, move to B, suck B. After that both rooms are clean and the loop ends.

**Q. What if room A is already clean and B is dirty?**
The agent moves to B, sucks B, then stops. It never sucks a clean room.

**Q. Difference between simple reflex and model-based agent?**
A simple reflex agent uses only the current percept. A model-based agent keeps internal
memory/state about the world (for example, which cells it already visited).

**Q. How would you extend it to 3 or 4 rooms?**
Add the rooms to the `state` dictionary and make the move logic choose the next dirty
room instead of only toggling A/B.

**Q. What is the time complexity?**
Constant per action, O(1). For `n` rooms it is O(n) per full cleaning pass.

**Common mistake:** sucking without checking dirt first. The code now checks `state[room]`
before sucking.

---

## LAB 2 – Model-Based Grid Agent

### What the program does
A 3×3 grid:
```
S . .
X . .
. . G
```
`S` = start, `X` = obstacle, `G` = goal. The agent moves right, down, left, up
(in that priority), avoids `X`, and remembers every cell it visited so it does not
go in circles.

### Expected output
```
Current position: (0, 0)
Current position: (0, 1)
Current position: (0, 2)
Current position: (1, 2)
Current position: (2, 2)
Goal reached
Visited cells: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
```

### Key code points
- `grid` is the agent's model of the world.
- `moves` lists the four possible directions.
- `visited` is the agent's **internal memory** – this is why it is model-based.
- `moved` becomes `True` if at least one neighbour is usable; if it stays `False`, the agent is stuck.
- `0 <= nr < 3 and 0 <= nc < 3` keeps the agent inside the grid.
- `grid[nr][nc] != "X"` avoids the obstacle.
- `(nr, nc) not in visited` prevents revisiting.

### Type of agent
**Model-based reflex agent** – it keeps an internal model (`visited`) and uses it
to choose the next action.

### PEAS
| Part | Answer |
|---|---|
| Performance | Reach `G`, avoid `X`, avoid repeated cells, use fewer moves |
| Environment | 3×3 grid with start, goal and obstacle |
| Actuators | Movement in four directions |
| Sensors | Position sensor, obstacle detection |

### Likely questions

**Q. Why is this model-based and not simple reflex?**
Because it stores `visited` and makes decisions using that memory. A simple reflex agent
would only look at the current cell and could loop forever.

**Q. Does this program find the shortest path?**
Not guaranteed. It uses a fixed direction priority (right, down, left, up), so it finds
*a* path, not necessarily the shortest. To guarantee the shortest path, use BFS.

**Q. What happens if no path exists?**
The `moved` flag remains `False`, the program prints `No path found` and breaks.

**Q. Why check `(nr, nc) not in visited`?**
To stop the agent from moving back into a cell it already explored, which prevents
infinite loops.

**Q. What is the advantage of memory here?**
It avoids repeated work and helps the agent escape dead ends.

**Q. Which search algorithm would you use for the shortest path?**
BFS (uniform cost for equal step cost), or A* if a heuristic is available.

**Q. Can this grid be bigger?**
Yes, but the bounds `3` must be changed, or use `len(grid)` and `len(grid[0])`.

**Q. Is the environment fully observable?**
In this program, yes – the agent can read the whole `grid`. A real robot would only
sense nearby cells.

**Common mistake:** forgetting the boundary check, which causes `IndexError`.

---

## LAB 3 – 8-Puzzle using A*

### What the program does
Solves the 8-puzzle from a start state to the goal:
```
Start            Goal
1 2 3            1 2 3
4 0 6            4 5 6
7 5 8            7 8 0
```
`0` is the blank tile. The program prints each state on the solution path.

### Expected output
```
Steps: 2
Step 0
[1, 2, 3]
[4, 0, 6]
[7, 5, 8]

Step 1
[1, 2, 3]
[4, 5, 6]
[7, 0, 8]

Step 2
[1, 2, 3]
[4, 5, 6]
[7, 8, 0]
```

### Key code points
- `heuristic(state)` counts misplaced tiles (ignoring the blank).
- `find_blank(state)` returns the row, column of `0`.
- `to_tuple(state)` converts the list-of-lists into a tuple-of-tuples so it can be used
  as a dictionary key / set element.
- `g_cost` stores the real cost (number of moves) from start to each state.
- `parent` stores the previous state, used to rebuild the path.
- `open_list` holds states not yet expanded.
- `min(open_list, key=lambda k: g_cost[k] + heuristic(k))` picks the state with the
  smallest **f = g + h**. This is the heart of A*.
- `new_cost < g_cost[next_key]` keeps only the cheapest way to reach a state.

### A* in one line
**f(n) = g(n) + h(n)**, where `g` is the cost so far and `h` is the estimated cost to
the goal. A* always expands the node with the smallest `f`.

### Type of technique
**Informed search** – it uses a heuristic to guide the search.

### Likely questions

**Q. What is a heuristic?**
An estimate of the remaining cost from a state to the goal. Here it is the number of
misplaced tiles.

**Q. Why is the misplaced-tiles heuristic admissible?**
Because one move can fix at most one misplaced tile, so the heuristic never
overestimates the true remaining cost. An admissible heuristic guarantees A* is optimal.

**Q. What is the difference between A* and greedy best-first search?**
Greedy best-first uses only `h`. A* uses `g + h`, so it also considers the cost already
paid. A* is optimal with an admissible heuristic; greedy is not.

**Q. What is the difference between A* and BFS?**
BFS expands by depth only and ignores the goal direction. A* uses a heuristic and
usually expands far fewer states.

**Q. What is the branching factor here?**
2 to 4, depending on where the blank is: corner = 2, edge = 3, centre = 4.

**Q. What is the total number of 8-puzzle states?**
9! = 362,880 arrangements, but only half are reachable from a given start, so
181,440 solvable states.

**Q. How do you check if an 8-puzzle is solvable?**
Count inversions (pairs where a larger number appears before a smaller one, ignoring
the blank). For a 3×3 puzzle, the puzzle is solvable if the inversion count is even.
The given start has 2 inversions, so it is solvable.

**Q. What is the time and space complexity of A*?**
Exponential in the worst case, O(b^d), where `b` is the branching factor and `d` is
the solution depth. Space is also O(b^d), which is A*'s main drawback.

**Q. Why do we need `to_tuple`?**
Because lists are unhashable in Python and cannot be dictionary keys or set members.
Tuples are hashable.

**Q. Why keep `parent`?**
To reconstruct the solution path after the goal is found, by walking backwards from
goal to start.

**Q. Can the heuristic be improved?**
Yes – Manhattan distance (sum of horizontal + vertical distances of each tile) is
stronger and still admissible, so it expands fewer states.

**Q. What happens if the puzzle is unsolvable?**
`astar` returns `None` and the program prints `No solution`.

**Common mistake:** using only `heuristic` (greedy) and calling it A*. A real A* must
include `g_cost`.

---

## LAB 4 – Tower of Hanoi (Iterative)

### What the program does
Moves `n` disks from peg `A` to peg `C` using `B` as helper, one disk at a time, and
never placing a larger disk on a smaller one. It prints every move.

For `n = 3`, expected output:
```
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
Solved in 7 moves
```

### Key code points
- `pegs` is a dictionary of three lists. The last element of each list is the top disk.
- `list(range(n, 0, -1))` puts the largest disk at the bottom and smallest on top.
- `move(peg1, peg2, name1, name2)` moves the smaller top disk to the other peg.
- The four cases in `move`:
  1. `peg1` empty → move top of `peg2` to `peg1`.
  2. `peg2` empty → move top of `peg1` to `peg2`.
  3. top of `peg1` smaller → move `peg1` → `peg2`.
  4. otherwise → move `peg2` → `peg1`.
- `order` defines the repeating pair of pegs.
  - Odd `n`: `A→C`, `A→B`, `B→C`.
  - Even `n`: `A→B`, `A→C`, `B→C`.
- Total moves = `2 ** n - 1`.

### Why the even/odd order changes
The smallest disk must move in the same direction every time (clockwise for odd `n`,
anti-clockwise for even `n`). Swapping the first move between `A→C` and `A→B` achieves
this.

### Likely questions

**Q. What is the minimum number of moves?**
`2^n - 1`. For `n = 3` it is 7, for `n = 4` it is 15.

**Q. Why 2^n - 1?**
Recurrence: `T(n) = 2·T(n-1) + 1`, `T(1) = 1`. Solving gives `T(n) = 2^n - 1`.

**Q. Write the recursive solution.**
```python
def hanoi(n, source, helper, target):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    hanoi(n - 1, source, target, helper)
    print("Move disk", n, "from", source, "to", target)
    hanoi(n - 1, helper, source, target)
```

**Q. What is the time complexity?**
O(2^n), because that many moves are made.

**Q. What is the space complexity?**
O(n) for the recursion stack in the recursive version. The iterative version uses
O(n) space for the pegs.

**Q. How does the code ensure a larger disk is never placed on a smaller one?**
The `move` function compares the top disks (`peg1[-1] < peg2[-1]`) and always moves the
smaller one onto the larger one.

**Q. Why is Tower of Hanoi used in AI?**
It is a classic state-space search / planning problem: define states, legal moves, and
a goal, then find a sequence of actions.

**Q. Is the solution optimal?**
Yes, the algorithm produces exactly the minimum `2^n - 1` moves.

**Q. What if `n = 0`?**
`total_moves = 0`, so the loop does not run and it prints `Solved in 0 moves`.

**Common mistake:** swapping peg names wrongly for even `n`, which breaks the order
and can cause an invalid move or wrong destination.

---

## LAB 5 – Blocks World using BFS

### What the program does
Three blocks `A`, `B`, `C` start on the table. The goal is `A` on `B`, `B` on `C`,
and `C` on the table. BFS finds the shortest sequence of moves.

### State representation
Each state is a tuple of `(block, on)` pairs:
```python
(("A", "Table"), ("B", "Table"), ("C", "Table"))
```
`("A", "B")` means block A is on block B.

### Expected output
```
Initial State:
(('A', 'Table'), ('B', 'Table'), ('C', 'Table'))

Goal State:
(('A', 'B'), ('B', 'C'), ('C', 'Table'))

BFS Solution:
Step 1: Move A onto B
Step 2: Move B onto C
```

### Key code points
- `blocked` = blocks that have another block on top, so they are **not clear**.
- A block can move only if it is clear (`block not in blocked`).
- A block can be placed only on the table or on another **clear** block.
- `tuple(sorted(new_state))` gives every state a fixed, comparable form.
- `visited` stores states already seen.
- `deque` + `popleft()` gives O(1) queue operations.
- `path + [action]` stores the moves taken to reach a state.

### Likely questions

**Q. What is the blocks world problem?**
A planning problem where blocks can be stacked, and the agent must reach a goal
configuration using legal moves. It is a classic AI planning domain.

**Q. Why BFS and not DFS?**
BFS is complete and gives the shortest (minimum-move) solution for equal-cost moves.
DFS may find a longer solution or go down a very deep branch.

**Q. Why sort the state?**
To create a canonical representation. The same physical arrangement must always produce
the same tuple, otherwise `visited` would treat identical states as different.

**Q. Why use `deque` instead of a list?**
`list.pop(0)` is O(n) because all elements shift. `deque.popleft()` is O(1).

**Q. What is the time complexity of BFS?**
O(b^d), where `b` is the branching factor and `d` is the solution depth. Space is also
O(b^d), because BFS stores all frontier states.

**Q. Why is the solution optimal?**
BFS explores states level by level, so the first time it reaches the goal is via the
fewest moves.

**Q. What does "clear" mean?**
A block is clear if no other block is on top of it, so it can be lifted.

**Q. Why are states stored as tuples and not lists?**
Tuples are hashable and can go into a `set` (`visited`); lists cannot.

**Q. What are the legal moves?**
1. Move a clear block to the table.
2. Move a clear block onto another clear block.

**Q. Can it handle more blocks?**
Yes, the same code works for any number of blocks, but the number of states grows
very fast.

**Q. How would you make it optimal with different move costs?**
Use uniform-cost search or Dijkstra instead of BFS.

**Common mistake:** not checking whether the target block is clear; that allows
stacking on a covered block, which is illegal.

---

## LAB 6 – N-Queens using Backtracking

### What the program does
Places `N` queens on an `N×N` board so that no two queens attack each other.
It prints the first solution for 4 queens and the first solution for 8 queens.

### Expected output (4-Queens)
```
4 Queens Solution:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0
```
Then a similar 8×8 board for 8 queens.

### Key code points
- `board[row][col] = 1` means a queen is placed there.
- `is_safe(board, row, col, n)` checks three directions **to the left**:
  1. the same row, columns `0..col-1`;
  2. the upper-left diagonal;
  3. the lower-left diagonal.
- `place_queens(board, col, n)` tries every row in the current column.
- If a placement works, it recurses to the next column.
- If recursion fails, it sets `board[row][col] = 0` — this is **backtracking**.
- Base case `col >= n` means all queens are placed.

### Why only check the left side?
Queens are placed column by column from left to right. Columns to the right are still
empty, so they cannot contain a queen yet. Checking left, upper-left, and lower-left is
enough.

### Likely questions

**Q. What is backtracking?**
A systematic way of trying choices, and when a choice leads to a dead end, undoing it
and trying the next option. It is DFS with pruning.

**Q. Why is N-Queens a constraint satisfaction problem (CSP)?**
It has variables (queen positions), domains (rows), and constraints (no two queens share
a row, column, or diagonal).

**Q. How many solutions does 4-Queens have?**
2 solutions.

**Q. How many solutions does 8-Queens have?**
92 solutions, of which 12 are fundamentally different (unique up to rotation/reflection).

**Q. What is the time complexity?**
Worst case O(N!), because in the first column there are N choices, then at most N-1,
and so on. With pruning it is much faster in practice.

**Q. What is the space complexity?**
O(N^2) for the board matrix. It can be reduced to O(N) by using a 1D array where
`arr[col] = row`.

**Q. What does `board[row][col] = 0` do?**
It removes the queen when the current choice fails, so the next row can be tried.
This is the undo step of backtracking.

**Q. Why does the function return `True` immediately after a successful recursion?**
Because the problem only asks for one valid solution. To print all solutions, do not
return `True`; instead print the board and continue.

**Q. How would you print all solutions?**
```python
def place_all(board, col, n):
    if col == n:
        print_board(board, n)
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            place_all(board, col + 1, n)
            board[row][col] = 0
```

**Q. Why is the diagonal check written with `i` and `j`?**
Because a diagonal changes both row and column by 1 each step. Upper-left decreases
both; lower-left increases row and decreases column.

**Q. Difference between backtracking and brute force?**
Brute force tries every complete arrangement. Backtracking stops as soon as a partial
arrangement is invalid, so it prunes most of the search space.

**Common mistake:** checking only rows and columns and forgetting diagonals, which
allows attacking queens.

---

## LAB 7 – Rule-Based Chatbot

### What the program does
A simple chatbot that matches the user's input against predefined rules and prints a
fixed response. Typing `bye` ends the conversation.

### Sample run
```
You: hi
Bot: Hello! How can I help you?
You: what is ai
Bot: AI stands for Artificial Intelligence.
You: bye
Bot: Goodbye! Have a nice day.
```

### Key code points
- `input(...).lower().strip()` makes matching case-insensitive and removes extra spaces.
- `if / elif / else` is the rule base.
- `user in ("hello", "hi")` matches multiple keywords with one condition.
- `while True` keeps the chat running; `break` exits on `bye`.
- The final `else` handles unknown input.

### Likely questions

**Q. What is a rule-based system?**
A system that makes decisions using a fixed set of if–then rules written by a human.
It does not learn from data.

**Q. Is this machine learning?**
No. There is no training and no model. It is pure pattern matching / rule-based AI.

**Q. What are the limitations?**
- It only understands exact predefined phrases.
- It cannot handle typos or new wording.
- It does not remember context.
- It cannot learn.

**Q. How would you improve it?**
- Use a dictionary of patterns to responses.
- Add keyword matching (`if "ai" in user`).
- Add synonyms and spell correction.
- Use NLP libraries (NLTK, spaCy) or a trained model for real understanding.

**Q. Why `.lower()` and `.strip()`?**
So `"Hello "`, `"HELLO"`, and `"hello"` all match the same rule.

**Q. What type of agent is a chatbot?**
A simple reflex / rule-based agent: percept = user text, action = predefined response.

**Q. How does the loop terminate?**
When the user enters `bye`, the code prints the goodbye message and executes `break`.

**Q. Give a real-world example of a rule-based chatbot.**
Early customer-support bots, IVR menu bots, and simple FAQ bots.

**Common mistake:** forgetting `break`, which makes the bot continue after `bye`.

---

## LAB 8 – Tic-Tac-Toe using Minimax

### What the program does
Human is `X`, AI is `O`. The human enters a position 1–9. The AI uses minimax to
choose the best move. The AI never loses; the best a human can get is a draw.

### Board positions
```
1 | 2 | 3
--|---|--
4 | 5 | 6
--|---|--
7 | 8 | 9
```

### Key code points
- `board` is a flat list of 9 cells.
- `check_winner(player)` checks all 8 winning lines (3 rows, 3 columns, 2 diagonals).
- `is_draw()` is true when there is no empty cell.
- `minimax(is_max)`:
  - `O` win → `+1`
  - `X` win → `-1`
  - draw → `0`
  - AI turn (`is_max = True`) → take the **maximum** score.
  - Human turn (`is_max = False`) → take the **minimum** score.
- `ai_move()` tries every empty cell, calls minimax, and keeps the highest score.
- `human_move()` validates input and retries on bad input.
- `board[i] = " "` after recursion **undoes** the trial move.

### Likely questions

**Q. What is minimax?**
A decision algorithm for two-player zero-sum games. One player (max) tries to maximize
the score, the other (min) tries to minimize it. Both are assumed to play optimally.

**Q. Why is the AI unbeatable?**
Minimax searches the entire game tree, so it always picks a move that avoids loss.
Tic-tac-toe is small enough to search fully.

**Q. What do the scores +1, -1, 0 mean?**
`+1` = AI (`O`) wins, `-1` = human (`X`) wins, `0` = draw.

**Q. Why `-math.inf` and `math.inf`?**
They are sentinels smaller/larger than any real score, so the first move always
replaces them.

**Q. What is the time complexity?**
Up to O(9!) ≈ 362,880 leaf nodes for the full game tree, but many branches end early.
Space is O(9) recursion depth.

**Q. What is alpha-beta pruning?**
An optimization for minimax that skips branches that cannot affect the final decision.
It gives the same result faster.

**Q. Why undo `board[i] = " "`?**
Because the trial move was only for evaluation; the real board must go back to its
previous state so the next candidate move can be tested.

**Q. Why does the AI sometimes choose a non-corner move?**
Because many moves may have the same minimax score. The code keeps the first best move
it finds. All of them are equally safe.

**Q. Is this reinforcement learning?**
No. Minimax is a search algorithm with a fixed evaluation; it does not learn from
experience.

**Q. What is a zero-sum game?**
A game where one player's gain is exactly the other's loss (win/lose/draw).

**Q. How would you make the AI beatable?**
Add a difficulty level that sometimes picks a random move, or limit the search depth.

**Common mistake:** forgetting to undo the board after minimax, which corrupts the
board and produces wrong moves.

---

## General AI questions teachers ask

**Q. Define Artificial Intelligence.**
The branch of computer science that builds systems able to perform tasks that normally
require human intelligence, such as reasoning, learning, perception, and decision-making.

**Q. What is an agent?**
Anything that perceives its environment through sensors and acts on it through
actuators.

**Q. What is PEAS?**
Performance measure, Environment, Actuators, Sensors – a framework for describing an
agent.

**Q. Types of agents?**
1. Simple reflex agent
2. Model-based reflex agent
3. Goal-based agent
4. Utility-based agent
5. Learning agent

**Q. What is the difference between uninformed and informed search?**
Uninformed search (BFS, DFS, UCS) has no extra knowledge about the goal. Informed search
(A*, greedy) uses a heuristic to estimate distance to the goal.

**Q. What is a heuristic?**
A problem-specific estimate of the cost from a state to the goal. It must be admissible
(never overestimate) for A* to be optimal.

**Q. BFS vs DFS?**

| | BFS | DFS |
|---|---|---|
| Data structure | Queue | Stack (or recursion) |
| Complete | Yes (finite graph) | Not always |
| Optimal | Yes for equal costs | No |
| Memory | High | Low |

**Q. What is the difference between search and optimization?**
Search finds a sequence of actions to reach a goal. Optimization finds the best solution
among many according to a cost/objective function.

**Q. What is a CSP?**
Constraint Satisfaction Problem: variables, domains, and constraints. N-Queens,
Sudoku, and map colouring are examples.

**Q. What is adversarial search?**
Search in games where an opponent also makes moves (minimax, alpha-beta).

**Q. What is the Turing Test?**
A test of machine intelligence where a human judge chats with a machine and a human; if
the judge cannot reliably tell which is which, the machine is considered intelligent.

**Q. What are the types of AI?**
- Narrow AI (weak AI) – specialized, e.g. chatbots, recommenders.
- General AI (strong AI) – human-level across tasks (still theoretical).
- Super AI – beyond human level (hypothetical).

**Q. Applications of AI.**
Speech recognition, computer vision, recommendation systems, self-driving cars,
medical diagnosis, game playing, chatbots, robotics.

---

## Python questions teachers ask

**Q. Difference between a list and a tuple?**
Lists are mutable (`[]`), tuples are immutable (`()`). Tuples are hashable and can be
used as dictionary keys or set elements; lists cannot.

**Q. Why can't a list be a dictionary key?**
Because lists are mutable and therefore unhashable. Python needs a stable hash.

**Q. Difference between a list and a set?**
A list is ordered and allows duplicates. A set is unordered, stores unique elements,
and gives fast membership checks (`in`).

**Q. What is a dictionary?**
A collection of key–value pairs with average O(1) lookup.

**Q. What does `deque` do?**
A double-ended queue from `collections`. `append` and `popleft` are O(1), which makes it
ideal for BFS.

**Q. What is recursion?**
A function calling itself with a smaller input, until a base case stops it.

**Q. What is the base case?**
The condition that ends the recursion, e.g. `if col >= n: return True` in N-Queens.

**Q. What is the difference between `return` and `break`?**
`return` exits the function and optionally sends a value back. `break` exits only the
nearest loop.

**Q. What is `math.inf`?**
A floating-point value larger than any other number, used as an initial "best" value.

**Q. What does `f"text {var}"` do?**
It is an f-string: it inserts the value of `var` into the string.

**Q. What does `.strip()` do?**
Removes leading and trailing whitespace.

**Q. What does `enumerate` do?**
Loops with both index and value: `for step, action in enumerate(path, 1)`.

**Q. What is a lambda function?**
A small anonymous function, e.g. `lambda k: g_cost[k] + heuristic(k)`.

---

## Common errors you might see and their meaning

| Error | Meaning | Fix |
|---|---|---|
| `IndentationError` | Wrong spaces/tabs | Use 4 spaces consistently |
| `IndexError` | Accessing outside a list | Check bounds, e.g. `0 <= nr < 3` |
| `TypeError: unhashable type: 'list'` | Using a list as dict key/set item | Convert to tuple |
| `EOFError` | Input ended while `input()` was waiting | Provide enough input; not a code bug |
| `ValueError` | Wrong type passed, e.g. `int("abc")` | Validate input, use try/except |
| `RecursionError` | Recursion never reaches base case | Check the base case and recursive step |

---

## How to demo each lab quickly

```bash
python3 LAB1.py
python3 LAB2.py
python3 LAB3.py
python3 LAB4.py      # type 3 or 4
python3 LAB5.py
python3 LAB6.py
python3 LAB7.py      # type hi, what is ai, bye
python3 LAB8.py      # type 5 to start
```

### If the teacher changes the input

- **LAB1:** edit the `state` dictionary to make rooms clean/dirty.
- **LAB2:** edit `grid` (`S`, `.`, `X`, `G`) and update the bounds if the size changes.
- **LAB3:** change `start` and `goal`; make sure the puzzle is solvable.
- **LAB4:** enter a different number of disks at runtime.
- **LAB5:** change `initial_state` and `goal_state`.
- **LAB6:** change `solve(4)` / `solve(8)` to another `n`.
- **LAB7:** add another `elif` rule before the final `else`.
- **LAB8:** to let the AI move first, call `ai_move()` before the loop.

---

## One-line summary to say in the lab

- **LAB1:** "A simple reflex vacuum agent that sucks dirty rooms and moves until both rooms are clean."
- **LAB2:** "A model-based agent that navigates a grid, remembers visited cells, and avoids obstacles."
- **LAB3:** "A* search for the 8-puzzle using misplaced tiles as the heuristic."
- **LAB4:** "An iterative Tower of Hanoi solver that makes the minimum 2^n − 1 moves."
- **LAB5:** "BFS over blocks-world states to find the shortest stacking plan."
- **LAB6:** "A backtracking N-Queens solver that checks rows and diagonals before placing each queen."
- **LAB7:** "A rule-based chatbot that replies using predefined if–else patterns."
- **LAB8:** "An unbeatable tic-tac-toe AI using the minimax algorithm."
