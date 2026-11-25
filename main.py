import os
line = "I made up the citation."
words = line.split()
data = line.encode("utf-8")
assert line.strip() and "\n" not in line and "\r" not in line
assert 1 <= len(line) <= 88 and 1 <= len(words) <= 5
assert 1 <= len(data) <= 88
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as handle:
    handle.write(line)
with open(path, "r", encoding="utf-8") as handle:
    assert handle.read() == line
