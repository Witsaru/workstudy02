import matplotlib.pyplot as plt
import numpy as np

class plotlib():
    def __init__(self):
        super().__init__()
        #self.process_round_time_s = {}
        self.round_time = {
                            'Step1': [0.7448, 0.8665, 0.7426, 0.9836, 1.0472, 0.9129, 0.6995, 2.0379, 0.6471, 1.67], 
                            'Step2': [1.5781, 1.5152, 1.568, 2.4691, 1.9675, 1.0511, 2.6231, 1.2264, 2.1881, 2.2667], 
                            'Step3': [0.8925, 0.8429, 1.0056, 1.0523, 1.8994, 0.9718, 0.6657, 0.892, 1.0807, 1.0888], 
                            'Step4': [2.1616, 1.8578, 1.726, 1.8549, 1.5327, 1.8751, 6.0498, 2.4227, 1.5315, 1.6678], 
                            'Step5': [1.7215, 1.1483, 1.2953, 1.055, 1.0239, 0.8706, 0.7563, 1.5349, 0.9478, 1.2382], 
                            'Step6': [9.0788, 9.0626, 9.0274, 8.7963, 9.8892, 9.6912, 10.633, 10.4639, 8.4693, 7.3155], 
                            'Step7': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
                           }
        
        self.num_key = 0
        self.list_time_process = []
        self.sum_time_process = []
        self.last_sum = 0

    def process_round_time_s(self, time):
        for x, y in time.items():
            self.list_time_process.append(y)
            self.num_key = len(y)

        list_t_p_array = np.array(self.list_time_process)
        # print(list_t_p_array.shape)
        # print(list_t_p_array[0:9,1])
        for i in range(self.num_key):
            sum_list = list_t_p_array[0:self.num_key,i]

            self.last_sum = sum_list.sum()
            self.sum_time_process.append(sum_list.sum())

        return self.last_sum

    
        # return fig


if __name__ == "__main__":
    plotlib().process_round_time_s()