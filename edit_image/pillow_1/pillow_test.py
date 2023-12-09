from PIL import Image
import os
import glob

def create_gif(in_dir,out_filename):
  path_list = sorted(glob.glob(os.path.join(*[in_dir,'*'])))
  imgs = []
  alphas = []
  img_gifs = []

  for i in range(len(path_list)):
    img = Image.open(path_list[i])
    img = img.convert('RGBA')
    alpha = img.getchannel('A')
    mask = Image.eval(alpha,lambda a: 255 if a <= 128 else 0)
    img_gif = img.quantize(colors=256)
    img_gif.paste(im=255,mask=mask)

    imgs.append(img_gif)

  imgs[0].save(out_filename,
               save_all=True, append_images=imgs[1:],optimize=False,duration=200,loop=0,transparency=255,disposal=2)
  
create_gif(in_dir='input', out_filename='dotchara1_run.gif')