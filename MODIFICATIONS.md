# Description of modifications (MPL 1.1 §3.3)

These word lists are derived, directly, from Original Code provided by the Initial Developers:

* **pt-PT:** José João de Almeida, Rui Vilela and Alberto Simões, Projecto Natura,
  Dep. Informática, Universidade do Minho (http://natura.di.uminho.pt/).
* **pt-BR:** Raimundo Santos Moura and the VERO contributors, LibreOffice Brazilian community
  (https://pt-br.libreoffice.org/projetos/vero/).

Changes made by MileAxis (2026; this export 2026-10-31), all done by `tools/build_lexicon.py`:

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
6. pt-BR only: the affix rules that produce the first person plural without its final s (used
   only before an enclitic, "fazemo-lo") and augmentatives of participles ("tuitadão") were not
   applied.
7. Removed the words rejected in an editorial review, listed in `editorial/<locale>-excluded.txt`.
8. Generated forms were cross-checked with the `hunspell` program against the same dictionary.

* pt-PT: GPLv2 / LGPLv2.1 / MPL 1.1 (tri-licensed); WordAxis redistributes under MPL 1.1. Affix-expanded; proper nouns, prefixes, Roman numerals, hyphenated and capitalised forms removed; diacritics folded (Ç kept). Interjections and foreign words removed (editorial allowlist kept); words rejected in editorial review removed (Tools/LexiconEditorial). Derived from the Original Code by José João de Almeida, Rui Vilela and Alberto Simões (Projecto Natura). Changes made by MileAxis in 2026; see Tools/build_lexicon.py.
* pt-BR: LGPLv3 / MPL 1.1 (dual-licensed; MPL version as listed in LibreOffice's licence notices); WordAxis redistributes under MPL 1.1. Affix-expanded; forbidden, hyphenated, abbreviated and capitalised forms removed; diacritics folded (Ç kept). Forms of the first person plural without the final s and augmentatives of participles not generated. Interjections and foreign words removed (editorial allowlist kept); words rejected in editorial review removed (Tools/LexiconEditorial). Derived from the Original Code by Raimundo Santos Moura (VERO). Changes made by MileAxis in 2026; see Tools/build_lexicon.py.
