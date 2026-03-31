# Anatomy of a Downstream Application, Dataloaders, and Baselines

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175225607?h=d245c7dba9&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Dataloaders deep dive with Andréss"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Lecture Aim
The session aims to provide a structured transition from theory to hands-on AI development. It focuses on elevating technical proficiency by teaching participants how to build robust data pipelines and simple baseline models. The goal is to move from understanding the Surya foundation model to implementing specific downstream applications like flare forecasting and filament detection.

### High Level Overview
This session establishes the fundamental elements of the AI training loop: the dataset, the model, and the optimization function. It emphasizes a structured methodology where researchers start with small data samples and simple linear baselines to ensure the pipeline is functional before moving to complex transformer fine-tuning. Participants learn to manage AWS resources, utilize PyTorch Lightning to reduce boilerplate code, and implement professional logging via Weights and Biases.

## Content Coverage
### Included Topics

- AWS resource allocation and the importance of using assigned GPU devices
- Critical SSH security protocols regarding the avoidance of the super user account
- The distinction between deterministic Datasets and stochastic DataLoaders
- Class inheritance in PyTorch for extending the Surya parent class to custom tasks
- Building simple baseline models such as linear regressions or persistence models
- Differentiable loss functions and the role of weighting multiple metrics
- Tensor dimension management and the use of the rearrange function
- Git submodule management for integrating the official Surya repository
- Real-time experiment tracking and logging with Weights and Biases

### Key Concepts

*Data Persistence and Indexing*

A dataset serves as the formalization of input and output pairs. It must be deterministic, meaning that requesting a specific index always yields the same data pair. This structure is built upon CSV-based indices that map timestamps to cloud-stored data stacks.

*The Stochastic DataLoader*

The DataLoader acts as the manager of the data. It handles batching, shuffling, and multi-worker processing. Unlike the dataset, it is often stochastic to facilitate gradient descent, allowing the model to see random subsets of data in each epoch.

*Class Inheritance*

Participants utilize child classes to inherit variables and functions from the Surya parent class. This allows them to reuse complex normalization and file-opening logic while overriding specific methods to append their own downstream targets, such as solar wind properties or filament masks.

*Baselines as Pipeline Verification*

A simple baseline, such as a linear fit that averages image channels, is essential. It allows for the creation of an entire end-to-end training loop without the memory overhead or architectural complexity of a foundation model, serving as a benchmark for later experiments.

*Differentiable Optimization*

Optimization is governed by loss functions that must be differentiable to allow for backpropagation. Researchers can express multiple priorities, such as flux balance and divergence-free fields, by weighting different terms within a single complex loss function.

*Tensor Dimensionality*

Training involves 5D tensors representing batch, channel, time, height, and width. Mismatched dimensions are the most frequent source of errors, requiring researchers to carefully monitor tensor shapes throughout the forward pass.

## Tutorial and Script References

*PyTorch Dataset Template*

The notebook Dataset PyTorch Dataset Template provides the structure for loading Surya scalars and intersecting custom downstream indices with the foundation model data.

*Baseline Template*

The baseline notebook demonstrates how to set CUDA device visibility and initialize the PyTorch Module. It includes the logic for linear regression on flare intensities and demonstrates the forward pass.

*PyTorch Lightning Module*

The Lightning implementation streamlines the training loop by handling training steps, validation steps, and optimizer configurations in a standardized class structure.

*Git and Submodules*

The command `git submodule update --init --recursive` is required to correctly fetch the official Surya repository assets into the local workshop environment.

## Training Objectives

1. Construct a custom Dataset class that successfully intersects Surya stacks with unique downstream targets
2. Implement a simple differentiable model that transforms input stacks into scalar or mask outputs
3. Configure a PyTorch Lightning trainer to manage epochs and validation runs
4. Successfully log a training run to the Weights and Biases dashboard for real-time performance tracking

## Slides and Resources

### Anatomy of a Downstream Application

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_1_Anatomy_of_DS_application.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_1_Anatomy_of_DS_application.pdf">download the PDF</a> to view it.</p>
</embed>

### Dataloaders

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_2_Dataloaders_Lecture.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_2_Dataloaders_Lecture.pdf">download the PDF</a> to view it.</p>
</embed>

### Baselines

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_3_Baselines_Lecture.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_3_Baselines_Lecture.pdf">download the PDF</a> to view it.</p>
</embed>

