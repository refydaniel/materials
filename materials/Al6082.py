# -*- coding: utf-8 -*-
#
from .helpers import mu0

# https://www.wikiwand.com/en/Electrical_resistivity_and_conductivity
# https://www.wikiwand.com/en/Aluminium
magnetic_permeability = 1.000022*mu0
# electrical_conductivity = 3.77e7
def electrical_conductivity(T):
    # return (1. + (3.9e-3 * (T-293)))/2.65e-8
    return (1. + (3.9e-3 * (T-293)))/4.105e-8

# density = 2.7e3  # liquid density
def density(T):
    return 2.7e3
# http://www.convertunits.com/molarmass/Silver
molar_mass = 26.982
molar_heat_capacity = 24.2
# specific_heat_capacity = 0.89e3
def specific_heat_capacity(T):
    # [3]
    return 910
thermal_conductivity = 237.0
thermal_diffusivity = 9.7e-5
