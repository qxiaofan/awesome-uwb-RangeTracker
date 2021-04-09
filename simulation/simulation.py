import os
import sys

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'trackerCore'))

from tracker import tracker
from simulationData import sim, readFromFile, saveToFile
from plot import plot_sim, plot_sim_error
from parameters import *



if __name__ == '__main__':

    #Using last time data or generate new simulation data
    #if UsingLastTimeData:
       #print("UsingLastTimeData\n")
       #simData = readFromFile()
       #print("simData: ",simData)
    #else:
    #print("generate simulation data\n")
    simData = sim()
    simData.generate_sim_root()
    simData.generate_sim()
    saveToFile(simData)
    
    # Create two tracker for compare
    myTrackerExp = tracker()
    refMyTracker = tracker()

    # Set tracker mode to simulation, disable the speedEstimator of the reference tracker
    myTrackerExp.setup_mode(IsSimulation)
    speedEstimatorSwitch = False
    refMyTracker.setup_mode(IsSimulation,speedEstimatorSwitch)

    # Set covariance for the EKF
    refMyTracker.ekf.set_covs(covS_X, covS_Y, covS_Ori, covS_LVel, covM_Range, covM_Ori)
    myTrackerExp.ekf.set_covs(covS_X, covS_Y, covS_Ori, covS_LVel, covM_Range, covM_Ori)

    # Set initial state for the EKF
    refMyTracker.ekf.set_initial_state(initialState)
    myTrackerExp.ekf.set_initial_state(initialState)

   #  #read uwb imu data from local txt file
   #  file_name  = "/home/yong/workspace/2_project_files/A_single_anchor_imu_ekf/awesome-uwb-RangeTracker/simulation/imu_uwb_align.txt"
   #  dataset= []
   #  file  = open(file_name, mode='r')
   #  for line in file:
   #     line = line.split()
   #     line = list(map(float,line))
   #     dataset.append(line)
   #  file.close()
   #  #print(dataset)

   # # # load measurement input from local txt
   #  timeInput = [x[0] for x in dataset] 
   #  uwbInput = [x[1] for x in dataset]
   #  yawInput = [x[3] for x in dataset]

    #load  uwb and imu yaw data from local txt
    #print("timeInput: ", timeInput)
    #print("uwbInput: ", uwbInput)
    #print("yawInput: ", yawInput)
  

    # Choose measurement input
    uwbInput = simData.uwbNoisy
    yawInput = simData.yawNoisy
    timeInput = simData.timestamp

    print("timeInput: ", timeInput)
    print('\n\n')
    print("uwbInput: ", uwbInput)
    print('\n\n')
    print("yawInput: ", yawInput)
    print('\n\n')
     

    print("Start the Tracker")
    for step in range(len(uwbInput)):
        measurement = [uwbInput[step], yawInput[step], timeInput[step]]
        refMyTracker.step(measurement)
        myTrackerExp.step(measurement)

    # Plot the result to result_cache folder
    plot_sim(simData,refMyTracker,myTrackerExp)
    plot_sim_error(simData,refMyTracker,myTrackerExp)
