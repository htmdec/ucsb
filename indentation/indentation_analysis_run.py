
import matplotlib.pyplot as plt
from scipy.signal import lfilter
import numpy as np
import pandas as pd
import math
import os
#%matplotlib qt #display in another window
from utilities import Average, get_sub, get_super, CMAP_Hardness, CMAP_SRS, CMAP_Vact, file_exists

# Main script for data analysis.
def indentation_analysis_run(Row, Col, i, color, b, a, J1, SR_diff, T, Kb, Burgers_Vector, source_path, dest_path,
                             Hardness_Table, Modulus_Table, SRS_Table, V_act_Table):

    for x in range (0,Row): # Row selection
        for y in range (0,Col): # Column selection
            m_Values = [] # Initialization of the Table for m values
            V_act_Values = [] # Initialization of the Table for Vact values
            while True: # Test selection
                # Initialization of the Tables needed for test averaging
                slope_Table = []
                k_idx = []
                k_idx_2 = []

                # Data importation and first filtration
                filename = 'Z' + str(x) + '.' + str(y) + '_T' + str(i) + '.CSV'
                filepath = os.path.join(source_path, filename)
                df = pd.read_csv(filepath)
                print(color.BOLD + color.RED,'\nZ' + str(x) + '.' + str(y) + '_T' + str(i),color.END)
                # print(msg)
                Tab = df.filter(items=['DEPTH','HARDNESS','MODULUS']) # Select only 'DEPTH', 'HARDNESS' and 'MODULUS' columns
                Tab = Tab.dropna(axis=0) # Delete all 'NaN' lines
                Tab = Tab.drop([0],axis=0) # Delete the first line (units line)
                Tab = Tab.astype(float) # Change the type category to 'float'
                TAB = np.array(Tab)

                # Data filtering process => smoothening/denoising of the signal
                Hardness_Filtered = lfilter(b, a, TAB[:,1])

                #plt.plot(TAB[:,0],TAB[:,1],'k-')
                #plt.plot(TAB[:,0],Hardness_Filtered,'g-')
                #plt.xlim(1000,3700)
                #plt.ylim(3,5)

                J1_min_1 = np.argmin(abs(TAB[:,0]-J1))
                TAB_idx_End = np.argmin(abs(TAB[:,0]-10000))
                #print('Index intervalle: from ',J1_min_1,'to ',TAB_idx_End)    

                for k in range (J1_min_1+100,TAB_idx_End-30):
                    slope_10 = abs((Hardness_Filtered[k+30]-Hardness_Filtered[k])/(TAB[k+30,0]-TAB[k,0]))
                    if slope_10>0.001:
                        slope_Table.append(slope_10)
                        k_idx.append(k)
                        #print(k_idx)
                        #plt.plot(TAB[k,0],Hardness_Filtered[k],'mx')
                j = 0
                while True:
                    try:
                        diff_k_idx = k_idx[j+1]-k_idx[j]
                    except IndexError:
                        break
                    if diff_k_idx>50:
                        k_idx_2.append(k_idx[j])
                        k_idx_2.append(k_idx[j+1])
                        #plt.plot(k_idx_2,'bx')
                    j = j + 1
                if len(k_idx_2) == 4:
                    B2_idx = k_idx_2[0]
                    B2 = B2_idx + 30
                    B1 = B2 - 50
                    A2 = B1 - 150
                    C1 = k_idx_2[1]
                    C2_idx = k_idx_2[2]
                    C2 = C2_idx + 30
                    D1 = k_idx_2[3]

                    #plt.plot(TAB[A1,0],Hardness_Filtered[A1],'rx')
                    #plt.plot(TAB[A2,0],Hardness_Filtered[A2],'b^')
                    #plt.plot(TAB[B1,0],Hardness_Filtered[B1],'rx')
                    #plt.plot(TAB[B2,0],Hardness_Filtered[B2],'b^')
                    #plt.plot(TAB[C1,0],Hardness_Filtered[C1],'rx')
                    #plt.plot(TAB[C2,0],Hardness_Filtered[C2],'b^')
                    #plt.plot(TAB[D1,0],Hardness_Filtered[D1],'rx')
                    #plt.show()

                    Hardness_J1 = []
                    Hardness_J2 = []
                    Hardness_J3 = []

                    for k in range(A2,B1):
                        Hardness_J1.append(Hardness_Filtered[k])
                        Hardness_Average_J1 = Average(Hardness_J1)
                    for k in range(C2,D1):
                        Hardness_J3.append(Hardness_Filtered[k])
                        Hardness_Average_J3 = Average(Hardness_J3)
                        Hardness_Average_SR1 = abs((Hardness_Average_J1 + Hardness_Average_J3)/2)
                    for k in range(B2,C1):
                        Hardness_J2.append(Hardness_Filtered[k])
                        Hardness_Average_SR2 = Average(Hardness_J2)
                    H_diff1 = abs(math.log(Hardness_Average_J1) - math.log(Hardness_Average_SR2))
                    H_diff2 = abs(math.log(Hardness_Average_SR2) - math.log(Hardness_Average_J3))

                    m1 = abs((H_diff1)/(SR_diff))
                    m2 = abs((H_diff2)/(SR_diff))
                    m = (m1 + m2) / 2
                    m_Values.append(m)
                    m_Average = Average(m_Values)

                    V_act = (3*math.sqrt(3)*T*Kb)/(m_Average*Hardness_Average_SR1*Burgers_Vector*10**(9))
                    V_act_Values.append(V_act)
                    V_act_Average = Average(V_act_Values)

                    print('Average H(SR1) = {0:.2f}'.format(Hardness_Average_SR1),'GPa')
                    print('Average h(SR2) = {0:.2f}'.format(Hardness_Average_SR2),'GPa')
                    print('m = {0:.3f}'.format(m),'\nV{}'.format(get_sub('a')) + ' = {0:.2f}'.format(V_act) + 'b{}'.format(get_super('3')))
                    print(color.BOLD + '\nStrain rate sensitivity m is {0:.6f}'.format(m_Average) + '.\nThe activation volume is {0:.6f}'.format(V_act_Average) + 'b{}.'.format(get_super('3')),color.END)
                    print(color.BOLD + '___________________________________________________________________',color.END) 
                else:
                    print('Data not used!')
                    print(color.BOLD + '___________________________________________________________________',color.END) 
                    pass 
                i = i + 1
                # Routine that checks if the next file exist. If not, generates an error message and prints the number of tests
                if not file_exists(x, y, i, source_path):
                    break
            Hardness_Table[x,y] = Hardness_Average_SR1
            SRS_Table[x,y] = m_Average
            V_act_Table[x,y] = V_act_Average
            i = 1
            y = y + 1
            # Routine that checks if the next file exist. If not, generates an error message and prints the number of tests
            if not file_exists(x, y, i, source_path):
                break
        y = 0
        x = x + 1
        # Routine that checks if the next file exist. If not, generates an error message and prints the number of tests
        if not file_exists(x, y, i, source_path):
            break

    Hardness_Table = np.flipud(Hardness_Table)
    plt.pcolormesh(Hardness_Table,shading='gouraud',cmap='Blues')
    CMAP_Hardness()
    plt.savefig(os.path.join(dest_path, 'CMAP_Hardness.png'), dpi=1200)
    plt.show()

    SRS_Table = np.flipud(SRS_Table)
    plt.pcolormesh(SRS_Table,shading='gouraud',cmap='Reds')
    CMAP_SRS()
    plt.savefig(os.path.join(dest_path, 'CMAP_SRS.png'),dpi=1200)
    plt.show()

    V_act_Table = np.flipud(V_act_Table)
    plt.pcolormesh(V_act_Table,shading='gouraud',cmap='Greens')
    CMAP_Vact()
    plt.savefig(os.path.join(dest_path, 'CMAP_Vact.png'),dpi=1200)
    plt.show()