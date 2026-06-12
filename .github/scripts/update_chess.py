import re
import requests
from datetime import datetime, timezone

USERNAME = "rottenpaintbrush"
README_PATH = "README.md"
API_URL = f"https://api.chess.com/pub/player/{USERNAME}/stats"
HEADERS = {"User-Agent": "github-profile-readme-updater/1.0"}


def fetch_stats():
    resp = requests.get(API_URL, headers=HEADERS, timeout=10)
    resp.raise_for_status()
    return resp.json()


def parse_mode(data, key):
    mode = data.get(key, {})
    if not mode:
        return None
    rating = mode.get("last", {}).get("rating", "—")
    best = mode.get("best", {}).get("rating", "—")
    record = mode.get("record", {})
    w = record.get("win", 0)
    l = record.get("loss", 0)
    d = record.get("draw", 0)
    return {"rating": rating, "best": best, "w": w, "l": l, "d": d}


def build_table(data):
    modes = [
        ("bullet", parse_mode(data, "chess_bullet")),
        ("blitz", parse_mode(data, "chess_blitz")),
        ("rapid", parse_mode(data, "chess_rapid")),
    ]

    rows = ""
    for name, stats in modes:
        if stats:
            rows += (
                f"    <tr>\n"
                f"      <td><b>{name}</b></td>\n"
                f"      <td><code>{stats['rating']}</code></td>\n"
                f"      <td><code>{stats['best']}</code></td>\n"
                f"      <td>{stats['w']}W &nbsp;·&nbsp; {stats['l']}L &nbsp;·&nbsp; {stats['d']}D</td>\n"
                f"    </tr>\n"
            )

    return (
        "<table>\n"
        "  <thead>\n"
        "    <tr>\n"
        "      <th>mode</th>\n"
        "      <th>rating</th>\n"
        "      <th>best</th>\n"
        "      <th>record</th>\n"
        "    </tr>\n"
        "  </thead>\n"
        "  <tbody>\n"
        f"{rows}"
        "  </tbody>\n"
        "</table>"
    )


def update_readme(table_html):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    new_block = (
        f"<!-- CHESS_STATS_START -->\n"
        f"{table_html}\n"
        f"<!-- CHESS_STATS_END -->"
    )
    content = re.sub(
        r"<!-- CHESS_STATS_START -->.*?<!-- CHESS_STATS_END -->",
        new_block,
        content,
        flags=re.DOTALL,
    )

    # update the timestamp line
    content = re.sub(
        r"<sub>auto-updated daily · last run: .*?</sub>",
        f"<sub>auto-updated daily · last run: {timestamp}</sub>",
        content,
    )

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Chess stats updated at {timestamp}")


if __name__ == "__main__":
    data = fetch_stats()
    table = build_table(data)
    update_readme(table)
