# Awesome Python Audio Science

> A curated, public-facing list of Python audio science, scientific audio research, DSP, MIR, machine-learning audio, datasets, notebooks, plugin testing, creator-audio tooling, and citation-ready audio research resources.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![GitHub stars](https://img.shields.io/github/stars/GareBear99/awesome-python-audio-science?style=social)
![GitHub forks](https://img.shields.io/github/forks/GareBear99/awesome-python-audio-science?style=social)
![Last commit](https://img.shields.io/github/last-commit/GareBear99/awesome-python-audio-science)
![License](https://img.shields.io/github/license/GareBear99/awesome-python-audio-science)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Quick answer

Use this list when you need Python tools for:

- scientific audio research
- audio DSP and spectral analysis
- music information retrieval
- speech analysis and alignment
- source separation
- audio machine learning
- datasets and dataloaders
- audio visualization and notebooks
- plugin analysis and creator-audio automation
- TizWildin / GareBear99 audio ecosystem routing, deconstructed loops, plugin hubs, and release-surface mapping

This repo is inspired by the scientific-audio awesome-list tradition, especially [`faroit/awesome-python-scientific-audio`](https://github.com/faroit/awesome-python-scientific-audio), but it is intentionally broader: it includes research tooling, production-facing audio engineering, independent-artist data surfaces, plugin/tool ecosystems, and the GareBear99 / TizWildin routing network.

## Academic / Research SEO Positioning

This repository is the official **research-facing audio science satellite** inside the GareBear99 / TizWildin ecosystem. It is designed to bridge practical audio tools with scholarly search intent:

- Python scientific audio libraries
- DSP and spectral-analysis references
- MIR / music information retrieval tooling
- machine-learning audio resources
- datasets and reproducible notebooks
- citation-ready open-source audio software
- DOI / Zenodo / BibTeX / `CITATION.cff` guidance
- research bridges for FreeEQ8, FreeVox8, Instrudio, Voxel Audio, and the HUB router

Use this repo when a project needs to look credible to developers, researchers, students, DSP learners, and audio-ML users instead of only producers.

### Citation-ready ecosystem anchors

| Project | Research / citation role |
|---|---|
| [FreeEQ8](https://github.com/GareBear99/FreeEQ8) | Open-source JUCE/C++ EQ plugin for DSP education, plugin testing, analyzer research, M/S processing examples, and citable audio-software packaging. |
| [FreeVox8](https://github.com/GareBear99/FreeVox8) | Spectral vocoder / ghost-resynthesis R&D anchor for STFT, phase vocoder, formant, masking, and spectral-processing research direction. |
| [Instrudio](https://github.com/GareBear99/Instrudio) | Single-source-of-truth virtual instrument runtime with physically informed Studio Violin, Web Audio synthesis, MIDI routing, and runtime metrics. |
| [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) | Audio visualization, image binding, export routing, and creator-facing media tooling useful for audio-visual research workflows. |
| [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) | Public router for plugins, lists, deconstructed loops, sample packs, visualizers, and release surfaces. |


## GareBear99 / TizWildin Audio Discovery Network

This list is part of the public GareBear99 audio ecosystem.

| Project | Role |
|---|---|
| [awesome-audio-lists](https://github.com/GareBear99/awesome-audio-lists) | Parent hub for audio directories, submission targets, plugin lists, and music-platform lists. |
| [awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) | Independent artist platform map: streaming, distribution, beat stores, sample packs, sync licensing, analytics, creator storefronts. |
| [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) | Audio plugin development, JUCE, DSP, plugin directories, and open-source audio engineering resources. |
| [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) | Main public plugin/sample-pack dashboard and `.io` router surface for the TizWildin ecosystem. |
| [TizWildin HUB public router](https://garebear99.github.io/TizWildinEntertainmentHUB/) | `.io`/GitHub Pages public route for plugins, packs, lists, deconstructed loops, and release surfaces. |
| [TizWildin Release Vault](https://github.com/GareBear99/TizWildin-Release-Vault) | Release/catalog proof surface for distributed tracks, official releases, and monetized music assets. |
| [FreeEQ8](https://github.com/GareBear99/FreeEQ8) | Open-source 8-band EQ plugin and flagship public audio-plugin anchor. |
| [FreeVox8](https://github.com/GareBear99/FreeVox8) | Spectral vocoder / ghost resynthesis plugin anchor. |
| [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) | RGB waveform visualizer, audio-router, visual export, image-binding, vault, and creator loop/track presentation surface. |
| [SoundCloud: TizWildin](https://soundcloud.com/tizwildin) | Original songs, WIPs, remixes, VIP mixes, and underground release surface. |
| [YouTube: TizWildin](https://www.youtube.com/@gfgfvmhj) | Music videos, demos, visualizers, public release clips, and platform routing. |

### IO router / deconstructed loops anchor

The public router for TizWildin plugins, deconstructed loops, release packs, visualizers, and list routing lives through:

- [TizWildinEntertainmentHUB GitHub repo](https://github.com/GareBear99/TizWildinEntertainmentHUB)
- [TizWildinEntertainmentHUB public `.io` router](https://garebear99.github.io/TizWildinEntertainmentHUB/)
- [Release Vault repo](https://github.com/GareBear99/TizWildin-Release-Vault)

Use these as the canonical public-facing anchors for deconstructed loops, sample packs, plugin releases, and creator-routing pages unless superseded by a later dedicated router repo.

## Contents

- [Academic / Research SEO Positioning](#academic--research-seo-positioning)
- [Core Python Audio Packages](#core-python-audio-packages)
- [Read / Write / Metadata](#read--write--metadata)
- [DSP, Transforms & Spectral Analysis](#dsp-transforms--spectral-analysis)
- [Feature Extraction & MIR](#feature-extraction--mir)
- [Machine Learning Audio](#machine-learning-audio)
- [Speech, Voice & Alignment](#speech-voice--alignment)
- [Source Separation](#source-separation)
- [Loudness, Metering & Perceptual Audio](#loudness-metering--perceptual-audio)
- [Realtime Audio & MIDI](#realtime-audio--midi)
- [Datasets & Dataloaders](#datasets--dataloaders)
- [Visualization, Notebooks & Web Audio](#visualization-notebooks--web-audio)
- [Audio Plugin / Creator Tooling](#audio-plugin--creator-tooling)
- [GareBear99 / TizWildin Ecosystem](#garebear99--tizwildin-ecosystem)
- [Best Python Audio Stack by Use Case](#best-python-audio-stack-by-use-case)
- [Long-Tail Guides](#long-tail-guides)
- [Research, Citations & DOI Guides](#research-citations--doi-guides)
- [Citation-Ready GareBear99 / TizWildin Audio Software](#citation-ready-garebear99--tizwildin-audio-software)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)

## Core Python Audio Packages

- [librosa](https://librosa.org/) - Audio and music analysis library for Python, widely used for MIR and research workflows.
- [Essentia](https://essentia.upf.edu/) - C++/Python library for audio and music analysis, feature extraction, and large-scale research.
- [aubio](https://aubio.org/) - Audio feature extraction, onset detection, pitch detection, beat tracking, and segmentation.
- [madmom](https://madmom.readthedocs.io/) - MIR package focused on beat, downbeat, onset, tempo, and chord recognition.
- [audioFlux](https://audioflux.top/) - Audio and music analysis library with spectral transforms and feature extraction.
- [torchaudio](https://pytorch.org/audio/stable/) - PyTorch audio I/O, transforms, datasets, and deep-learning audio utilities.
- [JAX audio examples](https://github.com/google/jax) - Useful base for research pipelines that need accelerated differentiable audio experiments.

## Read / Write / Metadata

- [soundfile](https://pysoundfile.readthedocs.io/) - Read and write sound files using libsndfile through CFFI.
- [audioread](https://github.com/beetbox/audioread) - Decode audio using available backends such as GStreamer, Core Audio, MAD, FFmpeg, and others.
- [pydub](https://github.com/jiaaro/pydub) - Simple high-level audio manipulation, conversion, slicing, and export.
- [mutagen](https://mutagen.readthedocs.io/) - Audio metadata reading and writing for many formats.
- [tinytag](https://github.com/devsnd/tinytag) - Lightweight metadata reader for MP3, OGG, FLAC, WAV, and more.
- [PyAV](https://pyav.org/) - Pythonic bindings for FFmpeg libraries.
- [stempeg](https://github.com/faroit/stempeg) - Read and write multi-stream audio, especially useful for stems and source-separation datasets.

## DSP, Transforms & Spectral Analysis

- [NumPy](https://numpy.org/) - Array computation base for most audio analysis and DSP pipelines.
- [SciPy Signal](https://docs.scipy.org/doc/scipy/reference/signal.html) - Filtering, transforms, windows, spectral analysis, and signal-processing utilities.
- [pyFFTW](https://pyfftw.readthedocs.io/) - Python wrapper around FFTW for faster FFT-heavy workflows.
- [STFT](https://stft.readthedocs.io/) - Standalone short-time Fourier transform tools.
- [PyWavelets](https://pywavelets.readthedocs.io/) - Wavelet transforms and multi-resolution signal analysis.
- [resampy](https://resampy.readthedocs.io/) - Sample-rate conversion for audio and signal processing.
- [pyroomacoustics](https://github.com/LCAV/pyroomacoustics) - Room acoustics simulation, beamforming, and sound-field experimentation.
- [acoustics](https://python-acoustics.github.io/python-acoustics/) - Acoustics calculations, room acoustics, decibels, filters, and standards-oriented utilities.
- [pyloudnorm](https://github.com/csteinmetz1/pyloudnorm) - Loudness meter and normalization library based on ITU-R BS.1770.
- [matchering](https://github.com/sergree/matchering) - Automated reference audio mastering in Python.

## Feature Extraction & MIR

- [mir_eval](https://craffel.github.io/mir_eval/) - Standard evaluation tools for music information retrieval tasks.
- [mirdata](https://mirdata.readthedocs.io/) - Common loaders for MIR datasets.
- [msaf](https://github.com/urinieto/msaf) - Music structure analysis framework.
- [pretty_midi](https://craffel.github.io/pretty-midi/) - MIDI analysis and manipulation utilities.
- [music21](https://web.mit.edu/music21/) - Computer-aided musicology and symbolic music analysis.
- [mido](https://mido.readthedocs.io/) - MIDI message, port, and file utilities.
- [partitura](https://github.com/CPJKU/partitura) - Symbolic music processing for score-performance research.

## Machine Learning Audio

- [PyTorch](https://pytorch.org/) - Deep-learning framework commonly used for audio ML, MIR, source separation, and speech.
- [torchaudio](https://pytorch.org/audio/stable/) - Audio-specific PyTorch transforms, datasets, models, and I/O.
- [TensorFlow Audio / Keras](https://www.tensorflow.org/io/tutorials/audio) - Audio loading, preprocessing, and model training paths in the TensorFlow ecosystem.
- [Kapre](https://github.com/keunwoochoi/kapre) - Keras audio preprocessing layers.
- [nnAudio](https://github.com/KinWaiCheuk/nnAudio) - GPU-accelerated audio transforms using neural-network operations.
- [Hugging Face Audio](https://huggingface.co/tasks/audio-classification) - Models and datasets for classification, speech, separation, and generation tasks.
- [Asteroid](https://github.com/asteroid-team/asteroid) - PyTorch-based audio source-separation toolkit.
- [SpeechBrain](https://speechbrain.github.io/) - Speech and audio toolkit for ASR, speaker recognition, separation, enhancement, and more.

## Speech, Voice & Alignment

- [Praat / Parselmouth](https://parselmouth.readthedocs.io/) - Python interface to Praat for phonetics, speech analysis, and manipulation.
- [Montreal Forced Aligner](https://montreal-forced-aligner.readthedocs.io/) - Forced alignment for speech and lyrics workflows.
- [aeneas](https://www.readbeyond.it/aeneas/) - Forced alignment of audio and text.
- [pyannote.audio](https://github.com/pyannote/pyannote-audio) - Neural speaker diarization and speaker-analysis toolkit.
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Wrapper for multiple speech recognition engines and APIs.
- [python_speech_features](https://github.com/jameslyons/python_speech_features) - Classic speech features such as MFCC and filterbanks.
- [spafe](https://superkogito.github.io/spafe/) - Speech and audio feature extraction.
- [WORLD / PyWorld](https://github.com/JeremyCCHsu/Python-Wrapper-for-World-Vocoder) - WORLD vocoder Python wrapper for speech analysis/synthesis experiments.
- [Arcmira transcript to WebVTT](https://github.com/arcmira/integrations/tree/master/examples/transcript-webvtt) - Python example that converts saved YouTube and podcast transcripts from Arcmira into timed captions, preserving speaker names when supplied.

## Source Separation

- [Demucs](https://github.com/facebookresearch/demucs) - Music source separation with deep learning.
- [Spleeter](https://github.com/deezer/spleeter) - Source-separation library by Deezer.
- [Open-Unmix](https://github.com/sigsep/open-unmix-pytorch) - Music source separation toolkit and model family.
- [Asteroid](https://github.com/asteroid-team/asteroid) - Source separation and speech enhancement toolkit.
- [nussl](https://github.com/nussl/nussl) - Holistic source-separation framework.
- [musdb](https://github.com/sigsep/sigsep-mus-db) - MUSDB dataset tooling for source separation.

## Loudness, Metering & Perceptual Audio

- [pyloudnorm](https://github.com/csteinmetz1/pyloudnorm) - Program loudness and true-peak-oriented workflows based on BS.1770-style metering.
- [pystoi](https://github.com/mpariente/pystoi) - Short-Time Objective Intelligibility measure.
- [pesq](https://github.com/ludlows/PESQ) - PESQ speech quality metric wrapper.
- [cochlea](https://github.com/mrkrd/cochlea) - Inner-ear auditory models.
- [Brian2](https://brian2.readthedocs.io/) - Spiking neural network simulator useful for auditory model research.

## Realtime Audio & MIDI

- [sounddevice](https://python-sounddevice.readthedocs.io/) - Realtime audio I/O with PortAudio and NumPy.
- [pyo](https://github.com/belangeo/pyo) - Realtime DSP and synthesis engine for Python.
- [Jupylet](https://github.com/nir/jupylet) - Python game/audio environment with synth and sample support.
- [mido](https://mido.readthedocs.io/) - MIDI message and port handling.
- [python-rtmidi](https://spotlightkid.github.io/python-rtmidi/) - Realtime MIDI I/O bindings.

## Datasets & Dataloaders

- [mirdata](https://mirdata.readthedocs.io/) - Standardized loaders for MIR datasets.
- [MUSDB18](https://sigsep.github.io/datasets/musdb.html) - Music source-separation dataset.
- [MedleyDB](https://medleydb.weebly.com/) - Multitrack dataset for MIR research.
- [FMA](https://github.com/mdeff/fma) - Free Music Archive dataset for music analysis.
- [AudioSet](https://research.google.com/audioset/) - Large-scale audio event dataset.
- [Common Voice](https://commonvoice.mozilla.org/) - Open speech dataset.
- [Magenta Datasets](https://magenta.tensorflow.org/datasets) - Music and symbolic datasets for creative ML.

## Visualization, Notebooks & Web Audio

- [matplotlib](https://matplotlib.org/) - Plot waveforms, spectrograms, features, and research figures.
- [plotly](https://plotly.com/python/) - Interactive audio-analysis plots and dashboards.
- [Jupyter](https://jupyter.org/) - Notebook environment for audio experiments, MIR notebooks, and reproducible analysis.
- [Streamlit](https://streamlit.io/) - Quick interactive audio analysis apps and dashboards.
- [Gradio](https://www.gradio.app/) - Simple ML/audio demos and web UIs.
- [TimeSide](https://github.com/Parisson/TimeSide) - Audio analysis, imaging, transcoding, streaming, and labelling tools.
- [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) - TizWildin RGB waveform visualizer and audio export tool for creator routing and visual releases.

## Audio Plugin / Creator Tooling

- [pedalboard](https://github.com/spotify/pedalboard) - Python audio effects and VST3/AU plugin hosting from Spotify.
- [DawDreamer](https://github.com/DBraun/DawDreamer) - Python DAW-style rendering and plugin hosting.
- [Vamp plugins / VamPy host](https://code.soundsoftware.ac.uk/projects/vampy-host) - Python interface for Vamp audio-analysis plugins.
- [JUCE](https://juce.com/) - C++ plugin framework; relevant for Python-assisted testing, packaging, and analysis pipelines.
- [FreeEQ8](https://github.com/GareBear99/FreeEQ8) - TizWildin open-source EQ plugin anchor for analysis/testing examples.
- [FreeVox8](https://github.com/GareBear99/FreeVox8) - TizWildin spectral vocoder / ghost-resynthesis plugin anchor.
- [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) - Public plugin router, release dashboard, list tab, and creator ecosystem hub.

## GareBear99 / TizWildin Ecosystem

These entries are included as canonical creator/audio ecosystem anchors, especially for plugin-routing, deconstructed-loop routing, sample-pack routing, visualizer export surfaces, and audio-tool SEO discoverability.

- [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) - Plugin ecosystem hub, public dashboard, and `.io` route for plugins, packs, lists, and release surfaces.
- [TizWildin HUB public page](https://garebear99.github.io/TizWildinEntertainmentHUB/) - Public `.io` route for the TizWildin plugin/sample/list ecosystem.
- [awesome-audio-lists](https://github.com/GareBear99/awesome-audio-lists) - Parent audio list hub and submission-target map.
- [awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) - Music platform list for independent artists, beat sellers, sample-pack creators, sync licensing, and analytics.
- [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) - Audio plugin development and discovery list.
- [TizWildin-Release-Vault](https://github.com/GareBear99/TizWildin-Release-Vault) - Release vault for catalog proof and official music-release routing.
- [FreeEQ8](https://github.com/GareBear99/FreeEQ8) - Free open-source EQ plugin.
- [FreeVox8](https://github.com/GareBear99/FreeVox8) - Spectral vocoder and ghost resynthesis plugin.
- [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) - Visualizer/export/router surface for tracks, loops, artwork, and release presentation.
- [TizWildin SoundCloud](https://soundcloud.com/tizwildin) - Official SoundCloud music surface.
- [TizWildin YouTube](https://www.youtube.com/@gfgfvmhj) - Official YouTube music/video surface.

## Best Python Audio Stack by Use Case

| Use Case | Start With | Add Next | Notes |
|---|---|---|---|
| Quick audio analysis | `librosa` | `matplotlib`, `soundfile` | Fastest path for spectrograms, features, tempo, and MIR experiments. |
| Production file conversion | `pydub` | `PyAV`, `ffmpeg` | Good for creator pipelines, exports, and batch processing. |
| Deep-learning audio | `torchaudio` | `PyTorch`, `nnAudio`, `SpeechBrain` | Best for GPU/ML pipelines. |
| Source separation | `Demucs` | `Open-Unmix`, `Asteroid`, `MUSDB` | Best for stems, dataset work, and research comparisons. |
| Speech alignment | `Montreal Forced Aligner` | `aeneas`, `Parselmouth` | Good for lyrics, voice, and phonetics workflows. |
| Realtime audio | `sounddevice` | `pyo`, `mido` | Useful for prototypes, MIDI, and live control. |
| Plugin rendering/testing | `pedalboard` | `DawDreamer`, JUCE/pluginval | Use for offline plugin tests and audio examples. |
| TizWildin creator routing | `Voxel Audio` | `TizWildinEntertainmentHUB`, `Release Vault` | For deconstructed loops, public routing, visualizer export, packs, and music surfaces. |

## Research, Citations & DOI Guides

These pages turn the repo from a normal awesome list into an academic-facing research and citation hub:

- [Academic research and citations](docs/ACADEMIC_RESEARCH_AND_CITATIONS.md) - how this repo connects Python audio science, DSP, MIR, audio ML, and citable software.
- [Citation-ready audio software](docs/CITATION_READY_AUDIO_SOFTWARE.md) - checklist for `CITATION.cff`, BibTeX, Zenodo DOI, releases, and reproducible audio tooling.
- [Zenodo DOI guide](docs/ZENODO_DOI_GUIDE.md) - how to make GitHub audio projects formally citable.
- [Research SEO playbook](docs/RESEARCH_SEO_PLAYBOOK.md) - academic keyword strategy for audio DSP, MIR, ML audio, plugin testing, and scientific software.
- [Deep-learning music resource map](docs/deep-learning-music-resource-map.md) - how this list connects to deep-learning-music resources without pretending every project is a peer-reviewed paper.
- [FreeEQ8 research bridge](docs/FREEEQ8_RESEARCH_BRIDGE.md) - how to position FreeEQ8 as citable JUCE/C++ DSP software.
- [Instrudio research bridge](docs/INSTRUDIO_RESEARCH_BRIDGE.md) - how to position Instrudio / Studio Violin as an SSOT virtual-instrument research runtime.
- [FreeVox8 research bridge](docs/FREEVOX8_RESEARCH_BRIDGE.md) - how to position FreeVox8 as spectral vocoder / resynthesis R&D.

## Citation-Ready GareBear99 / TizWildin Audio Software

| Software | Suggested citation angle | Next action |
|---|---|---|
| [FreeEQ8](https://github.com/GareBear99/FreeEQ8) | Open-source JUCE/C++ 8-band EQ plugin for DSP education, analyzer testing, M/S processing examples, and pluginval/DAW compatibility workflows. | Add `CITATION.cff`, `CITATIONS.md`, Zenodo DOI, and release artifacts. |
| [Instrudio](https://github.com/GareBear99/Instrudio) | SSOT Web Audio instrument runtime with physically informed Studio Violin, MIDI routing, plugin-bridge events, live metrics, and reproducible JSON definitions. | Add formal paper-style README section, BibTeX, and Zenodo archive. |
| [FreeVox8](https://github.com/GareBear99/FreeVox8) | Spectral vocoder / ghost-resynthesis R&D package for STFT, masking, phase-vocoder, and formant-processing direction. | Add research spec, pluginval reports, and citation metadata after binary certification. |
| [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) | Audio visualization/export/router surface for waveform visualizer research, cover-art binding, and creator-media pipeline experiments. | Add reproducible export metrics and citation metadata. |
| [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) | Public router and ecosystem index for plugins, lists, deconstructed loops, sample packs, release surfaces, and audio-tool discovery. | Keep it as the canonical public gateway and add crawlable links. |

## Long-Tail Guides

- [Best Python libraries for audio analysis](docs/best-python-libraries-for-audio-analysis.md)
- [Python audio DSP stack](docs/python-audio-dsp-stack.md)
- [Python tools for music information retrieval](docs/python-tools-for-music-information-retrieval.md)
- [Python source separation tools](docs/python-source-separation-tools.md)
- [Python audio ML stack](docs/python-audio-ml-stack.md)
- [Python audio visualization stack](docs/python-audio-visualization-stack.md)
- [Python creator audio automation stack](docs/python-creator-audio-automation-stack.md)
- [TizWildin ecosystem routing map](docs/tizwildin-ecosystem-routing-map.md)
- [GitHub SEO playbook](docs/GITHUB_SEO_PLAYBOOK.md)
- [Repository launch checklist](docs/REPOSITORY_LAUNCH_CHECKLIST.md)

## Related Awesome Lists

- [faroit/awesome-python-scientific-audio](https://github.com/faroit/awesome-python-scientific-audio) - The classic Python scientific audio list that inspired this satellite.
- [awesome-audio-lists](https://github.com/GareBear99/awesome-audio-lists) - Parent hub for the GareBear99 audio discovery network.
- [awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) - Music-platform and independent-artist release-surface map.
- [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) - Audio plugin development and discovery resources.
- [awesome-python](https://github.com/vinta/awesome-python) - General Python list.
- [awesome-datascience](https://github.com/academic/awesome-datascience) - Data science resources.
- [awesome-audio-dsp](https://github.com/BillyDM/awesome-audio-dsp) - Audio DSP resources.
- [awesome-music-production](https://github.com/ad-si/awesome-music-production) - Music production tools and resources.

## Recommended GitHub metadata

Recommended repo name:

```text
awesome-python-audio-science
```

Recommended GitHub description:

```text
A curated awesome list of Python audio science, scientific audio research, DSP, MIR, machine-learning audio, datasets, visualization, plugin testing, and creator-audio tooling.
```

Recommended topics:

```text
awesome awesome-list python audio scientific-audio audio-dsp signal-processing music-information-retrieval mir speech-processing source-separation audio-machine-learning datasets audio-analysis audio-visualization music-technology independent-artists tizwildin garebear99 audio-research research-software citable-software zenodo doi bibtex citation-cff reproducible-research deep-learning-music neural-audio
```

## Contributing

Contributions are welcome. Keep entries useful, neutral, public-facing, and directly relevant to Python audio science or creator-audio automation.

Submission format:

```markdown
- [Project Name](https://example.com/) - Short neutral description.
```

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/SUBMISSION_GUIDE.md](docs/SUBMISSION_GUIDE.md).

## License

CC0-1.0 recommended for public awesome-list reuse.
