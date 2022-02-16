# File encoding: utf8

from PIL import Image


list_a = [
r'C:\Users\강지웅\Desktop\20220214_115747.jpg',
r'C:\Users\강지웅\Desktop\20220214_115812.jpg',
]

a = Image.open(list_a[0]).transpose(Image.ROTATE_270).convert('RGB')
# a.show()
b = [Image.open(list_a[1]).transpose(Image.ROTATE_270).convert('RGB')]

list_b = [
r'C:\Users\강지웅\Desktop\20220214_115831.jpg',
r'C:\Users\강지웅\Desktop\20220214_115846.jpg',
r'C:\Users\강지웅\Desktop\20220214_115859.jpg',
r'C:\Users\강지웅\Desktop\20220214_115912.jpg',
r'C:\Users\강지웅\Desktop\20220214_115933.jpg',
r'C:\Users\강지웅\Desktop\20220214_115952.jpg'
]

list_rgb = []
for i in list_b:
    list_rgb.append(Image.open(i).transpose(Image.ROTATE_270).convert('RGB'))

list_rgb[0].save(r'C:\Users\강지웅\Desktop\test2.pdf', save_all=True, append_images=list_rgb[1:])
a.save(r'C:\Users\강지웅\Desktop\test.pdf', save_all=True, append_images=b)
