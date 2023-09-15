import librosa
import numpy as np
import soundfile as sf
import typer
from scipy import signal

app = typer.Typer()

def apply_filter(x, sampling_rate, cutoff_f, btype="low", order=3):
    b, a = signal.butter(order, cutoff_f, fs=sampling_rate, btype=btype)
    return signal.filtfilt(b, a, x)

@app.command()
def filter(input_filename: str, output_filename: str):

    wave, sr = librosa.load(input_filename, sr=None, mono=False)
    wave_clean = np.zeros(wave.shape)

    # print(f'np.max(wave): {np.max(wave)}')
    # print(f'np.min(wave): {np.min(wave)}')

    for i, rec in enumerate(wave):

        divisor = ((np.max(rec)-np.min(rec))*0.5)
        rec_norm = rec/divisor

        # print(f' rec[2344]: {rec[2344]}  rec_norm[2344]: {rec_norm[2344]}')

        # print(f' rec_norm shape: {rec_norm.shape} np.max(rec): {np.max(rec)} np.min(rec): {np.min(rec)} divisor(rec_norm): {divisor}')

        # print(f' rec[0]: {rec[0]}  rec_norm[0]: {rec_norm[0]}')

        # print(f'np.max(rec_norm): {np.max(rec_norm)}')
        # print(f'np.min(rec_norm): {np.min(rec_norm)}')

        # if i == 0:
        #     print(f'rec_norm[2344]: {rec_norm[2344]}')
        # if i == 1:
        #     print(f'rec_norm[34]: {rec_norm[34]}')
        # if i == 2:
        #     print(f'rec_norm[87]: {rec_norm[87]}')
        # if i == 3:
        #     print(f'rec_norm[789]: {rec_norm[789]}')

        # Apply band-pass filtering
        rec_filt = apply_filter(rec_norm, sr, 25, btype="high", order=6)
        rec_filt = apply_filter(rec_filt, sr, 500, btype="low", order=6)

        print(f'{i+1}')
        print(f'np.max(rec_filt): {np.max(rec_filt)}')
        print(f'np.min(rec_filt): {np.min(rec_filt)}')
        print(f'rec_filt[567]: {rec_filt[567]}')

        print(f'------------------------------------')

        # Assemble clean signals
        wave_clean[i-1, :] = rec_filt

    # Save the results
    # print(f'wave_clean size: {wave_clean.size} | {wave_clean.shape}')
    # print(f'final np.max(wave_clean): {np.max(wave_clean)}')
    # print(f'final np.min(wave_clean): {np.min(wave_clean)}')

    # print(f'wave_clean[0][2344]: {wave_clean[0][2344]}')


    sf.write(output_filename, wave_clean.T, sr, 'PCM_16')


if __name__ == "__main__":
    app()