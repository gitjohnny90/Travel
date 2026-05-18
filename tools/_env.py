"""Tiny .env loader so scripts don't need python-dotenv."""
from pathlib import Path


def load(path: str | Path = None) -> dict[str, str]:
    if path is None:
        path = Path(__file__).resolve().parent.parent / ".env"
    path = Path(path)
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def require(name: str) -> str:
    import os
    val = os.environ.get(name) or load().get(name)
    if not val:
        raise SystemExit(
            f"Missing {name}. Set it in .env (copy .env.example) or export it."
        )
    return val
