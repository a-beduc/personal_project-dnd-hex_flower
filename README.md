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
