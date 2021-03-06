from PIL import Image, ImageCms
import sys

if len(sys.argv) < 2:
		print("Give the filename as an argument")
filename = sys.argv[1]	
im = Image.open(filename)
if im.mode != "RGB":
  im = im.convert("RGB")

srgb_profile = ImageCms.createProfile("sRGB")
lab_profile  = ImageCms.createProfile("LAB")

rgb2lab_transform = ImageCms.buildTransformFromOpenProfiles(srgb_profile, lab_profile, "RGB", "LAB")
lab_im = ImageCms.applyTransform(im, rgb2lab_transform)
lab_im.save('worker.tiff')