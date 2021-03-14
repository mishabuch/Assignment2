import decimal
from itertools import product

import matplotlib.pyplot as plt
import pandas as pd


plt.title('NN-GA: Iterations vs Fitness')
for CE in [0.15,0.35,0.55,0.70,0.75,0.80,0.85,0.95]:
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/NN/SA_{}_LOG.csv'.format(CE))
    plt.plot(df.loc[:, "iteration"], df.loc[:, "acc_tst"], label='CE={}'.format(CE))

plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Fitness')
plt.show(block=False)
plt.show()

plt.title('NN-GA: Time Taken')
for CE in [0.15,0.35,0.55,0.70,0.75,0.80,0.85,0.95]:
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/NN/SA_{}_LOG.csv'.format(CE))
    plt.plot(df.loc[:, "iteration"], df.loc[:, "elapsed"], label='CE={}'.format(CE))

plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Time Taken in ms')
plt.show(block=False)
plt.show()