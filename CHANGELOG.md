# Changelog

## 2026-11-08 — Lists round 2: link re-audit

- Re-ran `scripts/check_links_live.py` across all 4 awesome lists (428 unique URLs): 400 alive, 12 bot-blocked, 6 dead, 9 connection-failed, 1 redirect.
- This repo: 0 dead links. The 2 connection-failed URLs in this repo (VamPy Host, juce.com) were verified alive via browser check — the VM network blocks them; they are not dead links.
- The 6 dead links across the 4 lists are all accounted for (annotated deletion, template placeholder, site outage, bot-blocked Facebook, login-gated Looperman) — no edit needed in this repo.
- No other changes: GitHub topics still unset pending Gary's pick (Decision 9); `data/resources.json` stays an 8-entry subset pending Gary (Decision 12 / Q22).

## 2026-05-05 — Academic / Research SEO maximization

- Promoted this repo as the official research-facing audio science satellite for the GareBear99 / TizWildin ecosystem.
- Added academic/research SEO positioning to the README.
- Added citation-ready ecosystem anchors for FreeEQ8, Instrudio, FreeVox8, Voxel Audio, and TizWildinEntertainmentHUB.
- Added `CITATION.cff`, `CITATIONS.md`, and `data/research_anchors.json`.
- Added research docs for citations, Zenodo DOI, research SEO, deep-learning-music mapping, FreeEQ8, Instrudio, and FreeVox8.
- Updated validation to enforce citation/research markers.


## 0.1.0 - 2026-05-04

- Initial public-facing awesome-list package.
- Added Python audio science, DSP, MIR, ML audio, speech, source separation, datasets, visualization, realtime audio, and plugin/creator-tooling sections.
- Added GareBear99 / TizWildin Audio Discovery Network section.
- Added IO router / deconstructed loops anchor through TizWildinEntertainmentHUB, public GitHub Pages router, and Release Vault.
- Added SEO docs, data files, validation scripts, issue forms, and GitHub workflow.
