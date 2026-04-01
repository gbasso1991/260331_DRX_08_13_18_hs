#%%
#  DRX en polvo de muestras NF@citrato 08 / 13 / 18 hs
# Librerias y paquetes 
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
from scipy.signal import find_peaks
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

# %% plot 1x1
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)

ax.plot(dostheta_08, intensity_08+75,alpha=0.9, label='8H',zorder=1)
ax.plot(dostheta_13, intensity_13+150,alpha=0.9, label='13H',zorder=2)
ax.plot(dostheta_18, intensity_18,alpha=0.9, label='18H',zorder=3)    

ax.legend()
ax.grid()            
ax.set_ylabel('Intensidad (u.a.)')
ax.set_xlabel('2θ (°)')
ax.set_xlim(20,80)
ax.set_ylim(0,)
plt.show()
#%% Vamos con lmfit 
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
plt.show()
#%%
peaks, props = find_peaks(y_corr,prominence=10,width=2,distance=50)

fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_18, y_corr, label='corrected')
ax.plot(dostheta_18[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
ax.set_ylim(0,)
ax.grid()
ax.legend()
plt.show()

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
    f.write('# Pico\tCentro (2theta °)\tAltura (u.a.)\tFWHM (°)\n')
    
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
#  Imprimir datos de picos en pantalla
print("\n" + "="*70)
print("RESULTADOS DEL AJUSTE DE PICOS - MUESTRA 18H")
print("="*70)
print(f"{'Pico':<6} {'2θ (°)':<12} {'Altura (u.a.)':<15} {'FWHM (°)':<12}")
print("-"*70)

for i in range(len(peaks)):
    prefix = f'p{i}_'
    
    center = result.params[f'{prefix}center'].value
    height = result.params[f'{prefix}height'].value
    sigma = result.params[f'{prefix}sigma'].value
    fwhm = 2.3548 * sigma
    
    print(f"{i:<6} {center:<12.4f} {height:<15.2f} {fwhm:<12.4f}")

print("="*70)
print(f"Total de picos encontrados: {len(peaks)}")
print("="*70)
#%%###########################################################################
# ahora 13 h

intensity= intensity_13
dostheta = dostheta_13
y_smooth = savgol_filter(intensity, 20, 3) # suavizado

background = minimum_filter(y_smooth, size=150) # fondo
background = gaussian_filter(background, sigma=10)

y_corr = y_smooth - background # señal corregida

fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_13, intensity_13,'-', label='raw')
ax.plot(dostheta_13, y_smooth,'-', label='smooth')
ax.plot(dostheta_13, background, label='background')
ax.plot(dostheta_13, y_corr, label='corrected')

ax.set_xlim(20,80)
ax.set_ylim(0,)
ax.grid()
ax.legend()
plt.show()
#%%
peaks, props = find_peaks(y_corr,prominence=12,width=10,distance=10)

fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_13, y_corr,'-', label='corrected')
ax.plot(dostheta_13[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
# ax.set_ylim(0,50)
ax.grid()
ax.legend()
plt.show()
#%% ajuste multi-Gaussiano
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
plt.savefig('ajuste_13h.png', dpi=300)
plt.show()


print(result.fit_report())
import numpy as np

# archivo de salida
fname = 'picos_13H.txt'

with open(fname, 'w') as f:
    
    # encabezado
    f.write('# Pico\tCentro (2theta °)\tAltura (u.a.)\tFWHM (°)\n')
    
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

#  Imprimir datos de picos en pantalla
print("\n" + "="*70)
print("RESULTADOS DEL AJUSTE DE PICOS - MUESTRA 18H")
print("="*70)
print(f"{'Pico':<6} {'2θ (°)':<12} {'Altura (u.a.)':<15} {'FWHM (°)':<12}")
print("-"*70)

for i in range(len(peaks)):
    prefix = f'p{i}_'
    
    center = result.params[f'{prefix}center'].value
    height = result.params[f'{prefix}height'].value
    sigma = result.params[f'{prefix}sigma'].value
    fwhm = 2.3548 * sigma
    
    print(f"{i:<6} {center:<12.4f} {height:<15.2f} {fwhm:<12.4f}")

print("="*70)
print(f"Total de picos encontrados: {len(peaks)}")
print("="*70)
# %%
