#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def CalcVp(strain,strain0, D, dt):
    
    strainR = (strain-strain0) / dt;
    
    RR = 0.5*((strainR[1,1]-strainR[2,2])**2+(strainR[1,1]-strainR[0,0])**2+(strainR[0,0]-strainR[2,2])**2) + 3*(strainR[1,2]**2+ strainR[0,2]**2+ strainR[0,1]**2);
    
    strainRII = np.sqrt(RR);
    vp = 2 * strainRII * D;    
    return vp;


def GetXi(c0,t,dt,mu1,mu2,ti,te):  # eq 59

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
# second invariant

    yy = np.sqrt(0.5*((sigma[1,1]-sigma[2,2])**2+(sigma[1,1]-sigma[0,0])**2+(sigma[0,0]-sigma[2,2])**2) + 3*(sigma[1,2]**2+sigma[0,2]**2+sigma[0,1]**2)) ;
    return yy;
      
def  StrainToStress(strain,L,M):

    # calc stress tensor from strain tensor
    sigma = np.zeros([3,3]);
    ss = np.matrix(strain);
#     print(ss);

    sigma[1,1]=(L+2/3*M)*ss.trace() + 2*M*(strain[1,1]-ss.trace()/3);
    sigma[2,2]=(L+2/3*M)*ss.trace() + 2*M*(strain[2,2]-ss.trace()/3);
    sigma[0,0]=(L+2/3*M)*ss.trace() + 2*M*(strain[0,0]-ss.trace()/3);

    sigma[1,2] = 2*M*strain[1,2];
    sigma[1,0] = 2*M*strain[1,0];
    sigma[2,0] = 2*M*strain[2,0];
    sigma[2,1] = 2*M*strain[2,1];
    sigma[0,1] = 2*M*strain[0,1];
    sigma[0,2] = 2*M*strain[0,2];
    
    P = (L+2*M/3)*sigma.trace(); # definition of P
    return sigma, P;


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
