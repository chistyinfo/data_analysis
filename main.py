import numpy as np
import matplotlib.pyplot as plt

#
X = 25.1  # which price i bought
S = np.linspace(13, 30, 10)  # low and high price of the item
PayoffLong = S-X
PayoffShort = X-S

plt.figure(figsize=[12, 8])

#
plt.subplot(1, 2, 1)
plt.plot(S, PayoffLong, label='Payoff ')
plt.axhline(y=0, xmin=0.0, xmax=1.0, color='k')
plt.title('Long Position of Beximco (Buy)')
plt.xlabel('Price Range', fontsize='xx-large')
plt.ylabel('Profit & Loss', fontsize='xx-large')
plt.legend(fontsize='xx-large')

#
plt.subplot(1, 2, 2)
plt.plot(S, PayoffShort, color='r', label='Payoff')
plt.axhline(y=0, xmin=0.0, xmax=1.0, color='k')
plt.title('Short Position of Beximco (Sell)')
plt.xlabel('Price Range', fontsize='xx-large')
plt.ylabel('Profit & Loss', fontsize='xx-large')
plt.legend(fontsize='xx-large')

plt.show()

# print(S)



