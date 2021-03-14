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
import opt.example.TravelingSalesmanEvaluationFunction as TravelingSalesmanEvaluationFunction
import opt.example.TravelingSalesmanRouteEvaluationFunction as TravelingSalesmanRouteEvaluationFunction
import opt.SwapNeighbor as SwapNeighbor
import opt.ga.SwapMutation as SwapMutation
import opt.example.TravelingSalesmanCrossOver as TravelingSalesmanCrossOver
import opt.example.TravelingSalesmanSortEvaluationFunction as TravelingSalesmanSortEvaluationFunction
import shared.Instance as Instance
import util.ABAGAILArrays as ABAGAILArrays

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

def ga_analysis(alg_func,pop,mate,mutate, ef, iters, filename):
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


N = 50
random = Random()
trials=5

points = [[0 for x in xrange(2)] for x in xrange(N)]
for i in range(0, len(points)):
    points[i][0] = random.nextDouble()
    points[i][1] = random.nextDouble()
    
maxIters=5001
ef = TravelingSalesmanRouteEvaluationFunction(points)
odd = DiscretePermutationDistribution(N)
nf = SwapNeighbor()
mf = SwapMutation()
cf = TravelingSalesmanCrossOver(ef)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)

output_file = './TSM/{}/TSM_{}_{}_LOG.csv'
"""
# Randomized Hill Climbing
rhc = RandomizedHillClimbing(hcp)
for i in range(trials):
    fname = output_file.format('RHC','RHC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(rhc, ef, maxIters, fname)

sa = SimulatedAnnealing(1E12, .999, hcp)
for i in range(trials):
    fname = output_file.format('SA','SA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(sa, ef, maxIters, fname)

ga = StandardGeneticAlgorithm(2000, 1500, 250, gap)
for i in range(trials):
    fname = output_file.format('GA','GA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(ga, ef, maxIters, fname)


ef = TravelingSalesmanSortEvaluationFunction(points);
fill = [N] * N
ranges = array('i', fill)
odd = DiscreteUniformDistribution(ranges);
df = DiscreteDependencyTree(.1, ranges); 
pop = GenericProbabilisticOptimizationProblem(ef, odd, df);
mimic = MIMIC(500, 100, pop)
for i in range(trials):
    fname = output_file.format('MIMIC','MIMIC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,time,fitness\n')
    train(mimic, ef, 1000, fname)
"""    

for pop,mate,mutate in product([2000],[300,400,500, 600],[100,250,500, 650]):
    fname = './TSM/GA_COOLING_EXPONENT_ANALYSIS_{}_{}_{}.csv'.format(pop,mate,mutate)
    with open(fname, 'w') as f:
        f.write('iterations,pop,mate,mutate,time,fitness\n')
    ga = StandardGeneticAlgorithm(pop, mate, mutate, gap)
    ga_analysis(ga, pop,mate,mutate, ef, 5000, fname)