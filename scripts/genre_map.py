"""Render assets/genre-map.png and .svg from styles.csv.

Runs inside the weekly sync workflow, so the map never drifts from the data.
Deterministic: fixed jitter seed, no timestamps in the files.
"""
import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

matplotlib.rcParams["svg.hashsalt"] = "suno-style-recipes"
INK, CREAM, VIO, AMB, MUTE = "#14121F", "#F6F1E7", "#8B6CFF", "#F2B33D", "#b9b3cf"

d = pd.read_csv("styles.csv")
n = len(d)
si_min = int(d.style_influence.min())
band = 100 - si_min
rng = np.random.default_rng(7)

def row(name):
    hit = d[d["style"] == name]
    return None if hit.empty else hit.iloc[0]

fig = plt.figure(figsize=(12.8, 6.4), dpi=100, facecolor=INK)
ax = fig.add_axes([0.07, 0.13, 0.62, 0.66], facecolor=INK)
x = d.weirdness + rng.uniform(-.45, .45, n)
y = d.style_influence + rng.uniform(-.35, .35, n)
ax.scatter(x, y, s=26, c=VIO, alpha=.55, linewidths=0)

marks = {"Bolero Clásico": ("Bolero", -4, 1.3), "Aria Operática": ("Operatic Aria", 3, .9),
         "Breakcore": ("Breakcore", -14, 1.6), "Sound Collage": ("Sound Collage", -6, -2.2),
         "Techno": ("Techno", 4, -1.8)}
for name, (label, dx, dy) in marks.items():
    r = row(name)
    if r is None:
        continue
    ax.scatter(r.weirdness, r.style_influence, s=70, c=AMB, zorder=3)
    ax.annotate(label, (r.weirdness, r.style_influence), (r.weirdness + dx, r.style_influence + dy),
                color=CREAM, fontsize=11, arrowprops=dict(arrowstyle="-", color=AMB, lw=.8))

for sp in ax.spines.values():
    sp.set_color("#3a3650")
ax.tick_params(colors=MUTE, labelsize=10)
ax.set_xlim(4, 84)
ax.set_ylim(si_min - 1.5, 101.5)
ax.set_xlabel("Weirdness  (tolerance for deviation)", color=CREAM, fontsize=11)
ax.set_ylabel("Style Influence  (genre fidelity)", color=CREAM, fontsize=11)

fig.text(.07, .9, f"{n} genres. Two dials.", color=CREAM, fontsize=30, weight="bold")
fig.text(.07, .845, f"Every documented style, placed by its Suno settings. "
                    f"Style Influence never drops below {si_min}.", color=MUTE, fontsize=12.5)

b, k = row("Bolero Clásico"), row("Breakcore")
side = [("What the map says", CREAM, 15, "bold"), None,
        ("The two dials move independently.", AMB, 12, None)]
if b is not None:
    side.append((f"Bolero sits at {b.weirdness} / {b.style_influence}.", CREAM, 12, None))
if k is not None:
    side.append((f"Breakcore sits at {k.weirdness} / {k.style_influence}.", CREAM, 12, None))
side += [None, (f"Style Influence lives in a {band}-point", AMB, 12, None),
         ("band. Drop it by 10 and you are", CREAM, 12, None),
         ("not loosening the genre —", CREAM, 12, None), ("you are leaving it.", CREAM, 12, None), None,
         ("A 50 / 50 default fits", AMB, 12, None), ("almost nothing on this chart.", CREAM, 12, None)]
yy = .78
for item in side:
    if item:
        fig.text(.74, yy, item[0], color=item[1], fontsize=item[2], weight=item[3] or "normal")
    yy -= .047

fig.text(.07, .04, f"suno-style-recipes · CC0 1.0 · {n} styles in CSV / JSON / Parquet", color="#8f89a8", fontsize=10)
fig.text(.74, .04, "musaisong.app/en/styles", color=AMB, fontsize=10)

os.makedirs("assets", exist_ok=True)
fig.savefig("assets/genre-map.png", facecolor=INK, metadata={"Software": None})
fig.savefig("assets/genre-map.svg", facecolor=INK, metadata={"Date": None, "Creator": None})
print(f"Map rendered: {n} styles, style influence floor {si_min}.")
