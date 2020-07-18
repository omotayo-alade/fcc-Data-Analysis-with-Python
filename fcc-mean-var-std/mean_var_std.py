import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    else: 
        a = np.array(list).reshape(3,3)
        mean = [np.mean(a, axis=0), np.mean(a, axis=1), np.mean(a)]
        var = [np.var(a, axis=0), np.var(a, axis=1), np.var(a)]
        std = [np.std(a, axis=0), np.std(a, axis=1), np.std(a)]
        maxx = [np.max(a, axis=0), np.max(a, axis=1), np.max(a)]
        minn = [np.min(a, axis=0), np.min(a, axis=1), np.min(a)]
        summ = [np.sum(a, axis=0), np.sum(a, axis=1), np.sum(a)]

        mean = [i.tolist() for i in mean]
        var = [i.tolist() for i in var]
        std = [i.tolist() for i in std]
        maxx = [i.tolist() for i in maxx]
        minn = [i.tolist() for i in minn]
        summ = [i.tolist() for i in summ]

        calculations = {
                        'mean': mean,
                        'variance': var,
                        'standard deviation': std,
                        'max': maxx,
                        'min': minn,
                        'sum': summ
                        }
        return calculations