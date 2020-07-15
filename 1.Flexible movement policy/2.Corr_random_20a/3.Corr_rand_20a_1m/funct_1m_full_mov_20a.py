# -*- coding: utf-8 -*-
"""
                            Functions Code

Platform for testing potential COVID-19 spread in Supermarkets

@author: Gustavo Hernandez Mejia
"""
import matplotlib.pyplot as plt
import math 
import random

prop_cycle = plt.rcParams['axes.prop_cycle'] #Colors
colors = prop_cycle.by_key()['color']

s1=1000  # 3500
s2=1900
alpha1=0.20
#_____________________ Scene 1 GENERAL MODEL___________________________________
"""
                        Agents and input parameters
"""


addi = 1
multi = 1

T1 = []
sis_1 = 12 * multi
for i in range(1, sis_1):
    T1.append([(i*addi)+1,2])
    
T2 = []
sis_2 = 15 * multi
for i in range(1, sis_2):
    T2.append([(i*addi)+12,2])
for i in range(0, 5):
    T2.append([27,(i*addi)+2])

T3 = []
sis_3 = 4 * multi
for i in range(0, sis_3):
    T3.append([27,(i*addi)+7])

#T4 = [[26,6],[25,6],[24,6],[23,6],[22,6],[21,6],[20,6]]
T4 = []
sis_4 = 7 * multi 
for i in range(sis_4+1, 0, -1):
    T4.append([(i*addi)+19,6])

#T5 = [[19.5,6],[18,6],[17,6],[16,6],[15,6],[14,6],[13,6],[12,6]]
T5 = []
sis_5 = 8 * multi
for i in range(sis_5, 0,-1):
    T5.append([(i*addi)+11,6])

#T6 = [[27,10.5],[27,12],[27,13],[27,14],[26,14],[25,14],[24,14],[23,14],[22,14],
#                                                              [21,14],[20,14]]
T6 = []
sis_6 = 4 * multi
for i in range(0, sis_6):
    T6.append([27,(i*addi)+11])
for i in range(7, 0, -1):
    T6.append([(i*addi)+19,14])

#T7 = [[26.5,10],[25,10],[24,10],[23,10],[22,10],[21,10],[20,10]]
T7 = []
sis_7 = 7 * multi
for i in range(sis_7, 0,-1):
    T7.append([(i*addi)+19,10])

#T8 = [[20,10.5],[20,12],[20,13.5]]
T8 = []
sis_8 = 4 * multi
for i in range(0, sis_8-1):
    T8.append([20,(i*addi)+11])

#T9 = [[20,6.5 7],[20,8],[20,9.5]]
T9 = []
sis_9 = 4 * multi
for i in range(0, sis_9-1):
    T9.append([20,(i*addi)+7])

#T10= [[19.5,10],[18,10],[17,10],[16,10],[15,10],[14,10],[13,10],[12,10]]
T10 = []
sis_10 = 8 * multi
for i in range(sis_10, 0,-1):
    T10.append([(i*addi)+11,10])

#T11= [[19,14],[18,14],[17,14],[16,14],[15,14],[14,14],[13,14],[12,14]]
T11 = []
sis_11 = 8 * multi
for i in range(sis_11, 0,-1):
    T11.append([(i*addi)+11,14])

#T12= [[12,11],[12,12],[12,13]]
T12 = []
sis_12 = 3 * multi
for i in range(0, sis_12):
    T12.append([12,(i*addi) + 11])

#T13= [[12,7],[12,8],[12,9]]
T13 = []
sis_13 = 3 * multi
for i in range(0, sis_13):
    T13.append([12,(i*addi) + 7])

#T14= [[12,3],[12,4],[12,5]]
T14 = []
sis_14 = 3 * multi
for i in range(0, sis_14):
    T14.append([12,(i*addi) + 3])

#T15= [[11,6],[10,6],[9,6],[8,6],[7,6],[6,6],[5,6]]
#T15 = []
#sis_15 = 8 * 2
#for i in range(sis_15, 0,-1):
#    T15.append([(i*0.5)+3.5,6])
#
##T16= [[11,10.5],[10,11],[9,11],[8,11],[7,11],[6,11],[5,11]]
#T16 = []
#sis_16 = 6 * 2
#T16.append([11.5,10.2])
#T16.append([11,10.5])
#for i in range(sis_16, 0,-1):
#    T16.append([(i*0.5)+4.5,11])
#
##T17= [[11,14],[10,14],[9,14],[8,14],[7,14],[6,14],[5,14]]
#T17 = []
#sis_17 = 7 * 2
#for i in range(sis_17, 0,-1):
#    T17.append([(i*0.5)+4.5,14])

