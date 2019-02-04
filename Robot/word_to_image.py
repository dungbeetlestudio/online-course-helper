from PIL import Image, ImageDraw, ImageFont
import os

def run(word,image_path):
    if os.path.exists(image_path + '.png'):
        return image_path + '.png'

    image = Image.new("RGBA",(22,22),'white')
    draw_table = ImageDraw.Draw(im=image)

    draw_table.text(xy=(0, 0), text=word, fill='#000000', font=ImageFont.truetype('./s.ttc', 22))
    image.save(image_path + '.png')  # 保存在当前路径下，格式为PNG
    image.close()
    return image_path + '.png'