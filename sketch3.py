# Import the required libraries of sketchpy as canvas
from sketchpy import canvas
# import the raw image in svg format
sk = canvas.sketch_from_svg(r"D:\2023_07_21 (1).svg")
#  print the image which you have import as raw data in svg formate with draw function(variable name.draw()).
sk.draw()

