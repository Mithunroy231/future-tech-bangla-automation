import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def create_script(topic):
    return f"""
# Future Tech বাংলা

বিষয়: {topic}

[HOOK]
আপনি কি জানেন, {topic} আমাদের ভবিষ্যৎ বদলে দিতে পারে?

[INTRO]
আজ আমরা এই প্রযুক্তি সম্পর্কে জানব।

[MAIN]
এই বিষয়ে নির্ভরযোগ্য তথ্য ও উদাহরণ যোগ করতে হবে।

[ENDING]
আরও বিজ্ঞান ও প্রযুক্তির ভিডিও পেতে
Future Tech বাংলা অনুসরণ করুন।
"""

def main():
    topic = input("ভিডিওর বিষয় লিখুন: ").strip()

    if not topic:
        print("বিষয় লিখতে হবে।")
        return

    output = ROOT / "output"
    output.mkdir(exist_ok=True)

    script = create_script(topic)
    path = output / "script_bn.md"
    path.write_text(script, encoding="utf-8")

    print(f"স্ক্রিপ্ট তৈরি হয়েছে: {path}")

if __name__ == "__main__":
    main()
