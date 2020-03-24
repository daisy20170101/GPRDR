#!/usr/bin/env python
# -*- coding: utf-8 -*-

# define functions used in GPR model based on GPRDI (Maurizio)

import numpy as np

def TransStrain(eff):  # eq. 67
    s11 = 2/3*eff[0]- 1/3*eff[1] - 1/3*eff[2] ;
    s22 = -1/3*eff[0]+ 2/3*eff[1] - 1/3*eff[2] ;
    s33 = -1/3*eff[0]- 1/3*eff[1] + 2/3*eff[2] ;
    s12 = eff[3];
    s13 = eff[4];
    s23 = eff[5];
    return s11,s22,s33,s12,s13,s23;

def CalcVp(strain,strain0, D, dt): # based on Horrendorf et al., 2019
    """
    % variables:
    % D: thickness of fault zone
    % dt: delta t
    % strain0, strain: strain tensor of this and last time step, respectively
    """    
    strainR = (strain-strain0) / dt;
    
    RR = 0.5*((strainR[1,1]-strainR[2,2])**2+(strainR[1,1]-strainR[0,0])**2+(strainR[0,0]-strainR[2,2])**2) + 3*(strainR[1,2]**2+ strainR[0,2]**2+ strainR[0,1]**2);
    
    strainRII = np.sqrt(RR);
    vp = 2 * strainRII * D;    
    return vp;

def CalcSlp(strain,strain0,dx,dt,slp0):
    slp = slp0;
    strainR = (strain-strain0)/dt;
    u = strainR[0,0]*dx*dt + slp0;
   # v = strainR[1,1]*dx + slp0[1];
   # w = strainR[2,2]*dx + slp0[2];
    slp = u;
    return slp;

def CalcEc(rho0,K1,K2,K_a,mu1,mu2,mu_a,strain):
    ee = (strain[0,0]-strain.trace()/3)**2+(strain[1,1]-strain.trace()/3)**2+(strain[2,2]-strain.trace()/3)**2+2*strain[1,2]**2+2*strain[0,2]**2+2*strain[0,1]**2;
    Ec = 0.5/rho0*(-(K1-K2)*K1*K2/K_a**2)*strain.trace()**2+1/rho0*(-(mu1-mu2)*mu1*mu2/mu_a**2)*(ee);
    
    return Ec;



def GetXi(c0,t,dt,mu1,mu2,ti,te):  # eq 59
    """
    % variables:
    % mu1,mu2: shear modulus
    % ti, te, t, dt: start and ending time of damage, time and delta t
    % c0: damage coeff. of last time step
    """
    # get damage coefficient c
    if (t<ti or t>te):
        dcdt = 0;
    else:
        dcdt = mu2*mu1*(mu1-(mu1-mu2)*(t-ti)/(te-ti))**-2.0*(te-ti)**-1.0;
#         Maurizio
#        dcdt = (t-ti)/(te-ti); # linear 
#         dcdt = (mu2 + (mu1-mu2)/(1+ ((t-ti)/(te-ti))^8 ) ^1/8 ) / mu2;
    c = c0+dt*dcdt;
    return c;

def second(sigma):
    """
    % variables:
    % sigma: stress tensor
    """
# second invariant

    yy = np.sqrt(0.5*((sigma[1,1]-sigma[2,2])**2+(sigma[1,1]-sigma[0,0])**2+(sigma[0,0]-sigma[2,2])**2) + 3*(sigma[1,2]**2+sigma[0,2]**2+sigma[0,1]**2)) ;
    return yy;
      
def  StrainToStress(strain,L,M):  # convert strain to stress
    """
    % variables:
    % L, M: averaged lame's and shear modulus
    """
    # calc stress tensor from strain tensor
    sigma = np.zeros((3,3));
    ss = strain;
    
    sigma[0,0]=(L+2/3*M)*ss.trace() + 2*M*(ss[0,0]-ss.trace()/3);
    sigma[1,1]=(L+2/3*M)*ss.trace() + 2*M*(ss[1,1]-ss.trace()/3);
    sigma[2,2]=(L+2/3*M)*ss.trace() + 2*M*(ss[2,2]-ss.trace()/3);

    sigma[1,2] = 2*M*strain[1,2];
    sigma[1,0] = 2*M*strain[1,0];
    sigma[2,0] = 2*M*strain[2,0];
    sigma[2,1] = 2*M*strain[2,1];
    sigma[0,1] = 2*M*strain[0,1];
    sigma[0,2] = 2*M*strain[0,2];
    
    P = (L+2*M/3)*(ss.trace()); # definition of P
    
    return sigma,P;


def calTauI(tau0,alpha,beta,y):  # eq. 60
    """
    % variables:
    % tau0, alpha, beta are constant
    % y (or Y) is J2 plasticity
    % xi is damage coeff. [0,1]
    """
    
    tau = np.zeros(np.size(tau0));
    tau = tau0*np.exp(alpha-beta*y);
    return tau;


def Get_energy(strain,rho,L,M):
    
    rhoE = 1/2*L*(strain[0,0]+strain[1,1]+strain[2,2])**2 + M*(strain[0,0]**2+strain[1,1]**2+strain[2,2]**2+ 2*strain[0,1]**2+ 2*strain[0,2]**2+ 2*strain[1,2]**2);
    
    return rhoE;
    


