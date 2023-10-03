import wave
import numpy as np
import os

# Get the current directory where the script is located
current_directory = os.path.dirname(os.path.abspath(__file__))

# Define the output directory path
output_directory = os.path.join(current_directory, "output")

# Ensure the output directory exists, create it if if doesn't
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Input WAV file path
input_wav_path = os.path.join(current_directory, "input.wav")


#open the wav file
with wave.open("input.wav", "rb") as wav_file:

    # Get the audio parameters
    sample_width = wav_file.getsampwidth()
    sample_rate = wav_file.getframerate()
    num_frames = wav_file.getnframes()
    num_channels = wav_file.getnchannels()

    # Read the audio data
    audio_data = wav_file.readframes(num_frames)

# Convert to NumPy array

#Convert the audio data to a NumPy array
audio_array = np.frombuffer(audio_data, dtype=np.int16)

# Apply Fourier Transform
# Now, we apply the FFT to transform the audio signal
# from the time domain to the frequency domain.
# The FFT converts a signal from its time representation to
# a representation in the frequency domain,
# allowing us to analyze the signal in terms of its constituent
# frequencies.

# apply the fast fourier transform (FFT)
audio_fft = np.fft.fft(audio_array)

# In the frequency domain, we can identify the noise components
# by analyzing the magnitude spectrum. The magnitude spectrum
# represents the amplitudes of different frequencies present
# in the audio signal.

# Calculate the magnitude spectrum
magnitude_spectrum = np.abs(audio_fft)

# Calculate Noise Threshold
# To determine which frequency components represent noise,
# we calculate a noise threshold based on statistical
# properties of the magnitude spectrum. Common approaches
# include using the mean or median of the magnitude spectrum
# as the threshold.

# Perform Spectral Subtraction
# Finally, we perform spectral subtraction to remove the noise
# from the audio signal. Spectral subtraction involves
# subtracting the noise spectrum from the magnitude
# spectrum and then applying the inverse FFT to obtain the
# denoised audio signal.

# Calculate the noise threshold (using mean with a minimum threshold)
noise_threshold = np.mean(magnitude_spectrum)
min_threshold = 0.1 # Adjust this value as needed

# Subtract the noise spectrum from the magnitude spectrum
denoised_spectrum = np.maximum(magnitude_spectrum-noise_threshold, 0)

# Inverse FFT obtain the denoised audio singal
denoised_audio_array = np.fft.ifft(denoised_spectrum)

# Cast the denoised audio to the appropriate data type
denoised_audio_array = denoised_audio_array.astype(np.int16)

# Output WAV file path (inside the output directory)
output_wav_path = os.path.join(output_directory, "denoised_output.wav")

# Save the denoised audio to a new WAV file
with wave.open(output_wav_path, "wb") as output_wav:
    output_wav.setparams((num_channels, sample_width, sample_rate, num_frames, "NONE", "not compressed"))
    output_wav.writeframes(denoised_audio_array.tobytes())