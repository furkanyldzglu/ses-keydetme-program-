import sounddevice as sd
import wave

def kayit_yap(dosya_adi, sure, ornek_rate=44100):
    # Ses kaydı yapmak için gerekli parametreleri ayarla
    kayit = sd.rec(int(sure * ornek_rate), samplerate=ornek_rate, channels=2, dtype='int16')
    sd.wait()

    # Ses kaydını bir dosyaya yaz
    with wave.open(dosya_adi, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(ornek_rate)
        wf.writeframes(kayit.tobytes())

if __name__ == "__main__":
    dosya_adi = "ders21.0 sonuc.wav"
    kayit_suresi = 30  # saniye cinsinden kayıt süresi

    print(f"Ses kaydı başlıyor... ({kayit_suresi} saniye)")
    kayit_yap(dosya_adi, kayit_suresi)
    print(f"Ses kaydı tamamlandı. Dosya adı: {dosya_adi}")

