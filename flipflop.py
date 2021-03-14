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
import time

import dist.DiscreteDependencyTree as DiscreteDependencyTree
import dist.DiscreteUniformDistribution as DiscreteUniformDistribution
import dist.Distribution as Distribution
import opt.DiscreteChangeOneNeighbor as DiscreteChangeOneNeighbor
import opt.EvaluationFunction as EvaluationFunction
import opt.GenericHillClimbingProblem as GenericHillClimbingProblem
import opt.HillClimbingProblem as HillClimbingProblem
import opt.NeighborFunction as NeighborFunction
import opt.RandomizedHillClimbing as RandomizedHillClimbing
import opt.SimulatedAnnealing as SimulatedAnnealing
import opt.example.FlipFlopEvaluationFunction as FlipFlopEvaluationFunction
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
import shared.ConvergenceTrainer as ConvergenceTrainer
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
            writer.writerow([i, ef.getFunctionEvaluations()-i,times[-1],ef.value(alg_func.getOptimal())])
            
    sum = 0;
    for i in range(len(times)):
        sum = sum + times[i];
    average = sum / len(times);
            
    print filename + ": " + str(ef.value(alg_func.getOptimal()))
    print "Function Evaluations: " + str(ef.getFunctionEvaluations()-iters)
    print "Iters: " + str(iters)
    print "Average Time taken:{}".format(average)
    print "----------------"

def sa_analysis(alg_func, x, ef, iters, filename):
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
            writer.writerow([i,x, times[-1],ef.value(alg_func.getOptimal())])
            
    sum = 0;
    for i in range(len(times)):
        sum = sum + times[i];
    average = sum / len(times);
            
    print filename + ": " + str(ef.value(alg_func.getOptimal()))
    print "Cooling exponent is :{}".format(x)
    print "Average Time taken:{}".format(average)
    print "----------------"

"""
Commandline parameter(s):
   none
"""

N=1000
T=N/5
fill = [2] * N
ranges = array('i', fill)
trials = 5
maxIters=5001
ef = FlipFlopEvaluationFunction()
odd = DiscreteUniformDistribution(ranges)
nf = DiscreteChangeOneNeighbor(ranges)
mf = DiscreteChangeOneMutation(ranges)
cf = SingleCrossOver()
df = DiscreteDependencyTree(.1, ranges)
hcp = GenericHillClimbingProblem(ef, odd, nf)
gap = GenericGeneticAlgorithmProblem(ef, odd, mf, cf)
pop = GenericProbabilisticOptimizationProblem(ef, odd, df)

output_file = './FlipFlop/{}/FlipFlop_{}_{}_LOG.csv'

# Randomized Hill Climbing
rhc = RandomizedHillClimbing(hcp)
for i in range(trials):
    fname = output_file.format('RHC','RHC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,fevals,time,fitness\n')
    train(rhc, ef, maxIters, fname)

sa = SimulatedAnnealing(1E11, .95, hcp)
for i in range(trials):
    fname = output_file.format('SA','SA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,fevals,time,fitness\n')
    train(sa, ef, maxIters, fname)

ga = StandardGeneticAlgorithm(200, 100, 10, gap)
for i in range(trials):
    fname = output_file.format('GA','GA', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,fevals,time,fitness\n')
    train(ga, ef, maxIters, fname)
    
cooling_exponent=1.0    
for i in range(1):
    for x in list(float_range(0, cooling_exponent, '0.05')):
        fname = './FlipFlop/SA_COOLING_EXPONENT_ANALYSIS_{}_{}.csv'.format(str(i+1),x)
        with open(fname, 'w') as f:
            f.write('iterations,x,time,fitness\n')
        sa = SimulatedAnnealing(1E11, x, hcp)
        sa_analysis(sa, x, ef, 6000, fname)
        
mimic = MIMIC(200, 20, pop)
for i in range(trials):
    fname = output_file.format('MIMIC','MIMIC', str(i + 1))
    with open(fname, 'w') as f:
        f.write('iterations,fevals,time,fitness\n')
    train(mimic, ef, 200, fname)
