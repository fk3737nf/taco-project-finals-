from  PIL import Image, ImageDraw, ImageFont
#Brian Huilman ITEC 1150-60. This is my finals project code that will generate a recipe book oft taco recipe including a rondom picture of a tc and three rondmly generated recipes.

image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')    # open image

image.thumbnail((800, 800))                  # resizing image to 800 so that the image would be smaller
image.save('christine-siracusa_thumbnail.jpeg')         # saved the image and it will show

# using draw = imageDraw(image) to draw text around the image
draw = ImageDraw.Draw(image)

# going to use font= image.true type to get the font size
font = ImageFont.truetype('DejaVuSans (1).ttf', 40)  # just downloaded if from the website to get the font on my image # the font size 40

# image font type, 40

# my next step is going to be choosing draw.text to draw text around the image and going to write Rondom Taco Recipe

draw.text([10, 475],'Rondom Taco Recipe ', fill='red', font=font)     # drawing text and putting 10 47 Rondom Tco Recipe for the color is optional you can choose any color.





image.show()   # this will show the image
image.save('Rondom Taco Recipe.jpeg')  # use image.save to save my image and choose Random Taco Recipe and the name.

