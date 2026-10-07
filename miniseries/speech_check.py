"""Pull every spoken line out of the mini-series option files and check them against options/BRIEF.md.

    python3 miniseries/speech_check.py [ep1_m1c.md ep2_laser.md ...]   (no arguments: every epN file)

For each option: the spoken lines (quoted text in the storyboard's last column), the word count,
the spoken numbers, and any line that also appears in another option.
"""
import pathlib
import re
import sys

OPT = pathlib.Path(__file__).resolve().parent / "options"
NUM_WORDS = r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|hundred|thousand|million)\b"
QUOTE = re.compile(r"[\"“]([^\"”]+)[\"”]")


def options(text):
    parts = re.split(r"^## (Option [A-C].*)$", text, flags=re.M)
    return [(parts[i], parts[i + 1]) for i in range(1, len(parts) - 1, 2)]


def spoken(section):
    lines = []
    for row in section.splitlines():
        if not row.startswith("|") or set(row) <= set("|-: "):
            continue
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) < 3 or cells[0] in ("#", "Shot"):
            continue
        lines += [q.strip() for q in QUOTE.findall(cells[-1])]
    return lines


def main():
    seen = {}
    names = sys.argv[1:] or sorted(p.name for p in OPT.glob("ep*.md"))
    for name in names:
        text = (OPT / name).read_text()
        print(f"===== {name} ({len(text.split())} words)")
        for head, body in options(text):
            said = spoken(body)
            words = sum(len(s.split()) for s in said)
            nums = [n for s in said for n in re.findall(r"\d[\d,.]*|" + NUM_WORDS, s, flags=re.I)]
            print(f"--- {head[:90]}\n    {words} spoken words; numbers: {', '.join(nums) or 'none'}")
            for s in said:
                key = re.sub(r"\W+", " ", s.lower()).strip()
                if key in seen and seen[key] != (name, head[:8]):
                    print(f"    REPEAT of {seen[key]}: {s}")
                seen.setdefault(key, (name, head[:8]))
                print(f"    · {s}")


if __name__ == "__main__":
    main()
