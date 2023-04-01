<p align="center">
  <img src="https://github.com/RamonFCerezo/Battleship/blob/main/img/Battleship.png" alt="Battleship game screenshot" style="display: block; margin: auto;">
</p>

<p>Development of the game 'Battleship' using the Python programming language and its Numpy library. This is also an approach to Object-Oriented Programming. The game will be developed within the Python console, as it does not have its own interface.</p>

<h1>Project Structure</h1>
<p>This project consists of 4 Python executable files:</p>

<h2>1. main.py</h2> 
<p>Executable of the game, contains the presentation messages, coordinate inputs, and the main logic of the game.</p>

<h2>2. functions.py</h2>
  <ul>
    <li><strong>random_boats_generator</strong> &#8594; Creates new boats of a specified size and validates them in their board</li>
    <li><strong>list_of_contiguous</strong> &#8594; Takes the previously generated boat and returns a list with the contiguous locations of it, including the boat locations</li>
    <li><strong>boat_placing</strong> &#8594; Places the new boat in the board depending on the player, replacing the empty space for an "O" in the index of the np.array</li>
    <li><strong>shoot</strong> &#8594; Function that allows both players to shoot one spot of the opponent's board. If the shot hits a boat, the player who did it keeps the turn. Otherwise, it will change. Will print the both shots and boats board in each turn</li>
  </ul>
  <h2><strong>3. classes.py</strong></h2> Class for every boat, that requires the length of the boat and the player as an input, and with that information it calls the functions of functions.py to create the boats in the right places, and place them on the boards
  <h2><strong>4. variables.py</strong></h2> Between the variables, we set three boards (player boats, player shots and cpu shots), both empty lists of boats, the number of lives that decrease every time a shot finds a rival's boat, and a boolean to define the turn.

<h1>How to play</h1>
<p>After executing main.py file, it automatically will place your 10 boats (1 with size 4, 2 with size 3, 3 with size 2 and 4 with size 1) and the 10 boats of the cpu. None of them will be next to other boat. Then, you will be asked to introduce the coordinates x and y to shoot towards the opponent board. If you touch a boat, then you keep the turn, if you fail, then cpu will attack. 
Game will finish when, either you or your opponent loses all their boats (or 20 lives).

