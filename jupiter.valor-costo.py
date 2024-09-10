
# jupiter.py
valor_futuro_flujos = 18000 
tasa_mensual = 0.01  
meses_inversion_original = 12  
inversion_mensual_original = 1000 
meses_inversion_extendido = 15 

def valor_presente_pagos(inversion_mensual, tasa, n_meses):
    vp_pagos = sum([inversion_mensual / (1 + tasa)**i for i in range(1, n_meses + 1)])
    return vp_pagos

vp_flujos_original = valor_futuro_flujos / (1 + tasa_mensual)**meses_inversion_original
vp_flujos_extendido = valor_futuro_flujos / (1 + tasa_mensual)**meses_inversion_extendido

vp_inversion_original = valor_presente_pagos(inversion_mensual_original, tasa_mensual, meses_inversion_original)

vpn_original = vp_flujos_original - vp_inversion_original

from scipy.optimize import fsolve

def calcular_costo_max(costo_mensual):
    vp_inversion_extendido = valor_presente_pagos(costo_mensual, tasa_mensual, meses_inversion_extendido)
    vpn_extendido = vp_flujos_extendido - vp_inversion_extendido
    return vpn_extendido - vpn_original

costo_max_aceptable = fsolve(calcular_costo_max, 1000)[0]

print(f"El costo mensual máximo aceptable es: ${costo_max_aceptable:.2f}")
# jupiter.py
valor_futuro_flujos = 18000 
tasa_mensual = 0.01  
meses_inversion_original = 12  
inversion_mensual_original = 1000 
meses_inversion_extendido = 15 

def valor_presente_pagos(inversion_mensual, tasa, n_meses):
    vp_pagos = sum([inversion_mensual / (1 + tasa)**i for i in range(1, n_meses + 1)])
    return vp_pagos

vp_flujos_original = valor_futuro_flujos / (1 + tasa_mensual)**meses_inversion_original
vp_flujos_extendido = valor_futuro_flujos / (1 + tasa_mensual)**meses_inversion_extendido

vp_inversion_original = valor_presente_pagos(inversion_mensual_original, tasa_mensual, meses_inversion_original)

vpn_original = vp_flujos_original - vp_inversion_original

from scipy.optimize import fsolve

def calcular_costo_max(costo_mensual):
    vp_inversion_extendido = valor_presente_pagos(costo_mensual, tasa_mensual, meses_inversion_extendido)
    vpn_extendido = vp_flujos_extendido - vp_inversion_extendido
    return vpn_extendido - vpn_original

costo_max_aceptable = fsolve(calcular_costo_max, 1000)[0]

print(f"El costo mensual máximo aceptable es: ${costo_max_aceptable:.2f}")
