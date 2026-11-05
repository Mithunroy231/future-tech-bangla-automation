from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "output" / "script_bn.md"
OUTPUT = ROOT / "output"

def main():
    if not SCRIPT.exists():
        print("আগে বাংলা স্ক্রিপ্ট তৈরি করুন।")
        return

    text = SCRIPT.read_text(encoding="utf-8")

    voice = OUTPUT / "voiceover.txt"
    subtitles = OUTPUT / "subtitles.txt"

    voice.write_text(text, encoding="utf-8")
    subtitles.write_text(text, encoding="utf-8")

    print("Voiceover text প্রস্তুত!")
    print("Subtitle text প্রস্তুত!")

if __name__ == "__main__":
    main()
