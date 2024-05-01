import numpy as np
import matplotlib.pyplot as plt

arrp = []; arrx = []; arry = []; x, y = 0, 0; n = 25000

transf = [(lambda x, y: (0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6)),
          (lambda x, y: (-0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44)),
          (lambda x, y: (0.20 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6)),
          (lambda x, y: (0, 0.16 * y))]

for _ in range(n):
    randk = np.random.choice(range(4), p=[0.85, 0.07, 0.07, 0.01])
    x, y = transf[randk](x, y)
    arrp.append((x, y))

for point in arrp:
    arrx.append(point[0])
    arry.append(point[1])

plt.figure(figsize=(5, 7), facecolor='lime')
plt.scatter(arrx, arry, s=1, color='darkgreen', marker='.')
plt.title('n = ' + str(n))
#plt.axis('equal')
plt.show()
