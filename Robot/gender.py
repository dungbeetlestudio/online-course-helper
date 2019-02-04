from PIL import Image
import colorsys

def is_male(im):
    px = im.load()

    for x in range(im.size[0]):
        for y in range(im.size[1]):
            a = colorsys.rgb_to_hls(px[x, y][0] / 255.0, px[x, y][1] / 255.0,
                                    px[x, y][2] / 255.0)
            if a[1] > 0.7:
                continue
            #print(x,y,a[2])
            if a[2] < 0.85:
                return True
            else:
                return False


# im = Image.open('temp/2.png')
# print(is_male(im))