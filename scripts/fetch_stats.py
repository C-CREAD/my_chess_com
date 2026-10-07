#!/usr/bin/env python3
"""Fetch Chess.com stats (PubAPI) for users in users.json -> site/data/stats.json.
Serial requests, identifying User-Agent, backoff on 429."""
from pathlib import Path
import datetime as dt, json, os, pathlib, sys, time
import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
# ROOT = Path(__file__).resolve().parent.parent
print("=>",ROOT)
BASE = "https://api.chess.com/pub/player"
CONTACT = os.environ.get("CONTACT", "https://github.com/your/my_chess_com")
MODES = ("rapid", "blitz", "bullet")
# Lower bounds. Your brief left 1100-1199 undefined; it joins Beginner here.
TIERS = [(2200, "Expert Player"), (1800, "Advanced Player"),
         (1200, "Intermediate Player"), (0, "Beginner / Casual")]

def tier(r): return next(n for t, n in TIERS if r >= t)

s = requests.Session()
s.headers["User-Agent"] = f"chess-tiers/1.0 (+{CONTACT})"

def get(url, tries=3):
    for i in range(tries):
        r = s.get(url, timeout=30)
        if r.status_code == 429:
            time.sleep(2 ** (i + 1)); continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"rate limited: {url}")

def build(user):
    u = user.lower()
    prof, stats = get(f"{BASE}/{u}"), get(f"{BASE}/{u}/stats")
    modes, tot = {}, {"win": 0, "loss": 0, "draw": 0}
    for m in MODES:
        d = stats.get(f"chess_{m}")
        if not d: continue
        rec, rating = d["record"], d["last"]["rating"]
        modes[m] = {"rating": rating, "best": d.get("best", {}).get("rating"),
                    "tier": tier(rating), **{k: rec[k] for k in tot}}
        for k in tot: tot[k] += rec[k]
    if not modes: raise ValueError("no rapid/blitz/bullet ratings")
    top = max(v["rating"] for v in modes.values())
    return {"username": prof.get("username", u), "name": prof.get("name"),
            "avatar": prof.get("avatar"), "url": prof.get("url"),
            "tier": tier(top), "modes": modes, "total": tot}

def main():
    data = None
    with open("users.json", "r+") as file:
        data = json.load(file)

    users = data["users"]
    players = []
    for u in users:
        try: players.append(build(u))
        except Exception as e: print(f"skip {u}: {e}", file=sys.stderr)
        time.sleep(0.5)  # stay serial and gentle
    if not players: sys.exit("no players fetched; keeping previous deploy")
    out = ROOT / "site" / "data"; out.mkdir(parents=True, exist_ok=True)
    (out / "stats.json").write_text(json.dumps(
        {"updated": dt.datetime.now(dt.timezone.utc).isoformat(), "players": players}, indent=1))
    print(f"wrote {len(players)} players")

if __name__ == "__main__": main()
