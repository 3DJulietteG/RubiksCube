# RubiksCube
Main scripts used to create a rigged Rubik's Cube

CheckBBoxNode.py (plugin):
I created boxes to define different areas corresponding to the Rubik's Cube's sections. 
The node is used to determine whether a joint is in a box or not by comparing the bounding box and position values.

RubikCube.py (script to run once):
This script is used to create a script job and a script node to run it when the scene opens.
The script job is run each time the selection changes.
If a controller is selected :
  -All constraint parents on joints are deleted
  -Check all corresponding CheckBBoxNodes to identify nearby joints
  -Create constraints between the controller and concerned joints
