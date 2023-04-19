from indentation_analysis_run import indentation_analysis_run
from utilities import color
import numpy as np
import math

def indentation_analysis_main():
    # Depth of the first jump (J1) as entered in the nanoindentation's method
    J1 = 1500

    # Strain rate (SR) used
    SR1 = 1
    SR2 = 0.01
    SR_diff = abs(math.log(SR1) - math.log(SR2)) # Log difference between SR1 and SR2 for the SR sensitivity m calculation (SRS)

    i = 1
    x = 0 # TODO: fix because x and y get overwritten by for loop inside run(). 
    y = 0

    Col, Row = 8, 6 # Number of columns (Col) and rows (Row). 
    Nb_zones = Col * Row # Number of zones.
    print('You have ',Nb_zones,' zones.') # Make sure you have the same number of zones indented as calculated here.

    # Tables creation to stock hardness, modulus and activation volumes of each zones.
    Hardness_Table = np.zeros((Row, Col))
    Modulus_Table = np.zeros((Row,Col)) #TODO: not being used
    SRS_Table = np.zeros((Row,Col))
    V_act_Table = np.zeros((Row,Col))

    # Parameters for data filtering
    n = 15  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1

    T = 295 # Temperature in Kelvin
    Kb = 1.38*10**(-23) # Boltzman constant
    Lattice_Param = 2.93*10**(-10) # Lattice parameter
    Burgers_Vector = ((Lattice_Param*math.sqrt(3))/2)**3 # Burgers vector calculation for perfect dislocations. This is for BCC structure. 
    
    source_path = '/srv/hemi01-j01/htmdec/ucsb/data/indentation/BRC603-B2/Low Res'
    dest_path = '/srv/hemi01-j01/htmdec/ucsb/data/indentation_analysis'
    
    # source_path = '/home/jovyan/work/data/BRC603-B2/Low Res' # reading from FUSE mounted version of the server filesystem 
    # dest_path = '/home/jovyan/work/workspace/data/indentation_analysis' # writing to tale local file system 
    
    indentation_analysis_run(Row, Col, i, color, b, a, J1, SR_diff, T, Kb, Burgers_Vector, source_path, dest_path, 
                             Hardness_Table, Modulus_Table, SRS_Table, V_act_Table)
    
    
    
