'''
process capability index
'''

import numpy as np

class process_capability_index: 

    def __init__(self, data, dimension_USL, dimension_LSL, gdt_flag):
        self.data = data
        self.dimension_USL = dimension_USL
        self.dimension_LSL = dimension_LSL
        self.gdt_flag = gdt_flag
   
    def basic_caculate(self):
        data_mean = np.mean(self.data)
        data_stdev = np.std(self.data)
        data_stdev_sampling = np.std(self.data, ddof=1)
        data_max = max(self.data)
        data_min = min(self.data)
        return print(
            'basic caculate results: ', "\n", 
            'mean: ', format(data_mean, '.2f'), "\n", 
            'stdev: ', format(data_stdev,'.2f'), '\n', 
            'max: ', format(data_max,'.2f'), '\n', 
            'min: ', format(data_min,'.2f')
        )

    def cpk_l(self):
        data_mean = np.mean(self.data)
        data_stdev = np.std(self.data)
        cpk_l = (data_mean - self.dimension_LSL) / (3 * data_stdev)
        return print(
            'cpk lower: ', format(cpk_l, '.2f')
        )

    def cpk_u(self):
        data_mean = np.mean(self.data)
        data_stdev = np.std(self.data)
        cpk_u = (self.dimension_USL - data_mean) / (3 * data_stdev)
        return print(
            'cpk upper: ', format(cpk_u, '.2f')
        )

    def cpk(self):
        data_mean = np.mean(self.data)
        data_stdev = np.std(self.data)
        cpk_l = (data_mean - self.dimension_LSL) / (3 * data_stdev)
        cpk_u = (self.dimension_USL - data_mean) / (3 * data_stdev)

        if self.gdt_flag == 0:
            cpk = max(cpk_l, cpk_u)
        elif self.gdt_flag == 1:
            cpk = cpk_u
        else:
            print("gdt_flag incorrect")
        
        return print(
            'cpk: ', format(cpk, '.2f')
            )

CTF201_DATA = [280.3444, 280.3151, 280.3206, 280.3216, 280.3048, 280.3248, 280.3033, 280.2902, 280.307, 280.319, 280.2959, 280.303, 280.2832, 280.2692, 280.3005, 280.286, 280.29, 280.2681, 280.2919, 280.2886, 280.2853, 280.2885, 280.2918, 280.33, 280.3458, 280.3482, 280.3293, 280.3111, 280.3287, 280.332, 280.3508, 280.3338, 280.3374, 280.3296, 280.3252, 280.317, 280.3198, 280.3294, 280.3323, 280.3162, 280.3575, 280.3176, 280.3006, 280.3417, 280.339, 280.33, 280.2911, 280.3296, 280.3813, 280.3629, 280.3525, 280.347, 280.3572]
CTF201 = process_capability_index(CTF201_DATA, 280.15, 280.41, 0)
CTF201.basic_caculate()
CTF201.cpk_l()
CTF201.cpk_u()
CTF201.cpk()