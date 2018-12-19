# -*- coding: utf-8 -*-

"""Main module."""
import tensorflow as tf
import argparse
import math
import json
tf.enable_eager_execution()
tfe = tf.contrib.eager

def getinput(): # pragma: no cover
    input = argparse.ArgumentParser()
    input.add_argument('--data_table', default='[[0,0],[1.57079,6],[3.14159,0]]', help = 'Input of data table' )
    input.add_argument('--c', type = float, default = 1, help = 'Value of c, default = 1' )
    input.add_argument('--basis_size', type = int, default = 3, help = 'Size of basis set' )
    data = input.parse_args()
    data.data_table = json.loads(data.data_table)
    return data

def calculateLHSValue(data, index1, index2):

    # This function calculate the value of scalar.
    # input: data table, index number1, index number2
    # output: scalar

    scalar = 0
    if index1 % 2 == 0:
        if index2 % 2 == 0:
            for i in range(len(data)):
                scalar += math.cos(index2 / 2 * data[i][0])* math.cos(index1 / 2 * data[i][0])
            return scalar

        else:
            for i in range(len(data)):
                scalar += math.sin((index2 + 1) / 2 * data[i][0])* math.cos(index1 / 2 * data[i][0])
            return scalar
        
    else:
        if index2 % 2 == 0:
            for i in range(len(data)):
                scalar += math.cos(index2 / 2 * data[i][0])* math.sin((index1 + 1) / 2 * data[i][0])
            return scalar

        else:
            for i in range(len(data)):
                scalar += math.sin((index2 + 1) / 2 * data[i][0])* math.sin((index1 + 1) / 2 * data[i][0])
            return scalar    

def calculateV0(data, size):

    # This function calculate the V0 of given data.
    # input: data table, size of basis
    # output: V0

    RHS = []
    LHS = []
    for j in range(size):
        if j % 2 != 0:
            sumR = [0]
            scalarL = []
            for k in range(size):
                sumR[0] += math.sin((j + 1) / 2 *data[k][0])* data[k][1]
                scalarL.append(calculateLHSValue(data, j, k))
            RHS.append(sumR)
            LHS.append(scalarL)
            
        else:
            sumR = [0]
            scalarL = []
            for k in range(size):
                sumR[0] += math.cos(j / 2 *data[k][0])* data[k][1]
                scalarL.append(calculateLHSValue(data, j, k))
            RHS.append(sumR)
            LHS.append(scalarL)
    RHS_tensor = tf.Variable(RHS, dtype=tf.float32)
    LHS_tensor = tf.Variable(LHS, dtype=tf.float32)
    V0 = tf.linalg.solve(LHS_tensor, rhs = RHS_tensor)
    print(V0)
    return V0

def buildHHat(V0, size, c):

    # This function build the H hat matix.
    # input: V0, size of basis, c
    # output: H hat
    sess = tf.Session()
    with sess.as_default():
        v0=V0.numpy()
    hHat = [[v0[i][0]]* size for i in range(size)]
    for i in range(size):
        hHat[i][i] += i ** 2 * c
    hHat_tensor = tf.Variable(hHat, dtype=tf.float32)
    print(hHat)
    return hHat_tensor

def printResult(eighe, eighv): # pragma: no cover
    # This function print the result of lowest energy and corresponding wave function.
    # input: eigenvalue, eigenvector.
    # output: lowest energy and wave fucntion.
    for i in range(len(eighe)):
        if eighe[i] > 0 :
            print('The lowest energy is {:.2f}.'.format(eighe[i]))
            for k in range(len(eighv)):
                if k == 0 :
                    print('The scalar of 1 is {:.2f}'.format(eighv[i][k]))
                elif k % 2 == 0:
                    scalar = k / 2
                    print('The scalar of cos{0}x is {1:2f}.'.format(scalar,eighv[i][k]))
                else:
                    scalar = (k + 1) / 2
                    print('The scalar of sin{0}x is {1:2f}.'.format(scalar,eighv[i][k]))
            break
                 
def main(): # pragma: no cover

    # This function start the program.
    # input: /
    # output: /

    data = getinput()
    v0Hat=calculateV0(data.data_table,data.basis_size)
    hHat = buildHHat(v0Hat, data.basis_size, data.c)
    e_tensor, v_tensor = tf.linalg.eigh(hHat)
    sess = tf.Session()
    with sess.as_default():
        e=e_tensor.numpy()
        v=v_tensor.numpy()
    printResult(e,v)

if __name__ == "__main__":
    main()