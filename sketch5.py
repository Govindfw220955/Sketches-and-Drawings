# Create new file in which we need to print sketch from our raw data image with the png file.
# Import libraries which is required for this canvas.
from sketchpy import canvas

# Import our Raw data image from our resources

jb = canvas.sketch_from_image(r"D:\1270014.png")

# Add threshold (change the quantity of black and white color)in the image which is imported from our local drive location

jb.draw(threshold=150)


