from PIL import Image, ImageFont, ImageDraw

herb = "\U0001F33F"
pretzel = u"\U0001F968"

emoji = pretzel



def i():
    size = (3, 5)
    offset = 0
    cfg = [0b111, 0b010, 0b010, 0b010, 0b111]
    

def ap():
    size = (1, 2)
    offset = 0
    cfg = [0b1, 0b1]

def comma():
    size = (1, 2)
    offset = 5
    cfg = [0b1, 0b1]


def emojize(img, cfg, fnt):
    draw = ImageDraw.Draw(img)
    size = cfg["size"]
    offset = cfg["offset"]
    c = cfg["c"]
    
    for i in range(size[1]):
        line = ""
        cur = c[i]
        for j in cur:
            if j == "x":
                line += emoji
            else:
                line += " "
        draw.text((0, 32 + (109 + 20) * i), line, fill = (256, 256, 256), embedded_color=True, font = fnt)
    img.save("out1.png")

if __name__ == "__main__":
    font = "./NotoColorEmoji.ttf"
    size = 109
    space = 27

    fnt = ImageFont.truetype(font, size=size, layout_engine=ImageFont.LAYOUT_RAQM)
    im = Image.new("RGBA", (800, 700), (256, 256, 256, 256))
    draw = ImageDraw.Draw(im)

    cfg = {"size": (3,5), "offset": 0, "c": ["xxx", "qxq", "qxq", "qxq", "xxx"]}
    cfg = {"size": (5,5), "offset": 0, "c": ["xqqqx", "xxqxx", "xqxqx", "xqqqx", "xqqqx"]}
    #cfg = {"size":(1, 2), "offset": 0, "c": ["x", "x"]}
    emojize(im, cfg, fnt)

#    draw.text((0, 32), emoji * 3, fill = (256, 256, 256), embedded_color=True, font=fnt)
#    draw.text((size + space, 32 + size + 20), emoji, fill = (256, 256, 256), embedded_color=True, font=fnt)
#    draw.text((size + space, 32 + (size + 20) * 2), emoji, fill = (256, 256, 256), embedded_color=True, font=fnt)
#    draw.text((size + space, 32 + (size + 20) * 3), emoji, fill = (256, 256, 256), embedded_color=True, font=fnt)
#    draw.text((0, 32 + (size + 20) * 4), emoji * 3, fill = (256, 256, 256), embedded_color=True, font=fnt)
#
#    im.save("./out.png")
