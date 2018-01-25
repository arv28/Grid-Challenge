# Grid-Challenge
Longest word from 8x8 grid of letters

A Python program that takes an 8x8 grid of letters and a list of words and returns the longest word from the list (ignoring case) that can be produced from the grid using the following procedure:
1. Start at any position in the grid, and use the letter at that position as the first letter in the candidate word.
2. Move to a position in the grid that would be a valid move for a knight in a game of chess, and add the letter at that position to the candidate word.
3. Repeat step 2 any number of times.

For example, if the list of words is ["algol", "fortran", "simula"] and the grid is:
```
  1 2 3 4 5 6 7 8
1 Q W E R T N U I
2 O P A A D F G H
3 T K L Z X C V B
4 N M R W F R T Y
5 U I O P A S D F
6 G H J O L Z X C
7 V B N M Q W E R
8 T Y U I O P A S
```
then the longest word from the list that can be produced using the rules is “fortran”, by starting at the ‘F’ at position (5, 4), and moving to (4, 6), then (3, 4), (1, 3), back to (3, 4) and then (4, 2) and finally (6,1). Again, note that the match is case-insensitive, and that grid positions can be reused.

Just another edit.
