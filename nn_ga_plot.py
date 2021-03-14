import decimal
from itertools import product

import matplotlib.pyplot as plt
import pandas as pd


plt.title('NN-GA: Iterations vs Fitness')
for pop, mate, mutate in product([100], [10, 30, 50], [10]):
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/NN/GA_{}_{}_{}_LOG.csv'.format(pop, mate, mutate))
    plt.plot(df.loc[:, "iteration"], df.loc[:, "acc_tst"], label='{},{},{}'.format(pop, mate, mutate))

plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Fitness')
plt.show(block=False)
plt.show()

plt.title('NN-GA: Time Taken')
for pop, mate, mutate in product([100], [10, 30, 50], [10]):
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/NN/GA_{}_{}_{}_LOG.csv'.format(pop, mate, mutate))
    plt.plot(df.loc[:, "iteration"], df.loc[:, "elapsed"], label='{},{},{}'.format(pop, mate, mutate))

plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Time Taken in ms')
plt.show(block=False)
plt.show()