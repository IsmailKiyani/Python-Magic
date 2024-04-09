from matplotlib import pyplot as plt
from rembg import remove
import cv2

input_path='/content/user.jpg'
output_path='/content/Output.jpg'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)

plt.imshow(cv2.cvtColor(input, cv2.COLOR_BGR2RGB))
plt.title('INPUT IMAGE')
plt.axis("off")
plt.show()

plt.im show(output)
plt.title('OUTPUT IMAGE')
plt.axis("off")
plt.show()