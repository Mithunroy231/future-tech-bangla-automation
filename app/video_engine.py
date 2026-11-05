from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"

def prepare_video():
    OUTPUT.mkdir(exist_ok=True)

    script_file = OUTPUT / "script_bn.md"

    if not script_file.exists():
        print("প্রথমে ভিডিওর স্ক্রিপ্ট তৈরি করুন।")
        return

    script = script_file.read_text(encoding="utf-8")

    scenes = {
        "project": "Future Tech বাংলা",
        "language": "Bengali",
        "script": script,
        "status": "awaiting_visual_production",
        "approval_required": True
    }

    result = OUTPUT / "video_plan.json"
    result.write_text(
        json.dumps(scenes, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("ভিডিওর পরিকল্পনা তৈরি হয়েছে।")
    print("পরবর্তী ধাপ: ভয়েস ও ভিজ্যুয়াল তৈরি।")

if __name__ == "__main__":
    prepare_video()
