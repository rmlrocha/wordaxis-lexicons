#!/usr/bin/env python3
"""
Exports the Source Code form of WordAxis's modified Portuguese word lists, which the
Mozilla Public License 1.1 (§3.2) requires to be published (Natura pt-PT and VERO pt-BR).

Writes a self-contained folder meant to be pushed as a public Git repository:

  lists/<locale>/words.txt     the playable list, one folded word per line, exactly as
                               encoded in the app's lexicon.dawg (checked against pack.json)
  lists/<locale>/spellings.tsv folded word <TAB> accented spelling(s), "|"-separated,
                               for the words whose spelling isn't just the folded word
  upstream/<pt_PT|pt_BR>/      the unmodified Hunspell files and READMEs used
  tools/build_lexicon.py       the script that produced the lists
  README.md, MODIFICATIONS.md, LICENSE (MPL 1.1)

Usage: python3 Tools/export_mpl_source.py <destination folder>
"""

import json
import os
import shutil
import sys
from collections import Counter
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_lexicon as bl  # noqa: E402

LOCALES = {"pt-PT": "pt_PT", "pt-BR": "pt_BR"}
LICENSE_TEXT = os.path.join(HERE, "..", "App", "WordAxis", "Resources", "Licenses", "MPL-1.1.txt")


def export(dest):
    os.makedirs(dest, exist_ok=True)
    summary = {}
    for locale, folder in LOCALES.items():
        stats = Counter()
        _, folded_to_display, _, _, playable = bl.playable_words(locale, stats)
        manifest = json.load(open(os.path.join(bl.DEFAULT_OUT, locale, "pack.json"), encoding="utf-8"))
        if len(playable) != manifest["wordCount"]:
            sys.exit(f"{locale}: {len(playable)} words, but pack.json says {manifest['wordCount']}; rebuild the packs first")
        out = os.path.join(dest, "lists", locale)
        os.makedirs(out, exist_ok=True)
        with open(os.path.join(out, "words.txt"), "w", encoding="utf-8") as f:
            f.writelines(w + "\n" for w in playable)
        with open(os.path.join(out, "spellings.tsv"), "w", encoding="utf-8") as f:
            for w in playable:
                spellings = sorted(folded_to_display[w])
                if spellings != [w.lower()]:  # only where folding lost accents (as display.idx)
                    f.write(w + "\t" + "|".join(spellings) + "\n")
        up = os.path.join(dest, "upstream", folder)
        os.makedirs(up, exist_ok=True)
        for name in os.listdir(os.path.join(bl.SRC, folder)):
            shutil.copy2(os.path.join(bl.SRC, folder, name), up)
        summary[locale] = (len(playable), manifest["lexiconSHA256"], manifest["license"])
        print(f"{locale}: {len(playable)} words")

    tools = os.path.join(dest, "tools")
    os.makedirs(tools, exist_ok=True)
    shutil.copy2(os.path.join(HERE, "build_lexicon.py"), tools)
    shutil.copy2(__file__, tools)
    shutil.copy2(LICENSE_TEXT, os.path.join(dest, "LICENSE"))
    write_docs(dest, summary)


def write_docs(dest, summary):
    today = date.today().isoformat()
    rows = "\n".join(f"| {loc} | {n:,} | `{sha[:16]}…` |" for loc, (n, sha, _) in summary.items())
    readme = f"""# WordAxis Portuguese word lists

Source Code form of the modified Portuguese word lists used by **WordAxis** (MileAxis), published
as required by section 3.2 of the Mozilla Public License 1.1.

| Pack | Words | App `lexicon.dawg` SHA-256 |
|---|---|---|
{rows}

* `lists/pt-PT/` is derived from the **Projecto Natura** Hunspell dictionary for Portuguese (Portugal),
  Copyright (C) 2006–2012 José João de Almeida, Rui Vilela and Alberto Simões, Universidade do Minho.
  Upstream tri-licence GPL 2 / LGPL 2.1 / MPL 1.1; these files are distributed under the **MPL 1.1**.
* `lists/pt-BR/` is derived from the **VERO** Hunspell dictionary for Portuguese (Brazil),
  Copyright (C) 2006–2013 Raimundo Santos Moura and the VERO contributors. Upstream dual licence
  LGPL v3 / MPL 1.1; these files are distributed under the **MPL 1.1**.

The full MPL 1.1 text is in `LICENSE`. What was changed, by whom and when is in `MODIFICATIONS.md`.

## Files

* `lists/<locale>/words.txt`: the playable list, one word per line, upper case, folded to the
  game's tile letters (accents removed, Ç kept). It is exactly the list in the app's lexicon.
* `lists/<locale>/spellings.tsv`: folded words with their accented spelling(s) from the
  dictionary, separated by `|`. Words missing from it are spelled exactly as in `words.txt`
  (in lower case).
* `upstream/`: the unmodified `.aff`, `.dic` and README files the lists were built from
  (LibreOffice dictionaries repository).
* `tools/build_lexicon.py`: the script that expands the affix rules, filters and folds the words.
  `tools/export_mpl_source.py` writes this folder. Both run inside the WordAxis source tree
  (they import each other and read the upstream files from `Tools/LexiconSources/`). They are
  published so the method can be read and reproduced.

Only the word lists are covered by the MPL. The WordAxis app, its code and its other assets are
not part of this repository and are distributed under MileAxis's own terms.

Exported {today}.
"""
    mods = f"""# Description of modifications (MPL 1.1 §3.3)

These word lists are derived, directly, from Original Code provided by the Initial Developers:

* **pt-PT:** José João de Almeida, Rui Vilela and Alberto Simões, Projecto Natura,
  Dep. Informática, Universidade do Minho (http://natura.di.uminho.pt/).
* **pt-BR:** Raimundo Santos Moura and the VERO contributors, LibreOffice Brazilian community
  (https://pt-br.libreoffice.org/projetos/vero/).

Changes made by MileAxis (2026; this export {today}), all done by `tools/build_lexicon.py`:

1. Every dictionary entry was expanded with its own affix rules (`.aff`) into the full list of
   word forms. No words were added; every word is a headword or a generated form.
2. Removed: proper nouns and other capitalised forms, hyphenated forms, abbreviations, prefixes,
   Roman numerals, forms the dictionary marks as forbidden (pt-BR), and words longer than 15 letters.
3. Removed interjections ("olá", "pum", "caramba"), except when another entry spells the same word.
4. Removed foreign words: entries tagged as foreign in the pt-PT dictionary and spellings that
   are not Portuguese (for example "th", "ph", "ck", double consonants such as "zz"), except an
   editorial allowlist of everyday loanwords (pizza, sushi, jazz, rock, ballet, …), listed in the script.
5. Folded to tile letters: upper case, accents removed, Ç kept. Words using letters with no tile
   were dropped.
6. Generated forms were cross-checked with the `hunspell` program against the same dictionary.

{"".join(f"* {loc}: {lic['license']}. {lic['modifications']}" + chr(10) for loc, (_, _, lic) in summary.items())}"""
    open(os.path.join(dest, "README.md"), "w", encoding="utf-8").write(readme)
    open(os.path.join(dest, "MODIFICATIONS.md"), "w", encoding="utf-8").write(mods)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    export(os.path.abspath(sys.argv[1]))
