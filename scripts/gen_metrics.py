#!/usr/bin/env python3
"""Generate self-hosted profile metric cards (SVG) for the MRUIL/MRUIL README.

Runs in GitHub Actions with the default GITHUB_TOKEN; writes SVGs into ./metrics/.
Replaces the public github-readme-stats / activity-graph instances, which are
rate-limited and frequently return 502 through GitHub's image proxy.
"""
import json, os, sys, math, datetime as dt, urllib.request, urllib.parse
from collections import Counter
from html import escape

USER = os.environ.get("GH_USER", "MRUIL")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
OUT = os.environ.get("OUT_DIR", "metrics")
PINS = [r for r in os.environ.get("PIN_REPOS", "WDNet,WeakMCN,LoViT,StableSPR").split(",") if r]
EXCLUDE_LANG_REPOS = {"MRUIL.github.io", "bay", "MRUIL"}
HIDE_LANGS = {l.strip() for l in os.environ.get("HIDE_LANGS", "Jupyter Notebook").split(",") if l.strip()}

# palette (matches banner.svg / mruil.github.io)
BG, LINE, TITLE, TEXT, MUTED = "#0d1117", "#1e293b", "#38bdf8", "#c9d1d9", "#8b949e"
ACC = ["#38bdf8", "#818cf8", "#a78bfa", "#f472b6", "#34d399", "#fbbf24", "#f87171", "#22d3ee"]
FONT = "font-family=\"'Segoe UI', Ubuntu, 'Helvetica Neue', Sans-Serif\""

