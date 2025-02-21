from PIL import Image, ImageDraw, ImageFont

def text_to_img(text, filename):
    with Image.new("RGB", (256, 256), (0, 0, 0)) as img:
        fnt = ImageFont.truetype("Roboto-Medium.ttf", 48)

        drawing = ImageDraw.Draw(img)

        drawing.multiline_text((133, 128), text, fill=(256, 256, 256), font=fnt, anchor="mm", align="center")

        img.save(filename + ".png")

text_to_img("foo bar", "test")
