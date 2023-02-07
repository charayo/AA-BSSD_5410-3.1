from PIL import Image, ImageDraw
import colorsys


def compare_pixels(pix1, pix2):
    return pix1[0][0] < pix2[0][0]  # only comparing red values
# def compare_pixels(pix1, pix2):


def storePixels(im):
    width = int(im.size[0])
    height = int(im.size[1])

    # store pixels in a list
    pixel_array = []
    yiq_pixels = []
    for i in range(width):
        for j in range(height):
            # get r and g and b values of pixel at position
            r, g, b = im.getpixel((i, j))  # make an i,j tuple before passing
            yiq = colorsys.rgb_to_yiq(r/255, g/255, b/255)
            yiq_pixels.append([yiq, (i, j)])
            pixel_array.append([(r, g, b), (i, j)])  # store pixels in double tuple
        # end for j
    # end for i
    return pixel_array, yiq_pixels  # send array back to main
# end def storePixels(im):


def pixels_to_image(im, pixels):
    outimg = Image.new("RGB", im.size)
    # check list element 0, tuple
    if type(pixels[0][0][0]) == float:
        print("YIQ")
        yiq_out = []
        for p in pixels:
            r, g, b = colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])
            r, g, b = int(r*255), int(g*255), int(b*255)
            yiq_out.append((r, g, b))
        outimg.putdata(yiq_out)
    else:
        outimg.putdata([p[0] for p in pixels])
    # outimg.show()
    return outimg
# def pixels_to_image(im, pixels):


def pixels_to_point(im, pixels):
    # default background color is black
    for p in pixels:
        if type(p[0][0]) == float:
            im.putpixel(p[1], tuple([int(v*255) for v in colorsys.yiq_to_rgb(p[0][0], p[0][1], p[0][2])]))
        else:  # dealing with rgb
            im.putpixel(p[1], p[0])
    im.show()
# def pixels_to_point(size, pixels):


def grayscale(im, pixels):
    draw = ImageDraw.Draw(im)
    for px in pixels:
        gray_av = int((px[0][0] + px[0][1] + px[0][2]) / 3)
        draw.point(px[1], (gray_av, gray_av, gray_av))
# def grayscale(im, pixels):