#T15= [[11,6],[10,6],[9,6],[8,6],[7,6],[6,6],[5,6]]
T15 = []
sis_15 = 8 * multi
T15.append([11.5,6.5])
T15.append([10.8,7.2])
for i in range(sis_15-2, 0,-1):
    T15.append([(i*addi)+4,8])

#T16= [[11,10.5],[10,11],[9,11],[8,11],[7,11],[6,11],[5,11]]
T16 = []
sis_16 = 6 * multi
T16.append([11,10.5])
#T16.append([11.4,10.5])
#T16.append([11.1,10.8])
for i in range(sis_16, 0,-1):
    T16.append([(i*addi)+4,11])

#T17= [[11,14],[10,14],[9,14],[8,14],[7,14],[6,14],[5,14]]
T17 = []
sis_17 = 7 * multi
for i in range(sis_17+1, 0,-1):
    T17.append([(i*addi)+4,14])
    
T18 = []
sis_18 = 8 * multi
for i in range(sis_18, 0,-1):
    T18.append([4,(i*addi)+6])
for i in range(4, 0,-1):
    T18.append([(i*addi)+0,6])

Min_dist = 1.5         # 1 m
No_content_prob = 0.5  # Bigger circle   original 0.5
content_prob = 0.35    # Smaller circle

#U_Pop = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, P13, P14, P15,
#                                                               CO1, CO2, CO3]
#I_Pop = [I1]
Agent_j = []


def T_traj(traj,U_Pop,I_Pop,Per): 
    
    paso = 1
    if traj == T1:
        ind = T1.index(Per) + paso
        if ind <= (len(T1)-1):
            Per = T1[T1.index(Per) + paso]
            next_traj = T1
