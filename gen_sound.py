import wave, struct, math, base64, io

sample_rate = 22050
duration = 0.09
n_samples = int(sample_rate * duration)

buf = io.BytesIO()
with wave.open(buf, 'wb') as wav_file:
    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)
    
    for i in range(n_samples):
        t = i / sample_rate
        freq = 600.0 + (1200.0 - 600.0) * (t / duration)
        sample = 1.0 if math.sin(2 * math.pi * freq * t) > 0 else -1.0
        envelope = math.exp(-25.0 * t)
        val = int(sample * envelope * 28000.0)
        wav_file.writeframes(struct.pack('<h', max(-32767, min(32767, val))))

wav_b64 = base64.b64encode(buf.getvalue()).decode('ascii')
print("data:audio/wav;base64," + wav_b64)
