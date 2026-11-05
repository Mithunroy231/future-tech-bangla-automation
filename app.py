import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def load_workflow():
    path = ROOT / "workflow.json"
    with path.open(encoding="utf-8") as file:
        return json.load(file)

def main():
    workflow = load_workflow()

    print("Future Tech বাংলা")
    print("ভিডিও অটোমেশন প্রস্তুতি")
    print("-" * 35)

    for number, step in enumerate(workflow["steps"], start=1):
        print(f"{number}. {step}")

    print("\nসব ধাপ লোড হয়েছে।")
    print("ভিডিও প্রকাশের আগে মালিকের অনুমোদন প্রয়োজন।")

if __name__ == "__main__":
    main()
