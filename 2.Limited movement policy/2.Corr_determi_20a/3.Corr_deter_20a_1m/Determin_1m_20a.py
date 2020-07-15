# -*- coding: utf-8 -*-
"""
                          Main Code
    
Platform for testing potential COVID-19 spread in Supermarkets 
Limited movement policy

Input:
    Susceptible agents as "Pi"
    Infected agent as "I1"

Outcome:
    Arrays with the distribution of potential new infected as 'infec_dist' 
    plot of 'infec_dist' 

@author: Gustavo Hernandez Mejia
"""


from funct_Determin_1m_20a import *
import matplotlib.pyplot as plt
import math   
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd
import random
from matplotlib.font_manager import FontProperties
import csv


#T1 = []
#sis_1 = 12 * 2
#for i in range(1, sis_1):
#    T1.append([(i*0.5)+0.5,2])


dot = 40
alpha3 = 0.5


#______________________________________________________________________________
"""
                        PRINCIPAL CODE
"""
infec_iter = []
time_iter = []
sim_cases = 1000

for event in range(sim_cases):

    max_step = 90
    step = 0
    P1_I = 0
    P2_I = 0
    P3_I = 0
    P4_I = 0
    P5_I = 0
    P6_I = 0
    P7_I = 0
    P8_I = 0
    P9_I = 0
    P10_I = 0
    P11_I = 0
    P12_I = 0
    P13_I = 0
    P14_I = 0
    P15_I = 0
    P16_I = 0
    P17_I = 0
    P18_I = 0
    P19_I = 0
    P20_I = 0
    Cas_1 = 0
    Cas_2 = 0
    Cas_3 = 0
    
    I1 = [2,2]        #   Infected

    P1 = [5,2]   # T1       #   Persons
    P2 = [15,2]
    P3 = [22,2]
    P4 = [27,2]
    P5 = [27,7]  # T3
    P6 = [22,6] 
    P7 = [8,14] 
    P8 = [27,12]
    P9 = [15,10]
    P10 = [18,6]
    P11 = [17,14]
    P12 = [20,14]
    P13 = [23,10]
    P14 = [8,11]  # T16
    P15 = [20,8]   # T9
    P16 = [19,2]   # T2
    P17 = [12,8]   # T9
    P18 = [12,12]   # T9
    P19 = [20,12]   # T9
    P20 = [9,11]   # T9
    
    CO1 = [6,15]        #   Check Out (CO)
    CO2 = [6,12]
    CO3 = [6,9]
    
    Pt_infe = [P1_I, P2_I, P3_I, P4_I, P5_I, P6_I, P7_I, P8_I, P9_I, P10_I, P11_I,
               P12_I, P13_I, P14_I, P15_I, P16_I, P17_I, P18_I, P19_I, P20_I,
                Cas_1, Cas_2, Cas_3]
    
    P_init = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13,
              P14, P15, P16 ,P17, P18, P19, P20, CO1, CO2, CO3]
    
    U_Pop = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13,
                     P14, P15, P16, P17, P18, P19, P20, CO1, CO2, CO3]
    I_Pop = [I1]
