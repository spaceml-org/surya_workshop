# Workshop Overview Videos

Welcome to the workshop. This section provides a quick video-based introduction to the key topics and additional context around Surya.

---
## Videos
- [Welcome from NASA - Madhulika Guhathakurta | NASA](lika)
- [Welcome from NASA-IMPACT - Rahul Ramachandran | NASA-IMPACT](rahul)
- [Foundation models for science: Johannes Schmude | IBM](johannes)
- [Surya 101: Sujit Roy | NASA-IMPACT](sujit)
- [What can Surya do for heliophysics? Andrés Muñoz-Jaramillo | SwRI](andres)
- [Introduction to the SuryaBench dataset: Dinesha Vasanta Hegde | University of Alabama in Huntsville](dinesha)
- [Downstream science demos](downstream)
- [HelioAI - what's next?](helioai)

--- 

(lika)=
### Welcome from NASA - Madhulika Guhathakurta

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174453225?h=a77850a832&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1 : Welcome from Madhulika Guhathakurta | NASA"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Introduction from Madhulika Guhathakurta to the Surya Science workshop, focused on integrating the Surya foundation model into heliophysics through rigorous testing and collaboration. This workshop is a shift away from typical product demonstrations toward a framework where AI is interrogated as a scientific object and its errors are analyzed for deeper physical insights. This introduction outlines a clear progression from understanding model foundations to validating results, emphasizing that success lies in generating sharper research questions rather than just achieving better technical metrics.

(rahul)=
### Welcome from NASA-IMPACT - Rahul Ramachandran

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174455045?h=e95462ceda&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Welcome from Rahul Ramachandran | NASA"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Rahul Ramachandran provides a strategic overview of NASA's AI for Science initiative, framing the Surya model within the broader historical mission of distilling knowledge from massive space science datasets. This talk explores how foundation models represent a paradigm shift from labor-intensive, bespoke modeling to scalable, self-supervised systems that can be adapted for diverse scientific applications. The presentation uses the success of the Prithvi Earth science model as a blueprint, challenging participants to move beyond traditional classification tasks toward innovative explorations of the model's underlying data representations.

(johannes)=
### Foundation models for science: Johannes Schmude | IBM

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174478630?h=402c4e6925&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Johannes Schmude | IBM"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Q&A

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174478314?h=5a74a66fec&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Q&amp;A with Johannes Schmude | IBM"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Johannes Schmude from IBM highlights the transformative potential of foundation models in science by drawing parallels to recent breakthroughs in atmospheric physics and weather forecasting. This includes a discussion on how these models serve as powerful new tools in the scientific quiver, offering massive computational speedups and data efficiency without replacing traditional physics-based methods.

The talk emphasizes that scientific foundation models are defined by their generalization across tasks and instruments, illustrated through examples like partial differential equation emulation and cross-modality satellite mapping. Schmude concludes that trust in these systems is built through a continuous, rigorous process of community validation and challenging the model’s limits rather than through a single, static explainability metric.

(sujit)=
### Surya 101: Sujit Roy | NASA-IMPACT

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174793156?h=d2714e824c&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Surya 101 with Sujit Roy | NASA-IMPACT"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Q&A

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174795798?h=b15886bbc3&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Q&amp;A with Sujit Roy | NASA-IMPACT"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Sujit Roy from NASA-IMPACT, introduces Surya as a 366-million parameter foundation model trained on nearly 260 terabytes of high-resolution solar data. The video details an innovative architecture that uses spectral blocks and sliding window attention to process massive 4K images while remaining flexible enough to be fine-tuned on standard consumer hardware.

The talk highlights how Surya outperforms traditional models in certain cases, such as solar flare and wind forecasting by leveraging self-supervised temporal learning rather than relying on human-labeled datasets. The session concludes by framing the model not just as a labeling tool, but as a gateway for scientists to interrogate physical processes and test hypotheses directly within a latent embedding space.

(andres)=
### What can Surya do for heliophysics? Andrés Muñoz-Jaramillo | SwRI

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174807211?h=63190628df&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: What can Surya do for heliophysics? with Andrés"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Andrés Muñoz-Jaramillo from Southwest Research Institute, introduces the potential applications of Surya in heliophysics. He transitions the workshop from high-level theory to the practical realities of building downstream applications, framing the process as a disciplined experimental exercise. He emphasizes that while Surya provides a massive repository of distilled knowledge from its time-advancement pretext task, success in fine-tuning requires researchers to establish clear baselines and value-added metrics. By using timestamps as a universal index, scientists can connect Surya’s internal representations to specific supervised tasks like flare forecasting or instrument translation, starting with small datasets to observe how the model scales.

The session also highlights the technical modularity of the architecture—including tokenizers, spectral blocks, and attention mechanisms—which users can manipulate to adapt the model to new domains. Crucially, the human researcher is often a risk factor in the AI loop, urging the community to maintain strict discipline with hold-out data to avoid self-deception. He concludes that the goal is not just to outperform existing models, but to use Surya as a catalyst for a more sophisticated, collaborative way of doing heliophysics.

(dinesha)=
### Introduction to the SuryaBench dataset: Dinesha Vasanta Hegde | University of Alabama in Huntsville

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174819147?h=ad681f9fab&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: SuryaBench dataset with Dinesha Vasanta Hegde | University of Alabama in Huntsville"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Q&A 

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1174820276?h=14021a7780&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Q&amp;A with Dinesha Vasanta Hegde"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Dinesha Vasanta Hegde from the University of Alabama in Huntsville introduces SuryaBench, the curated 360-terabyte dataset of native-resolution SDO data that serves as the essential fuel for the Surya foundation model. The talk details the rigorous preprocessing pipeline—including temporal synchronization, instrument degradation correction, and spatial homogenization—required to transform raw solar observations into a standardized, ML-ready resource spanning 14 years of activity. In addition to the core 13-channel dataset, the video highlights six auxiliary datasets designed for specific tasks like flare forecasting and active region segmentation, positioning SuryaBench as an open-source, high-fidelity pillar for the broader heliophysics community.

(downstream)=
### Downstream science demos

#### Berkay Aydin - Solar flare forecasting 

<div style="padding:62.50% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175196120?h=6a6bb97104&badge=0&autopause=0&player_id=0&app_id=58479/embed" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen frameborder="0" style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe></div>

#### Shah Bahauddin - Solar EUV irradiance modelling

<div style="padding:62.50% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175197605?h=29ca5b285a&badge=0&autopause=0&player_id=0&app_id=58479/embed" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen frameborder="0" style="position:absolute;top:0;left:0;width:100%;height:100%;"></iframe></div>

#### Vishal Upendran - Solar wind forecasting

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175198541?h=3df18393b5&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Vishal"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

#### Downstream science Q&A

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175202339?h=a9c6875039&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: Q&amp;A Downstream science demos"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

(helioai)=
### HelioAI - what’s next?

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175206930?h=8fd41296d5&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: HelioAI - what’s next? with Lika"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Introduction of the Helio AI Portal, a strategic shift from "project-based" AI, where models often disappear after a single paper, to a permanent, scalable scientific infrastructure. This platform is designed to provide the community with analysis-ready data, documented evaluations, and essential scientific metadata, ensuring that models like Surya are not just isolated demonstrations but shared resources that can be stress-tested and reused by everyone.

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175207372?h=2cde5a828f&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: HelioAI - what’s next? with Mike"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Walkthrough of HelioAI.org, a prototype web application designed to move heliophysics beyond "development in isolation" by centralizing the community's rapidly expanding library of AI artifacts. Unlike a static website, the portal features a content management system that allows researchers to upload projects, document the performance of downstream use cases, and provide the essential metadata required for both human discovery and agentic AI applications.

<div style="padding:62.5% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1175209220?h=dbd23d868e&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" referrerpolicy="strict-origin-when-cross-origin" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Day 1: HelioAI - what’s next? with Shing"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

*What to expect:* Exploration of the critical role of the SPASE (Space Physics Archive Search and Extract) metadata model, which has spent three decades standardizing how space science data is documented to ensure long-term reusability. The talk shares how this mature framework, already the de facto standard for NASA, ESA, and JAXA, is being extended to specifically describe AI/ML resources like the Surya model.