import imageio

filepath=['','']

images=[]

for filename in  filepath:
  images.append(imageio.imread(filename))
imageio.mimsave('Generated.gif',images,'GIF',duration=1)