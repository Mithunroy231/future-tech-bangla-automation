from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "app"))

from app import create_script

topic = input("ভিডিওর বিষয়: ").strip()

if not topic:
    raise SystemExit("বিষয় লিখতে হবে।")

output = ROOT / "output"
output.mkdir(exist_ok=True)

file = output / "script_bn.md"
file.write_text(create_script(topic), encoding="utf-8")

print(f"স্ক্রিপ্ট তৈরি হয়েছে: {file}")
