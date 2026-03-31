# Finetuning Architecture and Finetuning

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175482615?h=f2b6dcbc90&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 2: Lectures and tutorials with Andrés"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175478182?h=101cc31f93&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 2: Lecture: Finetuning with Andrés"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

## Lecture Aim
The primary objective of this session is to guide researchers through the transition from simple baseline models to sophisticated fine-tuning of the Surya foundation model. It focuses on the practical implementation of Low-Rank Adaptation (LoRA) as an efficient method for adapting large pre-trained weights to specific heliophysics downstream tasks while managing the complexities of shared cloud computing environments and version control.

### High Level Overview
This lecture provides a comprehensive look at the architectural differences between regression-based (1D) and image-based (2D) downstream applications. It bridges the gap between high-level concepts like attention-based learning and the mechanical reality of GPU memory management, mixed precision training, and data caching in AWS. The session emphasizes the use of LoRA to achieve high-performance results with limited data and provides a framework for comparing these advanced models against established baselines using standardized logging.

## Content Coverage
### Included Topics

- Operational management of AWS shared data caches and disk space constraints
- Advanced Git workflows for branching and merging upstream template changes
- The mechanics of Low-Rank Adaptation (LoRA) and its role in modifying attention layers
- Structural differences between Specformer 1D for scalar outputs and Specformer 2D for image masks
- Pooling strategies including global average, max, and attention-based pooling
- Weight initialization and the filtered checkpoint loading process
- Mixed precision training settings to optimize memory usage on GPUs
- Hyperparameter tuning and identifying optimal learning rates through training curves

### Key Concepts

*Low-Rank Adaptation (LoRA)*

LoRA serves as a memory-efficient alternative to full fine-tuning by adding small learnable matrices to every weight matrix. This allows for gentle modifications to the pre-trained attention layers without destroying the original foundational knowledge. It is particularly effective for heliophysics tasks where labeled data points are often scarce.

*Specformer 1D Architecture*

This variant is designed for tasks resulting in scalar values such as flare forecasting or solar wind speed prediction. It incorporates a pooling layer to collapse the high-dimensional internal representation of Surya into a single value.

*Specformer 2D Architecture*

The 2D variant is utilized for spatial tasks like segmentation or image translation. It employs a linear decoder and pixel shuffle operations to expand the internal embeddings back into the original spatial resolution of the input data.

*Global Pooling Strategies*

The model supports multiple ways to aggregate information across the spectral and spatial dimensions. These include global class tokens, transformer-based pooling, and attention-pooling, allowing the practitioner to choose how the model focuses on relevant data features.

*Filtered Checkpoint Loading*

A robust initialization process ensures that pre-trained weights are only loaded into layers where the name and size match the new downstream architecture. This allows for flexibility in changing input channels or output dimensions while still benefiting from the foundation model's learned weights.

*Learning Rate Sensitivity*

Training curves act as a diagnostic tool for model health. Highly erratic curves often indicate a learning rate that is too large, while flat curves suggest the model is learning too slowly. The lecture demonstrates how to use these visual cues to adjust hyperparameters.

## Tutorial and Script References

*Fine-Tuning Template*

The session transitions to the fine-tuning template notebook which mirrors the baseline structure but swaps the simple linear model for the Specformer backbone.

*Config YAML*

All architectural parameters including pooling types, embedding dimensions, and checkpoint paths are managed through a centralized configuration file to maintain consistency across experiments.

*GitHub Management*

The command `git merge origin main` is highlighted as the primary method for researchers to pull the latest architectural updates and template fixes into their personal development branches.

*Shared Environment Paths*

Personal datasets and pre-trained weights are located in the `/shared` HuggingFace directory on the AWS instances to avoid redundant storage usage and facilitate faster loading.

## Training Objectives

1. Successfully implement a LoRA-based fine-tuning run on the Surya backbone
2. Compare the performance of the fine-tuned model against the linear baseline using [Weights and Biases](https://wandb.ai/site/) logging
3. Navigate the 1D and 2D Specformer classes to select appropriate pooling or decoding strategies
4. Resolve potential dimension mismatches through the use of tensor rearrangement and pooling configuration

## Slides and Resources

### Finetuning Architecture

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_4_Finetuning_Architectures_Lecture.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_4_Finetuning_Architectures_Lecture.pdf">download the PDF</a> to view it.</p>
</embed>



