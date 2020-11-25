from PIL import Image, ImageDraw, ImageFont, FontFile

img = Image.new('RGB', (500, 300), color=(192, 52, 235))
text = "Postikortista päivää!"
ImageFont.load_path("arial.ttf")
d = ImageDraw.Draw(img)
d.text((50, 250), text, fill=(235, 128, 52))

d.polygon([(200, 100), (400, 100), (300, 250)], fill=(255, 255, 255))

d.ellipse((250, 100, 350, 200), fill = 'blue', outline ='blue')

img.save('picture123.png')