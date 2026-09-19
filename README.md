<div align="center">

<img src="assets/banner.svg" width="100%" alt="Yang Liu — Medical AI · Surgical Video Understanding · Vision-Language Models"/>

<br/>

<a href="https://mruil.github.io"><img src="https://img.shields.io/badge/Homepage-mruil.github.io-0ea5e9?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>
<a href="https://scholar.google.com/citations?user=Fgh4hTUAAAAJ"><img src="https://img.shields.io/badge/Google%20Scholar-Publications-4285F4?style=for-the-badge&logo=googlescholar&logoColor=white"/></a>
<a href="mailto:yang.9.liu@kcl.ac.uk"><img src="https://img.shields.io/badge/Email-yang.9.liu%40kcl.ac.uk-ea4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<img src="https://komarev.com/ghpvc/?username=MRUIL&style=for-the-badge&color=6366f1&label=PROFILE+VIEWS"/>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=2800&pause=900&color=38BDF8&center=true&vCenter=true&multiline=false&repeat=true&width=820&height=45&lines=PhD+in+Medical+AI+%E2%80%94+King's+College+London+(2026)+%7C+ex-Data+Scientist+%40+Proximie;Real-time+surgical+video+understanding+%E2%80%94+phase+recognition+at+scale;Vision-Language+Models+for+the+operating+room;Weakly-supervised+%26+unsupervised+medical+segmentation;MICCAI+%C2%B7+CVPR+%C2%B7+ICCV+%C2%B7+Medical+Image+Analysis+%C2%B7+WACV" alt="typing"/>

</div>

<br/>

## `>_ whoami`

```python
class YangLiu(Researcher):
    education   = ["PhD, King's College London — School of Biomedical Engineering & Imaging Sciences (2021–2026)",
                   "MSc, Huazhong University of Science and Technology (2019–2021), advised by Prof. Xiang Bai"]
    experience  = ["Proximie — Data Scientist, part-time (Jan–Jul 2025)",
                   "ByteDance — Computer Vision Algorithm Engineer, intern (2021)"]
    advisors    = {"primary": "Prof. Sébastien Ourselin", "co-supervisors": ["Prof. Prokar Dasgupta", "Dr. Alejandro Granados"]}

    research    = {
        "surgical video":   ["online phase recognition", "long-video transformers", "streaming VLMs"],
        "segmentation":     ["weakly-supervised referring segmentation", "unsupervised instrument segmentation"],
        "medical imaging":  ["echocardiography phase detection", "stroke lesion segmentation", "AD diagnosis from sMRI"],
        "vision-language":  ["language-driven visual tasks", "noise-injected cross-modal alignment"],
    }

    def mission(self):
        return "Build AI that watches surgery in real time and makes the operating room safer."
```

<br/>

## `>_ research highlights`

<table>
<tr>
<td width="50%" valign="top">

### 🩺 Surgical Video Understanding
Online, causal recognition of what is happening in the OR — from a single frame to a multi-hour procedure.

- **StableSPR** · MICCAI 2026 *(early accept, top 9%)* — temporal error-cascade loss + evidence-gated transition predictor for stable online phase recognition
- **LoViT** · Medical Image Analysis 2024 — long video transformer for surgical phase recognition
- **SKiT** · ICCV 2023 — fast key-information video transformer, real-time online inference
- **Motion-boundary unsupervised instrument segmentation** · MICCAI 2025

</td>
<td width="50%" valign="top">

### 🧠 Vision-Language & Segmentation
Learning with fewer labels, across modalities.

- **WeakMCN** · CVPR 2025 — multi-task collaborative network for weakly-supervised referring expression comprehension & segmentation
- **ArcSin** · language-driven visual tasks via adaptive-ranged cosine similarity noise injection
- **Super-BPD** · CVPR 2020 — boundary-to-pixel direction for fast image segmentation (~25 fps)
- **WDNet** · WACV 2021 — watermark-decomposition network + the CLWD dataset

</td>
</tr>
</table>

<div align="center">

🏆 **1st place** — MICCAI 2022 ATLAS Ischemic Stroke Lesion Segmentation Challenge (Team CTRL)

</div>

<br/>

## `>_ publications`

