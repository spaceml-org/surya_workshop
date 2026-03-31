# Lightning Presentations

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1176568364?h=0e1147a155&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 4: Lightning presentations Refletions"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

The lightning presentations served as the culmination of a three day intensive workshop designed to transition participants from zero to hero in AI application development. The primary goal was to validate the Surya foundation model across a diverse range of 14 downstream applications, proving its versatility in handling physical domains and resolutions beyond its original training parameters.

## High Level Overview
This session showcased the collective efforts of 14 diverse teams, largely composed of early career scientists. The presentations highlighted a major technical milestone where teams successfully fine-tuned the model in a cloud environment without needing local data copies. Projects spanned classification, regression, and image segmentation, demonstrating that Surya can be adapted to various solar phenomena including flare ribbons, coronal jets, and solar wind forecasting.

### Included Topics

- Theoretical vision of Surya as a pillar for heliophysics AI infrastructure
- Accessibility milestones involving remote data streaming from AWS S3 buckets
- Success stories of participants with no prior AI experience building functional pipelines
- Preliminary results across multiple modalities such as magnetograms and EUV irradiance
- Strategies for overcoming hardware constraints such as out of memory errors and disk space limits
- Future collaborative goals for joint publications and community building


## Key Concepts and Team Results

*Filament and Feature Detection*

- Prediction filament channels using H-alpha images as a ground truth for UV contrast enhancement
- Flare ribbon segmentation pipeline using binary cross entropy to identify transient brightenings
- Short-lived coronal jet classification with a vision for future active learning
- Identify closed magnetic field configurations within coronal holes

*Forecasting and Regression*

- Forecast Dst indices three days ahead to predict geomagnetic storm intensity using extreme event thresholds
- Binary flare forecasting by applying M-class intensity thresholds to prediction windows
- Nowcasting of solar EUV irradiance to fill gaps in the short wavelength spectrum
- Mapped 2D solar wind speeds to replace traditional empirical relations with machine learning outputs

*Physics-Guided and Generative Modeling*

- Embedded physical laws like divergence-free constraints directly into the learning objective
- Diffusion refiners to improve the structural accuracy of predicted active region evolution
- Validated vector magnetogram quality by testing suitability for nonlinear force-free extrapolations
- Synthesized spectral line profiles from predicted vector magnetograms to mimic polarimetric observations

*Historical Reconstruction and Translation*

- Image-to-image translation to reconstruct line-of-sight magnetograms from EUV channels
- Reconstruction of historical solar EUV data from Ca II K images reaching back to the early 20th century

## Tutorial and Script References

*Cloud Infrastructure*

The presentations confirmed the efficacy of the workshop infrastructure that allows for transparent fine-tuning on remote machines. This confirms that the Surya data loader can handle direct streaming from S3 buckets to bypass local storage limitations.

*LoRA Adapters*

Most teams utilized the Low-Rank Adaptation templates provided earlier in the week to inject trainable matrices into the frozen backbone. This proved successful for teams working with very small sample sizes ranging from 10 to 6,000 images.

*PyTorch Lightning Integration*

The success of these lightning presentations was built upon the shared Lightning modules that standardized training and validation steps. This allowed teams to focus on their specific science targets rather than boilerplate code.

*Weights and Biases Logging*

Teams used the unified logging system to track training and validation loss curves. This provided immediate feedback on whether their specific downstream tasks were learnable within the limited timeframe.

## Slides and Resources

### AI Infrastructure Reflection

<embed src="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_6_AI_Infrastructure.pdf" width='100%' height='600px' type='application/pdf'>
    <p>If this browser does not support PDFs, please download <a href="https://spaceml-org.github.io/surya_workshop/_static/slides/2026_AMJ_Surya_Workshop_6_AI_Infrastructure.pdf">download the PDF</a> to view it.</p>
</embed>