#    Agent_j = []
    U_Pop_2 = [[P1,0],[P2,0],[P3,0],[P4,0],[P5,0],[P6,0],[P7,0],
          [P8,0],[P9,0],[P10,0],[P11,0],[P12,0],[P13,0],[P14,0],
          [P15,0],[P16,0],[P17,0],[P18,0],[P19,0],[P20,0],
          [CO1,0],[CO2,0],[CO3,0]]
    
    Agent_j = []
    traj_nex = T_traj(T1,U_Pop,I_Pop,I1)
    
    for i in range(len(I_Pop)-1):
        for j in range(len(U_Pop_2)):
            if (U_Pop_2[j][0] == I_Pop[i+1]):
                U_Pop_2[j][1] = 1
    
    

    traj_U1 = U_traj(T1,P1)
    U_Pop_2[0][0] = traj_U1[1]
    traj_U2 = U_traj(T2,P2)
    U_Pop_2[1][0] = traj_U2[1]
    traj_U3 = U_traj(T2,P3)
    U_Pop_2[2][0] = traj_U3[1]
    traj_U4 = U_traj(T2,P4)
    U_Pop_2[3][0] = traj_U4[1]
    traj_U5 = U_traj(T3,P5)
    U_Pop_2[4][0] = traj_U5[1]
    
    traj_U6 = U_traj(T4,P6)
    U_Pop_2[5][0] = traj_U6[1]
    traj_U7 = U_traj(T17,P7)
    U_Pop_2[6][0] = traj_U7[1]
    traj_U8 = U_traj(T6,P8)
    U_Pop_2[7][0] = traj_U8[1]
    
  
    traj_U9 = U_traj(T10,P9)
    U_Pop_2[8][0] = traj_U9[1]
    traj_U10 = U_traj(T5,P10)
    U_Pop_2[9][0] = traj_U10[1]
    traj_U11 = U_traj(T11,P11)
    U_Pop_2[10][0] = traj_U11[1]
    traj_U12 = U_traj(T6,P12)
    U_Pop_2[11][0] = traj_U12[1]
    traj_U13 = U_traj(T7,P13)
    U_Pop_2[12][0] = traj_U13[1]
    
    traj_U14 = U_traj(T16,P14)
    U_Pop_2[13][0] = traj_U14[1]
    traj_U15 = U_traj(T9,P15)
    U_Pop_2[14][0] = traj_U15[1]
    
    traj_U16 = U_traj(T2,P16)
    U_Pop_2[15][0] = traj_U16[1]
    traj_U17 = U_traj(T13,P17)
    U_Pop_2[16][0] = traj_U17[1]
    traj_U18 = U_traj(T12,P18)
    U_Pop_2[17][0] = traj_U18[1]
    traj_U19 = U_traj(T8,P19)
    U_Pop_2[18][0] = traj_U19[1]
    traj_U20 = U_traj(T16,P20)
    U_Pop_2[19][0] = traj_U20[1]
    
    
    I_Pop = [traj_nex[2]]
    U_Pop = []
    for i in range(len(U_Pop_2)):
        if (1 == U_Pop_2[i][1]):
            I_Pop.append(U_Pop_2[i][0])
        else:
            U_Pop.append(U_Pop_2[i][0])
    
    Inf_prev = []
    
    while step < max_step:   
        Agent_j = []
        traj_nex = T_traj(traj_nex[0],U_Pop,I_Pop,traj_nex[2])
        
        for i in range(len(I_Pop)-1):
            for j in range(len(U_Pop_2)):
                if (U_Pop_2[j][0] == I_Pop[i+1]):
                    U_Pop_2[j][1] = 1
        
        if traj_nex[0] == 0:
            break

    
        traj_U1 = U_traj(traj_U1[0],traj_U1[1])
        U_Pop_2[0][0] = traj_U1[1]
        if (T1[0] == U_Pop_2[0][0] and 1 == U_Pop_2[0][1]):
            Inf_prev.append(U_Pop_2[0][0])
            U_Pop_2[0][1] = 0

    #    print(f'P1 = {P1}')
        traj_U2 = U_traj(traj_U2[0],traj_U2[1])
        U_Pop_2[1][0] = traj_U2[1]
        if (T1[0] == U_Pop_2[1][0] and 1 == U_Pop_2[1][1]):
            Inf_prev.append(U_Pop_2[1][0])
            U_Pop_2[1][1] = 0
    #    print(f'P2 = {P2}')
        traj_U3 = U_traj(traj_U3[0],traj_U3[1])
        U_Pop_2[2][0] = traj_U3[1]
        if (T1[0] == U_Pop_2[2][0] and 1 == U_Pop_2[2][1]):
            Inf_prev.append(U_Pop_2[2][0])
            U_Pop_2[2][1] = 0
    #    print(f'P3 = {P3}')
        traj_U4 = U_traj(traj_U4[0],traj_U4[1])
        U_Pop_2[3][0] = traj_U4[1]
        if (T1[0] == U_Pop_2[3][0] and 1 == U_Pop_2[3][1]):
            Inf_prev.append(U_Pop_2[3][0])
            U_Pop_2[3][1] = 0
    #    print(f'P4 = {P4}')
        traj_U5 = U_traj(traj_U5[0],traj_U5[1])
        U_Pop_2[4][0] = traj_U5[1]
        if (T1[0] == U_Pop_2[4][0] and 1 == U_Pop_2[4][1]):
            Inf_prev.append(U_Pop_2[4][0])
            U_Pop_2[4][1] = 0
    #    print(f'P5 = {P5}')
        traj_U6 = U_traj(traj_U6[0],traj_U6[1])
        U_Pop_2[5][0] = traj_U6[1]
        if (T1[0] == U_Pop_2[5][0] and 1 == U_Pop_2[5][1]):
            Inf_prev.append(U_Pop_2[5][0])
            U_Pop_2[5][1] = 0
    #    print(f'P6 = {P6}')
        traj_U7 = U_traj(traj_U7[0],traj_U7[1])
        U_Pop_2[6][0] = traj_U7[1]
        if (T1[0] == U_Pop_2[6][0] and 1 == U_Pop_2[6][1]):
            Inf_prev.append(U_Pop_2[6][0])
            U_Pop_2[6][1] = 0
    #    print(f'P7 = {P7}')
        traj_U8 = U_traj(traj_U8[0],traj_U8[1])
        U_Pop_2[7][0] = traj_U8[1]
        if (T1[0] == U_Pop_2[7][0] and 1 == U_Pop_2[7][1]):
            Inf_prev.append(U_Pop_2[7][0])
            U_Pop_2[7][1] = 0
    #    print(f'P8 = {P8}')
        traj_U9 = U_traj(traj_U9[0],traj_U9[1])
        U_Pop_2[8][0] = traj_U9[1]
        if (T1[0] == U_Pop_2[8][0] and 1 == U_Pop_2[8][1]):
            Inf_prev.append(U_Pop_2[8][0])
            U_Pop_2[8][1] = 0
    #    print(f'P9 = {P9}')
        traj_U10 = U_traj(traj_U10[0],traj_U10[1])
        U_Pop_2[9][0] = traj_U10[1]
        if (T1[0] == U_Pop_2[9][0] and 1 == U_Pop_2[9][1]):
            Inf_prev.append(U_Pop_2[9][0])
            U_Pop_2[9][1] = 0
    #    print(f'P10 = {P10}')
        traj_U11 = U_traj(traj_U11[0],traj_U11[1])
        U_Pop_2[10][0] = traj_U11[1]
        if (T1[0] == U_Pop_2[10][0] and 1 == U_Pop_2[10][1]):
            Inf_prev.append(U_Pop_2[10][0])
            U_Pop_2[10][1] = 0
    #    print(f'P11 = {P11}')
        traj_U12 = U_traj(traj_U12[0],traj_U12[1])
        U_Pop_2[11][0] = traj_U12[1]
        if (T1[0] == U_Pop_2[11][0] and 1 == U_Pop_2[11][1]):
            Inf_prev.append(U_Pop_2[11][0])
            U_Pop_2[11][1] = 0
    #    print(f'P12 = {P12}')
        traj_U13 = U_traj(traj_U13[0],traj_U13[1])
        U_Pop_2[12][0] = traj_U13[1]
        if (T1[0] == U_Pop_2[12][0] and 1 == U_Pop_2[12][1]):
            Inf_prev.append(U_Pop_2[12][0])
            U_Pop_2[12][1] = 0
    #    print(f'P13 = {P13}')
        traj_U14 = U_traj(traj_U14[0],traj_U14[1])
        U_Pop_2[13][0] = traj_U14[1]
        if (T1[0] == U_Pop_2[13][0] and 1 == U_Pop_2[13][1]):
            Inf_prev.append(U_Pop_2[13][0])
            U_Pop_2[13][1] = 0
        
        traj_U15 = U_traj(traj_U15[0],traj_U15[1])
        U_Pop_2[14][0] = traj_U15[1]
        if (T1[0] == U_Pop_2[14][0] and 1 == U_Pop_2[14][1]):
            Inf_prev.append(U_Pop_2[14][0])
            U_Pop_2[14][1] = 0
        
        traj_U16 = U_traj(traj_U16[0],traj_U16[1])
        U_Pop_2[15][0] = traj_U16[1]
        if (T1[0] == U_Pop_2[15][0] and 1 == U_Pop_2[15][1]):
            Inf_prev.append(U_Pop_2[15][0])
            U_Pop_2[15][1] = 0
        
        traj_U17 = U_traj(traj_U17[0],traj_U17[1])
        U_Pop_2[16][0] = traj_U17[1]
        if (T1[0] == U_Pop_2[16][0] and 1 == U_Pop_2[16][1]):
            Inf_prev.append(U_Pop_2[16][0])
            U_Pop_2[16][1] = 0
        
        traj_U18 = U_traj(traj_U18[0],traj_U18[1])
        U_Pop_2[17][0] = traj_U18[1]
        if (T1[0] == U_Pop_2[17][0] and 1 == U_Pop_2[17][1]):
            Inf_prev.append(U_Pop_2[17][0])
            U_Pop_2[17][1] = 0
        
        traj_U19 = U_traj(traj_U19[0],traj_U19[1])
        U_Pop_2[18][0] = traj_U19[1]
        if (T1[0] == U_Pop_2[18][0] and 1 == U_Pop_2[18][1]):
            Inf_prev.append(U_Pop_2[18][0])
            U_Pop_2[18][1] = 0
        
        traj_U20 = U_traj(traj_U20[0],traj_U20[1])
        U_Pop_2[19][0] = traj_U20[1]
        if (T1[0] == U_Pop_2[19][0] and 1 == U_Pop_2[19][1]):
            Inf_prev.append(U_Pop_2[19][0])
            U_Pop_2[19][1] = 0
        
        
        I_Pop = [traj_nex[2]]
        U_Pop = []
        for i in range(len(U_Pop_2)):
            if (1 == U_Pop_2[i][1]):
                I_Pop.append(U_Pop_2[i][0])
            else:
                U_Pop.append(U_Pop_2[i][0])
        
 
        
        step = step + 1


    coun = 0
    for i in range(len(U_Pop_2)):
        if (1 == U_Pop_2[i][1]):
            coun = coun + 1
    
    infec_iter.append(coun + len(Inf_prev))
    time_iter.append((step))
    
