# What 564 documented genres reveal about how Suno's settings actually behave

Most advice about Suno's generation settings is handed down rather than measured. You are told to keep weirdness somewhere around 20 to 40 and style influence somewhere around 70 to 90, and then you are left to work out the rest by burning credits. The advice is not wrong exactly. It is just untested, and when you test it against a large enough corpus, parts of it turn out to describe a space that does not exist.

This is what happens when you read 564 documented music styles as data rather than as a lookup table. Each style in the catalogue carries a style prompt, a tempo, a weirdness value, a style influence value and a canonical song structure, grouped into 18 families. The whole thing is public domain, published as CSV, JSON and Parquet, so every number below can be checked against the source in about two minutes rather than taken on trust.

**Disclosure:** I built and maintain this catalogue. It exists because I needed it for a paid product that writes song lyrics, and the settings table turned out to be the part worth giving away. The numbers are not marketing claims; they are the inputs I use, and they are falsifiable. If you find a row that is wrong, the repository has an issue template for exactly that.

## Style influence is a floor, not a dial

Here is the finding that changed how I write prompts. Across all 564 styles, style influence runs from **78 to 100**. The median is 92. Eighty per cent of the catalogue sits at 90 or above. Exactly two styles in the entire set fall below 80, and both are in the same corner of hip-hop.

Now look again at the common advice: set style influence between 70 and 90. Between 70 and 77, the catalogue contains **zero styles**. Not few — none. A third of that recommended band describes settings that no documented genre in this corpus uses, which means the advice is quietly calibrated against a 0-to-100 scale that has no practical existence. The working range is roughly 22 points wide, and it sits almost entirely in the top fifth of the slider.

The consequence is a matter of step size. If you think you are working with a 100-point scale, dropping style influence by 10 feels like a nudge. Against a 22-point working range, 10 points is close to half the usable scale, and it is enough to move a generation from "this genre" to "something adjacent that I did not ask for". When people report that lowering style influence for a bit of creative freedom produced an unrecognisable track, this is the arithmetic behind it. They did not loosen the constraint. They removed it.

The practical rule that follows: move style influence in steps of two or three, not ten. And when output feels generic, raise it before you touch anything else. Generic output is usually a symptom of under-constraint, not of insufficient strangeness.

## The two settings move together, but only halfway

Weirdness and style influence are correlated at **-0.455** across the 564 styles. Negative, which is intuitive: the more a genre is defined by convention, the less room there is to be strange inside it. Mariachi Tradicional sits at weirdness 9 and style influence 100. Bolero Clásico is at 12 and 99. These are genres whose audiences know the rules by heart, and where surprise reads as a defect rather than as personality.

But -0.455 is the interesting part, not the minus sign. A correlation of that size means the two settings explain only about a fifth of each other's variation. They move together roughly half the time and go their own way the rest of it. So the mental model of a single "conventional to experimental" slider, with the two settings locked together on it, is wrong — and it is wrong in a way you can see directly in the data.

Take every style in the catalogue with weirdness at exactly 60, the same deliberately high value. **Rage** sits at style influence 80. **Hyperpop** sits at 95. Both are asking the model for maximum strangeness. They are asking for it under completely different conditions: Rage wants strangeness *and* permission to drift away from the genre, while Hyperpop wants strangeness held tightly inside a form that is itself very specific. Fifteen points apart on a 22-point working range is not a nuance. It is the difference between a track that wanders and a track that detonates on purpose.

The same pattern appears at weirdness 58: **Cloud Rap** at style influence 78, **Fourth World** at 93. Equally strange on paper, and the second one is pinned to its genre while the first is allowed to dissolve.

This is why the generic 50/50 starting point gives the worst of both. It sets style influence to a value no documented style uses, and weirdness to a value that only 46 of the 564 styles exceed, so it lands in the gap between a genre you can recognise and an experiment you chose on purpose. If you want strangeness, decide separately whether you want it held or released. That second decision is the one the single-slider model hides.

One more thing worth knowing about weirdness: above 50 it stops being a setting and starts being a genre. Only 46 styles in the whole catalogue go there, and they cluster almost entirely in the noise and experimental family — Noise at 78, Power Electronics at 80, Musique Concrète at 74, Breakcore at 70, Sound Collage at 70. If you are writing a pop song and you push weirdness to 60 for a bit of character, you are not adding character. You are requesting membership in a club with 46 members, and yours is not one of them.

## When tempo does not apply

Tempo in the catalogue runs from 45 BPM to 220, with a median of 100, and it is the least mysterious of the three settings: it does exactly what it says. The instructive case is the exception.

Nine of the 564 styles carry no tempo at all. Dark Ambient, Drone Experimental, Electroacústica, Música Aleatoria, Musique Concrète, Noise, Power Electronics, Señal Sin Nombre and Sound Collage are free-time. There is no pulse to set, because the absence of one is the genre's entire proposition.

This is a small detail with a large data-hygiene lesson attached. Those nine styles were originally stored as BPM 0, and 0 is not a description of anything — it is a false number that quietly drags down every average you compute and, worse, gets pasted into a prompt where it means nothing. In the published dataset they are now an empty cell in the CSV, `null` in the JSON and a dash in the Markdown table. If you build anything on top of a genre dataset, check how it encodes absence before you trust its means.

The practical version: for these nine, leave the tempo field alone. Setting a BPM does not make them faster. It makes them wrong.

## What the three settings do not solve

Here is the limit of everything above. The settings get you the sound. They do not get you the lyric, and the lyric is where most AI songs come apart — because a language model will cheerfully produce a technically correct chorus that any genre could have produced.

No combination of BPM, weirdness and style influence will stop a soul ballad from sliding into melodrama, keep a cumbia from sounding like a beer advert, or prevent a repetitive techno lyric from going flat on the fourth pass. Those are writing problems, they are specific to each genre, and they sit entirely outside the three numbers. Each style page in the catalogue carries a craft note naming the one writing problem that style creates, which is the part of the work the settings cannot reach: <https://musaisong.app/en/styles>

The settings are the easy half. They are worth measuring properly precisely so that you stop blaming them for the hard half.

---

The full catalogue of 564 styles — style prompt, BPM, weirdness, style influence and canonical song structure for each — is public domain under CC0 1.0, as [CSV](styles.csv), [JSON](styles.json) and [Parquet](styles.parquet), and mirrored on [Hugging Face](https://huggingface.co/datasets/musaisong/suno-style-recipes). Repository: <https://github.com/samuelgrupolimex-prog/suno-style-recipes>
