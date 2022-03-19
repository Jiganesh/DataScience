import numpy as np

def calculate(list):
  if len(list) ==9:
    array = np.array(list);
    matrix = array.reshape((3,3))
    mean1 = matrix.mean(axis =0).tolist()
    mean2 = matrix.mean(axis =1).tolist()
    mean3 = matrix.mean()
    lmean =[mean1, mean2, mean3]
  
    
    variance1 = matrix.var(axis=0).tolist()
    variance2 = matrix.var(axis=1).tolist()
    variance3 = matrix.var()
    lvariance = [variance1, variance2, variance3]
  
    std1 = matrix.std(axis=0).tolist()
    std2 = matrix.std(axis=1).tolist()
    std3 = matrix.std()
    lstd =[std1, std2, std3]
  
    max1 = matrix.max(axis=0).tolist()
    max2 = matrix.max(axis=1).tolist()
    max3 = matrix.max()
    lmax = [max1, max2, max3]
  
    min1 = matrix.min(axis=0).tolist()
    min2 = matrix.min(axis=1).tolist()
    min3 = matrix.min()
    lmin = [min1, min2, min3]
  
    sum1 = matrix.sum(axis=0).tolist()
    sum2 = matrix.sum(axis=1).tolist()
    sum3 = matrix.sum()
    lsum = [sum1, sum2, sum3]
  
    calculations = {'mean':lmean, 'variance': lvariance, 'standard deviation': lstd, 'max':lmax , 'min':lmin ,'sum':lsum}
    
    return calculations
  else :
    raise ValueError ("List must contain nine numbers.")
  
    

  