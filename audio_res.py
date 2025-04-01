import librosa
import numpy as np
import soundfile as sf

def enhance_audio(audio_path):
    y, sr = librosa.load(audio_path)
    y = librosa.effects.preemphasis(y)
    sf.write("enhanced_audio.wav", y, sr)
    return "enhanced_audio.wav"
