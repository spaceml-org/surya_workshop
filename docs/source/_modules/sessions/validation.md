# Validation

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1176268895?h=447c33c790&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 3: Validation day"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


## Lecture Aim
The primary objective of this session is to shift the mindset of practitioners from viewing AI as a deterministic tool to recognizing it as a stochastic process. The lecture focuses on establishing rigorous validation protocols, the necessity of baselines, and transitioning from interactive notebooks to scalable training scripts for the Surya model.

### High Level Overview
This lecture addresses the philosophical and practical requirements for successful machine learning in Heliophysics. It covers the inherent noise in data, the risks of human-induced overfitting, and the structural methods used to ensure model generalizability. Participants are guided through the logistics of distributed GPU training and the importance of benchmarking performance against simple models.

## Content Coverage
### Included Topics
- The stochastic nature of machine learning and its resemblance to real-world noise
- Philosophical distinctions between the problem one can solve versus the problem one wants to solve
- Standard protocols for data splitting into training, validation, and test sets
- The utility of ensembles in identifying model confusion and improving researcher discipline
- Technical setup for overnight training runs using Python scripts (specific to the workshop)
- Performance optimization through increased worker counts and direct bucket connections
- Specific strategies for handling hemispheric asymmetry and solar cycle dependency in data

### Key Concepts

*Stochasticity and Noise*

Machine learning is a stochastic problem masking as a deterministic one. Results are often samples out of a universe of possibilities, meaning metrics must be viewed as probabilistic rather than absolute values.

*The Human as a Single Point of Failure*

Human researchers are the main risk for underperformance. The tendency to obsessively chase metrics on a test set leads to overfitting and models that fail in operational conditions.

*Validation Protocols*

Strict adherence to protocols separates useful applications from curiosities. This includes locking away a test set that mimics future operational conditions and never making architectural or hyperparameter decisions based on its performance.

*Data Splitting Strategy*

For heliophysics, a yearly split with a buffer based on months is recommended. This ensures solar activity is represented without leaking information between training and validation sets.

*Ensembles*

Training multiple models or members allows researchers to move away from chasing single-digit improvements in one model. Agreement or disagreement within an ensemble provides informative data about model confidence.

*Baselines and the Spherical Cat*

A baseline, such as a simple logistic regression, is mandatory for scientific rigor. It serves as the simplest reference point to justify the complexity of a fine-tuned transformer model.

## Tutorial and Script References

*Python Training Script*

The lecture marks the transition from interactive notebooks to Python scripts, which can be designed for overnight execution and handles both baseline training and Surya fine-tuning.

*Git Workflow*

A reminder to run the `git merge origin main` command to update their branches with the latest training scripts and configuration patches.

*Performance Tuning*

To optimize training speed, the num workers parameter in the data loader should be increased to 28 or 30. This reduces bottlenecks when fetching batches from the AWS storage buckets (specific to the workshop).

*GPU Assignments*

The environment utilizes a multi-GPU setup where participants are assigned specific devices and IP addresses to avoid memory clashes during group stress tests (specific to the workshop).

## Training Objectives

1. Execute runs with different amounts of training data while keeping validation sets identical to measure return on investment
2. Conduct concurrent runs comparing a baseline model against a fine-tuned Surya model
3. Utilize ensemble members to develop a stochastic statement about downstream application performance

## Slides and Resources

### Validation

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_5_Validation.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_5_Validation.pdf">download the PDF</a> to view it.</p>
</embed>

