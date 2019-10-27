'''
Name: Sidharth Banerjee
ID  : 1001622703
'''

import numpy as np
import pandas as pd

pulse0 = np.ones( 10 )
pulse0 = pulse0/np.linalg.norm(pulse0)
pulse1 = np.append( np.ones( 5 ), -1*np.ones( 5 ) )
pulse1 = pulse1/np.linalg.norm(pulse1)

def return_bit(df_10):
    u = np.array(df_10['Data'])
    similarity_0 =  abs((np.dot(u, pulse0))/(np.linalg.norm(u)*np.linalg.norm(pulse0)))
    similarity_1 =  abs((np.dot(u, pulse1))/(np.linalg.norm(u)*np.linalg.norm(pulse1)))
    if (similarity_1 > similarity_0):
        return 1
    else:
        return 0

def return_binary(list_8):
    b = map(str, list_8)
    binary_seq = ''.join(b)
    return binary_seq

df = pd.read_csv('data-communications.csv', header = None)
df = df.T
df.columns = ['Data']

data_bits = []
for i in range (0, len(df), 10):
    data_bits.append(return_bit(df[i:i+10]))

binary_data = []
for i in range (0, len(data_bits), 8):
    binary_data.append(return_binary(data_bits[i:i+8]))

sentence = ""
for i in range (0, len(binary_data), 1):
    sentence += chr(int(binary_data[i], 2))

print(sentence)
