## Assignment 1 

### Requirements:
- You would require Python 3.7, Pandas and sklearn
- An IDE which supports running Jython
- You can use Eclipse, with PyDev installed from the market place.
- Plotting code is in Python 3.7, Pandas and matplotlib

#### You can find the Code here:
https://github.com/mishabuch/Assignment2

1) This project uses the ABAGAIL library from Pushkar's git repo, located in the ABAGAIL folder.
----To run the project, you must first do:
1. Create folders 
FlipFlop/GA, - log files for results for Flipflop with GA
FlipFlop/SA, - log files for results for Flipflop with SA
FlipFlop/RHC,- log files for results for Flipflop with RHC
FlipFlop/MIMIC, - log files for results for Flipflop with MIMIC
Knapsack/GA, - log files for results for Knapsack with GA
Knapsack/SA, - log files for results for Knapsack with SA
Knapsack/RHC,- log files for results for Knapsack with RHC
Knapsack/MIMIC, - log files for results for Knapsack with MIMIC
TSM/GA, - log files for results for TSM with GA
TSM/SA, - log files for results for TSM with SA
TSM/RHC,- log files for results for TSM with RHC
TSM/MIMIC,- log files for results for TSM with MIMIC
NN - - log files for results for back propagation and GA,SA,RHC with NN
PLOTS/FF - plots for accuracy and computation time for Flipflop
PLOTS/KNAPSACK - plots for accuracy and computation time for Knapsack
PLOTS/TSM - plots for accuracy and computation time for TSM
PLOTS/NN - plots for accuracy and computation time for NN-Backpropagation and other algorithms

2) To create the data files for back propagation experiment, run the load_data_for_nn.py file in python env. This will create a training.csv, test.csv and validation.csv files, which will be used the Neural Net experiment.

3) To run the Jython files, please modify the files so that the ABAGAIL.jar file is in the system path for the particular user.

4) Same way, modify paths of the log files in {}_plots.py files after running the algorithms.

Files for the algorithms:
 
1) nn-backpropagation.py - Backpropagation training of neural network
2) nn-rhc.py - Randomised Hill Climbing training of neural network
3) nn-sa.py - Simulated Annleaing training of neural network
4) nn-ga.py - Genetic Algorithm training of neural network
5) knapsack.py - Randomised Optimisation to solve the Knapsack problem
5) flipflop.py - Randomised Optimisation to solve the Flip Flop problem
6) tsm.py - Randomised Optimisation to solve the Traveling Salesman Problem
7) flipflop_plot.py - Plotting of parameters and accuracy for flipflop
8) knapsack_plot.py - Plotting of parameters and accuracy for knapsack
9) tsp_plot.py - Plotting of parameters and accuracy for tsm
10) nn_back_propagation_plot.py - Plotting of parameters and accuracy for nn_back_propagation
11) nn_ga_plot.py - Plotting of parameters and accuracy for nn_ga
12) nn_sa_plot.py - Plotting of parameters and accuracy for nn_sa
12) nn_rhc_plot.py - Plotting of parameters and accuracy for nn_rhc

Dataset folder
datasets - contains the diabetes retinotherapy dataset


All the results of accuracy and computation times are stored in .csv files in the respective folders mentioned above. The PLOTS folder contains the graphs of the comparisons.

##### REFERENCES:
https://github.com/pushkar/ABAGAIL
https://github.com/JonathanTay/CS-7641-assignment-2 - Particularly the nn back propagation errorOnDataSet function