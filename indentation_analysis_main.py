from .indentation_analysis_run import indentation_analysis_run
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import numpy as np
import math
#%matplotlib qt #display in another window

class color: # Color class to customize your 'print()' functions
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)
    
## This part regroups all the 'def' functions used in the code. Change or add what you need. 

def Hardness_Plot_Format(): # Function that define the format of your plots
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
    plt.rcParams.update({'font.size': 9}) # maximum font size for non-resized figures
     
    # x axis parmameter
    plt.xlim(0,4000)
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.tick_params(axis='x', which='minor', direction='in', length=5, width=1, top=1)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(5))
    plt.xlabel("Depth (nm)", fontsize=12)

    # y axis parmameter
    plt.ylim(0,8)
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.tick_params(axis='y', which='minor', direction='in', length=5, width=1, right=1)
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.ylabel("Hardness, H (GPa)", fontsize=12)
    
def Modulus_Plot_Format(): # Function that define the format of your plots
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
    plt.rcParams.update({'font.size': 9}) # maximum font size for non-resized figures
     
    # x axis parmameter
    plt.xlim(0,4000)
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.tick_params(axis='x', which='minor', direction='in', length=5, width=1, top=1)
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator(5))
    plt.xlabel("Depth (nm)", fontsize=12)

    # y axis parmameter
    plt.ylim(0,150)
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.tick_params(axis='y', which='minor', direction='in', length=5, width=1, right=1)
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator(2))
    plt.ylabel("Modulus, E (GPa)", fontsize=12)

def CMAP_Hardness():
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
    plt.rcParams.update({'font.size': 9}) # maximum font size for non-resized figures
     
    # x axis parmameter
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.xlabel("Column")

    # y axis parmameter
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.ylabel("Row")

    plt.colorbar(label='Hardness, H (GPa)')

def CMAP_Modulus():
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
    plt.rcParams.update({'font.size': 9}) # maximum font size for non-resized figures
     
    # x axis parmameter
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.xlabel("Column")

    # y axis parmameter
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.ylabel("Row")

    plt.colorbar(label='Modulus, E (GPa)')

def CMAP_SRS():
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
    plt.rcParams.update({'font.size': 9}) # maximum font size for non-resized figures
     
    # x axis parmameter
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.xlabel("Column")

    # y axis parmameter
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.ylabel("Row")

    plt.colorbar(label='Strain rate sensitivity, m')

def CMAP_Vact():
    plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
    plt.gcf().set_dpi(1200)     # 300 minimum dpi for scientific figures, 
                               # 400 for figures with text
                               # save color figures as RGB format
    plt.rcParams.update({'axes.linewidth': 1}) # between 0.5 and 1 pt
     
    # x axis parmameter
    plt.tick_params(axis='x', direction='in', length=10, width=1, top=1, labelsize=10)
    plt.xlabel("Column")

    # y axis parmameter
    plt.tick_params(axis='y', direction='in', length=10, width=1, right=1, labelsize=10)
    plt.ylabel("Row")

    plt.colorbar(label='Activation volume, V{} '.format(get_sub('a')) + '(b{})'.format(get_super('3')))

def idx_max(liste):
    max = liste[0]
    a = 0 
    for i in range(len(liste)):
        if liste[i] > max:
            max  = liste [i]
            a = i
    return max, a 

def Average(lst):
    return sum(lst) / len(lst)

def indentation_analysis_main():
    # Depth of the first jump (J1) as entered in the nanoindentation's method
    J1 = 1500

    # Strain rate (SR) used
    SR1 = 1
    SR2 = 0.01
    SR_diff = abs(math.log(SR1) - math.log(SR2)) # Log difference between SR1 and SR2 for the SR sensitivity m calculation (SRS)

    i = 1
    x = 0
    y = 0

    Col, Row = 8, 6 # Number of columns (Col) and rows (Row). 
    Nb_zones = Col * Row # Number of zones.
    print('You have ',Nb_zones,' zones.') # Make sure you have the same number of zones indented as calculated here.

    # Tables creation to stock hardness, modulus and activation volumes of each zones.
    Hardness_Table = np.zeros((Row, Col))
    Modulus_Table = np.zeros((Row,Col))
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
    
    Z_path = '/srv/hemi01-j01/htmdec/ucsb/data/indentation/BRC603-B2/Low Res/Z'
    dest_path = '/srv/hemi01-j01/htmdec/ucsb/data/analysis'
    indentation_analysis_run(Row, Col, color, b, a, J1, SR_diff, T, Kb, Burgers_Vector, Z_path, dest_path)
    
    
    
