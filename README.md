# RubiksCube
Main scripts used to create a rigged Rubik's Cube

CheckBBoxNode.py (plugin):

(I created boxes to define different areas corresponding to the Rubik's Cube's sections.)
The node is used to determine whether a joint is in a box by comparing the bounding box and position values.

RubikCube.py (script to run once):

This script creates a script job and a script node to run when the scene opens.
The script job is run each time the selection changes.
If a controller is selected :

  -All joints in controllers hierarchies are moved back to their offset groups
  
  -Check all corresponding CheckBBoxNodes to identify nearby joints
  
  -Parents concerned joints to the controller
