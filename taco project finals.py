from  PIL import Image, ImageDraw, ImageFont
#Brian Huilman ITEC 1150-60. This is my finals project code that will generate a recipe book oft taco recipe including a rondom picture of a tc and three rondmly generated recipes.

image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # open image

image.thumbnail((800, 800))                  # resizing image to 800 so that the image would be smaller
image.save('christine-siracusa_thumbnail.jpeg')         # saved the image and it will show


