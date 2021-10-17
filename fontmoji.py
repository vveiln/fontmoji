import json
from PIL import Image, ImageFont, ImageDraw

# some emoji codes
herb = '\U0001F33F'
pretzel = '\U0001F968'
peach = '\U0001f351'

FONT_FILE = './NotoColorEmoji.ttf'
FONT_SIZE = 109
FONT = ImageFont.truetype(FONT_FILE, size=FONT_SIZE, layout_engine=ImageFont.LAYOUT_RAQM)

EMOJI = peach

# each emoji letter contains 7 emoji lines,
#the first and the last lines are used for superscripts and subscripts
LETTER_HEIGHT = 7 
EMOJI_DISTANCE = 27

LINE_DISTANCE = 20
LINE_HEIGHT = FONT_SIZE * LETTER_HEIGHT + LINE_DISTANCE * (LETTER_HEIGHT - 1)

BACKGROUND_COLOR = (256, 256, 256, 256) #white
#BACKGROUND_COLOR = (0, 0, 0, 256)

LETTER_DISTANCE_WIDTH = EMOJI_DISTANCE * 3
LETTER_DISTANCE = Image.new('RGBA', (LETTER_DISTANCE_WIDTH, LINE_HEIGHT), BACKGROUND_COLOR)

def emojize_letter(cfg):    
    desc = cfg['desc']
    assert(len(desc) == LETTER_HEIGHT)

    columns = cfg['columns']
    width = (FONT_SIZE + EMOJI_DISTANCE) * columns
    img = Image.new('RGBA', (width, LINE_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(img)
    
    for i in range(LETTER_HEIGHT):
        line = ''
        row = desc[i]
        assert(len(row) == columns)
        for j in row:
            if j == 'x':
                line += EMOJI
            else:
                line += ' '
        LINE_SHIFT = (FONT_SIZE + LINE_DISTANCE) * i
        draw.text((0, LINE_SHIFT), line, fill = BACKGROUND_COLOR, embedded_color=True, font = FONT)
    return img

def concat(imgs):
    width = sum([im.width for im in imgs]) + LETTER_DISTANCE_WIDTH * (len(imgs) + 1)
    dst = Image.new('RGBA', (width, imgs[0].height), BACKGROUND_COLOR)
    dst.paste(LETTER_DISTANCE, (0, 0))
    w = LETTER_DISTANCE_WIDTH
    for i in imgs:
        dst.paste(i, (w, 0))
        dst.paste(LETTER_DISTANCE,(w + i.width, 0))
        w += i.width + LETTER_DISTANCE_WIDTH
    return dst

def concat_lines(imgs):
    height = sum([im.height for im in imgs])
    dst = Image.new('RGBA', (max([i.width for i in imgs]), height), BACKGROUND_COLOR)
    h = 0
    for i in imgs:
        dst.paste(i, (0, h))
        h += i.height
    return dst

def emojize(sentence):
    with open('./letters.json', 'r') as f:
        cfg = json.load(f)
    
    lines = [concat([emojize_letter(cfg[l]) for l in phrase]) for phrase in sentence.upper().split('\n')]
    img = concat_lines(lines)
    return img

if __name__ == '__main__':
    sentence = 'fontmoji'
    img = emojize(sentence)
    img.save("out.png")
