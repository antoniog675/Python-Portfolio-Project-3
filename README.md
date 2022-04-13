# BATTLESHIPS

<p>BATTLESHIPS is a terminal game created using Python and deployed on Heroku</p>
<p>This is a very basic version of the actual game, 1 ship takes up 1 point of the board, user will play against the computer, scores will be tracked for the user and a winner is decided when all ships are hit or if user and computer run out of turns.
<!-- Add image of deployed game with a live link-->

## How the game works
<hr>
<ol>
<li>As soon as game is loaded it will greet the player and ask for their name.</li>
<li>It will then ask them if they are ready to play and if player enter 'Y' the boards will be loaded and ships positions will be placed for them, on the users board the ships are going to be marked as 'X'</li>
<li>Players will have 10 guesses to hit the computers 5 ships, winner at the end of all the turns is the one with the most hit ships, if the player or computer hit all 5 ships first then they will be the winner.</li>
<li>The question "Guess a battleship location" will appear with "Enter the row of the ship 1-6" input straight after, players will need to put a value between 1-6, after a valid input is put players will need to input a letter between A-F on the "Enter the column of the ship A-F" for another input</li>
<li>After this is done computer will take a guess as well, both locations guessed by the computer and user will be processed, it will return a message stating whether the user hit, missed or guessed already, and will also state whether the computer hit or missed the users ship.
If user already guessed the location the game will not continue until it enters a new location.</li>
<li>After this is done players will be asked if they wish to continue, if 'Y' the board with updated locations will be uploaded, if users enter 'N' then the game will exit instantly and state "GAME OVER"</li>
<li>When game continues the new board will be loaded with '~' for a missed target by either player, 'X' on the computers board if user hit the computers battleship and a '*' on players board if the computer hit the players board.</li>
<li>User will need to guess a new location and this process will be repeated until player or computer hits all ships first, or if they run out of turns the player with the highest hit ship count will win!</li>
<li>Game will state the winner and exit the game</li>
</ol>

## Features


