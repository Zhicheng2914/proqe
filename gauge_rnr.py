import numpy as np


class gauge_rnr:

    def __init__(self, data, dimension_USL, dimension_LSL, sigma):
        self.data = data
        self.dimension_USL = dimension_USL
        self.dimension_LSL = dimension_LSL
        self.sigma = sigma
        self.tolerance = dimension_USL - dimension_LSL

    def list_all_data(self):
        row = 0
        for row in range(0,10):
            for column in range(0,9):
                print(self.data[row][column], end=', ')
                column += 1
            print(end='\n')
            column = 0
            row +=1

    def basic_caculate(self):
        data_mean = np.mean(self.data)
        data_stdev = np.std(self.data)
        print(
            'mean: ', round(data_mean, 4), '\n'
            'stdev: ', round(data_stdev, 4)
        )
        return data_mean, data_stdev

    def transfer_to_std_matrix(self):
        singleop_data = []
        data_stdev = []
        for row in range(0,10):
            for column in range(0,9,3):
                for i in range(0,3):
                    singleop_data.append(self.data[row][column+i])
                singleop_stdev = np.std(singleop_data)
                data_stdev.append(singleop_stdev)
                singleop_data = []
                i = 0
        data_stdev=[data_stdev[i:i+3] for i in range(0,len(data_stdev),3)]
        # print('stdev matrix: ', '\n', data_stdev)
        return data_stdev

    def transfer_to_mean_matrix(self):
        singleop_data = []
        data_mean = []
        for row in range(0,10):
            for column in range(0,9,3):
                for i in range(0,3):
                    singleop_data.append(self.data[row][column+i])
                singleop_mean = np.mean(singleop_data)
                data_mean.append(singleop_mean)
                singleop_data = []
                i = 0
        data_mean=[data_mean[i:i+3] for i in range(0,len(data_mean),3)]
        # print('mean matrix: ', '\n', data_mean)
        return data_mean

    def repeatability(self):
        data_stdev = self.transfer_to_std_matrix()
        operator_1_stdev = []
        operator_2_stdev = []
        operator_3_stdev = []
        for row in range(0, 10):
            operator_1_stdev.append(data_stdev[row][0])
        for row in range(0, 10):
            operator_2_stdev.append(data_stdev[row][1])
        for row in range(0, 10):
            operator_3_stdev.append(data_stdev[row][2])
        repeatability_of_operator_1 = self.sigma * np.average(operator_1_stdev) / self.tolerance
        repeatability_of_operator_2 = self.sigma * np.average(operator_2_stdev) / self.tolerance
        repeatability_of_operator_3 = self.sigma * np.average(operator_3_stdev) / self.tolerance
        print(
            ' The repeatability of OP 1: {:.2%}\n'.format(repeatability_of_operator_1), 
            'The repeatability of OP 2: {:.2%}\n'.format(repeatability_of_operator_2), 
            'The repeatability of OP 3: {:.2%}\n'.format(repeatability_of_operator_3)
        )
        repeatability_list = []
        repeatability_list.append(repeatability_of_operator_1)
        repeatability_list.append(repeatability_of_operator_2)
        repeatability_list.append(repeatability_of_operator_3)
        repeatability = max(repeatability_list)
        print('The total repeatability is: {:.2%}\n'.format(repeatability))

    def reproducibility(self):
        data_mean = self.transfer_to_mean_matrix()
        sample_mean = []
        all_study_var = []
        all_reproducibility = []
        for row in range(0,10):
            single_sample_mean = np.mean(self.data[row])
            sample_mean.append(single_sample_mean)
        for row in range(0,10):
            single_study_var = self.sigma * np.sqrt(pow((data_mean[row][0] - sample_mean[row]),2) + pow((data_mean[row][1] - sample_mean[row]),2) + pow((data_mean[row][2] - sample_mean[row]),2))
            single_reproducibility = (4 * single_study_var) / self.tolerance
            all_study_var.append(single_study_var)
            all_reproducibility.append(single_reproducibility)
            reproducibility = np.mean(all_reproducibility)

        print('The total reproducibility is: {:.2%}\n'.format(reproducibility))
        

CTF704_DATA = [[0.096, 0.1001, 0.103, 0.1007, 0.0985, 0.0973, 0.0954, 0.0965, 0.0952],
[0.0145, 0.0191, 0.0204, 0.0195, 0.0129, 0.0149, 0.013, 0.0178, 0.0191],
[0.096, 0.0923, 0.0988, 0.0894, 0.0952, 0.1021, 0.094, 0.0933, 0.0995],
[0.0948, 0.1001, 0.1005, 0.0918, 0.1008, 0.0944, 0.1001, 0.0996, 0.1],
[0.0345, 0.0394, 0.031, 0.0307, 0.0349, 0.0404, 0.0283, 0.0319, 0.0355],
[0.117, 0.1185, 0.1209, 0.1126, 0.1187, 0.113, 0.1227, 0.1218, 0.1216],
[0.0662, 0.0624, 0.0656, 0.0598, 0.0699, 0.0659, 0.061, 0.065, 0.0648],
[0.1733, 0.1806, 0.1849, 0.1828, 0.1845, 0.1847, 0.1722, 0.1763, 0.178],
[0.0752, 0.0638, 0.0652, 0.0745, 0.0695, 0.0724, 0.0708, 0.0664, 0.0652],
[0.046, 0.0449, 0.0419, 0.0452, 0.0496, 0.0533, 0.0519, 0.0461, 0.0514]]

CTF704 = gauge_rnr(CTF704_DATA,1.1,0,4)

# CTF704.list_all_data()
# CTF704.basic_caculate()
CTF704.repeatability()
CTF704.reproducibility()

'''
var = (data_mean[0][0] - sample_mean[0])^2 + (data_mean[0][1] - sample_mean[0])^2 + (data_mean[0][2] - sample_mean[0])^2
data_mean[1][0] - sample_mean[1]
data_mean[1][2] - sample_mean[1]

'''