#%% DRX en polvo de muestras NF@citrato 08 / 13 / 18 hs
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
from scipy.signal import savgol_filter
from scipy.ndimage import minimum_filter, gaussian_filter
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

# %% ploteo todos 
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)

ax.plot(dostheta_08, intensity_08+150,alpha=0.9,lw=0.9, label='8H',zorder=1)
ax.plot(dostheta_13, intensity_13+75,alpha=0.9,lw=0.9, label='13H',zorder=2)
ax.plot(dostheta_18, intensity_18,alpha=0.9,lw=0.9, label='18H',zorder=3)    

ax.legend()
ax.grid()            
ax.set_ylabel('Intensidad (u.a.)')
ax.set_xlabel('2θ (°)')
ax.set_xlim(20,80)
ax.set_ylim(0,)
plt.suptitle('DRX en polvo - NF@citrato 08 / 13 / 18 hs')
plt.savefig('DRX_08_13_18h.png', dpi=400)
plt.show()
#%% 18 h 
# Suavizado, fondo y corrección 
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
#%% picos
peaks, props = find_peaks(y_corr,prominence=10,width=2,distance=50)

fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_18, y_corr, label='corrected')
ax.plot(dostheta_18[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
ax.set_ylim(0,)
ax.grid()
ax.legend()
plt.show()

# %% Ajuste
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
# %% print
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
#%% 13 h
# suavizado

intensity= intensity_13
dostheta = dostheta_13
y_smooth = savgol_filter(intensity, 20, 3) # suavizado

background = minimum_filter(y_smooth, size=150) # fondo
background = gaussian_filter(background, sigma=10)

y_corr = y_smooth - background # señal corregida

fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta, intensity,'-', label='raw')
ax.plot(dostheta, y_smooth,'-', label='smooth')
ax.plot(dostheta, background, label='background')
ax.plot(dostheta, y_corr, label='corrected')

ax.set_xlim(20,80)
ax.set_ylim(0,)
ax.grid()
ax.legend()
plt.show()
#%% picos
peaks, props = find_peaks(y_corr,prominence=12,width=10,distance=10)
peaks = np.insert(peaks, -1, 2763) # agrego a mano el pico de 75.26° que no se detecta con find_peaks
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta, y_corr,'.', label='corrected')
ax.plot(dostheta[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
ax.set_ylim(0,)
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

    params[f'{prefix}sigma'].set(value=0.1, min=0.02, max=1)
    params[f'{prefix}center'].set(value=dostheta[p], min=dostheta[p]-0.5, max=dostheta[p]+0.5)
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
#% Imprimir datos de picos en pantalla
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

#%% 08 h 
# Suavizado, fondo y corrección 
intensity= intensity_08
dostheta = dostheta_08
# suavizado
y_smooth = savgol_filter(intensity, 20, 3)

# fondo
background = minimum_filter(y_smooth, size=150)
background = gaussian_filter(background, sigma=10)

# señal corregida
y_corr = y_smooth - background

#ploteo
fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_08, intensity_08,'-', label='raw')
ax.plot(dostheta_08, y_smooth,'-', label='smooth')
ax.plot(dostheta_08, background, label='background')
ax.plot(dostheta_08, y_corr, label='corrected')

ax.set_xlim(20,80)
ax.set_ylim(0,)
ax.grid()
ax.legend()
plt.show()

#%% picos
peaks, props = find_peaks(y_corr,prominence=9,width=2,distance=10)
peaks = np.sort(np.append(peaks, [257, 2759, 2945]))



fig,ax=plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.plot(dostheta_18, y_corr,'.', label='corrected')
ax.plot(dostheta_18[peaks], y_corr[peaks], 'r.', label='peaks')
ax.set_xlim(20,80)  
ax.set_ylim(0,)
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

    params[f'{prefix}sigma'].set(value=0.1, min=0.02, max=1)
    params[f'{prefix}center'].set(value=dostheta[p], min=dostheta[p]-0.5, max=dostheta[p]+0.5)
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
plt.savefig('ajuste_08h.png', dpi=300)
plt.show()

# archivo de salida
fname = 'picos_08H.txt'

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
#% Imprimir datos de picos en pantalla
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

#%%#############################################################################################################################
#%% Indexación de picos y comparacion con patrones de referencia (PDF)

def lector_drx_softw(path):
    with open(path, 'rb') as f:
        codificacion = chardet.detect(f.read())['encoding']
    data = pd.read_table(path, header=0,
                         names=('Pos. [°2Th.]', 'Height [cts]', 'FWHM [°2Th.]'),
                         usecols=(1,2,3),
                         decimal=',',
                         engine='python',
                         encoding=codificacion)
    dostheta = pd.Series(data['Pos. [°2Th.]'][:]).to_numpy(dtype=float)
    intensidad =  pd.Series(data['Height [cts]'][:]).to_numpy(dtype=float)
    beta = pd.Series(data['FWHM [°2Th.]'][:]).to_numpy(dtype=float)
    
    return dostheta , intensidad, beta
# Levanto datos de picos detectados por el software de DRX (PDF) para cada muestra
dostheta_softw_18,I_softw_18,beta_softw_18 = lector_drx_softw('info/picos_db-18.TXT')
dostheta_softw_13,I_softw_13,beta_softw_13 = lector_drx_softw('info/picos_db-13.TXT')
dostheta_softw_08,I_softw_08,beta_softw_08 = lector_drx_softw('info/picos_db-08.TXT')

def lector_drx_py(path):
    '''Para los resultados que obtuvimos con el ajuste multi-Gaussiano'''
    data = pd.read_table(path, header=0,
                         names=('Pico', 'Centro (2theta °)', 'Altura (u.a.)', 'FWHM (°)'),
                         usecols=(0,1,2,3),
                         decimal='.',
                         engine='python')
    dostheta = pd.Series(data['Centro (2theta °)'][:]).to_numpy(dtype=float)
    intensidad =  pd.Series(data['Altura (u.a.)'][:]).to_numpy(dtype=float)
    beta = pd.Series(data['FWHM (°)'][:]).to_numpy(dtype=float)
    
    return dostheta , intensidad, beta

dostheta_py_18,I_py_18,beta_py_18 = lector_drx_py('resultados/picos_18H.txt')
dostheta_py_13,I_py_13,beta_py_13 = lector_drx_py('resultados/picos_13H.txt')
dostheta_py_08,I_py_08,beta_py_08 = lector_drx_py('resultados/picos_08H.txt')



# %%
fig, (ax1,ax2,ax3) = plt.subplots(3,1,figsize=(9,9), constrained_layout=True,sharex=True)
ax1.plot(dostheta_18, intensity_18,label='18h',c='C2')
ax1.vlines(dostheta_softw_18, 0, I_softw_18, color='r', ls='-.',label='picos detectados sofware')
ax1.vlines(dostheta_py_18, 0, I_py_18, color='g', ls='--',label='picos detectados Python')

ax2.plot(dostheta_13, intensity_13,label='13h',c='C1')
ax2.vlines(dostheta_softw_13, 0, I_softw_13, color='r', ls='-.',label='picos detectados sofware')
ax2.vlines(dostheta_py_13, 0, I_py_13, color='g', ls='--',label='picos detectados Python')

ax3.plot(dostheta_08, intensity_08,label='8h',c='C0')  
ax3.vlines(dostheta_softw_08, 0, I_softw_08, color='r', ls='-.',label='picos detectados sofware')
ax3.vlines(dostheta_py_08, 0, I_py_08, color='g', ls='--',label='picos detectados Python')


for ax in (ax1,ax2,ax3):
    ax.grid()
    ax.set_xlim(20,80)
    ax.set_ylim(0,)
    ax.legend()
ax3.set_xlabel('2θ (°)')
# %% Ahora cargo los datos de las tarjetas

dostheta_magnetita_db =np.array([30.1465, 35.5092, 37.1445, 43.1565,47.2527, 53.5422, 57.0770, 62.6790, 65.9046,66.9617, 71.1118, 74.1574, 75.1618, 79.1370])
I_magnetita_db = np.array([87, 289, 999, 76, 205, 6, 85, 280, 367, 81, 27, 68, 28, 22]) #

dostheta_maghemita_db = np.array([23.7711,26.1025,30.2406, 32.1244, 33.8820, 35.6302, 37.2492, 38.8470, 40.3767, 43.2835, 44.7035, 46.0712,
    50.0070, 53.7325, 54.9243, 56.1056, 57.2714,   59.5679, 60.6850, 62.9250, 63.9941, 65.0721,67.2014, 68.2527, 69.3051, 71.3757, 72.4013,    74.4707, 75.4423, 76.4424, 77.4425, 79.4461])
I_maghemita_db = np.array([ 5,5, 35, 2,2, 100, 3,1,1, 16, 1, 0, 2, 10,  1,1, 24, 1,2, 34, 1,1, 0,1,1,3,1,5,2, 0, 0, 1]) #

dostheta_hematita_db = np.array([24.1378, 33.1522, 35.6112, 39.2756, 40.8544,    43.5177, 49.4791, 54.0892, 56.1504, 57.4275,
    57.5885, 62.4490, 63.9892, 66.0260, 69.5987,    71.9352, 72.2601, 75.4282, 77.7272, 78.7577])
I_hematita_db = np.array([30, 100, 70, 3, 20,3, 40, 45, 1,5, 10,30, 30, 0, 3, 10, 6,8,4,2]) #
#%%
fig,ax = plt.subplots(figsize=(9,5), constrained_layout=True,sharex=True)
ax.vlines(dostheta_magnetita_db, 0, I_magnetita_db/max(I_magnetita_db), color='r', ls='-',label='magnetita')
ax.vlines(dostheta_maghemita_db, 0, I_maghemita_db/max(I_maghemita_db), color='g', ls='-',label='maghemita')
ax.vlines(dostheta_hematita_db, 0, I_hematita_db/max(I_hematita_db), color='b', ls='-',label='hematita')
ax.grid()
ax.set_xlabel('2θ (°)')
ax.set_xlim(20,80)
ax.set_ylim(0,)
ax.legend()
plt.suptitle('Patrones de referencia - Magnetita, Maghemita y Hematita')


# %% Comparo

fig18,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(10,6), constrained_layout=True,sharex=True)

