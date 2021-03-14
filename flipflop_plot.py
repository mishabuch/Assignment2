import decimal

import matplotlib.pyplot as plt
import pandas as pd

SA_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA/FlipFlop_SA_1_LOG.csv')
SA_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA/FlipFlop_SA_2_LOG.csv')
SA_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA/FlipFlop_SA_3_LOG.csv')
SA_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA/FlipFlop_SA_4_LOG.csv')
SA_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA/FlipFlop_SA_5_LOG.csv')

SA_1_df.add(SA_2_df)
SA_1_df.add(SA_3_df)
SA_1_df.add(SA_4_df)
SA_1_df.add(SA_5_df)
SA_1_df.divide(5.0)

GA_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/GA/FlipFlop_GA_1_LOG.csv')
GA_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/GA/FlipFlop_GA_2_LOG.csv')
GA_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/GA/FlipFlop_GA_3_LOG.csv')
GA_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/GA/FlipFlop_GA_4_LOG.csv')
GA_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/GA/FlipFlop_GA_5_LOG.csv')

GA_1_df.add(GA_2_df)
GA_1_df.add(GA_3_df)
GA_1_df.add(GA_4_df)
GA_1_df.add(GA_5_df)
GA_1_df.divide(5.0)

RHC_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/RHC/FlipFlop_RHC_1_LOG.csv')
RHC_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/RHC/FlipFlop_RHC_2_LOG.csv')
RHC_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/RHC/FlipFlop_RHC_3_LOG.csv')
RHC_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/RHC/FlipFlop_RHC_4_LOG.csv')
RHC_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/RHC/FlipFlop_RHC_5_LOG.csv')

RHC_1_df.add(RHC_2_df)
RHC_1_df.add(RHC_3_df)
RHC_1_df.add(RHC_4_df)
RHC_1_df.add(RHC_5_df)
RHC_1_df.divide(5.0)

MIMIC_1_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/MIMIC/FlipFlop_MIMIC_1_LOG.csv')
MIMIC_2_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/MIMIC/FlipFlop_MIMIC_2_LOG.csv')
MIMIC_3_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/MIMIC/FlipFlop_MIMIC_3_LOG.csv')
MIMIC_4_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/MIMIC/FlipFlop_MIMIC_4_LOG.csv')
MIMIC_5_df = pd.read_csv('/Users/amisha/eclipse-workspace/assignment2/FlipFlop/MIMIC/FlipFlop_MIMIC_5_LOG.csv')

MIMIC_1_df.add(MIMIC_2_df)
MIMIC_1_df.add(MIMIC_3_df)
MIMIC_1_df.add(MIMIC_4_df)
MIMIC_1_df.add(MIMIC_5_df)
MIMIC_1_df.divide(5.0)

plt.title('Flip Flop: Iterations vs Fitness')
plt.plot(SA_1_df.loc[:, "iterations"], SA_1_df.loc[:, "fitness"], label='SA')
plt.plot(GA_1_df.loc[:, "iterations"], GA_1_df.loc[:, "fitness"], label='GA')
plt.plot(RHC_1_df.loc[:, "iterations"], RHC_1_df.loc[:, "fitness"], label='RHC')
plt.plot(MIMIC_1_df.loc[:, "iterations"], MIMIC_1_df.loc[:, "fitness"], label='MIMIC')
plt.legend()
plt.xlabel('Iterations')
plt.ylabel('Fitness')
plt.show(block=False)
plt.show()

plt.title('Flip Flop: Iterations vs Time Taken')
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


list_cooling_factor = []
list_fitness_means = []
list_time_means = []
for x in list(float_range(0, 1.0, '0.05')):
    df = pd.read_csv(
        '/Users/amisha/eclipse-workspace/assignment2/FlipFlop/SA_COOLING_EXPONENT_ANALYSIS_1_{}.csv'.format(x))
    list_cooling_factor.append(round(df['x'].mean(), 2))
    list_fitness_means.append(df['fitness'].max())
    list_time_means.append(df['time'].mean())

plt.title('Flip Flop: CoolingFactor vs Fitness')
plt.plot(list_cooling_factor, list_fitness_means)
plt.xticks(list_cooling_factor)
plt.legend()
plt.xlabel('Cooling Factor')
plt.ylabel('Average Fitness Over 5000 iterations')
plt.show(block=False)
plt.show()

plt.title('Flip Flop: CoolingFactor vs Time Taken')
plt.plot(list_cooling_factor, list_time_means)
plt.xticks(list_cooling_factor)
plt.legend()
plt.xlabel('Cooling Factor')
plt.ylabel('Average Time Taken Over 5000 iterations (in seconds)')
plt.show(block=False)
plt.show()