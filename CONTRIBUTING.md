# Contributing

These are starting points, not gospel. If you found numbers that hold a genre better, the correction is welcome.

## Proposing a settings correction

Open an issue with the **Settings correction** form. It asks for four things:

1. **Style** — the row, exactly as it appears in `STYLES.md`.
2. **The numbers you used** — BPM, Weirdness, Style Influence.
3. **What changed** — what the output did differently. "Held the genre through the bridge instead of drifting to pop" is useful; "sounded better" is not.
4. **Model and date** — Suno or Udio, which version, when. A setting that was right in March can be wrong in September.

## Proposing a new style

Use the **Propose a style** form: same shape, plus the style prompt you used. The catalogue documents 564 styles; gaps are welcome.

## Two rules

- **No artist names.** Describe the sound — vocal technique, instrumentation, era of production — never who it resembles. Suno rejects names, and the recipe breaks.
- **Do not edit the data files by hand.** `styles.csv`, `styles.json`, `styles.parquet` and `STYLES.md` are regenerated every Monday from the source catalogue. Corrections go through issues and land at the source.

## What this repo is not

It is not a place to promote a product. The README ends with one clearly declared section about MUSAI, the paid product this catalogue comes from; that section is the only commercial content here and it will stay that way. Pull requests that add commercial links will be closed.

## License

Contributions are released under CC0 1.0, same as the rest of the repo.
