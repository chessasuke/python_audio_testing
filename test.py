


import numpy as np


if __name__ == "__main__":

    wave = [127, -128, 123, 56, -45, 23, 45, 12]
    
    for rec in enumerate(wave):
        print('rec')
        print(rec)
        # Normalize the signal
        rec_norm = rec/((np.max(rec)-np.min(rec))*0.5)
        print('rec_norm')
        print(rec_norm)