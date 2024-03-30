# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 07:16:48 2024

@author: james.caplinger


Validation checks:

"""

import numpy as np


def nepers_to_dB(nepers):
    return nepers*20*np.log10(np.e)

def grainSize(N):
    """From buckingham 2005, returns grain size as a function of N"""
    Del = 1
    Nmin = 0.37
    B = ((1-N)/(1-Nmin))**(1/3)
    return 2*Del*(2*B-1)/(1-B)

def rho(T,S,p):
    """mason.gmu.edu/~gklinger/seawater.pdf
    T -> temperature in C
    S -> Salinity in PsU
    p -> pressure/depth in km
    For 30<=S<=40, -2<=T<=30, p<= 6 km"""
    C=999.83+5.053*p-0.048*p**2
    beta = .808-0.0085*p
    alpha = 0.0708*(1+.351*p+0.068*(1-0.0683*p)*T)
    gamma = 0.003*(1-0.059*p-0.012*(1-0.64*p)*T)

    return C+beta*S-alpha*T-gamma*(35-S)*T

def bulkModulus(cw,rho_w):
    return cw**2*rho_w

## SAND CONSTANTS
rho_g = 2650
kg = 38e9

## SCALING CONSTANTS
No = 0.377
do = 0.3
uo = 1000.0
H = 78.8
Ho = 74.14


## water parameters
T = 25.  # degrees C 
S = 34.615341  # salinity
p = 0    # depth in km
cw = 1500 # sound speed m/s
# calculate water dnesity and bulk modulus
rho_w = rho(T,S,p)
kw = bulkModulus(cw, rho_w)



# # inputs
# d = .3  # depth (m)
# N = .377  # porosity
# n = 0.08854
# tau_p = .12
# tau_s = 1.77
# gamma_po = 354.53e6
# gamma_so = 44.699e6

# no depth dependence used here
d = 0.3

N_range = {'min':0.377,'default':0.377,'max':0.95}
n_range = {'min':0.05054,'default':0.08854,'max':0.12654}
tau_p_range = {'min':0.054,'default':0.12,'max':0.186}
tau_s_range = {'min':1.77,'default':1.77,'max':100.}
gamma_po_range = {'min':193.6e6,'default':354.53e6,'max':515.45e6}
gamma_so_range = {'min':27.962e6,'default':44.677e6,'max':61.436e6}

def VGS(d,N,n,tau_p,tau_s,gamma_po,gamma_so):

    ug = grainSize(N)
    f = np.linspace(10,1000,num=1000) # in Hz
    
    
    
    # bulk density and Mallock Wood's Speed
    rho_o = N*rho_w+(1-N)*rho_g
    ko = 1/(N/kw+(1-N)/kg)
    co = np.sqrt(ko/rho_o)
    
    
    # compressional and shear coefficients
    gammaCoef = ((1-N)*ug*d*H)/((1-No)*uo*do*Ho)
    gamma_p = gamma_po*gammaCoef**(1/3)
    gamma_s = gamma_so*gammaCoef**(2/3)
    
    # big guy chi
    X = (gamma_p+(4/3)*gamma_s)/(rho_o*co**2)
    
    ## frequency dependent terms
    w = 2*np.pi*f
    # g(w)
    if np.isnan(tau_p): # GS
        g_p=np.ones_like(f)
        g_s=np.ones_like(f)
    else: #VGS
        g_p = (1+1/(1j*w*tau_p))**(n-1)
        g_s = (1+1/(1j*w*tau_s))**(n-1)
        
    # compressional wave speed
    cp = co/np.real((1+X*(1j*w)**n*g_p)**(-1/2))    
    # compressional wave attenuation
    alpha_p = nepers_to_dB(-w/co*np.imag((1+X*(1j*w)**n*g_p)**(-1/2)))
    
    # shear wave speed
    cs = np.sqrt(gamma_s/rho_o)/np.real(((1j*w)**n*g_s)**(-1/2))
    # shear wave attenutation 
    alpha_s = nepers_to_dB(-w*np.sqrt(rho_o/gamma_s)*np.imag(((1j*w)**n*g_s)**(-1/2)))
    
    
    ## load reference data
    # gs data
    # cp_gs = gCSV.loadXYdata('data/B2007_gs_cp.csv')
    # alpha_gs = gCSV.loadXYdata('data/B2007_gs_alphap.csv')
    
    # # vgs data
    # cp_vgs = gCSV.loadXYdata('data/B2007_vgs_cp.csv')
    # alpha_vgs = gCSV.loadXYdata('data/B2007_vgs_alphap.csv')
    
    alpha_p_wl = alpha_p*cp/f
    alpha_s_wl = alpha_s*cs/f
    
    return cp, cs, alpha_p, alpha_s

# ## plotting 
# fig,(ax1,ax2,ax3) = plt.subplots(3,1,sharex=True)

# ax1.semilogx(f,cp)
# #ax1.semilogx(cp_gs.x,cp_gs.y,label='GS',linestyle='--')
# #ax1.semilogx(cp_vgs.x,cp_vgs.y,label='VGS',linestyle='--',color='r')
# ax2.semilogx(f,alpha_p)
# #ax2.loglog(alpha_gs.x,alpha_gs.y,label='GS',linestyle='--')
# #ax2.loglog(alpha_vgs.x,alpha_vgs.y,label='vGS',linestyle='--',color='r')

# ax3.semilogx(f,alpha_p_wl)

# ax2.set_xlabel('frequency (kHz)')

# ax1.set_ylabel('cp (m/s)')
# ax2.set_ylabel('alpha_p (dB/m)')
# ax3.set_ylabel('alpha_p (dB/wl)')

# ax1.grid(visible=True,which='both')
# ax2.grid(visible=True,which='both')
# ax3.grid(visible=True,which='both')

# fig2,(ax3,ax4,ax5) = plt.subplots(3,1,sharex=False)

# ax3.semilogx(f,cs)

# ax4.semilogx(f,alpha_s)
# ax5.semilogx(f,alpha_s_wl)


# ax4.set_xlabel('frequency (kHz)')

# ax3.set_ylabel('cs (m/s)')
# ax4.set_ylabel('alpha_s (dB/m)')
# ax5.set_ylabel('alpha_s (dB/wl)')


# ax3.grid(visible=True,which='both')
# ax4.grid(visible=True,which='both')
# ax5.grid(visible=True,which='both')


