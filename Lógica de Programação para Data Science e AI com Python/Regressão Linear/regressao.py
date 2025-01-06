import numpy as np
def correlacao(x, y):
    covariacao = np.cov(x, y, bias=True) [0][1]
    variancia_x = np.var(x)
    variancia_y = np.var(y)
    return covariacao / np.sqrt(variancia_x) * variancia_y

def inclinacao(x,y, correlacao):
    stdx = np.std(x)
    stdy = np.std(y)
    return correlacao * (stdy / stdx)

def interceptacao (x, y, inclinacao):
    mediax = np.mean (x)
    mediay = np.mean(y)
    return mediay - mediax * inclinacao 

def previsao(interceptacao, inclinacao, valor):
    return interceptacao + (inclinacao*valor)
    