import os.path

import librosa
import numpy as np
import pandas as pd
from scipy.stats import skew, kurtosis


# Getting the  file paths included audio
audio_file = "audio path"
# y will contain the audio signal and sr will contain sample rate
y, sr = librosa.load(audio_file)

# Calculate the mean frequency
mean_frequency = librosa.feature.spectral_centroid(y=y, sr=sr)

# Calculate Standard Deviation and Variance
std_deviation = np.std(y)
variance = np.var(y)

# Calculate skewness and Kurtosis
skewness = skew(y)
kurt = kurtosis(y)

# Calculate Range
audio_range = np.max(y) - np.min(y)

# Calculate Percentiles
percentiles = np.percentile(y, [25, 50, 75])
# here 50 is the mean value also


# Data saving process .....
# Define the directory path where you want to save the csv file
output_dir = "output_folder"

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Create a DataFrame to store the results
data= {
    "Mean Frequency": mean_frequency,
    "Standard Deviation": [std_deviation],
    "Variance": [variance],
    "Skewness": [skewness],
    "kurtosis": [kurt],
    "Range": [audio_range],
    "25th Percentile": [percentiles[0]],
    "50th Percentile (Mean)": [percentiles[1]],
    "75th Percentile": [percentiles[2]]
}

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
output_csv_file = "output.csv"
df.to_csv(output_csv_file, index= True)