#            print(f'T1:{Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T2
                Per = T2[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T14
                Per = T14[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
    
#    for i in range(len(traj)):
#        for j in range(len(U_Pop)):
#            h = (traj[i][0]- U_Pop[j][0])**2 + (traj[i][1]- U_Pop[j][1])**2
#            Dist = math.sqrt(h)
#            if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
#                I_Pop.append(U_Pop[j])
#                Agent_j.append(j)
#    indices1 = Agent_j
#    U_Pop = [i for j, i in enumerate(U_Pop) if j not in indices]  
#    Normal    
#    if traj == T1:
##        print('T1')
#        if (random.random() < 0.5):
#            next_traj = T2
#            Per = T2[0]
#        else:
#            next_traj = T14
#            Per = T14[0]
    if traj == T2:
#        print('T2')
        ind = T2.index(Per) + paso
        if ind <= (len(T2)-1):
            Per = T2[T2.index(Per) + paso]
            next_traj = T2
#            print(f'T2: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T3
                Per = T3[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T4
                Per = T4[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
                
    if traj == T3:
#        print('T3')
        ind = T3.index(Per) + paso
        if ind <= (len(T3)-1):
            Per = T3[T3.index(Per) + paso]
            next_traj = T3
#            print(f'T3: {Per}')
#            print(f'T1, {P}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T6
                Per = T6[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T7
                Per = T7[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
                
    if traj == T4:
#        print('T4')
        ind = T4.index(Per) + paso
        if ind <= (len(T4)-1):
            Per = T4[T4.index(Per) + paso]
            next_traj = T4
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T5
                Per = T5[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T9
                Per = T9[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T5:
#        print('T5')
        ind = T5.index(Per) + paso
        if ind <= (len(T5)-1):
            Per = T5[T5.index(Per) + paso]
            next_traj = T5
#            print(f'T5: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T14[::-1]
                Per = T14[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
            elif (random.random() < 0.5):
                next_traj = T13
                Per = T13[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
#                indices1 = Agent_j
            else:
                next_traj = T15
                Per = T15[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T6:
#        print('T6')
        ind = T6.index(Per) + paso
        if ind <= (len(T6)-1):
            Per = T6[T6.index(Per) + paso]
            next_traj = T6
#            print(f'T6: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T11
                Per = T11[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T8[::-1]
                Per = T8[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T7:
#        print('T7')
        ind = T7.index(Per) + paso
        if ind <= (len(T7)-1):
            Per = T7[T7.index(Per) + paso]
            next_traj = T7
#            print(f'T7: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T9[::-1]
                Per = T9[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T8
                Per = T8[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T10
                Per = T10[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
                
    if traj == T8:
#        print('T8')
        ind = T8.index(Per) + paso
        if ind <= (len(T8)-1):
            Per = T8[T8.index(Per) + paso]
            next_traj = T8
#            print(f'T8: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T11
            Per = T11[0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
            
    if traj == T9:
#        print('T9')
        ind = T9.index(Per) + paso
        if ind <= (len(T9)-1):
            Per = T9[T9.index(Per) + paso]
            next_traj = T9
#            print(f'T9: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T7[::-1]
                Per = T7[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T8
                Per = T8[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T10
                Per = T10[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T10:
#        print('T10')
        ind = T10.index(Per) + paso
        if ind <= (len(T10)-1):
            Per = T10[T10.index(Per) + paso]
            next_traj = T10
#            print(f'T10: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T13[::-1]
                Per = T13[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T16
                Per = T16[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T12
                Per = T12[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T11:
#        print('T11')
        ind = T11.index(Per) + paso
        if ind <= (len(T11)-1):
            Per = T11[T11.index(Per) + paso]
            next_traj = T11
#            print(f'T11: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T17
                Per = T17[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T12[::-1]
                Per = T12[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T12:
#        print('T12')
        ind = T12.index(Per) + paso
        if ind <= (len(T12)-1):
            Per = T12[T12.index(Per) + paso]
            next_traj = T12
#            print(f'T12: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T17
                Per = T17[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T11[::-1]
                Per = T11[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T13:
#        print('T13')
        ind = T13.index(Per) + paso
        if ind <= (len(T13)-1):
            Per = T13[T13.index(Per) + paso]
            next_traj = T13
#            print(f'T13: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T16
                Per = T16[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j    
            else:
                next_traj = T10[::-1]
                Per = T10[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T14:
#        print('T14')
        ind = T14.index(Per) + paso
        if ind <= (len(T14)-1):
            Per = T14[T14.index(Per) + paso]
            next_traj = T14
#            print(f'T14: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T13
                Per = T13[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T5[::-1]
                Per = T5[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T15
                Per = T15[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T15:
#        print('T15')
        ind = T15.index(Per) + paso
        if ind <= (len(T15)-1):
            Per = T15[T15.index(Per) + paso]
            next_traj = T15
#            print(f'T15: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T18
            Per = T18[2]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        
    if traj == T16:
#        print('T16')
        ind = T16.index(Per) + paso
        if ind <= (len(T16)-1):
            Per = T16[T16.index(Per) + paso]
            next_traj = T16
#            print(f'T16: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T18
            Per = T18[1]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        
    if traj == T17:
#        print('T17')
        ind = T17.index(Per) + paso
        if ind <= (len(T17)-1):
            Per = T17[T17.index(Per) + paso]
            next_traj = T17
#            print(f'T17: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T18
            Per = T18[0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        
    if traj == T18:
        ind = T18.index(Per) + paso
        if ind <= (len(T18)-1):
            Per = T18[T18.index(Per) + paso]
            next_traj = T18
#            print(f'T18: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
#        print('T17')
            next_traj = 0
    
    
    
    #    Inverted direction 
    if traj == T3[::-1]:
#        print('T3-')
        ind = T3[::-1].index(Per) + paso
        if ind <= (len(T3[::-1])-1):
            Per = T3[::-1][T3[::-1].index(Per) + paso]
            next_traj = T3[::-1]
#            print(f'T3-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T4
            Per = T4[0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        
    if traj == T4[::-1]:
#        print('T4-')
        ind = T4[::-1].index(Per) + paso
        if ind <= (len(T4[::-1])-1):
            Per = T4[::-1][T4[::-1].index(Per) + paso]
            next_traj = T4[::-1]
#            print(f'T4-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T3
            Per = T3[0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        
    if traj == T5[::-1]:
#        print('T5-')
        ind = T5[::-1].index(Per) + paso
        if ind <= (len(T5[::-1])-1):
            Per = T5[::-1][T5[::-1].index(Per) + paso]
            next_traj = T5[::-1]
#            print(f'T5-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T9
                Per = T9[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T4[::-1]
                Per = T4[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
        
    if traj == T7[::-1]:
#        print('T7-')
        ind = T7[::-1].index(Per) + paso
        if ind <= (len(T7[::-1])-1):
            Per = T7[::-1][T7[::-1].index(Per) + paso]
            next_traj = T7[::-1]
#            print(f'T7-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T6
                Per = T6[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T3[::-1]
                Per = T3[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T8[::-1]:
#        print('T8-')
        ind = T8[::-1].index(Per) + paso
        if ind <= (len(T8[::-1])-1):
            Per = T8[::-1][T8[::-1].index(Per) + paso]
            next_traj = T8[::-1]
#            print(f'T8-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T7[::-1]
                Per = T7[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T9[::-1]
                Per = T9[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T10
                Per = T10[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T9[::-1]:
#        print('T9-')
        ind = T9[::-1].index(Per) + paso
        if ind <= (len(T9[::-1])-1):
            Per = T9[::-1][T9[::-1].index(Per) + paso]
            next_traj = T9[::-1]
#            print(f'T9-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T5
                Per = T5[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T4[::-1]
                Per = T4[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T10[::-1]:
#        print('T10-')
        ind = T10[::-1].index(Per) + paso
        if ind <= (len(T10[::-1])-1):
            Per = T10[::-1][T10[::-1].index(Per) + paso]
            next_traj = T10[::-1]
#            print(f'T10-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T7[::-1]
                Per = T7[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            elif (random.random() < 0.5):
                next_traj = T9[::-1]
                Per = T9[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T8
                Per = T8[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            
    if traj == T11[::-1]:
#        print('T11-')
        ind = T11[::-1].index(Per) + paso
        if ind <= (len(T11[::-1])-1):
            Per = T11[::-1][T11[::-1].index(Per) + paso]
            next_traj = T11[::-1]
#            print(f'T11-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            next_traj = T8[::-1]
            Per = T8[::-1][0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
            
    if traj == T12[::-1]:
#        print('T12-')
        ind = T12[::-1].index(Per) + paso
        if ind <= (len(T12[::-1])-1):
            Per = T12[::-1][T12[::-1].index(Per) + paso]
            next_traj = T12[::-1]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T16
                Per = T16[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T10[::-1]
                Per = T10[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
        
    if traj == T13[::-1]:
#        print('T13-')
        ind = T13[::-1].index(Per) + paso
        if ind <= (len(T13[::-1])-1):
            Per = T13[::-1][T13[::-1].index(Per) + paso]
            next_traj = T13[::-1]
#            print(f'T13-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
            indices1 = Agent_j
        else:
            if (random.random() < 0.5):
                next_traj = T15
                Per = T15[0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
                indices1 = Agent_j
            else:
                next_traj = T5[::-1]
                Per = T5[::-1][0]
                for j in range(len(U_Pop)):
                    h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                    Dist = math.sqrt(h)
                    if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                        I_Pop.append(U_Pop[j])
                        Agent_j.append(j)
#                indices1 = Agent_j
            
    if traj == T14[::-1]:
#        print('T14-')
        ind = T14[::-1].index(Per) + paso
        if ind <= (len(T14[::-1])-1):
            Per = T14[::-1][T14[::-1].index(Per) + paso]
            next_traj = T14[::-1]
#            print(f'T14-: {Per}')
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
#            indices1 = Agent_j
        else:
            next_traj = T2
            Per = T2[0]
            for j in range(len(U_Pop)):
                h = (Per[0]- U_Pop[j][0])**2 + (Per[1]- U_Pop[j][1])**2
                Dist = math.sqrt(h)
                if (Dist <= Min_dist) and (random.random() < No_content_prob) and (U_Pop[j] not in I_Pop):
                    I_Pop.append(U_Pop[j])
                    Agent_j.append(j)
#            indices1 = Agent_j
    
    
    return next_traj, I_Pop, Per





def U_traj(traj,P): 
    
                  
    paso = 1
    if traj == T1:
        ind = T1.index(P) + paso
        if ind <= (len(T1)-1):
            P = T1[T1.index(P) + paso]
            next_traj = T1
#            print(f'T1, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T2
                P = T2[0]
#                print(f'T2, {P}')
            else:
                next_traj = T14
                P = T14[0]
#                print(f'T14, {P}')
            

    if traj == T2:
        ind = T2.index(P) + paso
        if ind <= (len(T2)-1):
            P = T2[T2.index(P) + paso]
            next_traj = T2
#            print(f'T2, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T3
                P = T3[0]
#                print(f'T3, {P}')
            else:
                next_traj = T4
                P = T4[0]
#                print(f'T4, {P}')



    if traj == T3:
        ind = T3.index(P) + 3
        if ind <= (len(T3)-1):
           P = T3[T3.index(P) + paso]
           next_traj = T3
#           print(f'T3, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T6
                P = T6[0]
#                print(f'T6, {P}')
            else:
                next_traj = T7
                P = T7[0]
#                print(f'T7, {P}')
                
    if traj == T4:
        ind = T4.index(P) + paso
        if ind <= (len(T4)-1):
           P = T4[T4.index(P) + paso]
           next_traj = T4
#           print(f'T4, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T5
                P = T5[0]
#                print(f'T5, {P}')
            else:
                next_traj = T9
                P = T9[0]
#                print(f'T9, {P}')
                
    if traj == T5:
        ind = T5.index(P) + paso
        if ind <= (len(T5)-1):
           P = T5[T5.index(P) + paso]
           next_traj = T5
#           print(f'T5, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T14[::-1]
                P = T14[0]
#                print(f'T14, {P}')
            else: 
#            (random.random() < 0.5):
                next_traj = T13
                P = T13[0]
#                print(f'T13, {P}')
#            else:
#                next_traj = T15
#                P = T15[0]
#                print(f'T15, {P}')
            
    if traj == T6:
        ind = T6.index(P) + paso
        if ind <= (len(T6)-1):
           P = T6[T6.index(P) + paso]
           next_traj = T6
#           print(f'T6, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T11
                P = T11[0]
#                print(f'T11, {P}')
            else:
                next_traj = T8[::-1]
                P = T8[0]
#                print(f'T8, {P}')
            
    if traj == T7:
        ind = T7.index(P) + paso
        if ind <= (len(T7)-1):
           P = T7[T7.index(P) + paso]
           next_traj = T7
#           print(f'T7, {P}')
        else:   
            if (random.random() < 0.5):
                next_traj = T9[::-1]
                P = T9[0]
#                print(f'T9, {P}')
            elif (random.random() < 0.5):
                next_traj = T8
                P = T8[0]
#                print(f'T8, {P}')
            else:
                next_traj = T10
                P = T10[0]
#                print(f'T10, {P}')
            
    if traj == T8:
#        ind = T8.index(P) + 3
#        if ind <= (len(T8)-1):
#           P = T8[T8.index(P) + 3]
#           next_traj = T8
##           print(f'T8, {P}')
#        else:
        next_traj = T11
        P = T11[0]
#            print(f'T11, {P}')
    
    
    if traj == T9:
#        ind = T9.index(P) + 3
#        if ind <= (len(T9)-1):
#           P = T9[T9.index(P) + 3]
#           next_traj = T9
##           print(f'T9, {P}')
#        else:
        if (random.random() < 0.5):
            next_traj = T7[::-1]
            P = T7[0]
#                print(f'T7, {P}')
        elif (random.random() < 0.5):
            next_traj = T8
            P = T8[0]
#                print(f'T8, {P}')
        else:
            next_traj = T10
            P = T10[0]
#                print(f'T10, {P}')
    
    
    if traj == T10:
        ind = T10.index(P) + paso
        if ind <= (len(T10)-1):
           P = T10[T10.index(P) + paso]
           next_traj = T10
#           print(f'T10, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T13[::-1]
                P = T13[::-1][0]
#                print(f'T13, {P}')
            elif (random.random() < 0.5):
                next_traj = T16
                P = T16[0]
#                print(f'T16, {P}')
            else:
                next_traj = T12
                P = T12[0]
#                print(f'T12, {P}')
            
    if traj == T11:
        ind = T11.index(P) + paso
        if ind <= (len(T11)-1):
           P = T11[T11.index(P) + paso]
           next_traj = T11
#           print(f'T11, {P}')
        else:
#            next_traj = T12[::-1]
#            P = T12[0]
#            print(f'T12, {P}')
            if (random.random() < 0.5):
                next_traj = T17
                P = T17[0]
#                print(f'T17, {P}')
            else:
                next_traj = T12[::-1]
                P = T12[::-1][0]
#                print(f'T12, {P}')
            
    if traj == T12:
#        ind = T12.index(P) + 3
#        if ind <= (len(T12)-1):
#           P = T12[T12.index(P) + 3]
#           next_traj = T12
##           print(f'T12, {P}')
#        else:
#            next_traj = T11[::-1]
#            P = T11[0]
#            print(f'T11, {P}')
        if (random.random() < 0.5):
            next_traj = T17
            P = T17[0]
#                print(f'T17, {P}')
        else:
            next_traj = T11[::-1]
            P = T11[::-1][0]
#                print(f'T11, {P}')
    
    if traj == T13:
#        ind = T13.index(P) + 3
#        if ind <= (len(T13)-1):
#           P = T13[T13.index(P) + 3]
#           next_traj = T13
##           print(f'T13, {P}')
#        else:
#            next_traj = T10[::-1]
#            P = T10[0]
#            print(f'T10, {P}')
        if (random.random() < 0.5):
            next_traj = T16
            P = T16[0]
#                print(f'T16, {P}')
        elif (random.random() < 0.5):
            next_traj = T12
            P = T12[0]
        else:
            next_traj = T10[::-1]
            P = T10[::-1][0]
#                print(f'T10, {P}')
    
    if traj == T14:
#        ind = T14.index(P) + 3
#        if ind <= (len(T14)-1):
#           P = T14[T14.index(P) + 3]
#           next_traj = T14
##           print(f'T14, {P}')
#        else:
        if (random.random() < 0.5):
            next_traj = T13
            P = T13[0]
#                print(f'T13, {P}')
        elif(random.random() < 0.5):
            next_traj = T5[::-1]
            P = T5[::-1][0]
#                print(f'T5, {P}')
        else:
            next_traj = T15
            P = T15[0]
#                print(f'T15, {P}')1
            
    if traj == T15:
        ind = T15.index(P) + paso
        if ind <= (len(T15)-1):
           P = T15[T15.index(P) + paso]
           next_traj = T15
        else:
            next_traj = T18
            P = T18[2]
    
    if traj == T16:
        ind = T16.index(P) + paso
        if ind <= (len(T16)-1):
           P = T16[T16.index(P) + paso]
           next_traj = T16
        else:
            next_traj = T18
            P = T18[1]
    
    if traj == T17:
        ind = T17.index(P) + paso
        if ind <= (len(T17)-1):
           P = T17[T17.index(P) + paso]
           next_traj = T17
        else:
            next_traj = T18
            P = T18[0]
        
    if traj == T18:
        ind = T18.index(P) + paso    
        if ind <= (len(T18)-1):
           P = T18[T18.index(P) + paso]
           next_traj = T18
        else:
            next_traj = T1
            P = T1[0]
#            print('T1')
        
        
        
        
    
    #    Inverted direction 
    if traj == T3[::-1]:
        ind = T3[::-1].index(P) + paso
        if ind <= (len(T3[::-1])-1):
           P = T3[::-1][T3[::-1].index(P) + paso]
           next_traj = T3[::-1]
#           print(f'T3-, {P}')
        else:
            next_traj = T4
            P = T4[0]
#            print(f'T4, {P}')
    
    
    if traj == T4[::-1]:
        ind = T4[::-1].index(P) + paso
        if ind <= (len(T4[::-1])-1):
           P = T4[::-1][T4[::-1].index(P) + paso]
           next_traj = T4[::-1]
#           print(f'T4-, {P}')
        else:
            next_traj = T3
            P = T3[0]
#            print(f'T3, {P}')
        
        
    if traj == T5[::-1]:
        ind = T5[::-1].index(P) + paso
        if ind <= (len(T5[::-1])-1):
           P = T5[::-1][T5[::-1].index(P) + paso]
           next_traj = T5[::-1]
#           print(f'T5-, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T9
                P = T9[0]
#                print(f'T9, {P}')
            else:
                next_traj = T4[::-1]
                P = T4[::-1][0]
#                print(f'T4-, {P}')
            
            
    if traj == T7[::-1]:
        ind = T7[::-1].index(P) + paso
        if ind <= (len(T7[::-1])-1):
           P = T7[::-1][T7[::-1].index(P) + paso]
           next_traj = T7[::-1]
#           print(f'T7-, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T6
                P = T6[0]
#                print(f'T6, {P}')
            else:
                next_traj = T3[::-1]
                P = T3[::-1][0]
#                print(f'T3-, {P}')
            
    if traj == T8[::-1]:
#        ind = T8[::-1].index(P) + 3
#        if ind <= (len(T8[::-1])-1):
#           P = T8[::-1][T8[::-1].index(P) + 3]
#           next_traj = T8[::-1]
##           print(f'T8-, {P}')
#        else:
        if (random.random() < 0.5):
            next_traj = T7[::-1]
            P = T7[::-1][0]
#                print(f'T7-, {P}')
        elif (random.random() < 0.5):
            next_traj = T9[::-1]
            P = T9[::-1][0]
#                print(f'T9-, {P}')
        else:
            next_traj = T10
            P = T10[::-1][0]
#                print(f'T10-, {P}')
            
            
    if traj == T9[::-1]:
#        ind = T9[::-1].index(P) + 3
#        if ind <= (len(T9[::-1])-1):
#           P = T9[::-1][T9[::-1].index(P) + 3]
#           next_traj = T9[::-1]
##           print(f'T9-, {P}')
#        else:
            if (random.random() < 0.5):
                next_traj = T5
                P = T5[0]
    #                print(f'T5, {P}')
            else:
                next_traj = T4[::-1]
                P = T4[::-1][0]
#                print(f'T4-, {P}')
            
            
    if traj == T10[::-1]:
        ind = T10[::-1].index(P) + paso
        if ind <= (len(T10[::-1])-1):
           P = T10[::-1][T10[::-1].index(P) + paso]
           next_traj = T10[::-1]
#           print(f'T10-, {P}')
        else:
            if (random.random() < 0.5):
                next_traj = T7[::-1]
                P = T7[::-1][0]
#                print(f'T7-, {P}')
            elif (random.random() < 0.5):
                next_traj = T9[::-1]
                P = T9[::-1][0]
#                print(f'T9-, {P}')
            else:
                next_traj = T8
                P = T8[::-1][0]
#                print(f'T8-, {P}')
            
            
    if traj == T11[::-1]:
        ind = T11[::-1].index(P) + paso
        if ind <= (len(T11[::-1])-1):
           P = T11[::-1][T11[::-1].index(P) + paso]
           next_traj = T11[::-1]
#           print(f'T11-, {P}')
        else:
            next_traj = T8[::-1]
            P = T8[::-1][0]
#            print(f'T8-, {P}')
        
        
    if traj == T12[::-1]:
#        ind = T12[::-1].index(P) + 3
#        if ind <= (len(T12[::-1])-1):
#           P = T12[::-1][T12[::-1].index(P) + 3]
#           next_traj = T12[::-1]
##           print(f'T12-, {P}')
#        else:
#            next_traj = T10[::-1]
#            P = T10[::-1][0]
#            print(f'T10-, {P}')
        if (random.random() < 0.5):
            next_traj = T16
            P = T16[0]
#                print(f'T16, {P}')
        elif (random.random() < 0.5):
            next_traj = T10[::-1]
            P = T10[::-1][0]
#                print(f'T10-, {P}')
        else:
            next_traj = T13[::-1]
            P = T13[::-1][0]
                
            
            
    if traj == T13[::-1]:
#        ind = T13[::-1].index(P) + 3
#        if ind <= (len(T13[::-1])-1):
#           P = T13[::-1][T13[::-1].index(P) + 3]
#           next_traj = T13[::-1]
##           print(f'T13-, {P}')
#        else:
#            next_traj = T5[::-1]
#            P = T5[::-1][0]
#            print(f'T5-, {P}')
        if (random.random() < 0.5):
            next_traj = T14[::-1]
            P = T14[::-1][0]
#                print(f'T10-, {P}')
        elif (random.random() < 0.5):
            next_traj = T5[::-1]
            P = T5[::-1][0]
#                print(f'T10-, {P}')
        else:
            next_traj = T15
            P = T15[0]
            
            
    if traj == T14[::-1]:
#        ind = T14[::-1].index(P) + 3
#        if ind <= (len(T14[::-1])-1):
#           P = T14[::-1][T14[::-1].index(P) + 3]
#           next_traj = T14[::-1]
##           print(f'T14-, {P}')
#        else:
        next_traj = T2
        P = T2[0]
#            print(f'T2, {P}')
    
    
    return next_traj, P























