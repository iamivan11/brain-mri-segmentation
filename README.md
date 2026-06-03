# Brain MRI Segmentation With Traditional CV

We study 2D and 3D brain MRI tissue segmentation using traditional computer
vision techniques, developing and evaluating multiple approaches to segment 6
tissue classes from T1-weighted data.

## Data

### 1: Brain MRI (T1-weighted)

- **Description**: 10 consecutive axial cross-sections of a publicly available
  T1-weighted MRI of a single human subject, paired with pre-segmented
  ground-truth labels for comparison and evaluation.
- **Classes (6 tissue types)**:
  - Label 0: Air
  - Label 1: Skin/scalp
  - Label 2: Skull
  - Label 3: CSF (Cerebrospinal Fluid)
  - Label 4: Gray Matter
  - Label 5: White Matter
- **Images**: grayscale, 362×434 pixels per slice, 10 slices at 1mm intervals
  (10mm total span).

<img src="demo/t1_1.png" width="350" alt="T1 MRI">
<img src="demo/gt_1.png" width="350" alt="Ground Truth">

## Setup

### Requirements

- Python >=3.10, <3.13
- Poetry (recommended) or pip

### Installation

```bash
# Clone repository
git clone https://github.com/iamivan11/brain-mri-segmentation.git
cd brain-mri-segmentation

# Install Poetry (if not installed)
curl -sSL https://install.python-poetry.org | python3 -

# Create environment and install dependencies
poetry install
poetry shell

# Setup pre-commit hooks
pre-commit install
pre-commit run -a
```

### Usage

```bash
# Add the data: place brain.mat in the project root
# (must contain 'T1' MRI data and 'label' ground-truth arrays)

# Main experiments, evaluations and results
jupyter notebook notebooks/main.ipynb

# Step-by-step explanations
jupyter notebook notebooks/step_by_step.ipynb
```

## Structure

```
brain-mri-segmentation/
├── README.md                    # This file
├── pyproject.toml               # Project dependencies and configuration
├── poetry.lock                  # Locked dependency versions
├── brain.mat                    # MRI data and ground truth labels
├── brain_mri_segmentation/     # Core package
│   ├── __init__.py
│   ├── basic.py                # Basic utilities
│   ├── metrics.py              # Evaluation metrics
│   ├── segmentation.py         # Segmentation algorithms
│   └── visualization.py        # Visualization utilities
├── notebooks/                   # Jupyter notebooks
│   ├── main.ipynb              # Complete experiments and evaluation
│   └── step_by_step.ipynb      # Step-by-step explanations
└── demo/                        # Visualization outputs and results
    ├── a1_2d_1.png
    ├── a1_a2_a3_2d.png
    ├── a2_2d_1.png
    ├── a2_3d_1.png
    ├── a3_2d_1.png
    ├── a3_3d_1.png
    ├── gt_1.png
    ├── gt_a2_a3_3d.png
    └── t1_1.png
```

## Tech Stack

The stack favors classical computer vision over deep learning — every
segmentation step (brain extraction, thresholding, clustering) is handled by a
single mature, well-documented library, keeping the pipeline lightweight and
fully reproducible without GPUs or training data.

<table>
  <thead>
    <tr>
      <th>Layer</th>
      <th>Choice</th>
      <th>Why this over alternatives</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Image processing / CV</td>
      <td><strong>scikit-image</strong></td>
      <td>Ready-made active contours (MCV/MGAC), morphology and multi-Otsu — the core of the methods</td>
    </tr>
    <tr>
      <td><strong>OpenCV</strong></td>
      <td>Fast, battle-tested primitives for the lower-level image ops</td>
    </tr>
    <tr>
      <td>Numerics</td>
      <td><strong>NumPy</strong></td>
      <td>Vectorized array math underpinning every slice and 3D-volume operation</td>
    </tr>
    <tr>
      <td>Clustering</td>
      <td><strong>scikit-learn</strong></td>
      <td>Robust, well-tuned K-Means for intensity-based tissue grouping</td>
    </tr>
    <tr>
      <td>Visualization</td>
      <td><strong>Matplotlib</strong></td>
      <td>Direct control over the side-by-side slice and segmentation figures</td>
    </tr>
    <tr>
      <td>Notebooks</td>
      <td><strong>Jupyter</strong> (ipykernel)</td>
      <td>Interactive experiments and step-by-step explanations live alongside results</td>
    </tr>
    <tr>
      <td>Env &amp; packaging</td>
      <td><strong>Poetry</strong></td>
      <td>Single lockfile + virtualenv for reproducible installs (vs raw pip + requirements.txt)</td>
    </tr>
    <tr>
      <td>Lint &amp; format</td>
      <td><strong>Ruff</strong></td>
      <td>One Rust tool replaces flake8 + black + isort, near-instant</td>
    </tr>
    <tr>
      <td>Pre-commit hooks</td>
      <td><strong>pre-commit</strong></td>
      <td>Auto-enforces formatting and checks before every commit</td>
    </tr>
  </tbody>
</table>
