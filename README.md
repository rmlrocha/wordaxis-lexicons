# WordAxis Portuguese word lists

Source Code form of the modified Portuguese word lists used by **WordAxis** (MileAxis), published
as required by section 3.2 of the Mozilla Public License 1.1.

| Pack | Words | App `lexicon.dawg` SHA-256 |
|---|---|---|
| pt-PT | 371,990 | `9cb23bd0419b4207…` |
| pt-BR | 2,050,645 | `a6ae10fa500b476c…` |

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

Exported 2026-10-30.
