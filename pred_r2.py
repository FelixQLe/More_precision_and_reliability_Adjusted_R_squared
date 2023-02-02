
import numpy as np

class r_squared:
    """
    Calculation of 3 r_squared metrics
    unadjust r2, adjjust r2, and predicted r2 score
    """

    def __init__(self, y_true, y_pred, X):
        self.y_true = y_true
        self.y_pred = y_pred
        self.X = X

    def r2_score(self):
        """
            Calculation of the r-squared, goodness of fit metric
        """
        sse = sum(np.square(self.y_pred - self.y_true))
        mean = float(sum(self.y_true)) / float(len(self.y_true))
        sst = sum(np.square(self.y_true - mean))

        return 1. - sse/sst

    def adj_r2_score(self):
        """
        Adjust R-squared functions with fomular:
        Adjusted R2 = 1 – [(1-R2)*(n-1)/(n-k-1)]
        R2 = R-squared, n = number of samples/rows in the data set, p = number of predictors/ features
        """
        #def adj_r_squared(model, X, y):
        r2 = r_squared.r2_score(self)

        return 1 - (((1 - r2) * (len(self.X) - 1)) / (len(self.X) - len(self.X.columns) - 1))

    #@classmethod
    def press_statistic(self):
        """
        Calculation of the `Press Statistics <https://www.otexts.org/1580>`_
        """
        res = self.y_pred - self.y_true
        if int(self.X.shape[1]) >= 2000: #dataset more than 2000 features will cause SVD error
            #to demontrate the problem, in reality we dont need this if and else
            hat = self.X.iloc[:,:2000].dot(np.linalg.pinv(self.X.iloc[:,:2000]))
        else:
            hat = self.X.dot(np.linalg.pinv(self.X))
        den = (1 - np.diagonal(hat))
        sqr = np.square(res/den)

        return sqr.sum()

    def predicted_r2_score(self):

        """
        Calculation of the `Predicted R-squared <https://rpubs.com/RatherBit/102428>`_
        """
        press = r_squared.press_statistic(self)
        sst  = np.square(self.y_true - self.y_true.mean() ).sum()

        return 1 - press / sst