ax1.plot(dostheta_18, intensity_18/max(intensity_18), label='18h')
ax1.vlines(dostheta_magnetita_db, 0, I_magnetita_db/max(I_magnetita_db), color='r', ls='-',label='magnetita')

ax2.plot(dostheta_18, intensity_18/max(intensity_18), label='18h')
ax2.vlines(dostheta_maghemita_db, 0, I_maghemita_db/max(I_maghemita_db), color='g', ls='-',label='maghemita')

ax3.plot(dostheta_18, intensity_18/max(intensity_18), label='18h')
ax3.vlines(dostheta_hematita_db, 0, I_hematita_db/max(I_hematita_db), color='b', ls='-',label='hematita')
for ax in (ax1,ax2,ax3):
    ax.grid()
    ax.set_xlim(20,80)
    ax.set_ylim(0,)
    ax.legend()


ax3.set_xlabel('2θ (°)')
plt.suptitle('DRX NF@cit 18h vs referencias')
plt.show()

#%%
fig13,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(10,6), constrained_layout=True,sharex=True)

ax1.plot(dostheta_13, intensity_13/max(intensity_13), label='13h')
ax1.vlines(dostheta_magnetita_db, 0, I_magnetita_db/max(I_magnetita_db), color='r', ls='-',label='magnetita')

