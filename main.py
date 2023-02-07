import colorsys

from SortFunctions import selection_sort, quicksort, quickSortIterative, mergeSort
from SearchFunctions import binary_search_sub
from PixelFunctions import storePixels, pixels_to_image, pixels_to_point, compare_pixels, grayscale
from PIL import Image, ImageDraw


def imageManipulation(rgb):
    # getting user's desired RGB value
    # IMG_NAME = 'monkey'
    functioncall = 0

    with Image.open(IMG_NAME + '.jpg') as im:
        pixels, yiq_pixels = storePixels(im)
        # print("stored: ", len(pixels), len(yiq_pixels))  # check for equal length
        print("Processing image...")
        print("*****************************************************************")
        mergeSort(yiq_pixels, compare_pixels)
        sorted_im = pixels_to_image(im, yiq_pixels)
        print("Image sorted")
        r, g, b = rgb.split(",")[0], rgb.split(",")[1], rgb.split(",")[2]
        target = (int(r) / 255, int(g) / 255, int(b) / 255)
        yiq_target = colorsys.rgb_to_yiq(target[0], target[1], target[2])
        subi = binary_search_sub([r[0][0] for r in yiq_pixels], 0, len(yiq_pixels) - 1, yiq_target[0])
        print("target found at: ", subi)
        grayscale(im, pixels)  # original pixels turned gray

    return subi, im, yiq_pixels


# end with Image. open (IMG_NAME + ' jpg') as im:
#   *******************


def handlePixelsToPoint(im, yiq_pixels, subi, choice="nil"):
    print("handlePixels")

    if choice == "t":
        tolerance = int(len(yiq_pixels) / 4)
        if isReversed:
            subi += tolerance
        else:
            subi -= tolerance
        print("tolerance", tolerance)
        tempImg = im.copy()
        pixels_to_point(tempImg, yiq_pixels[subi:])
        return subi
    # in order give the reverse effect, there's a need to copy the image else the same im will keep being
    # affected by the if statement
    if choice == "r" and (not isReversed):
        # print("Subi is reversed")
        tempImg = im.copy()
        pixels_to_point(tempImg, yiq_pixels[:subi])
        return tempImg

    elif choice == "nil" or (choice == "r" and isReversed):
        # print("Default Subi used")
        tempImg = im.copy()
        pixels_to_point(tempImg, yiq_pixels[subi:])
        return tempImg


def main(bool_reversed, img):
    is_Reversed = bool_reversed
    imgCopy = img

    def defaultCall(rgb="183,198,144"):
        subiRes, imRes, yiq_pixelsRes = imageManipulation(rgb)

        handlePixelsToPoint(imRes, yiq_pixelsRes, subiRes, )
        # print("default call")
        return subiRes, imRes, yiq_pixelsRes,

    (subi, im, yiq_pixels) = defaultCall()
    sub_i = subi

    def getPrompt():
        user_prompt = input("Enter Q to save, R to reverse the Subi, T to modify Subi, and C to enter RGB ")
        print("choice is :", user_prompt)
        return user_prompt

    prompt_inp = getPrompt()
    if prompt_inp.lower() == "q":
        # save my image data from memory to a file
        im.save('highlighted' + IMG_NAME + '.jpg', 'JPEG')

    while prompt_inp.lower() != "q":

        if prompt_inp.lower() == "r":
            handlePixelsToPoint(im, yiq_pixels, subi, "r")
            is_Reversed = not is_Reversed
            prompt_inp = getPrompt()

        elif prompt_inp.lower() == "c":
            userRGB = input("Enter your rgb color separated by comma")
            defaultCall(userRGB)
            prompt_inp = getPrompt()
        elif prompt_inp.lower() == "t":
            sub_i = handlePixelsToPoint(im, yiq_pixels, sub_i, "t")
            prompt_inp = getPrompt()
        else:
            print("Enter a valid option")
            prompt_inp = getPrompt()


# end def main()


if __name__ == "__main__":
    global IMG_NAME
    IMG_NAME = 'monkey'
    global prompt
    global isReversed
    global sub_i
    global imageFile
    isReversed = False
    main(isReversed, imageFile)
