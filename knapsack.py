import sys
import os
import csv

sys.path.append("/assignment2/ABAGAIL.jar")
import java.io.FileReader
import java.io.File as File
import java.lang.String as String
import java.lang.StringBuffer as StringBuffer
import java.lang.Boolean as Boolean
import java.util.Random as Random
from time import clock
from itertools import product
import time

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import dist.DiscretePermutationDistribution as DiscretePermutationDistribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FourPeaksEvaluationFunction as FourPeaksEvaluationFunction
import opt.ga.CrossoverFunction as CrossoverFunction
import opt.ga.SingleCrossOver as SingleCrossOver
import opt.ga.DiscreteChangeOneMutation as DiscreteChangeOneMutation
import opt.ga.GenericGeneticAlgorithmProblem as GenericGeneticAlgorithmProblem
import opt.ga.GeneticAlgorithmProblem as GeneticAlgorithmProblem
import opt.ga.MutationFunction as MutationFunction
import opt.ga.StandardGeneticAlgorithm as StandardGeneticAlgorithm
import opt.ga.UniformCrossOver as UniformCrossOver
import opt.prob.GenericProbabilisticOptimizationProblem as GenericProbabilisticOptimizationProblem
import opt.prob.MIMIC as MIMIC
import opt.prob.ProbabilisticOptimizationProblem as ProbabilisticOptimizationProblem
import shared.FixedIterationTrainer as FixedIterationTrainer
import opt.SwapNeighbor as SwapNeighbor
import opt.ga.SwapMutation as SwapMutation
import shared.Instance as Instance
import util.ABAGAILArrays as ABAGAILArrays
import opt.example.KnapsackEvaluationFunction as KnapsackEvaluationFunction

from array import array
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

def train(alg_func, ef, iters, filename):
    #ef.resetFunctionEvaluationCount()
    fit = FixedIterationTrainer(alg_func,10)
    times =[0]
    with open(filename, "a") as results:
        writer= csv.writer(results, delimiter=',')
        for i in range(0,iters,10):
            start = clock()
            fit.train()
            elapsed = time.clock()-start
            times.append(times[-1]+elapsed)
            writer.writerow([i, times[-1],ef.value(alg_func.getOptimal())])
            
    sum = 0;
    for i in range(len(times)):
        sum = sum + times[i];
    average = sum / len(times);
            
    print filename + ": " + str(ef.value(alg_func.getOptimal()))
    print "Function Evaluations: " + str(ef.getFunctionEvaluations()-iters)
    print "Iters: " + str(iters)
    print "Average Time taken:{}".format(average)
    print "----------------"

def mimic_analysis(alg_func,pop,mate,mutate, ef, iters, filename):
    #ef.resetFunctionEvaluationCount()
    fit = FixedIterationTrainer(alg_func,10)
    times =[0]
    with open(filename, "a") as results:
        writer= csv.writer(results, delimiter=',')
        for i in range(0,iters,10):
            start = clock()
            fit.train()
            elapsed = time.clock()-start
            times.append(times[-1]+elapsed)
            writer.writerow([i,pop,mate,mutate, times[-1],ef.value(alg_func.getOptimal())])
            
    sum = 0;
    for i in range(len(times)):
        sum = sum + times[i];
    average = sum / len(times);
            
    print filename + ": " + str(ef.value(alg_func.getOptimal()))
    print "pop,mate,mutate :{},{},{}".format(pop,mate,mutate)
    print "Average Time taken:{}".format(average)
    print "----------------"

random = Random()
# The number of items
NUM_ITEMS = 40
# The number of copies each
COPIES_EACH = 4
# The maximum weight for a single element
MAX_WEIGHT = 50
# The maximum volume for a single element
MAX_VOLUME = 50
# The volume of the knapsack 
KNAPSACK_VOLUME = MAX_VOLUME * NUM_ITEMS * COPIES_EACH * .4

# create copies
fill = [COPIES_EACH] * NUM_ITEMS
copies = array('i', fill)

# create weights and volumes
fill = [0] * NUM_ITEMS
weights = array('d', fill)
volumes = array('d', fill)
for i in range(0, NUM_ITEMS):
    weights[i] = random.nextDouble() * MAX_WEIGHT
    volumes[i] = random.nextDouble() * MAX_VOLUME


# create range
fill = [COPIES_EACH + 1] * NUM_ITEMS
ranges = array('i', fill)
trials=5
maxIters=5001
ef = KnapsackEvaluationFunction(weights, volumes, KNAPSACK_VOLUME, copies)
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = UniformCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
"""
output_file = './Knapsack/{}/Knapsack_{}_{}_LOG.csv'
# Randomized Hill Climbing
rhc = RandomizedHillClimbing(hcp)
for i in range(trials):
    fname = output_file.format('RHC','RHC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(rhc, ef, maxIters, fname)

sa = SimulatedAnnealing(100, .95, hcp)
for i in range(trials):
    fname = output_file.format('SA','SA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(sa, ef, maxIters, fname)
    
ga = StandardGeneticAlgorithm(200, 150, 25, gap)
for i in range(trials):
    fname = output_file.format('GA','GA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(ga, ef, maxIters, fname)


mimic = MIMIC(200, 100, pop)
for i in range(trials):
    fname = output_file.format('MIMIC','MIMIC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(mimic, ef, maxIters, fname)
"""
for samples, keep, m in product([40], [20], [0.1, 0.3, 0.5, 0.7, 0.9]):
    fname = './Knapsack/MIMIC_ANALYSIS_{}_{}_{}.csv'.format(samples, keep, m)
    with open(fname, 'w') as f:
        f.write('iterations,pop,mate,mutate,time,fitness\n')
    ef = KnapsackEvaluationFunction(weights, volumes, KNAPSACK_VOLUME, copies)
    odd = DiscreteUniformDistribution(ranges)
    nf = DiscreteChangeOneNeighbor(ranges)
    mf = DiscreteChangeOneMutation(ranges)
    cf = SingleCrossOver()
    gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
    df = DiscreteDependencyTree(m, ranges)
    pop = GenericProbabilisticOptimizationProblem(ef, odd, df)
    mimic = MIMIC(samples, keep, pop)
    mimic_analysis(mimic, samples, keep, m, ef, 5000, fname)
