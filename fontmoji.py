from PIL import Image, ImageFont, ImageDraw

herb = "\U0001F33F"
pretzel = u"\U0001F968"

emoji = pretzel


def emojize(cfg, fnt):
    size = cfg["size"]
    offset = cfg["offset"]
    c = cfg["c"]
    
    width = (109 + 27) * size[0]
    height = 109 * (1 + 5 + 1) + 20 * 6
    img = Image.new("RGBA", (width, height), (256, 256, 256, 256))
    draw = ImageDraw.Draw(img)
    
    for i in range(size[1]):
        line = ""
        cur = c[i]
        for j in cur:
            if j == "x":
                line += emoji
            else:
                line += " "
        draw.text((0, 109 + (109 + 20) * i), line, fill = (256, 256, 256), embedded_color=True, font = fnt)
    return img

def concat(imgs):
    width = sum([im.width for im in imgs])
    dst = Image.new('RGB', (width, imgs[0].height))
    w = 0
    for i in imgs:
        dst.paste(i, (w, 0))
        w += i.width
    return dst

if __name__ == "__main__":
    font = "./NotoColorEmoji.ttf"
    size = 109
    space = 27

    fnt = ImageFont.truetype(font, size=size, layout_engine=ImageFont.LAYOUT_RAQM)
    im = Image.new("RGBA", (800, 700), (256, 256, 256, 256))


    cfg1 = {"size": (3,5), "offset": 0, "c": ["xxx", "qxq", "qxq", "qxq", "xxx"]}
    cfg2 = {"size": (5,5), "offset": 0, "c": ["xqqqx", "xxqxx", "xqxqx", "xqqqx", "xqqqx"]}
    cfga = {"size": (5,5), "offset": 0, "c": ["qqxqq", "qxqxq", "qxqxq", "xxxxx", "xqqqx"]}
    #cfg = {"size":(1, 2), "offset": 0, "c": ["x", "x"]}
    buf = Image.new("RGBA", (50, (109 * 7 + 20 * 6)), (256, 256, 256, 256))
    img1 = emojize(cfg1, fnt)
    img2 = emojize(cfg2, fnt)
    imga = emojize(cfga, fnt)
    
    concat([img1, buf, img2, buf, img2]).save("out.png")
