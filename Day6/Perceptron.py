# Perceptron class
import numpy as np

class Perceptron(object):
    # eta  1 0.1 0.01
    def __init__(self, eta=0.01, n_iter=10):
        self.eta =eta 
        self.n_iter= n_iter 
    
    '''
    X = Data
    y = Labels
    '''
    def fit(self,X ,y):
        self.w_ = np.zeros( 1 + X.shape[1])
        self.errors_ = []

        for e in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                # print(f"{target}( {xi} ) = {self.predict(xi)}")
                update = self.eta * ( target - self.predict(xi) )
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
                # print(f"Epoc {e}/{self.n_iter} error {errors} ({update}) of {xi} with {self.eta}")

            self.errors_.append(errors)
        
        return self 
    
    def net_input(self,X ):
        return np.dot(X, self.w_[1:]) + self.w_[0]
        
    def predict(self, X):
        return np.where( self.net_input(X) >= 0.0, 1, -1)

