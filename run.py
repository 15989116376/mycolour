

def pic(pic_pos):
    from PIL import Image
    return_list=[]
    def RGB_to_Hex(rgb):
        RGB = rgb.split(',')  # 将RGB格式划分开来
        color = '#'
        for i in RGB:
            num = int(i)
            # 将R、G、B分别转化为16进制拼接转换并大写  hex() 函数用于将10进制整数转换成16进制，以字符串形式表示
            color += str(hex(num))[-2:].replace('x', '0').upper()
        return color

    from PIL import Image

    im = Image.open(pic_pos)

    pix_list=[]
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            pix = im.getpixel((x, y))
            pix_list.append(pix)
        return_list.append(pix_list)
    return return_list