import matplotlib.pyplot as plt
from PIL import Image

plt.rcParams['font.sans-serif'] = "SimHei"
img = Image.open("lena.tiff")

img_r ,img_g ,img_b = img.split()
plt.figure(figsize = (10,10))

plt.subplot(221)
plt.axis("off")
img_R = img.resize((50,50))
img_R1 = img_R.convert("L")
plt.imshow(img_R1,cmap="gray")
plt.title("R-缩放",fontsize = 14)

plt.subplot(222)
img_G2 = img.transpose(Image.FLIP_LEFT_RIGHT)
img_G2 = img.convert("L")
img_G1 = img_G2.transpose(Image.ROTATE_270)

plt.imshow(img_G1,cmap="gray")
plt.title("G-镜像+旋转",fontsize = 14)


plt.subplot(223)
plt.axis("off")
img_B = img.convert("L")
img_B1 = img.crop((0,0,150,150))
plt.imshow(img_B1,cmap="gray")
plt.title("B-裁剪",fontsize = 14)


plt.subplot(224)
plt.axis("off")
img_rgb = Image.merge("RGB",[img_r,img_g,img_b])
plt.imshow(img_rgb)
img_rgb.save("test.png")
plt.title("RGB",fontsize = 14)


plt.show()


