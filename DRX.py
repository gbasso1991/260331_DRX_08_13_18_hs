#%% Librerias y paquetes 
import numpy as np
from uncertainties import ufloat, unumpy
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob
import os
import chardet
import re
import matplotlib as mpl
from scipy.optimize import curve_fit
from lmfit.models import GaussianModel
# %% Data
data_08 = np.loadtxt('data/08H.ASC', skiprows=0)
data_13 = np.loadtxt('data/13H.ASC', skiprows=0)
data_18 = np.loadtxt('data/18H.ASC', skiprows=0)

dostheta_08 = data_08[:, 0]
intensity_08 = data_08[:, 1]

dostheta_13 = data_13[:, 0]
intensity_13 = data_13[:, 1]

dostheta_18 = data_18[:, 0]
intensity_18 = data_18[:, 1]
#%%
# %% plot 1x1
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)

ax.plot(dostheta_08, intensity_08,alpha=0.9, label='8H')

ax.plot(dostheta_13, intensity_13,alpha=0.9, label='13H')

ax.plot(dostheta_18, intensity_18,alpha=0.9, label='18H')    

ax.legend()
ax.grid()            
ax.set_ylabel('Intensidad (u.a.)')
ax.set_xlabel('2θ (°)')
ax.set_xlim(20,80)
# #%% Busco maximos con find_peaks
# from scipy.signal import find_peaks

# peaks_18, prop_18 = find_peaks(intensity_18, width=5, distance=50)

# print("\n--- 18H ---")
# for i, p in enumerate(peaks_18):
#     print(f"2θ = {dostheta_18[p]:.2f}°, I = {intensity_18[p]:.1f}, prom = {prop_18['prominences'][i]:.1f}")


# fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
# ax.plot(dostheta_18, intensity_18, label='raw')

# ax.plot(dostheta_18[peaks_18], intensity_18[peaks_18], 'r.')

# ax.set_xlim(20,80)
# ax.set_ylim(0,)
# ax.grid()
# ax.legend()

#%% Vamos de nuevo con lmfit 
from scipy.signal import savgol_filter
from scipy.ndimage import minimum_filter, gaussian_filter

intensity= intensity_18
dostheta = dostheta_18
# suavizado
y_smooth = savgol_filter(intensity, 20, 3)

# fondo
background = minimum_filter(y_smooth, size=150)
background = gaussian_filter(background, sigma=10)

# señal corregida
y_corr = y_smooth - background

#ploteo
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_18, intensity_18,'-', label='raw')
ax.plot(dostheta_18, y_smooth,'-', label='smooth')
ax.plot(dostheta_18, background, label='background')
ax.plot(dostheta_18, y_corr, label='corrected')

ax.set_xlim(20,80)
ax.set_ylim(0,)
ax.grid()
ax.legend()
#%%
from scipy.signal import find_peaks

peaks, props = find_peaks(
    y_corr,
    prominence=10,
    width=2,
    distance=50)
#
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_18, y_corr, label='corrected')
ax.plot(dostheta_18[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
ax.set_ylim(0,)
ax.grid()
ax.legend()

# %%
model = None
params = None

for i, p in enumerate(peaks):
    prefix = f'p{i}_'
    g = GaussianModel(prefix=prefix)

    if model is None:
        model = g
        params = g.make_params()
    else:
        model += g
        params.update(g.make_params())

    params[f'{prefix}center'].set(value=dostheta[p])
    params[f'{prefix}sigma'].set(value=0.1)
    params[f'{prefix}amplitude'].set(value=y_corr[p])

result = model.fit(y_corr, params, x=dostheta)

fig, (ax, ax_res) = plt.subplots(2, 1, figsize=(10,7),gridspec_kw={'height_ratios': [3,1]},constrained_layout=True,sharex=True)

# ax.plot(dostheta, y_corr, 'k',lw=1, label='data')

# --- ajuste total ---
ax.plot(dostheta, result.best_fit, 'r-', label='fit total', lw=1.5)

# --- componentes individuales ---
components = result.eval_components(x=dostheta)

for name, comp in components.items():
    ax.plot(dostheta, comp, '--', label=name, alpha=0.7)

# --- centros de picos ---
centers = [result.params[f'p{i}_center'].value for i in range(len(peaks))]
ax.plot(centers, [max(y_corr)*0.5]*len(centers), 'r|', label='centros')

# --- estilo ---
ax.set_ylabel('Intensidad (u.a.)')
ax.set_title('Ajuste multi-Gaussiano')
ax.legend(ncol=2, fontsize=8)
ax.grid()
ax.set_xlim(dostheta.min(), dostheta.max())
# RESIDUOS
residuals = y_corr - result.best_fit

ax_res.plot(dostheta, residuals, 'k')
ax_res.axhline(0, color='r', ls='--')

ax_res.set_xlabel('2θ (°)')
ax_res.set_ylabel('residuos')
ax_res.grid()
plt.savefig('ajuste_18h.png', dpi=300)
plt.show()


print(result.fit_report())
import numpy as np

# archivo de salida
fname = 'picos_18H.txt'

with open(fname, 'w') as f:
    
    # encabezado
    f.write('# Pico\tCentro (2θ °)\tAltura (u.a.)\tFWHM (°)\n')
    
    for i in range(len(peaks)):
        prefix = f'p{i}_'
        
        # parámetros del fit
        center = result.params[f'{prefix}center'].value
        sigma  = result.params[f'{prefix}sigma'].value
        amplitude = result.params[f'{prefix}amplitude'].value
        
        # FWHM (en mismas unidades que dostheta → grados)
        fwhm = 2.3548 * sigma
        
        # altura (más útil que amplitude en DRX)
        height = result.params[f'{prefix}height'].value
        
        # escribir fila
        f.write(f'{i}\t{center:.4f}\t{height:.2f}\t{fwhm:.4f}\n')

print(f'Resultados guardados en: {fname}')
# %%