lar = max(infec_iter)+1
infec_dist = []   
for i in range(lar):
    infec_dist.append(infec_iter.count(i))
#    print('{}: {}'.format(i,infec_dist[i]))
    
infec_num = []   
for i in range(len(infec_dist)):
    infec_num.append(infec_dist[i]*i)

new_List =  np.divide(infec_dist, sim_cases)*100
ax1=plt.figure(figsize=(10,7), facecolor='w', edgecolor='k') 
plt.bar(np.arange(lar), new_List, color = colors[9], alpha=0.7)
#plt.hist(new_List, color = "skyblue")
plt.xlabel("Number of potential newly infected (20 a, 1 inf)(Total infected {})".format(sum(infec_num)), fontsize=16)
plt.ylabel("Repetition of cases (1 m, determin) (%)", fontsize=16)
plt.ylim(0, 50)
plt.rc('xtick', labelsize=14)    # fontsize of the tick labels
plt.rc('ytick', labelsize=14) 
#plt.grid(True)
#plt.xticks([])
#plt.yticks([])
#ax1.savefig('Test_determi_1m_20a.pdf', format='pdf', dpi=1400)
plt.show() 
    
print ('\nTotal of possible newly infected in 1000 simulations (1 m): {}'.format(sum(infec_num)) )

#lenT = (len(T1)+ len(T2)+ len(T3)+ len(T4)+ len(T5)+ len(T6)+ len(T7)+ len(T8) +
#        len(T18)+ len(T9)+ len(T10)+ len(T11)+ len(T12)+ len(T13)+ 
#        len(T15) + len(T16) + len(T17))
#lenT
