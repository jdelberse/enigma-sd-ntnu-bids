# Trondheim Dataset (`ntnu-bids`)

## Overview

This dataset contains MRI data from a sleep manipulation study conducted at the Norwegian University of Science and Technology. It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Trondheim |
| Affiliation | Norwegian University of Science and Technology |
| Country | Norway |
| Participants (N) | 73 |
| Age, mean (SD), years | 27.8 (5.3) |
| Male (%) | 47.9 |

## Sleep protocol

- **BL**: baseline (habitual) sleep
- **SR**: sleep restriction, 3h delay in sleep onset

Baseline session: T2BL
Follow-up session: T3SR or T4SR

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | Siemens Skyra |
| Sequence | MPRAGE |
| TR (ms) | 2300 |
| TE (ms) | 2.92 |
| TI (ms) | 900 |
| Flip angle (°) | 9 |

### Diffusion-weighted (`dwi/`)

| Parameter | Value |
|---|---|
| Scanner | Siemens Skyra |
| Sequence | DTI EPI |
| Resolution (mm³) | 2 x 2 x 2 |
| TR (ms) | 4000 |
| TE (ms) | 116 |
| b-values (s/mm²) | 0, 1000 |
| Phase-encoding direction | AP |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`, `dwi/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Smevik, H. et al. Poorer sleep health is associated with altered brain activation during cognitive control processing in healthy adults. Cereb Cortex 33, 7100–7119 (2023). [https://doi.org/10.1093/cercor/bhad024](https://doi.org/10.1093/cercor/bhad024)


## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)
