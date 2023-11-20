from PIL import Image, ImageDraw, ImageFont
# create an image object
#imgObject=Image.new('RGB',(1200,800),(47, 224, 192))
imgObject=Image.open('table-3375313.jpg')
# create a font object
font_object=ImageFont.truetype('E:\\Font\\sunday-spring\\Sunday Spring.ttf',300)
# Create a drawing object
drawing_object=ImageDraw.Draw(imgObject)
# Draw the text on image
drawing_object.multiline_text((300,1200),"MV's Code Guide",fill=(255,255,255),font=font_object)
# save the image
imgObject.save('myImage.jpg')