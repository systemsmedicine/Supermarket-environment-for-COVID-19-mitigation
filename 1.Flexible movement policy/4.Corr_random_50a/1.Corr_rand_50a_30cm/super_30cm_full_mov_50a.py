# -*- coding: utf-8 -*-
"""
                          Main Code
    
Platform for testing potential COVID-19 spread in Supermarkets 

Input:
    Susceptible agents as "Pi"
    Infected agent as "I1"

Outcome:
    Arrays with the distribution of potential new infected as 'infec_dist' 
    plot of 'infec_dist' 

@author: Gustavo Hernandez Mejia
"""


from funct_30cm_full_mov_50a import *
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

    max_step = 300 #  461*0.6
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
    P21_I = 0
    P22_I = 0
    P23_I = 0
    P24_I = 0
    P25_I = 0
    P26_I = 0
    P27_I = 0
    P28_I = 0
    P29_I = 0
    P30_I = 0
    
    P31_I = 0
    P32_I = 0
    P33_I = 0
    P34_I = 0
    P35_I = 0
    P36_I = 0
    P37_I = 0
    P38_I = 0
    P39_I = 0
    P40_I = 0

    P41_I = 0
    P42_I = 0
    P43_I = 0
    P44_I = 0
    P45_I = 0
    P46_I = 0
    P47_I = 0
    P48_I = 0
    P49_I = 0
    P50_I = 0
    Cas_1 = 0
    Cas_2 = 0
    Cas_3 = 0
    
    I1 = [1.2,2]        #   Infected

    P1 = [1.5,2]   # T1       #   Persons
    P2 = [1.8,2]
    P3 = [22.2,2]
    P4 = [27,2]
    P5 = [27,7.1]  # T3
    P6 = [22.4,6] 
    P7 = [8.2,14] 
    P8 = [27,12]
    P9 = [15,10]
    P10 = [14.1,6]
    P11 = [16.5,14]
    P12 = [20,14]   # T6
    P13 = [23,10]
    P14 = [8.2,11]  # T16
    P15 = [20,8.1]   # T9
    P16 = [12,4]   # T9
    P17 = [12,8.1]   # T9
    P18 = [12,12.4]   # T9
    P19 = [20,12.4]   # T9
    P20 = [9.1,11]   # T9
    
    P21 = [14.1,14]  # T11
    P22 = [21.2,14]  # T6
    P23 = [26,10]    # T7
    P24 = [8.2,8]   # T15
    P25 = [20,6.6]   # T9
    P26 = [12,2.5]     # T14
    P27 = [18,6]   # T5
    P28 = [8.1,2]  # T1
    P29 = [27,13.5]  # T6
    P30 = [26,6]   # T4
    
    
    P31 = [18,14]       # T11
    P32 = [25.4,14]     # T6
    P33 = [7,8]         # T15
    P34 = [27,8]        # T3
    P35 = [21.2,10]     # T7
    P36 = [21,2]        # T2
    P37 = [12,6]        # T5
    P38 = [10.5,2]      # T1
    P39 = [27,11.1]     # T6
    P40 = [24.2,6]      # T4
    
    P41 = [11.2,14]      # T17
    P42 = [6.1,14]       # T17
    P43 = [18, 2]        # T2
    P44 = [12,2]         # T1
    P45 = [18,10]        # T10
    P46 = [14.1,10]      # T10
    P47 = [15,6]         # T5
    P48 = [6,2]          # T1
    P49 = [27,3.2]       # T2
    P50 = [20,6]         # T4
    
    
    
    
    CO1 = [6,15]        #   Check Out (CO)
    CO2 = [6,12]
    CO3 = [6,9]
    
    Pt_infe = [P1_I, P2_I, P3_I, P4_I, P5_I, P6_I, P7_I, P8_I, P9_I, P10_I, 
          P11_I, P12_I, P13_I, P14_I, P15_I, P16_I, P17_I, P18_I, P19_I, P20_I,
          P21_I, P22_I, P23_I, P24_I, P25_I, P26_I, P27_I, P28_I, P29_I, P30_I,
          P31_I, P32_I, P33_I, P34_I, P35_I, P36_I, P37_I, P38_I, P39_I, P40_I,
          P41_I, P42_I, P43_I, P44_I, P45_I, P46_I, P47_I, P48_I, P49_I, P50_I,
                Cas_1, Cas_2, Cas_3]
    
    P_init = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, 
              P11, P12, P13, P14, P15, P16 ,P17, P18, P19, P20,
              P21, P22, P23, P24, P25, P26 ,P27, P28, P29, P30,
              P31, P32, P33, P34, P35, P36 ,P37, P38, P39, P40,
              P41, P42, P43, P44, P45, P46 ,P47, P48, P49, P50, CO1, CO2, CO3]
    
    
    U_Pop = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, 
             P11, P12, P13, P14, P15, P16, P17, P18, P19, P20,
             P21, P22, P23, P24, P25, P26, P27, P28, P29, P30,
             P31, P32, P33, P34, P35, P36 ,P37, P38, P39, P40,
             P41, P42, P43, P44, P45, P46 ,P47, P48, P49, P50, CO1, CO2, CO3]
    
    I_Pop = [I1]
