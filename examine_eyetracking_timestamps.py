import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np

fp = '/home/apocalyvec/Downloads/Pilot1_High_1.mat'
data = sio.loadmat(fp)


eyetracking_timestamps = data['Unity_VarjoEyeTracking'][0][1][0, :]
eyetraccking_timestamps_diff = np.diff(eyetracking_timestamps)

# fig, ax = plt.subplots(tight_layout=True)
plt.hist(eyetraccking_timestamps_diff,
         bins=np.linspace(4.9e-3, 5.1e-3, 1000))
plt.xlabel('Varjo eyetracking sampling interval')
plt.ylabel('Frequency')
plt.show()

np.mean(eyetraccking_timestamps_diff)
np.std(eyetraccking_timestamps_diff)