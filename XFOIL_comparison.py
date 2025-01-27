### Section 2.0: PYXFOIL Practice
#STANDARD IMPORTS
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import fsolve
import pyxfoil
import csv
import mses

# Plot the experimental data form research papers
    #[1] Drela, Mark. "XFOIL: An analysis and design system for low Reynolds number airfoils." Low Reynolds Number Aerodynamics: Proceedings of the Conference Notre Dame, Indiana, USA, 5–7 June 1989. Berlin, Heidelberg: Springer Berlin Heidelberg, 1989.
    #[2] Drela, Mark. "Design and optimization method for multi-element airfoils." Aerospace Design Conference. 1993.
    #[3] Drela, Mark, and Michael B. Giles. "Viscous-inviscid analysis of transonic and low Reynolds number airfoils." AIAA journal 25.10 (1987): 1347-1355.
    #[4] Drela, Mark. "Pros & cons of airfoil optimization." Frontiers of Computational Fluid Dynamics 1998. 1998. 363-381.

# Study Cases

alfa_seq = np.linspace(0,20,21)

# Eppler 387

eppler_path = 'data/Eppler 387/Eppler 387.dat'

    # Drag Polar
    # Re = [2e5, 1e5, 6e4]


    # Cp Distribution 
    # Ma = 0
    # Re = 1e5
    # Alfa = 3.742

eppler_Ma = 0
eppler_Re = [2e5, 1e5, 6e4]
eppler_alfa = 3.742

# Creating Polar and Surface CP Files

pyxfoil.GetPolar(foil=eppler_path, naca=False, alfs=eppler_alfa, Ma=eppler_Ma,Re=eppler_Re[1])

for Re in eppler_Re:
    pyxfoil.main(foil=eppler_path, naca=False, alfs=alfa_seq, Ma=eppler_Ma,Re=Re)


# FX67-K-170

fx_path = 'data/FX67-K-170/FX67-K-170.dat'

    # Cp Distribution
    # Ma = 0
    # Re = 2e5
    # Alfa = 4.156

fx_Ma = 0
fx_Re = 2e5
fx_alfa = 4.156

pyxfoil.main(foil=fx_path, naca=False, alfs=fx_alfa, Ma=fx_Ma,Re=fx_Re)


    # Error Convergence as a function of Panels

# RAE 2822

rae_path = 'data/RAE 2822/RAE 2822.dat'

    # Cp Distribution 
    # Ma = 0.676
    # Re = 5.7e6
    # Alfa = 2.165

    # Cp Distribution
    # Ma = 0.75
    # Re = 6.2e6
    # Alfa = 2.734

rae_Ma = [0.676, 0.75]
rae_Re = [5.7e6, 6.2e6]
rae_alfa = [2.165, 2.734]

pyxfoil.main(foil=rae_path, naca=False, alfs=rae_alfa[0], Ma=rae_Ma[0],Re=rae_Re[0])
pyxfoil.main(foil=rae_path, naca=False, alfs=rae_alfa[1], Ma=rae_Ma[1],Re=rae_Re[1])

# LNV109A

lnv_path = 'data/LNV109A/LNV109A.dat'

    # Drag Polar
    # Re = [2.5e5, 3.75e5, 5e5, 6.5e5]
    
    # Cp Distribution
    # Ma = 0.1
    # Re = 5e5
    # Alfa = 7.358

    # Cp Distribution
    # Ma = 0.1
    # Re = 3.75e5
    # Alfa = 3.459

lnv_Ma = 0.1
lnv_Re = [2.5e5, 3.75e5, 5e5, 6.5e5]
lnv_alfa = [7.358, 3.459]

pyxfoil.main(foil=lnv_path, naca=False, alfs=lnv_alfa[0], Ma=lnv_Ma,Re=lnv_Re[2])
pyxfoil.main(foil=lnv_path, naca=False, alfs=lnv_alfa[1], Ma=lnv_Ma,Re=lnv_Re[1])

for Re in lnv_Re:
    pyxfoil.main(foil=lnv_path, naca=False, alfs=alfa_seq, Ma=lnv_Ma,Re=Re)

# LA203A

la_path = 'data/LA203A/LA203A.dat'

    # Drag Polar
    # Re = [2.5e5, 3.75e5, 5e5]

    # Cp Distribution
    # Ma = 0.1
    # Re = 2.5e5
    # Alfa = 3.28

la_Ma = 0.1
la_Re = [2.5e5, 3.75e5, 5e5]
la_alfa = 3.28

pyxfoil.main(foil=la_path, naca=False, alfs=la_alfa, Ma=la_Ma,Re=la_Re[0])

for Re in la_Re:
    pyxfoil.main(foil=la_path, naca=False, alfs=alfa_seq, Ma=la_Ma,Re=Re)

##### 
# Compare XFOIL and Experimental Data
