import json
import os
from pathlib import Path

TOP = 200


def assemble() -> str:
    file = Path(__file__).resolve().parent / "entry.txt"
    content = file.read_text(encoding="utf-8").strip()
    assert content, "entry.txt is blank"
    assert len(content) <= TOP, f"{len(content)} chars exceeds {TOP}"
    return content


def place(content: str) -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    folder = Path(base)
    folder.mkdir(parents=True, exist_ok=True)
    placed = folder / "entry.txt"
    placed.write_text(content, encoding="utf-8")
    return placed


def report(placed: Path, content: str) -> None:
    print(json.dumps({"placed": str(placed), "chars": len(content), "cap": TOP, "ok": True}))


if __name__ == "__main__":
    body = assemble()
    report(place(body), body)
