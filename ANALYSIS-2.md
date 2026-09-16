# The 9 genres where BPM doesn't apply — and what to write instead

There is a field in every AI music generator that looks compulsory and isn't. Tempo. You type a number, the model builds a grid, and everything you wrote gets laid across it. For 555 of the 564 styles in this catalogue that is exactly what you want. For nine of them it is the single fastest way to destroy the track before the first bar.

These are the free-time genres: **Dark Ambient / Sound Art, Drone Experimental, Electroacústica, Música Aleatoria, Musique Concrète, Noise, Power Electronics, Señal Sin Nombre and Sound Collage.** They have no pulse. Not a slow pulse — none. The absence is the genre's whole proposition, and a number in the tempo field contradicts it before the model has read a single word of your lyric.

**Disclosure:** I built and maintain the catalogue these numbers come from. It is public domain (CC0), published as CSV, JSON and Parquet, so everything below can be checked against the source rather than taken on trust.

## The data-hygiene trap that hides them

Until recently these nine were stored in my own dataset as **BPM 0**, and that is worth admitting because it is the most common way this problem propagates. Zero is not a description of anything. It is a number that means "we had nowhere to put this", and it does two kinds of damage.

It sinks your averages: nine zeros dragged the catalogue's mean tempo down by about two beats per minute, quietly, in every calculation anyone ran on the file. And worse, it is *copyable*. Someone reads the row, sees 0, pastes 0 into the tempo field, and the generator does not interpret that as "free time" — it treats it as an invalid input and falls back to its default, which lands somewhere near 120. You asked for Musique Concrète and got Musique Concrète with a house beat under it.

They are now an empty cell in the CSV, `null` in the JSON and a dash in the Markdown table. If you ever build on a genre dataset, check how it encodes absence before you trust a single average it produces.

## The surprise in the numbers

The intuition is that genres without tempo are the loose ones. Free time, free rules, anything goes. The catalogue says the opposite.

Across all 564 styles, style influence — how tightly the model is held to the genre — has a median of 92. These nine sit at a median of **91**, ranging from 89 to 95. They are as tightly bound as the rest of the catalogue. Not loose at all.

What is unusual about them is the other slider. Their weirdness runs **66 to 80, median 72**, against a catalogue median of 26. And all nine belong to a single family.

Put those two facts together and you get the actual instruction, which is not intuitive: **these genres want maximum strangeness held under maximum constraint.** They are not a licence to be vague. They are a very specific tradition of being strange, and the model knows that tradition. Loosen style influence "because it's experimental" and you do not get a freer piece — you get a generic ambient wash, which is what the model reaches for when nothing holds it.

## What replaces the meter

Here is the part nobody tells you. Losing tempo does not mean losing structure. It means swapping one kind of structure for another.

Look at the canonical section structures for these nine and the same shape appears every time:

| Style | Structure |
|---|---|
| Noise | Noise emergence → feedback layers → sonic wall → abrasive climax → decay |
| Drone Experimental | Opening tone → layering → slow transformation → peak density → decay |
| Musique Concrète | Concrete sound → manipulation → tape montage → abstract development → spatial resolution |
| Sound Collage | Spoken fragment → field sound layers → narrative juxtaposition → dense climax → silence |
| Power Electronics | Brutal emergence → feedback layers → overwhelming wall → visceral climax → abrupt cut |

Five stages, every time: **something emerges, it accumulates, it reaches maximum density, it resolves.**

That is a dramatic arc rather than a metric one. Verse and chorus are measured in bars; this is measured in *pressure*. So when you write for these genres, you are not writing lines to fit a grid — you are deciding at which point in a rising density your words arrive, and at which point they stop.

Practically: give yourself five movements, not four verses. Decide what enters first and let it be small. Decide what the maximum is. Decide whether it decays, resolves, or gets cut off — Power Electronics ends on an abrupt cut, Sound Collage ends in silence, and those are different endings for your last line, not decoration.

## Repetition stops being rhythmic and becomes textural

In a song with a pulse, a repeated line lands on a beat, and the beat is what makes the repetition feel intentional. Take the pulse away and repetition has to justify itself some other way.

The answer these genres have used for seventy years: repetition becomes **texture**. A phrase repeated without a grid does not feel like a hook, it feels like an accumulation — each return is slightly buried under what has been added since, so the line is not restated, it is *eroded*.

That changes how you write the line. A hook is built to survive being heard identically twenty times. A textural phrase is built to change meaning as it gets harder to hear. Which means: write a line that is still legible at 30% audibility, and make it one that gets *more* ambiguous as it degrades, not less. Short vowels. Concrete nouns. No clause that depends on a word arriving intact at the end.

And where the tempo field can't help you, the negation moves into the style prompt. The catalogue entries for these genres carry it explicitly — Noise's prompt literally contains *"no rhythm"*, Música Aleatoria's carries *"indeterminate timing"* and *"silence as composition"*. That is where you tell the model there is no grid. Not in a number.

## The two mistakes, every time

**One: writing to an implied beat anyway.** Most writers count syllables out of habit, so the lines come out metrically even. Over free time, even lines sound like a pop song with the drums muted — the grid is audible precisely because it is missing. The fix is to write in breath-lengths instead of syllable-counts. Let one fragment be two words and the next be nineteen. Unevenness is not sloppiness here; it is the only thing that proves there was never a grid.

**Two: confusing "no pulse" with "no shape".** This is the more common and more fatal one. Without a chorus to aim at, writers produce a mood board — six atmospheric images in a row, none of which arrives, because nothing was built up to. The five-stage arc above is the fix, and it is not optional. A piece of Dark Ambient that never reaches peak density is not restrained. It is unfinished.

## What the settings still won't solve

Empty the tempo field, hold style influence at 91, push weirdness past 70, and you will get a convincing texture. You will not get a convincing lyric — because the hardest question in these genres is not what the track sounds like, it is how much can be left unsaid before the words stop meaning anything at all.

That is a writing problem, it is different in every one of these nine, and no slider reaches it. Each style in the catalogue carries a craft note naming its own version of it — the full pages for [Musique Concrète](https://musaisong.app/en/style/musique-concrete) and [Sound Collage](https://musaisong.app/en/style/sound-collage) are a good place to see what that looks like in practice.

---

The full catalogue of 564 styles — style prompt, BPM, weirdness, style influence and canonical song structure for each — is public domain under CC0 1.0, as [CSV](styles.csv), [JSON](styles.json) and [Parquet](styles.parquet), and mirrored on [Hugging Face](https://huggingface.co/datasets/musaisong/suno-style-recipes). Every style also has a full page: <https://musaisong.app/en/styles>

Part one of this series, on what the corpus reveals about the two settings that matter most, is [here](ANALYSIS.md).
