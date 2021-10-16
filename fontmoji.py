import json
from PIL import Image, ImageFont, ImageDraw

herb = "\U0001F33F"
pretzel = u"\U0001F968"

emoji = pretzel


def emojize(cfg, fnt):
    
    c = cfg["c"]
    assert(len(c) == 7)

    width = (109 + 27) * cfg["width"]
    height = 109 * (1 + 5 + 1) + 20 * 6
    img = Image.new("RGBA", (width, height), (256, 256, 256, 256))
    draw = ImageDraw.Draw(img)
    
    for i in range(7):
        line = ""
        cur = c[i]
        assert(len(cur) == cfg["width"])
        for j in cur:
            if j == "x":
                line += emoji
            else:
                line += " "
        draw.text((0, (109 + 20) * i), line, fill = (256, 256, 256), embedded_color=True, font = fnt)
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


    cfg1 = {"width": 3, "c": ["qqq", "xxx", "qxq", "qxq", "qxq", "xxx", "qqq"]}
    cfg2 = {"width": 5, "c": ["qqqqq", "xqqqx", "xxqxx", "xqxqx", "xqqqx", "xqqqx", "qqqqq"]}
    cfga = {"width": 3, "c": ["qqq", "qxq", "xqx", "xqx", "xxx", "xqx", "qqq"]}
    cfgap = {"width": 1, "c": ["q", "x", "x", "q", "q", "q", "q"]}
    cfgcomma = {"width": 2, "c": ["qq", "qq", "qq", "qq", "qq", "xq", "xq"]}
    #cfg = {"size":(1, 2), "offset": 0, "c": ["x", "x"]}
    buf = Image.new("RGBA", (27 * 3, (109 * 7 + 20 * 6)), (256, 256, 256, 256))
    img1 = emojize(cfg1, fnt)
    img2 = emojize(cfg2, fnt)
    imga = emojize(cfga, fnt)
    imgap = emojize(cfgap, fnt)
    imgcomma = emojize(cfgcomma, fnt)
   
    with open("./letters.json", "r") as f:
        cfg = json.load(f)
    imgb = emojize(cfg["?"], fnt)


    concat([img1, buf, img2, buf, img2, buf, imga, buf, imgcomma, buf, imga, buf, imgb]).save("out.png")
