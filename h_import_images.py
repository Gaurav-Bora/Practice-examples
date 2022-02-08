from PIL import Image, ImageFilter

img = Image.open(r'C:\Users\Gaurav\OneDrive\Desktop\video edit\documents msc\compressed\adharcardG.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
print (filtered_img.save('blur.png', 'png'))
