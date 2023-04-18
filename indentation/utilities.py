import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter, AutoMinorLocator
import os

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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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
    # plt.rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
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


def file_exists(x, y, i, source_path):
    try: # Routine that checks if the next file exist. If not, generates an error message and prints the number of tests
        filename='Z' + str(x) + '.' + str(y) + '_T' + str(i)+ '.CSV'
        filepath = os.path.join(source_path, filename)
        with open(filepath):pass
    except IOError:
        error_msg = filepath + str(' not found! ') +color.END + '\nEnd.' 
        print(error_msg)
        print(color.BOLD + '___________________________________________________________________',color.END) 
        return 0
    return 1