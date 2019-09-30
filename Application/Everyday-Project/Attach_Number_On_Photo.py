from PIL import ImageDraw,Image,ImageColor,ImageFont

def add_num(pic):
    #create a draw object
    draw = ImageDraw.Draw(pic)
    #create a font
    myfont = ImageFont.truetype('/Library/Fonts/Arial.ttf', 100)

    fillcolor = ImageColor.getrgb("rgb(255,0,0)")
    width,height = pic.size
    draw.text((width-70,0), '7', font=myfont, fill=fillcolor)

    pic.save('result.jpg', 'jpeg')
    return 0

if __name__ == "__main__":
    photo = Image.open('ronaldo-7.jpg')
    add_num(photo)