#    Agent_j = []
    
    U_Pop_2 = [[P1,0],[P2,0],[P3,0],[P4,0],[P5,0],[P6,0],[P7,0],
          [P8,0],[P9,0],[P10,0],[P11,0],[P12,0],[P13,0],[P14,0],
          [P15,0],[P16,0],[P17,0],[P18,0],[P19,0],[P20,0],
          [P21,0],[P22,0],[P23,0],[P24,0],
          [P25,0],[P26,0],[P27,0],[P28,0],[P29,0],[P30,0],
          [P31,0],[P32,0],[P33,0],[P34,0],
          [P35,0],[P36,0],[P37,0],[P38,0],[P39,0],[P40,0],
          [P41,0],[P42,0],[P43,0],[P44,0],
          [P45,0],[P46,0],[P47,0],[P48,0],[P49,0],[P50,0],
          [CO1,0],[CO2,0],[CO3,0]]
    
    #_________________________________________________________________
#    ax=plt.figure(figsize=(10,7), facecolor='w', edgecolor='k') 
#    #plt.scatter(I_Pop[0][0], I_Pop[0][1], marker="1", s=dot, color=colors[3])
#    for i in range(len(T1)):
#        plt.scatter(T1[i][0], T1[i][1], marker=".", s=dot, color=colors[0],alpha = alpha3)
#    for i in range(len(T2)):
#        plt.scatter(T2[i][0], T2[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#    for i in range(len(T3)):
#        plt.scatter(T3[i][0], T3[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3)
#    for i in range(len(T4)):
#        plt.scatter(T4[i][0], T4[i][1], marker=".", s=dot, color=colors[5],alpha = alpha3) 
#    for i in range(len(T5)):
#        plt.scatter(T5[i][0], T5[i][1], marker=".", s=dot, color=colors[6],alpha = alpha3) 
#    for i in range(len(T6)):
#        plt.scatter(T6[i][0], T6[i][1], marker=".", s=dot, color=colors[8],alpha = alpha3) 
#    for i in range(len(T7)):
#        plt.scatter(T7[i][0], T7[i][1], marker=".", s=dot, color=colors[9],alpha = alpha3) 
#    for i in range(len(T8)):
#        plt.scatter(T8[i][0], T8[i][1], marker=".", s=dot, color=colors[0],alpha = alpha3) 
#    for i in range(len(T9)):
#        plt.scatter(T9[i][0], T9[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3) 
#    for i in range(len(T10)):
#        plt.scatter(T10[i][0], T10[i][1], marker=".", s=dot, color=colors[3],alpha = alpha3)
#    for i in range(len(T11)):
#        plt.scatter(T11[i][0], T11[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#    for i in range(len(T12)):
#        plt.scatter(T12[i][0], T12[i][1], marker=".", s=dot, color=colors[5],alpha = alpha3)
#    for i in range(len(T13)):
#        plt.scatter(T13[i][0], T13[i][1], marker=".", s=dot, color=colors[7],alpha = alpha3)
#    for i in range(len(T14)):
#        plt.scatter(T14[i][0], T14[i][1], marker=".", s=dot, color=colors[8],alpha = alpha3)
#    for i in range(len(T15)):
#        plt.scatter(T15[i][0], T15[i][1], marker=".", s=dot, color=colors[9],alpha = alpha3)
#    for i in range(len(T16)):
#        plt.scatter(T16[i][0], T16[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3)
#    for i in range(len(T17)):
#        plt.scatter(T17[i][0], T17[i][1], marker=".", s=dot, color=colors[3],alpha = alpha3)
#    for i in range(len(T18)):
#        plt.scatter(T18[i][0], T18[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#    for i in range(len(U_Pop)):
#        plt.scatter(U_Pop[i][0], U_Pop[i][1], s=s1, color=colors[2], marker='o',
#                                                                    alpha=alpha1)
#        plt.scatter(U_Pop[i][0], U_Pop[i][1], marker="1", s=80, color=colors[2])
#    for i in range(len(I_Pop)):
#        plt.scatter(I_Pop[i][0], I_Pop[i][1], s=s1, color=colors[3], marker='o',
#                                                                    alpha=alpha1)
#        plt.scatter(I_Pop[i][0], I_Pop[i][1], marker="1", s=dot, color=colors[3])
#    plt.scatter(I_Pop[0][0], I_Pop[0][1], s=s1, color=colors[3], marker='o',
#                                            alpha = alpha1)
#    plt.xlim(0, 30)
#    plt.ylim(0, 16)
#    plt.xlabel("\n Supermarket Layout (20 agents) ", fontsize=14)
#    #plt.ylabel("layout y-axis (m)", fontsize=14)
##    plt.grid(True)
#    plt.xticks([])
#    plt.yticks([])
##    ax.savefig('super_2m_20a.pdf', format='pdf', dpi=1400)
#    plt.show() 
    #_________________________________________________________________
    
    
    Agent_j = []
    traj_nex = T_traj(T1,U_Pop,I_Pop,I1)
    
    for i in range(len(I_Pop)-1):
        for j in range(len(U_Pop_2)):
            if (U_Pop_2[j][0] == I_Pop[i+1]):
                U_Pop_2[j][1] = 1
    
    
    traj_U1 = U_traj(T1,P1)
    U_Pop_2[0][0] = traj_U1[1]
    traj_U2 = U_traj(T1,P2)
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
    
    traj_U16 = U_traj(T14,P16)
    U_Pop_2[15][0] = traj_U16[1]
    traj_U17 = U_traj(T13,P17)
    U_Pop_2[16][0] = traj_U17[1]
    traj_U18 = U_traj(T12,P18)
    U_Pop_2[17][0] = traj_U18[1]
    traj_U19 = U_traj(T8,P19)
    U_Pop_2[18][0] = traj_U19[1]
    traj_U20 = U_traj(T16,P20)
    U_Pop_2[19][0] = traj_U20[1]
    
    
    traj_U21 = U_traj(T11,P21)
    U_Pop_2[20][0] = traj_U21[1]
    traj_U22 = U_traj(T6,P22)
    U_Pop_2[21][0] = traj_U22[1]
    traj_U23 = U_traj(T7,P23)
    U_Pop_2[22][0] = traj_U23[1]
    traj_U24 = U_traj(T15,P24)
    U_Pop_2[23][0] = traj_U24[1]
    traj_U25 = U_traj(T9,P25)
    U_Pop_2[24][0] = traj_U25[1]
    traj_U26 = U_traj(T14,P26)
    U_Pop_2[25][0] = traj_U26[1]
    traj_U27 = U_traj(T5,P27)
    U_Pop_2[26][0] = traj_U27[1]
    traj_U28 = U_traj(T1,P28)
    U_Pop_2[27][0] = traj_U28[1]
    traj_U29 = U_traj(T6,P29)
    U_Pop_2[28][0] = traj_U29[1]
    traj_U30 = U_traj(T4,P30)
    U_Pop_2[29][0] = traj_U30[1]
    
    
    traj_U31 = U_traj(T11,P31)
    U_Pop_2[30][0] = traj_U31[1]
    traj_U32 = U_traj(T6,P32)
    U_Pop_2[31][0] = traj_U32[1]
    traj_U33 = U_traj(T15,P33)
    U_Pop_2[32][0] = traj_U33[1]
    traj_U34 = U_traj(T3,P34)
    U_Pop_2[33][0] = traj_U34[1]
    traj_U35 = U_traj(T7,P35)
    U_Pop_2[34][0] = traj_U35[1]
    traj_U36 = U_traj(T2,P36)
    U_Pop_2[35][0] = traj_U36[1]
    traj_U37 = U_traj(T5,P37)
    U_Pop_2[36][0] = traj_U37[1]
    traj_U38 = U_traj(T1,P38)
    U_Pop_2[37][0] = traj_U38[1]
    traj_U39 = U_traj(T6,P39)
    U_Pop_2[38][0] = traj_U39[1]
    traj_U40 = U_traj(T4,P40)
    U_Pop_2[39][0] = traj_U40[1]
    
    traj_U41 = U_traj(T17,P41)
    U_Pop_2[40][0] = traj_U41[1]
    traj_U42 = U_traj(T17,P42)
    U_Pop_2[41][0] = traj_U42[1]
    traj_U43 = U_traj(T2,P43)
    U_Pop_2[42][0] = traj_U43[1]
    traj_U44 = U_traj(T1,P44)
    U_Pop_2[43][0] = traj_U44[1]
    traj_U45 = U_traj(T10,P45)
    U_Pop_2[44][0] = traj_U45[1]
    traj_U46 = U_traj(T10,P46)
    U_Pop_2[45][0] = traj_U46[1]
    traj_U47 = U_traj(T5,P47)
    U_Pop_2[46][0] = traj_U47[1]
    traj_U48 = U_traj(T1,P48)
    U_Pop_2[47][0] = traj_U48[1]
    traj_U49 = U_traj(T2,P49)
    U_Pop_2[48][0] = traj_U49[1]
    traj_U50 = U_traj(T4,P50)
    U_Pop_2[49][0] = traj_U50[1]
    
    
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
        
        traj_U21 = U_traj(traj_U21[0],traj_U21[1])
        U_Pop_2[20][0] = traj_U21[1]
        if (T1[0] == U_Pop_2[20][0] and 1 == U_Pop_2[20][1]):
            Inf_prev.append(U_Pop_2[20][0])
            U_Pop_2[20][1] = 0
    #    print(f'P11 = {P11}')
        traj_U22 = U_traj(traj_U22[0],traj_U22[1])
        U_Pop_2[21][0] = traj_U22[1]
        if (T1[0] == U_Pop_2[21][0] and 1 == U_Pop_2[21][1]):
            Inf_prev.append(U_Pop_2[21][0])
            U_Pop_2[21][1] = 0
    #    print(f'P12 = {P12}')
        traj_U23 = U_traj(traj_U23[0],traj_U23[1])
        U_Pop_2[22][0] = traj_U23[1]
        if (T1[0] == U_Pop_2[22][0] and 1 == U_Pop_2[22][1]):
            Inf_prev.append(U_Pop_2[22][0])
            U_Pop_2[22][1] = 0
    #    print(f'P13 = {P13}')
        traj_U24 = U_traj(traj_U24[0],traj_U24[1])
        U_Pop_2[23][0] = traj_U24[1]
        if (T1[0] == U_Pop_2[23][0] and 1 == U_Pop_2[23][1]):
            Inf_prev.append(U_Pop_2[23][0])
            U_Pop_2[23][1] = 0
        
        traj_U25 = U_traj(traj_U25[0],traj_U25[1])
        U_Pop_2[24][0] = traj_U25[1]
        if (T1[0] == U_Pop_2[24][0] and 1 == U_Pop_2[24][1]):
            Inf_prev.append(U_Pop_2[24][0])
            U_Pop_2[24][1] = 0
        
        traj_U26 = U_traj(traj_U26[0],traj_U26[1])
        U_Pop_2[25][0] = traj_U26[1]
        if (T1[0] == U_Pop_2[25][0] and 1 == U_Pop_2[25][1]):
            Inf_prev.append(U_Pop_2[25][0])
            U_Pop_2[25][1] = 0
        
        traj_U27 = U_traj(traj_U27[0],traj_U27[1])
        U_Pop_2[26][0] = traj_U27[1]
        if (T1[0] == U_Pop_2[26][0] and 1 == U_Pop_2[26][1]):
            Inf_prev.append(U_Pop_2[26][0])
            U_Pop_2[26][1] = 0
        
        traj_U28 = U_traj(traj_U28[0],traj_U28[1])
        U_Pop_2[27][0] = traj_U28[1]
        if (T1[0] == U_Pop_2[27][0] and 1 == U_Pop_2[27][1]):
            Inf_prev.append(U_Pop_2[27][0])
            U_Pop_2[27][1] = 0
        
        traj_U29 = U_traj(traj_U29[0],traj_U29[1])
        U_Pop_2[28][0] = traj_U29[1]
        if (T1[0] == U_Pop_2[28][0] and 1 == U_Pop_2[28][1]):
            Inf_prev.append(U_Pop_2[28][0])
            U_Pop_2[28][1] = 0
        
        traj_U30 = U_traj(traj_U30[0],traj_U30[1])
        U_Pop_2[29][0] = traj_U30[1]
        if (T1[0] == U_Pop_2[29][0] and 1 == U_Pop_2[29][1]):
            Inf_prev.append(U_Pop_2[29][0])
            U_Pop_2[29][1] = 0
        
        
        traj_U31 = U_traj(traj_U31[0],traj_U31[1])
        U_Pop_2[30][0] = traj_U31[1]
        if (T1[0] == U_Pop_2[30][0] and 1 == U_Pop_2[30][1]):
            Inf_prev.append(U_Pop_2[30][0])
            U_Pop_2[30][1] = 0
    #    print(f'P11 = {P11}')
        traj_U32 = U_traj(traj_U32[0],traj_U32[1])
        U_Pop_2[31][0] = traj_U32[1]
        if (T1[0] == U_Pop_2[31][0] and 1 == U_Pop_2[31][1]):
            Inf_prev.append(U_Pop_2[31][0])
            U_Pop_2[31][1] = 0
    #    print(f'P12 = {P12}')
        traj_U33 = U_traj(traj_U33[0],traj_U33[1])
        U_Pop_2[32][0] = traj_U33[1]
        if (T1[0] == U_Pop_2[32][0] and 1 == U_Pop_2[32][1]):
            Inf_prev.append(U_Pop_2[32][0])
            U_Pop_2[32][1] = 0
    #    print(f'P13 = {P13}')
        traj_U34 = U_traj(traj_U34[0],traj_U34[1])
        U_Pop_2[33][0] = traj_U34[1]
        if (T1[0] == U_Pop_2[30][0] and 1 == U_Pop_2[33][1]):
            Inf_prev.append(U_Pop_2[33][0])
            U_Pop_2[33][1] = 0
        
        traj_U35 = U_traj(traj_U35[0],traj_U35[1])
        U_Pop_2[34][0] = traj_U35[1]
        if (T1[0] == U_Pop_2[34][0] and 1 == U_Pop_2[34][1]):
            Inf_prev.append(U_Pop_2[34][0])
            U_Pop_2[34][1] = 0
        
        traj_U36 = U_traj(traj_U36[0],traj_U36[1])
        U_Pop_2[35][0] = traj_U36[1]
        if (T1[0] == U_Pop_2[36][0] and 1 == U_Pop_2[36][1]):
            Inf_prev.append(U_Pop_2[36][0])
            U_Pop_2[36][1] = 0
        
        traj_U37 = U_traj(traj_U37[0],traj_U37[1])
        U_Pop_2[36][0] = traj_U37[1]
        if (T1[0] == U_Pop_2[37][0] and 1 == U_Pop_2[37][1]):
            Inf_prev.append(U_Pop_2[37][0])
            U_Pop_2[37][1] = 0
        
        traj_U38 = U_traj(traj_U38[0],traj_U38[1])
        U_Pop_2[37][0] = traj_U38[1]
        if (T1[0] == U_Pop_2[38][0] and 1 == U_Pop_2[38][1]):
            Inf_prev.append(U_Pop_2[38][0])
            U_Pop_2[38][1] = 0
        
        traj_U39 = U_traj(traj_U39[0],traj_U39[1])
        U_Pop_2[38][0] = traj_U39[1]
        if (T1[0] == U_Pop_2[38][0] and 1 == U_Pop_2[38][1]):
            Inf_prev.append(U_Pop_2[38][0])
            U_Pop_2[38][1] = 0
        
        traj_U40 = U_traj(traj_U40[0],traj_U40[1])
        U_Pop_2[39][0] = traj_U40[1]
        if (T1[0] == U_Pop_2[39][0] and 1 == U_Pop_2[39][1]):
            Inf_prev.append(U_Pop_2[39][0])
            U_Pop_2[39][1] = 0
        
        
        traj_U41 = U_traj(traj_U41[0],traj_U41[1])
        U_Pop_2[40][0] = traj_U41[1]
        if (T1[0] == U_Pop_2[40][0] and 1 == U_Pop_2[40][1]):
            Inf_prev.append(U_Pop_2[40][0])
            U_Pop_2[40][1] = 0
    #    print(f'P11 = {P11}')
        traj_U42 = U_traj(traj_U42[0],traj_U42[1])
        U_Pop_2[41][0] = traj_U42[1]
        if (T1[0] == U_Pop_2[41][0] and 1 == U_Pop_2[41][1]):
            Inf_prev.append(U_Pop_2[41][0])
            U_Pop_2[41][1] = 0
    #    print(f'P12 = {P12}')
        traj_U43 = U_traj(traj_U43[0],traj_U43[1])
        U_Pop_2[42][0] = traj_U43[1]
        if (T1[0] == U_Pop_2[42][0] and 1 == U_Pop_2[42][1]):
            Inf_prev.append(U_Pop_2[42][0])
            U_Pop_2[42][1] = 0
    #    print(f'P13 = {P13}')
        traj_U44 = U_traj(traj_U44[0],traj_U44[1])
        U_Pop_2[43][0] = traj_U44[1]
        if (T1[0] == U_Pop_2[43][0] and 1 == U_Pop_2[43][1]):
            Inf_prev.append(U_Pop_2[43][0])
            U_Pop_2[43][1] = 0
        
        traj_U45 = U_traj(traj_U45[0],traj_U45[1])
        U_Pop_2[44][0] = traj_U45[1]
        if (T1[0] == U_Pop_2[44][0] and 1 == U_Pop_2[44][1]):
            Inf_prev.append(U_Pop_2[44][0])
            U_Pop_2[44][1] = 0
        
        traj_U46 = U_traj(traj_U46[0],traj_U46[1])
        U_Pop_2[45][0] = traj_U46[1]
        if (T1[0] == U_Pop_2[45][0] and 1 == U_Pop_2[45][1]):
            Inf_prev.append(U_Pop_2[45][0])
            U_Pop_2[45][1] = 0
        
        traj_U47 = U_traj(traj_U47[0],traj_U47[1])
        U_Pop_2[46][0] = traj_U47[1]
        if (T1[0] == U_Pop_2[46][0] and 1 == U_Pop_2[46][1]):
            Inf_prev.append(U_Pop_2[46][0])
            U_Pop_2[46][1] = 0
        
        traj_U48 = U_traj(traj_U48[0],traj_U48[1])
        U_Pop_2[47][0] = traj_U48[1]
        if (T1[0] == U_Pop_2[47][0] and 1 == U_Pop_2[47][1]):
            Inf_prev.append(U_Pop_2[47][0])
            U_Pop_2[47][1] = 0
        
        traj_U49 = U_traj(traj_U49[0],traj_U49[1])
        U_Pop_2[48][0] = traj_U49[1]
        if (T1[0] == U_Pop_2[48][0] and 1 == U_Pop_2[48][1]):
            Inf_prev.append(U_Pop_2[48][0])
            U_Pop_2[48][1] = 0
        
        traj_U50 = U_traj(traj_U50[0],traj_U50[1])
        U_Pop_2[49][0] = traj_U50[1]
        if (T1[0] == U_Pop_2[49][0] and 1 == U_Pop_2[49][1]):
            Inf_prev.append(U_Pop_2[49][0])
            U_Pop_2[49][1] = 0
        
        
        I_Pop = [traj_nex[2]]
        U_Pop = []
        for i in range(len(U_Pop_2)):
            if (1 == U_Pop_2[i][1]):
                I_Pop.append(U_Pop_2[i][0])
            else:
                U_Pop.append(U_Pop_2[i][0])
        
         #_________________________________________________________________
         