| Year | Venue | Paper | Links |
|:---:|:---:|---|:---:|
| 2026 | ![MICCAI](https://img.shields.io/badge/MICCAI-early%20accept-22d3ee?style=flat-square) | **Stabilizing Temporal Inference Dynamics for Online Surgical Phase Recognition** — Yang Liu\*, Ning Zhu\*, J. Peng, X. Chen, A. Granados, G. Wang, S. Ourselin | [arXiv](https://arxiv.org/abs/2605.16387) · [code](https://github.com/MRUIL/StableSPR) |
| 2026 | ![TCSVT](https://img.shields.io/badge/IEEE%20TCSVT-journal-fbbf24?style=flat-square) | **SLIM: High-Throughput Watermarking with Stationary Latent Manifolds** — Q. Yan, Z. Chen, Yang Liu†, Z. Cai† | — |
| 2025 | ![MICCAI](https://img.shields.io/badge/MICCAI-2025-22d3ee?style=flat-square) | **Motion-Boundary-Driven Unsupervised Surgical Instrument Segmentation in Low-Quality Optical Flow** — Yang Liu, P. Wu, J. Huo, G. Zhang, Z. Yuan, C. Bergeles, R. Sparks, P. Dasgupta, A. Granados, S. Ourselin | [arXiv](https://arxiv.org/abs/2403.10039) |
| 2025 | ![CVPR](https://img.shields.io/badge/CVPR-2025-818cf8?style=flat-square) | **WeakMCN: Multi-task Collaborative Network for Weakly Supervised Referring Expression Comprehension and Segmentation** — Yang Liu\*, Silin Cheng\*, X. He, S. Ourselin, L. Tan, G. Luo | [arXiv](https://arxiv.org/abs/2505.18686) · [code](https://github.com/MRUIL/WeakMCN) |
| 2025 | ![ICME](https://img.shields.io/badge/ICME-2025-34d399?style=flat-square) | **A Domain Generalization Framework Based on Wavelet-Driven Structural Enhancement and Contrastive Alignment** — Y. Xu, T. Zhang, Yang Liu | — |
| 2024 | ![MedIA](https://img.shields.io/badge/Medical%20Image%20Analysis-journal-f472b6?style=flat-square) | **LoViT: Long Video Transformer for Surgical Phase Recognition** — Yang Liu, M. Boels, L. C. Garcia-Peraza-Herrera, T. Vercauteren, P. Dasgupta, A. Granados, S. Ourselin | [paper](https://www.sciencedirect.com/science/article/pii/S1361841524002913) · [code](https://github.com/MRUIL/LoViT) |
| 2024 | ![ISBI](https://img.shields.io/badge/ISBI-2024-a78bfa?style=flat-square) | **Gray Matter-Guided Attention Network for AD Diagnosis Using Structural MRI** — Y. Zhang, H. Cai, Y. Du, B. Xu, Yang Liu† | [paper](https://ieeexplore.ieee.org/abstract/document/10635472) |
| 2024 | ![arXiv](https://img.shields.io/badge/arXiv-preprint-b31b1b?style=flat-square) | **DDSB: An Unsupervised and Training-free Method for Phase Detection in Echocardiography** — Z. Bu\*, Yang Liu\*†, et al. | [arXiv](https://arxiv.org/abs/2403.12787) · [code](https://github.com/MRUIL/DDSB) |
| 2024 | ![arXiv](https://img.shields.io/badge/arXiv-preprint-b31b1b?style=flat-square) | **ArcSin: Adaptive ranged cosine Similarity injected noise for Language-Driven Visual Tasks** — Yang Liu, X. Yu, G. Zhang, Z. Zhu, C. Bergeles, P. Dasgupta, A. Granados, S. Ourselin | [arXiv](https://arxiv.org/abs/2402.17298) |
| 2023 | ![ICCV](https://img.shields.io/badge/ICCV-2023-a78bfa?style=flat-square) | **SKiT: a Fast Key Information Video Transformer for Online Surgical Phase Recognition** — Yang Liu, J. Huo, J. Peng, R. Sparks, P. Dasgupta, A. Granados, S. Ourselin | [paper](https://openaccess.thecvf.com/content/ICCV2023/html/Liu_SKiT_a_Fast_Key_Information_Video_Transformer_for_Online_Surgical_ICCV_2023_paper.html) · [repo](https://github.com/MRUIL/SKiT) |
| 2021 | ![WACV](https://img.shields.io/badge/WACV-2021-34d399?style=flat-square) | **WDNet: Watermark-Decomposition Network for Visible Watermark Removal** — Yang Liu, Z. Zhu, X. Bai | [paper](https://openaccess.thecvf.com/content/WACV2021/papers/Liu_WDNet_Watermark-Decomposition_Network_for_Visible_Watermark_Removal_WACV_2021_paper.pdf) · [code](https://github.com/MRUIL/WDNet) |
| 2020 | ![CVPR](https://img.shields.io/badge/CVPR-2020-818cf8?style=flat-square) | **Super-BPD: Super Boundary-to-Pixel Direction for Fast Image Segmentation** — J. Wan, Yang Liu, D. Wei, X. Bai, Y. Xu | [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wan_Super-BPD_Super_Boundary-to-Pixel_Direction_for_Fast_Image_Segmentation_CVPR_2020_paper.pdf) · [code](https://github.com/JianqiangWan/Super-BPD) |

<sub>\* equal contribution &nbsp;·&nbsp; † corresponding author</sub>

<br/>

## `>_ featured repositories`

<div align="center">

<a href="https://github.com/MRUIL/WDNet"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MRUIL&repo=WDNet&theme=tokyonight&hide_border=true&bg_color=0d1117" /></a>
<a href="https://github.com/MRUIL/WeakMCN"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MRUIL&repo=WeakMCN&theme=tokyonight&hide_border=true&bg_color=0d1117" /></a>
<a href="https://github.com/MRUIL/LoViT"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MRUIL&repo=LoViT&theme=tokyonight&hide_border=true&bg_color=0d1117" /></a>
<a href="https://github.com/MRUIL/StableSPR"><img src="https://github-readme-stats.vercel.app/api/pin/?username=MRUIL&repo=StableSPR&theme=tokyonight&hide_border=true&bg_color=0d1117" /></a>

</div>

<br/>

## `>_ tech stack`

<div align="center">

**Deep Learning**<br/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"/>
<img src="https://img.shields.io/badge/Lightning-792EE5?style=for-the-badge&logo=lightning&logoColor=white"/>
<img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/timm-000000?style=for-the-badge&logo=github&logoColor=white"/>
<img src="https://img.shields.io/badge/CUDA-76B900?style=for-the-badge&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/ONNX-005CED?style=for-the-badge&logo=onnx&logoColor=white"/>

**Vision · Medical · Multimodal**<br/>
<img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white"/>
<img src="https://img.shields.io/badge/MONAI-1E90FF?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/SAM%20%2F%20EfficientSAM-0467DF?style=for-the-badge&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/CLIP%20%2F%20VLM-412991?style=for-the-badge&logo=openai&logoColor=white"/>
<img src="https://img.shields.io/badge/OpenMMLab-2F80ED?style=for-the-badge&logoColor=white"/>

**Infra · Tooling**<br/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=cplusplus&logoColor=white"/>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"/>
<img src="https://img.shields.io/badge/Slurm%20HPC-1F6FEB?style=for-the-badge&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/>
<img src="https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white"/>
<img src="https://img.shields.io/badge/Weights%20%26%20Biases-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black"/>

</div>

<br/>

## `>_ github analytics`

<div align="center">

<img height="180" src="https://github-readme-stats.vercel.app/api?username=MRUIL&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&include_all_commits=true&count_private=true&rank_icon=github" />
<img height="180" src="https://github-readme-stats.vercel.app/api/top-langs/?username=MRUIL&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&langs_count=8&exclude_repo=MRUIL.github.io,bay" />

<br/>

<img src="https://streak-stats.demolab.com?user=MRUIL&theme=tokyonight&hide_border=true&background=0D1117&ring=38BDF8&fire=F472B6&currStreakLabel=38BDF8" />

<br/><br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=MRUIL&theme=tokyo-night&hide_border=true&bg_color=0d1117&color=38bdf8&line=818cf8&point=f472b6&area=true" width="95%"/>

<br/><br/>

<img src="https://github-profile-trophy.vercel.app/?username=MRUIL&theme=tokyonight&no-frame=true&no-bg=true&row=1&column=7&margin-w=8" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/MRUIL/MRUIL/output/github-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/MRUIL/MRUIL/output/github-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/MRUIL/MRUIL/output/github-snake-dark.svg" width="95%" />
</picture>

</div>

<br/>

## `>_ timeline`

```text
2026.05  ◆ MICCAI 2026 early accept (top 9%) — StableSPR          ◆ IEEE TCSVT — SLIM
2026.01  ◆ PhD awarded, King's College London
2025     ◆ CVPR 2025 — WeakMCN   ◆ MICCAI 2025   ◆ ICME 2025   ◆ Data Scientist @ Proximie (Jan–Jul)
2024     ◆ Medical Image Analysis — LoViT   ◆ ISBI 2024   ◆ DDSB / ArcSin preprints
2023     ◆ ICCV 2023 — SKiT
2022     ◆ 1st place, MICCAI ATLAS Stroke Lesion Segmentation Challenge
2021     ◆ MSc, HUST   ◆ CV Algorithm Engineer intern @ ByteDance   ◆ PhD begins @ KCL, London  
2020–21  ◆ CVPR 2020 — Super-BPD   ◆ WACV 2021 — WDNet
```

<br/>

<div align="center">

**Open to collaboration on surgical AI, medical video understanding and vision-language models.**<br/>
<sub>yang.9.liu@kcl.ac.uk</sub>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:070b18,50:1e3a8a,100:38bdf8&height=110&section=footer" width="100%"/>

</div>
