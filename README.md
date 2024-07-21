# Malagasy Domino Game (Daomy)
Overview  
This is a traditional Malagasy-style domino game, designed for 2 or 3 players. The game can be played
in multiple rounds, but can also end after just one if some conditions are met.  

Game Setup  
- Domino Set: The game uses a standard set of 28 unique dominoes.  
- Players: 2 or 3 players can participate  
- Distribution: Each player receives 7 dominoes at random.  
- Point: Each player starts with 0 point  
- Hidden Information: Players cannot see the dominoes held by others or the remaining dominoes in the set.  

How to play  
1. Deciding which winning rules will be applied (for the whole game):  
   - Max point (mandatory): the first player to reach this amount of point wins (generally 80 or 120)  
   - Calendar day (optional): scoring an amount of points which is equal to the
day date (just the day) means victory (Example: scoring 17 points on a 17th February or any other month)  
   - Lone player(optional): the first player to reach half of the max point wins
if no other player managed to score  
   - Half of max point (mandatory): the player who scores so much points as the half
of the max point by just one round wins  
   - Double-six (optional): ending a round by placing a double-six domino ([6, 6]) means victory  

2. Starting a round:
   - For the first round, the player holding the highest double (e.g., [6, 6] > [5,5] > ...) starts
by placing this double as the first piece of the domino snake
   - Play then proceeds clockwise  

3. Placing Dominoes
   - Players take turns placing a domino at either of the domino snake  
   - Players must place a domino if he has at least one domino that can be placed
   - A domino can be placed only if one of its end matches the exposed end of the snake  
   - If a player manages to place all their 7 dominoes on the snake, no other player can place
any more dominoes.

4. Winning a round and scoring points  
   - Placing all dominoes: a player wins the round if they are the first to place all their
   dominoes on the snake.  
     - Scoring: The winner receives points equal to the sum of the values of all remaining dominoes
     held by other players. The value of a domino is the sum of the numbers on its ends.
   - No matching domino: If no player can place a domino on the snake, the round ends.
     - Scoring: 
       - each player sums the values of their remaining dominoes.
       - The player with the lowest total value wins the round and receives points equal
       to the sum of the values of the remaining dominoes from other players.
       - If two or more players tie for the lowest total value, the round is
       a draw and no points are awarded  

5. Subsequent rounds:  
   - A new round follows until one of the previously winning conditions is fulfilled  
   - In the new round, the starting player is the one following the previous round's starter,
   continuing in a circular order.