def api(path, params=None):
    url = "https://api.github.com" + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json", "User-Agent": "profile-metrics"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def gql(query, variables):
    req = urllib.request.Request("https://api.github.com/graphql", data=json.dumps({"query": query, "variables": variables}).encode(),
                                 headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json", "User-Agent": "profile-metrics"})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.load(r)
    if "errors" in d: raise RuntimeError(d["errors"])
    return d["data"]

def fmt(n):
    return f"{n/1000:.1f}k" if n >= 1000 else str(n)

def card(w, h, title, body, title_x=25):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" {FONT}>
<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="10" fill="{BG}" stroke="{LINE}"/>
<text x="{title_x}" y="35" font-size="18" font-weight="600" fill="{TITLE}">{escape(title)}</text>
{body}
</svg>'''

# ---------------------------------------------------------------- data
user = api(f"/users/{USER}")
repos = []
page = 1
while True:
    batch = api(f"/users/{USER}/repos", {"per_page": 100, "page": page, "type": "owner"})
    repos += batch
    if len(batch) < 100: break
    page += 1
own = [r for r in repos if not r["fork"]]
stars = sum(r["stargazers_count"] for r in repos)

# languages (bytes) over own repos
lang = Counter()
for r in own:
    if r["name"] in EXCLUDE_LANG_REPOS: continue
    try:
        for k, v in api(f"/repos/{USER}/{r['name']}/languages").items(): lang[k] += v
    except Exception as e:
        print("lang skip", r["name"], e, file=sys.stderr)

# contributions per year (GraphQL) + daily calendar
created = dt.datetime.strptime(user["created_at"], "%Y-%m-%dT%H:%M:%SZ").year
now = dt.datetime.utcnow()
Q = """query($login:String!,$from:DateTime!,$to:DateTime!){ user(login:$login){ contributionsCollection(from:$from,to:$to){
  totalCommitContributions restrictedContributionsCount totalPullRequestContributions totalIssueContributions totalPullRequestReviewContributions
  contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount } } } } } }"""
commits = prs = issues = reviews = total_contrib = 0
days = {}
for y in range(created, now.year + 1):
    frm = dt.datetime(y, 1, 1); to = min(dt.datetime(y, 12, 31, 23, 59, 59), now)
    c = gql(Q, {"login": USER, "from": frm.isoformat() + "Z", "to": to.isoformat() + "Z"})["user"]["contributionsCollection"]
    commits += c["totalCommitContributions"] + c["restrictedContributionsCount"]
    prs += c["totalPullRequestContributions"]; issues += c["totalIssueContributions"]; reviews += c["totalPullRequestReviewContributions"]
    total_contrib += c["contributionCalendar"]["totalContributions"]
    for w in c["contributionCalendar"]["weeks"]:
        for d in w["contributionDays"]: days[d["date"]] = d["contributionCount"]

os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- 1) stats card
rows = [("Total stars", fmt(stars)), ("Total commits", fmt(commits)), ("Pull requests", fmt(prs)),
        ("Contributions", fmt(total_contrib)), ("Followers", fmt(user["followers"]))]
body = []
for i, (lbl, val) in enumerate(rows):
    y = 76 + i * 27
    body.append(f'<rect x="25" y="{y-11}" width="4" height="14" rx="2" fill="{ACC[i % len(ACC)]}"/>'
                f'<text x="40" y="{y}" font-size="14" fill="{TEXT}">{escape(lbl)}</text>'
                f'<text x="240" y="{y}" font-size="15" font-weight="700" fill="{ACC[i % len(ACC)]}">{val}</text>')
cx, cy, rr = 400, 120, 42
body.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="{LINE}" stroke-width="7"/>')
body.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="url(#g)" stroke-width="7" stroke-linecap="round" '
            f'stroke-dasharray="{2*math.pi*rr:.1f}" stroke-dashoffset="{2*math.pi*rr*0.22:.1f}" transform="rotate(-90 {cx} {cy})"/>')
body.append(f'<text x="{cx}" y="{cy-2}" text-anchor="middle" font-size="22" font-weight="800" fill="{TEXT}">{len(own)}</text>'
            f'<text x="{cx}" y="{cy+16}" text-anchor="middle" font-size="11" fill="{MUTED}">repos</text>')
defs = f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{ACC[0]}"/><stop offset="0.5" stop-color="{ACC[1]}"/><stop offset="1" stop-color="{ACC[3]}"/></linearGradient></defs>'
open(f"{OUT}/stats.svg", "w", encoding="utf-8").write(card(495, 220, f"{user.get('name') or USER}'s GitHub Stats", defs + "".join(body)))

# ---------------------------------------------------------------- 2) top languages (compact)
top = [(k, v) for k, v in lang.most_common() if k not in HIDE_LANGS][:8]; tot = sum(v for _, v in top) or 1
x = 25; segs = []
for i, (k, v) in enumerate(top):
    w = 445 * v / tot; segs.append(f'<rect x="{x:.1f}" y="52" width="{max(w,2):.1f}" height="8" fill="{ACC[i % len(ACC)]}"/>'); x += w
labels = []
for i, (k, v) in enumerate(top):
    col, row = i % 2, i // 2
    lx, ly = 25 + col * 230, 90 + row * 22
    labels.append(f'<circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{ACC[i % len(ACC)]}"/>'
                  f'<text x="{lx+18}" y="{ly}" font-size="12" fill="{TEXT}">{escape(k)} <tspan fill="{MUTED}">{100*v/tot:.1f}%</tspan></text>')
open(f"{OUT}/langs.svg", "w", encoding="utf-8").write(card(495, 100 + 22 * math.ceil(len(top) / 2) + 6, "Most Used Languages", "".join(segs) + "".join(labels)))

# ---------------------------------------------------------------- 3) pinned repo cards
LANG_COLOR = {"Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "C++": "#f34b7d", "JavaScript": "#f1e05a", "Shell": "#89e051", "HTML": "#e34c26", "CSS": "#563d7c", "SCSS": "#c6538c"}
for name in PINS:
    r = next((r for r in repos if r["name"].lower() == name.lower()), None)
    if not r:
        try: r = api(f"/repos/{USER}/{name}")
        except Exception: continue
    import textwrap
    lines = textwrap.wrap((r.get("description") or "").strip(), 58)[:2] or ["No description"]
    if len(textwrap.wrap((r.get("description") or "").strip(), 58)) > 2: lines[1] = lines[1][:55].rstrip() + "…"
    lg = r.get("language") or "—"
    body = (f'<text x="25" y="36" font-size="16" fill="{TITLE}">▣</text>'
            + "".join(f'<text x="25" y="{64 + 18*i}" font-size="13" fill="{MUTED}">{escape(t)}</text>' for i, t in enumerate(lines))
            + f'<circle cx="30" cy="112" r="6" fill="{LANG_COLOR.get(lg, "#8b949e")}"/><text x="42" y="116" font-size="12" fill="{TEXT}">{escape(lg)}</text>'
            f'<text x="{42 + 7*len(lg) + 30}" y="116" font-size="12" fill="{TEXT}">★ {fmt(r["stargazers_count"])}</text>'
            f'<text x="{42 + 7*len(lg) + 90}" y="116" font-size="12" fill="{TEXT}">⑂ {fmt(r["forks_count"])}</text>')
    open(f"{OUT}/pin-{r['name']}.svg", "w", encoding="utf-8").write(card(400, 135, r["name"], body, title_x=47))

# ---------------------------------------------------------------- 4) activity graph — last 180 days
N = 180
series = []
for i in range(N - 1, -1, -1):
    d = (now - dt.timedelta(days=i)).strftime("%Y-%m-%d"); series.append((d, days.get(d, 0)))
W, Hh, L, R, T, B = 1000, 300, 60, 25, 55, 45
mx = max(1, max(v for _, v in series))
def px(i): return L + (W - L - R) * i / (N - 1)
def py(v): return T + (Hh - T - B) * (1 - v / mx)
pts = [(px(i), py(v)) for i, (_, v) in enumerate(series)]
path = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)
area = path + f" L{pts[-1][0]:.1f},{Hh-B} L{pts[0][0]:.1f},{Hh-B} Z"
grid = []
for k in range(5):
    y = T + (Hh - T - B) * k / 4; val = round(mx * (1 - k / 4))
    grid.append(f'<line x1="{L}" y1="{y:.1f}" x2="{W-R}" y2="{y:.1f}" stroke="{LINE}" stroke-dasharray="3 5"/>'
                f'<text x="{L-10}" y="{y+4:.1f}" text-anchor="end" font-size="11" fill="{MUTED}">{val}</text>')
months = []
for i, (d, _) in enumerate(series):
    if d.endswith("-01"):
        months.append(f'<text x="{px(i):.1f}" y="{Hh-B+22}" text-anchor="middle" font-size="11" fill="{MUTED}">{dt.datetime.strptime(d, "%Y-%m-%d").strftime("%b")}</text>')
dots = "".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{ACC[3]}"/>' for (x, y), (_, v) in zip(pts, series) if v == mx and v > 0)
tot180 = sum(v for _, v in series)
body = (f'<defs><linearGradient id="a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{ACC[0]}" stop-opacity="0.45"/><stop offset="1" stop-color="{ACC[1]}" stop-opacity="0"/></linearGradient></defs>'
        + "".join(grid) + f'<path d="{area}" fill="url(#a)"/><path d="{path}" fill="none" stroke="{ACC[0]}" stroke-width="2" stroke-linejoin="round"/>' + dots + "".join(months)
        + f'<text x="{W-R}" y="35" text-anchor="end" font-size="13" fill="{MUTED}">{tot180} contributions in the last {N} days · updated {now:%Y-%m-%d}</text>')
open(f"{OUT}/activity.svg", "w", encoding="utf-8").write(card(W, Hh, "Contribution Activity", body))

json.dump({"stars": stars, "commits": commits, "prs": prs, "issues": issues, "contrib": total_contrib, "followers": user["followers"], "repos": len(own),
           "langs": top, "generated": now.isoformat()}, open(f"{OUT}/summary.json", "w"), indent=1)
print("ok", stars, commits, prs, issues, total_contrib, len(own), top[:3])
