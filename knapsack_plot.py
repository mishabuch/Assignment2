import decimal
from itertools import product

import matplotlib.pyplot as plt
import pandas as pd

SA_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/SA/Knapsack_SA_1_LOG.csv')
SA_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/SA/Knapsack_SA_2_LOG.csv')
SA_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/SA/Knapsack_SA_3_LOG.csv')
SA_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/SA/Knapsack_SA_4_LOG.csv')
SA_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/SA/Knapsack_SA_5_LOG.csv')

SA_1_df.add(SA_2_df)
SA_1_df.add(SA_3_df)
SA_1_df.add(SA_4_df)
SA_1_df.add(SA_5_df)
SA_1_df.divide(5.0)

GA_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/GA/Knapsack_GA_1_LOG.csv')
GA_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/GA/Knapsack_GA_2_LOG.csv')
GA_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/GA/Knapsack_GA_3_LOG.csv')
GA_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/GA/Knapsack_GA_4_LOG.csv')
GA_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/GA/Knapsack_GA_5_LOG.csv')

GA_1_df.add(GA_2_df)
GA_1_df.add(GA_3_df)
GA_1_df.add(GA_4_df)
GA_1_df.add(GA_5_df)
GA_1_df.divide(5.0)

RHC_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/RHC/Knapsack_RHC_1_LOG.csv')
RHC_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/RHC/Knapsack_RHC_2_LOG.csv')
RHC_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/RHC/Knapsack_RHC_3_LOG.csv')
RHC_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/RHC/Knapsack_RHC_4_LOG.csv')
RHC_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/RHC/Knapsack_RHC_5_LOG.csv')

RHC_1_df.add(RHC_2_df)
RHC_1_df.add(RHC_3_df)
RHC_1_df.add(RHC_4_df)
RHC_1_df.add(RHC_5_df)
RHC_1_df.divide(5.0)

MIMIC_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC/Knapsack_MIMIC_1_LOG.csv')
MIMIC_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC/Knapsack_MIMIC_2_LOG.csv')
MIMIC_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC/Knapsack_MIMIC_3_LOG.csv')
MIMIC_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC/Knapsack_MIMIC_4_LOG.csv')
MIMIC_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC/Knapsack_MIMIC_5_LOG.csv')

MIMIC_1_df.add(MIMIC_2_df)
MIMIC_1_df.add(MIMIC_3_df)
MIMIC_1_df.add(MIMIC_4_df)
MIMIC_1_df.add(MIMIC_5_df)
MIMIC_1_df.divide(5.0)

plt.title('Knapsack: Iterations vs Fitness')
plt.plot(SA_1_df.loc[:, "iterations"], SA_1_df.loc[:, "fitness"], label='SA')
plt.plot(GA_1_df.loc[:, "iterations"], GA_1_df.loc[:, "fitness"], label='GA')
plt.plot(RHC_1_df.loc[:, "iterations"], RHC_1_df.loc[:, "fitness"], label='RHC')
plt.plot(MIMIC_1_df.loc[:, "iterations"], MIMIC_1_df.loc[:, "fitness"], label='MIMIC')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Fitness')
plt.show(block=False)
plt.show()

plt.title('Knapsack: Iterations vs Time Taken')
plt.plot(SA_1_df.loc[:, "iterations"], SA_1_df.loc[:, "time"], label='SA')
plt.plot(GA_1_df.loc[:, "iterations"], GA_1_df.loc[:, "time"], label='GA')
plt.plot(RHC_1_df.loc[:, "iterations"], RHC_1_df.loc[:, "time"], label='RHC')
plt.plot(MIMIC_1_df.loc[:, "iterations"], MIMIC_1_df.loc[:, "time"], label='MIMIC')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Time Taken (in seconds)')
plt.show(block=False)
plt.show()


def float_range(start, stop, step):
    while start < stop:
        yield float(start)
        start += decimal.Decimal(step)


pop_mate_mutate_combo = []
list_fitness_means = []
list_time_means = []
for samples, keep, m in product([40], [20], [0.9, 0.7, 0.5, 0.3, 0.1]):
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/Knapsack/MIMIC_ANALYSIS_{}_{}_{}.csv'.format(samples, keep, m))
    pop_mate_mutate_combo.append('{}_{}_{}'.format(samples, keep, m))
    list_fitness_means.append(df['fitness'].mean())
    list_time_means.append(df['time'].mean())

plt.title('Knapsack: Samples,ToKeep,M vs Fitness')
plt.plot(pop_mate_mutate_combo, list_fitness_means)
plt.xticks(pop_mate_mutate_combo)
plt.legend()
plt.xlabel('Samples,ToKeep,M')
plt.ylabel('Average Fitness Over 5000 iterations')
plt.show(block=False)
plt.show()

plt.title('Knapsack: Samples,ToKeep,M vs Time Taken')
plt.plot(pop_mate_mutate_combo, list_time_means)
plt.xticks(pop_mate_mutate_combo)
plt.legend()
plt.xlabel('Samples,ToKeep,M')
plt.ylabel('Average Time Taken Over 5000 iterations (in seconds)')
plt.show(block=False)
plt.show()
