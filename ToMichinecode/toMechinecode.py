import numpy as np
import pandas as pd

sentences = pd.read_csv('sourcecode.csv',sep='\n',header=None)
print(sentences)
R_type = {'mult':'000000','add':'000000','slt':'000000'}
LS_type = {'lw':'100011','sw':'101011'}
I_type = {'addi':'001000','beq':'000100'}
typee = {'mult':R_type,'add':R_type,'slt':R_type,'lw':LS_type,'sw':LS_type,'addi':I_type,'beq':I_type}

funct_code = {'mult':'011000','add':'100000','slt':101010}
sentences.rename(columns={0:'Source'},inplace=True)
sentences['INS'] = sentences['Source'].str.split(' ').str.get(0)
sentences['VAL'] = sentences['Source'].str.split(' ').str.get(1)

val_code = {'$0':0,
            '$at':1,
            '$v0':2,
            '$v1': 3,
            '$a0': 4,
            '$a1': 5,
            '$a2': 6,
            '$a3': 7,
            '$t0': 8,
            '$t1': 9,
            '$t2': 10,
            '$t3': 11,
            '$t4': 12,
            '$t5': 13,
            '$t6': 14,
            '$t7': 15,
            '$s0': 16,
            '$s1': 17,
            '$s2': 18,
            '$s3': 19,
            '$s4': 20,
            '$s5': 21,
            '$s6': 22,
            '$s7': 23,
            '$t8': 24,
            '$t9': 25,
            '$k0': 26,
            '$k1': 27,
            'gp': 28,
            'sp': 29,
            'fp': 30,
            'ra': 31,
            }

def z_ochange(char):
    if char=='0':
        return '1'
    else:
        return '0'


def buma(strr):
    strr = list(strr)
    lentt = len(strr)
    for i in range(lentt-1):
        strr[i+1] = (z_ochange(strr[i+1]))
    for j in range(len(strr)-1,0,-1):
        if strr[j] == '1':
            strr[j] = '0'
        else:
            strr[j] = '1'
            break
    strr[0] = '1'
    return ''.join(strr)
        






def fillbit(strr,goal):
    fill = '0'
    if strr[0] == '-':
        fill = '1'
        strr = buma(strr)
    lenthh = len(strr)
    for i in range(goal-lenthh):
        strr = fill + strr
    return strr

def tocode(row):
    INS = row['INS']
    VAL = row['VAL']
    if INS in typee:
        op = typee[INS][INS]
        if typee[INS] == R_type:
            fc = funct_code[INS]
            temp = VAL.split(sep=',')
            rs = fillbit(format(val_code[temp[1]],'b'),5)
            rt = fillbit(format(val_code[temp[2]], 'b'),5)
            rd = fillbit(format(val_code[temp[0]], 'b'),5)
            shamt = '00000'
            totcode = op + rs + rt + rd + shamt + fc
        elif typee[INS] == LS_type:
            VAL = VAL.replace('(',',').replace(')','')
            temp = VAL.split(sep=',')
            rs = fillbit(format(val_code[temp[2]],'b'),5)
            rt = fillbit(format(val_code[temp[0]],'b'),5)
            imm = fillbit(format(int(temp[1]),'b'),16)
            totcode = op + rs + rt + imm

        elif typee[INS] == I_type:
            temp = VAL.split(sep=',')
            rs = fillbit(format(val_code[temp[1]],'b'),5)
            rt = fillbit(format(val_code[temp[0]],'b'),5)
            imm = fillbit(format(int(temp[2]),'b'),16)
            totcode = op + rs + rt + imm
        else:
            totcode ='no_type'
    else:
        totcode = 'no_type'
    return totcode

sentences['bitcode'] = sentences.apply(tocode,axis=1)
sentences['bitcode'].to_csv('Bitcode.csv',sep='\n',index=False)
print(sentences['bitcode'])
