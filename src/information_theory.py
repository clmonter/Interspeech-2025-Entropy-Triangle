import numpy as np

######################
## Marginal and joint entropies
######################

def entropy(C):

    # Input:
    # C: confussion matrix

    # where 
    # X ~ P(x) : real labels
    # Y ~ P(y) : predicted labels

    # Outputs:
    # entropy of r.v. X H(x)
    # entropy of r.v. Y H(y)
    # joint entropy between two r.v.'s H(x,y)

    N = np.sum(C)

    marginals_x = np.sum(C, axis=1)/N
    marginals_y = np.sum(C, axis=0)/N

    ## assert non-zero marginals (otherwise, the logarithm would be indetermined)
    #marginals_x = marginals_x[marginals_x > 0]
    #marginals_y = marginals_y[marginals_x > 0]

    accum_x = 0
    accum_y = 0

    for i in range(len(marginals_x)):
        prob_x = marginals_x[i]
        prob_y = marginals_y[i]

        if prob_x != 0:
            accum_x = accum_x + (prob_x * np.log2(prob_x))

        if  prob_y != 0:
            accum_y = accum_y + (prob_y * np.log2(prob_y))

    #H_x = - np.sum(marginals_x * np.log2(marginals_x))
    #H_y = - np.sum(marginals_y * np.log2(marginals_y))

    H_x = - accum_x
    H_y = - accum_y

    C_prob = C/N

    operations = []

    for i in range(C_prob.shape[0]):
        for j in range(C_prob.shape[1]):      

            if C_prob[i,j] == 0:
                oper = 0

            else:
                oper = C_prob[i,j] * np.log2(C_prob[i,j])

            operations.append(oper)

    #operations = np.nan_to_num(operations)

    H_xy = - np.sum(operations)

    return H_x, H_y, H_xy

######################
## Conditional entropies
######################

def conditional_entropy(C):
    
  # Input:
  # C: confussion matrix

  # where 
  # X ~ P(x) : real labels
  # Y ~ P(y) : predicted labels

  # Outputs:
  # conditional entropy H p(x|y)
  # conditional entropy H p(y|x)

  ## Theory
  # H(A|B) = - sum {p(A,B) * log (p(A|B))}
  # p(A|B) = P(A∩B)/P(B)

  N = np.sum(C) # Number of samples

  marginals_x = np.sum(C, axis=1)/N # P(x)
  marginals_y = np.sum(C, axis=0)/N # P(y)

  ## assert non-zero marginals (otherwise, the logarithm would be indetermined)
  #marginals_x = marginals_x[marginals_x > 0]
  #marginals_y = marginals_y[marginals_x > 0]

  C_prob = C/N

  operations_x = []
  operations_y = []

  for i in range(C_prob.shape[0]):
    for j in range(C_prob.shape[1]):
      
        if C_prob[i,j] == 0 or marginals_y[j]==0:
           oper_x = 0
        
        if C_prob[i,j] == 0 or marginals_y[j]==0:
           oper_y = 0

        if C_prob[i,j]!=0 and marginals_y[j]!=0:
            oper_x = C_prob[i,j] * np.log2((C_prob[i,j])/marginals_y[j])
        
        if C_prob[i,j]!=0 and marginals_x[j]!=0:
            oper_y = C_prob[i,j] * np.log2((C_prob[i,j])/marginals_x[i])

        operations_x.append(oper_x)
        operations_y.append(oper_y)

  #operations_x = np.nan_to_num(operations_x)
  #operations_y = np.nan_to_num(operations_y)

  H_pxy = - np.sum(operations_x) # H(x|y)
  H_pyx = - np.sum(operations_y) # H(y|x)

  return H_pxy, H_pyx

def calculate_everything(cm, normalize=True):
    
    ## First, we calculate the entropy of the uniform distribution
    C = cm.shape[0] 
    Ux = Uy = 1/C
    H_Ux = H_Uy = np.log2(C)

    H_x, H_y, H_xy = entropy(cm)

    # BLUE: Redundance or divergence with respect to the uniformity
    delta_H_x = H_Ux - H_x
    delta_H_y = H_Uy - H_y

    # RED: Variation of information
    H_pxy, H_pyx = conditional_entropy(cm)

    # GREEN: Mutual information
    mi = H_x + H_y - H_xy

    if normalize == True:
        # BLUE: Redundance or divergence with respect to the uniformity
        delta_H_x = delta_H_x/H_Ux
        delta_H_y = delta_H_y/H_Uy

        # RED: Variation of information
        H_pxy = H_pxy/H_Ux
        H_pyx = H_pyx/H_Uy

        # GREEN: Mutual information
        mi = mi/H_Ux

    metrics = {'x': [delta_H_x, mi, H_pxy],
               'y': [delta_H_y, mi, H_pyx]}
    
    return metrics