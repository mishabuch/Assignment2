import decimal
from itertools import product

import matplotlib.pyplot as plt
import pandas as pd

NN_RHC_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/NN/RHC_LOG.csv')

plt.title('NN-RHC: Iterations vs Accuracy')
plt.plot(NN_RHC_df.loc[:, "iteration"], NN_RHC_df.loc[:, "acc_trg"], label='Training Accuracy')
plt.plot(NN_RHC_df.loc[:, "iteration"], NN_RHC_df.loc[:, "acc_tst"], label='Testing Accuracy')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Accuracy')
plt.show(block=False)
plt.show()

plt.title('NN-RHC: Iterations vs MSE')
plt.plot(NN_RHC_df.loc[:, "iteration"], NN_RHC_df.loc[:, "MSE_trg"], label='Training MSE')
plt.plot(NN_RHC_df.loc[:, "iteration"], NN_RHC_df.loc[:, "MSE_tst"], label='Testing MSE')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('MSE')
plt.show(block=False)
plt.show()

plt.title('NN-RHC: Iterations vs Time Taken')
plt.plot(NN_RHC_df.loc[:, "iteration"], NN_RHC_df.loc[:, "elapsed"], label='Time Taken')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Time Taken in ms')
plt.show(block=False)
plt.show()