#        ax=plt.figure(figsize=(10,7), facecolor='w', edgecolor='k') 
#        #plt.scatter(I_Pop[0][0], I_Pop[0][1], marker="1", s=dot, color=colors[3])
#        for i in range(len(T1)):
#            plt.scatter(T1[i][0], T1[i][1], marker=".", s=dot, color=colors[0],alpha = alpha3)
#        for i in range(len(T2)):
#            plt.scatter(T2[i][0], T2[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#        for i in range(len(T3)):
#            plt.scatter(T3[i][0], T3[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3)
#        for i in range(len(T4)):
#            plt.scatter(T4[i][0], T4[i][1], marker=".", s=dot, color=colors[5],alpha = alpha3) 
#        for i in range(len(T5)):
#            plt.scatter(T5[i][0], T5[i][1], marker=".", s=dot, color=colors[6],alpha = alpha3) 
#        for i in range(len(T6)):
#            plt.scatter(T6[i][0], T6[i][1], marker=".", s=dot, color=colors[8],alpha = alpha3) 
#        for i in range(len(T7)):
#            plt.scatter(T7[i][0], T7[i][1], marker=".", s=dot, color=colors[9],alpha = alpha3) 
#        for i in range(len(T8)):
#            plt.scatter(T8[i][0], T8[i][1], marker=".", s=dot, color=colors[0],alpha = alpha3) 
#        for i in range(len(T9)):
#            plt.scatter(T9[i][0], T9[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3) 
#        for i in range(len(T10)):
#            plt.scatter(T10[i][0], T10[i][1], marker=".", s=dot, color=colors[3],alpha = alpha3)
#        for i in range(len(T11)):
#            plt.scatter(T11[i][0], T11[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#        for i in range(len(T12)):
#            plt.scatter(T12[i][0], T12[i][1], marker=".", s=dot, color=colors[5],alpha = alpha3)
#        for i in range(len(T13)):
#            plt.scatter(T13[i][0], T13[i][1], marker=".", s=dot, color=colors[7],alpha = alpha3)
#        for i in range(len(T14)):
#            plt.scatter(T14[i][0], T14[i][1], marker=".", s=dot, color=colors[8],alpha = alpha3)
#        for i in range(len(T15)):
#            plt.scatter(T15[i][0], T15[i][1], marker=".", s=dot, color=colors[9],alpha = alpha3)
#        for i in range(len(T16)):
#            plt.scatter(T16[i][0], T16[i][1], marker=".", s=dot, color=colors[1],alpha = alpha3)
#        for i in range(len(T17)):
#            plt.scatter(T17[i][0], T17[i][1], marker=".", s=dot, color=colors[3],alpha = alpha3)
#        for i in range(len(T18)):
#            plt.scatter(T18[i][0], T18[i][1], marker=".", s=dot, color=colors[4],alpha = alpha3)
#        for i in range(len(U_Pop)):
#            plt.scatter(U_Pop[i][0], U_Pop[i][1], s=s1, color=colors[2], marker='o',
#                                                                        alpha=alpha1)
#            plt.scatter(U_Pop[i][0], U_Pop[i][1], marker="1", s=80, color=colors[2])
#        for i in range(len(I_Pop)):
#            plt.scatter(I_Pop[i][0], I_Pop[i][1], s=s1, color=colors[3], marker='o',
#                                                                        alpha=alpha1)
#            plt.scatter(I_Pop[i][0], I_Pop[i][1], marker="1", s=dot, color=colors[3])
#        plt.scatter(I_Pop[0][0], I_Pop[0][1], s=s1, color=colors[3], marker='o',
#                                                alpha = alpha1)
#        plt.xlim(0, 30)
#        plt.ylim(0, 16)
#        plt.xlabel("\n Supermarket Layout (20 agents) ", fontsize=14)
#        #plt.ylabel("layout y-axis (m)", fontsize=14)
#        #plt.grid(True)
#        plt.xticks([])
#        plt.yticks([])
#        #ax.savefig('super_2m_20a.pdf', format='pdf', dpi=1400)
#        plt.show() 
        # _________________________________________________________________
        
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
plt.bar(np.arange(lar), new_List, color = colors[1], alpha=0.7)
#plt.hist(new_List, color = "skyblue")
plt.xlabel("Number of potential newly infected (Total infected {})".format(sum(infec_num)), fontsize=16)
plt.ylabel("Repetition of cases (30 cm) (%)", fontsize=16)
plt.ylim(0, 20)
plt.rc('xtick', labelsize=14)    # fontsize of the tick labels
plt.rc('ytick', labelsize=14) 
#plt.grid(True)
#plt.xticks([])
#plt.yticks([])
#ax1.savefig('Test_corr_30cm_50a.pdf', format='pdf', dpi=1400)
plt.show() 
    
print ('\nTotal of possible newly infected in 1000 simulations (30 cm, 50a): {}'.format(sum(infec_num)) )

#lenT = (len(T1)+ len(T2)+ len(T3)+ len(T4)+ len(T5)+ len(T6)+ len(T7)+ len(T8) +
#        len(T18)+ len(T9)+ len(T10)+ len(T11)+ len(T12)+ len(T13)+ len(T14)+ 
#        len(T15) + len(T16) + len(T17))
#lenT