ax2.plot(dostheta_13, intensity_13/max(intensity_13), label='13h')
ax2.vlines(dostheta_maghemita_db, 0, I_maghemita_db/max(I_maghemita_db), color='g', ls='-',label='maghemita')

ax3.plot(dostheta_13, intensity_13/max(intensity_13), label='13h')
ax3.vlines(dostheta_hematita_db, 0, I_hematita_db/max(I_hematita_db), color='b', ls='-',label='hematita')
for ax in (ax1,ax2,ax3):
    ax.grid()
    ax.set_xlim(20,80)
    ax.set_ylim(0,)
    ax.legend()


ax3.set_xlabel('2θ (°)')
plt.suptitle('DRX NF@cit 13h vs referencias')
plt.show()
#%%
fig08,(ax1,ax2,ax3) = plt.subplots(3,1,figsize=(10,6), constrained_layout=True,sharex=True)

ax1.plot(dostheta_08, intensity_08/max(intensity_08), label='08h')
ax1.vlines(dostheta_magnetita_db, 0, I_magnetita_db/max(I_magnetita_db), color='r', ls='-',label='magnetita')

ax2.plot(dostheta_08, intensity_08/max(intensity_08), label='08h')
ax2.vlines(dostheta_maghemita_db, 0, I_maghemita_db/max(I_maghemita_db), color='g', ls='-',label='maghemita')

ax3.plot(dostheta_08, intensity_08/max(intensity_08), label='08h')
ax3.vlines(dostheta_hematita_db, 0, I_hematita_db/max(I_hematita_db), color='b', ls='-',label='hematita')
for ax in (ax1,ax2,ax3):
    ax.grid()
    ax.set_xlim(20,80)
    ax.set_ylim(0,)
    ax.legend()


ax3.set_xlabel('2θ (°)')
plt.suptitle('DRX NF@cit 08h vs referencias')


# %%
