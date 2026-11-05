# add_voice.py - adds an Egyptian Arabic male voice (ar-EG-ShakirNeural) to the reel
# Needs: Python 3, ffmpeg + ffprobe in PATH, and:  pip install edge-tts
# Run:   python add_voice.py        (keep reel-t1d-ebv-silent.mp4 in the same folder)
import asyncio, json, os, subprocess
VOICE = "ar-EG-ShakirNeural"      # Egyptian male. Egyptian female: ar-EG-SalmaNeural
RATE = "-5%"                      # speech speed
VIDEO = "reel-t1d-ebv-silent.mp4"
OUT = "reel-t1d-ebv-voice.mp4"
SCENES = json.loads(r"""[{"text": "هل ممكن فيروس إبشتاين-بار يكون له علاقة بالسكر من النوع الأول؟", "dur": 4.9}, {"text": "فيروس إبشتاين-بار بيصيب أغلب البالغين في العالم، وغالبًا من غير أعراض.", "dur": 4.9}, {"text": "السكر من النوع الأول مرض مناعي ذاتي، الجهاز المناعي بيهاجم خلايا بيتا المنتجة للإنسولين في البنكرياس.", "dur": 6.7}, {"text": "المرض بيحصل لما تجتمع عوامل وراثية مع عوامل بيئية، ومنها العدوى الفيروسية.", "dur": 5.2}, {"text": "بعض الدراسات لاحظت علاقة بين فيروس إبشتاين-بار وبداية المناعة الذاتية ضد البنكرياس، لكن النتائج مش متسقة بين الدراسات.", "dur": 7.5}, {"text": "وفي تفسيرات مقترحة، زي التشابه الجزيئي بين بروتينات الفيروس وبروتينات الجسم، وتنشيط الجهاز المناعي، ودور الخلايا البائية اللي بيستقر فيها الفيروس.", "dur": 8.6}, {"text": "بس لازم نكون واضحين: ده ارتباط، ومش دليل على إن الفيروس هو السبب.", "dur": 5.6}, {"text": "والإصابة بالفيروس لوحدها لا تعني إنك هتصاب بالسكر، لأن الغالبية العظمى من المصابين بيه مابيصابوش.", "dur": 6.4}, {"text": "ومفيش حاليًا تحليل للفيروس أو علاج مضاد له بيُنصح بيه للوقاية من السكر من النوع الأول.", "dur": 6.7}, {"text": "لو ظهر عطش شديد وكثرة تبول ونزول في الوزن وإرهاق، اعمل تحليل سكر فورًا وراجع الدكتور.", "dur": 6.7}, {"text": "ده للتثقيف فقط. وللحجز اتصل بعيادة دكتور محمود يونس في كفر الشيخ.", "dur": 5.2}]""")

def run(*a):
    return subprocess.run(a, check=True, capture_output=True, text=True).stdout

def dur(p):
    return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p).strip())

async def tts(text, path):
    import edge_tts
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(path)

def build(tts_fn=tts):
    os.makedirs("voice", exist_ok=True)
    wavs = []
    for i, s in enumerate(SCENES, 1):
        mp3 = "voice/s%02d.mp3" % i
        wav = "voice/s%02d.wav" % i
        asyncio.run(tts_fn(s["text"], mp3))
        d, target = dur(mp3), s["dur"]
        tempo = max(1.0, min(1.35, d / (target - 0.3)))
        run("ffmpeg", "-y", "-loglevel", "error", "-i", mp3, "-af",
            "atempo=%.3f,apad=whole_dur=%.2f" % (tempo, target), "-t", "%.2f" % target,
            "-ar", "44100", "-ac", "1", wav)
        print("scene %d: voice %.1fs, slot %.1fs, tempo %.2f" % (i, d, target, tempo))
        wavs.append(wav)
    with open("voice/list.txt", "w") as f:
        for w in wavs:
            f.write("file '%s'\n" % os.path.basename(w))
    run("ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", "voice/list.txt", "-c", "copy", "voice/all.wav")
    run("ffmpeg", "-y", "-loglevel", "error", "-i", VIDEO, "-i", "voice/all.wav", "-map", "0:v", "-map", "1:a",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", "-movflags", "+faststart", OUT)
    print("Done:", OUT)

if __name__ == "__main__":
    build()
