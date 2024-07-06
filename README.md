the goal is to create a python script that would automatically get the game day weather following the hex-flower path decided randomly by a 2d6 dices roll.

we need a function to : 
  + create a pseudo flower and it's logic pathes
- représenter chaque position de case par un tuple (ligne, colonne)
- créer un objet case qui contient :
  - sa position
  - ses mouvements
  - le temps associé et les infos qui y sont associées
     + is it useful to display the flower ? if it is create a way to display the flower
  
  + save current position
  + create a movement based on a 2d6 roll
  + export content associated with current position (description / rules / etc)
  + create a user interface to allow DM to force a new position


idea : use cubic position to represent the coordinates of every hex
(x, y, z)
where x represent diagonal top left to bottom right
where y represent the vertical from top to bottom
where z represent the diagonal top right to bottom left

create a file .init that contains info of every hex based on their position
coordinates (0, 0, 0) represent the center of the flower
x, y, z can range from -2 to 2

a movement can be
+ N = (1, 0, -1)
+ NE = (1, 1, 0)
+ SE = (0, 1, 1)
+ S = (-1, 0, 1)
+ SW = (-1, -1, 0)
+ NW = (0, -1, -1)

A move where x or y or z reach 3 or -3 is out of bound.
When it happens:
+ If the move is going either N or S then instead swap x and z value
+ If the move is going either NW, SW, SE, NE then
  + modified values become negative modified values and then swap modified values position
+ Some out of bound move might even be negate like going north when reaching the Ray of Hope hex