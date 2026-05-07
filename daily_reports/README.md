# Daily Reports

最近三天日报（最新在前）：

# [20260506](./202605/20260506.md)
## 📌 今日概况

今日共检索候选论文 11 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现三大趋势：一是基础模型轻量化适配（LoRA微调、扩散模型几何控制），二是自主智能体架构创新（多模态元规划器、视觉语言跟踪），三是零标注学习范式兴起（自监督地理推理、原型学习）。量子计算与模糊逻辑也开始渗透高光谱异常检测领域。

## ✨ 今日亮点

- LoRA微调地理基础模型实现野火精准制图，降低 Sentinel-2 应用门槛
- 轻量化多模态元规划器框架打通遥感感知与决策执行闭环
- 零标注地理推理模型 RemoteZero 突破人工标注依赖瓶颈

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260506] Hyperspectral Anomaly Detection Using Einstein Fuzzy Computing and Quantum Neural Network | Lin Chia-Hsiang, Young Si-Sheng, Langari Reza | the Department of Electrical Engineering, Na- verse network architectures；the Institute of Computer and Communication Engineer- Nevertheless, relying solely on residual-based detectors may；the Department of Mechanical Engineering, Texas | 爱因斯坦模糊计算与量子神经网络结合，为高光谱异常检测提供新型混合智能架构。 | [#335](https://github.com/thinson/RS-PaperClaw/issues/335) |
| [20260506] Low-Rank Adaptation of Geospatial Foundation Models for Wildfire Mapping Using Sentinel-2 Data | Shibli Ali, Nascetti Andrea, Ban Yifang | KTH Royal Institute of Technology | 基于LoRA的地理基础模型参数高效微调，实现Sentinel-2野火燃烧区高精度自动提取。 | [#472](https://github.com/thinson/RS-PaperClaw/issues/472) |
| [20260506] Bridging Perception and Action: A Lightweight Multimodal Meta-Planner Framework for Robust Earth Observation Agents | Xu Jinghui, Shangguan Boyi, Zhu Mengke, Liu Hao, Jiang Junhuan, He Guangjun, Feng Pengming, Jin Shichao, Liang Bin, Chang Yongzhe, Tan Junbo, Zhang Tiantian, Wang Xueqian | State Key Laboratory of Space Information System and Integrated Application | 轻量级多模态元规划器框架支撑地球观测智能体从感知到行动的自主闭环决策。 | [#473](https://github.com/thinson/RS-PaperClaw/issues/473) |
| [20260506] VL-UniTrack: A Unified Framework with Visual-Language Prompts for UAV-Ground Visual Tracking | Xu Boyue, Hou Ruichao, Ren Tongwei, Wu Gangshan | State Key Laboratory for Novel Software Technology, Nanjing University | VL-UniTrack统一视觉语言提示框架，实现无人机与地面跨视角目标跟踪协同。 | [#474](https://github.com/thinson/RS-PaperClaw/issues/474) |
| [20260507] Delay-Aware Large-Small Model Collaboration over LEO Satellite Networks | Guo Mingyu, Wu Wen, Wang Ying, Zhang Songge, Li Liang | Frontier Research Center, Pengcheng Laboratory；School of Information and Communication Engineering, Beijing University of Posts and Telecommunications | 大小模型协同架构结合多智能体强化学习，优化低轨卫星网络边缘计算任务卸载。 | [#475](https://github.com/thinson/RS-PaperClaw/issues/475) |
| [20260507] Efficient Geometry-Controlled High-Resolution Satellite Image Synthesis | Vasilescu Vlad, Faur Daniela, Costăchioiu Teodor | Univ. POLITEHNICA Bucharest；SIGMA Lab, CAMPUS Institute；GEOSENSE, CAMPUS Institute | 几何约束扩散模型实现高分辨率卫星影像可控合成，提升生成图像空间精度。 | [#476](https://github.com/thinson/RS-PaperClaw/issues/476) |
| [20260506] RemoteZero: Geospatial Reasoning with Zero Human Annotations | Yao Liang, Liu Fan, Xu Shengxiang, Zhang Chuanyi, Min Rui, Di Shimin, Zheng Yuhui | Hohai University；Southeast University | RemoteZero零标注框架以自监督强化学习驱动多模态大模型地理空间推理能力。 | [#477](https://github.com/thinson/RS-PaperClaw/issues/477) |
| [20260506] UAV as Urban Construction Change Monitor: A New Benchmark and Change Captioning Model | Gao Yupeng, Li Tianyu, Wang Guoqing, Yang Yang | University of Electronic Science and Technology of China | 无人机城市建筑变化监测新基准与变化描述模型，推动细粒度时序遥感理解。 | [#478](https://github.com/thinson/RS-PaperClaw/issues/478) |

## 🔎 观察

- 参数高效微调（PEFT）正成为遥感基础模型落地的关键路径，LoRA等技术显著降低行业适配成本
- 智能体架构从单一感知向"感知-规划-执行"全链条演进，多模态融合与元学习成为核心支撑技术

---

Powered by OpenClaw🦞

---

# [20260505](./202605/20260505.md)
## 📌 今日概况

今日共检索候选论文 6 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦物理建模与数据质量提升。单篇入选论文提出物理感知的数据集构建方法，针对高分辨率卫星影像去阴影任务，强调从合成数据生成源头解决真实场景适配问题，体现领域对物理可解释性与数据工程并重的趋势。

## ✨ 今日亮点

- 物理感知合成：将大气辐射传输模型嵌入阴影数据集生成流程
- 任务针对性：专为高分辨率卫星影像阴影去除设计基准数据
- 跨机构协作：奥地利、德国、英国多所高校与研究所联合攻关

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260505] deSEO: Physics-Aware Dataset Creation for High-Resolution Satellite Image Shadow Removal | Beltrame Lorenzo, Salzinger Jules, Svoboda Filip, Fanta-Jende Phillipp, Lampert Jasmin, Timofte Radu, Körner Marco | Austrian Institute of Technology；University of Cambridge；University of Würzburg；Technical University of Munich (TUM)；Technical University of Munich (TUM), Munich Data Science Institute (MDSI)；ELLIS Unit Jena, Friedrich Schiller University of Jena | deSEO提出物理感知的高分辨率卫星影像阴影去除数据集构建方法，通过嵌入辐射传输模型提升合成数据的真实场景适配性。 | [#469](https://github.com/thinson/RS-PaperClaw/issues/469) |

## 🔎 观察

- 卫星影像去阴影任务长期受困于真实标注稀缺，物理驱动的合成数据生成或成破局关键路径
- 多机构跨国合作模式在遥感AI领域持续深化，欧洲研究网络在数据基础设施建设中表现活跃

---

Powered by OpenClaw🦞

---

# [20260504](./202605/20260504.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 6 篇。

今日遥感AI研究呈现多元化趋势：基础模型优化与轻量化部署并进，涵盖视觉基础模型对比、扩散模型蒸馏等方向；应用场景拓展至能源监测、废弃物管理与灾害响应；多源数据融合技术持续深化，包括SAR极化融合与全色锐化等。

## ✨ 今日亮点

- SlimDiffSR通过扩散模型蒸馏实现轻量化超分辨率，兼顾性能与效率
- 撒哈拉以南非洲 crowdsourced UAV 废弃物检测开源模型，服务可持续发展
- RAFNet提出区域感知融合网络，优化全色锐化中的空间-光谱信息平衡

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260504] AI and Open-data Driven Scalable Solar Power Profiling | Zhang Shiliang, Maharjan Sabita, Turgut Damla | the Department of Computer can transfer across tasks and domains. We exploit this to；the Foundation AI models, trained on large；diverse datasets, Department of Informatics, University of Oslo, Norway | 基于基础AI模型与开放数据，构建可扩展的太阳能光伏设施识别与功率估算框架 | [#462](https://github.com/thinson/RS-PaperClaw/issues/462) |
| [20260504] Open-access model for detecting openly dumped dispersed municipal solid waste from crowdsourced UAV imagery in Sub-Saharan Africa | Knoblauch Steffen, Ram Kumar Muthusamy, Luis M. A. Bettencourt, Velis Costas, Chrzanowski Pierre, Edward Charles Anderson, Masters Pete, Maholi Innocent, Inguane Antonio, Szamek Levi, Zipf Alexander | HeiGIT at Heidelberg University；Interdisciplinary Centre of Scientific Computing (IWR), Heidelberg University；GIScience Research Group, Heidelberg University；Urban Science Laboratory, Department of Ecology and Evolution, The University of Chicago；Santa Fe Institute；Complexity Science Hub；Imperial College London；Global Facility for Disaster Reduction and Recovery (GFDRR), World Bank；Humanitarian OpenStreetMap Team；Open Map Development Tanzania；Data4Moz | 面向撒哈拉以南非洲开发开源深度学习模型，从众源无人机影像中检测露天分散垃圾堆放点 | [#463](https://github.com/thinson/RS-PaperClaw/issues/463) |
| [20260504] Rethinking Electro-Optical Vision Foundation Models for Remote Sensing Retrieval: A Controlled Comparison with Generalist VFM | Park Hyobin, Seo Minseok, Choi Dong-Geol | ANTLAB；Korea Advanced Institute of Science and Technology (KAIST)；Hanbat National University | 系统对比电光视觉基础模型与通用VFM在遥感检索任务中的跨场景泛化能力差异 | [#464](https://github.com/thinson/RS-PaperClaw/issues/464) |
| [20260504] SlimDiffSR: Toward Lightweight and Efficient Remote Sensing Image Super-Resolution via Diffusion Model Distillation | Wang Ce, Hu Zhenyu, Sun Wanjie | School of Remote Sensing and Information Engineering, Wuhan University | 提出扩散模型蒸馏策略SlimDiffSR，实现轻量高效的遥感影像超分辨率重建 | [#465](https://github.com/thinson/RS-PaperClaw/issues/465) |
| [20260504] RAFNet: Region-Aware Fusion Network for Pansharpening | Zhang Jianing, Zhou Zijian, Sun Kai | the College of Artificial domain responses of dynamically generated weights often；the School of Mathematics and Statistics, Xi’an Jiaotong to construct adaptive kernels within the Fourier domain, un- | 设计区域感知融合网络RAFNet，通过动态权重生成自适应傅里叶域核进行全色锐化 | [#466](https://github.com/thinson/RS-PaperClaw/issues/466) |
| [20260504] Cross-Polarization Fusion of VV AND VH SAR Observations for Improved Flood Mapping | Talreja Jagrati, Tewodros Syum Gebre, Leila Hashemi Beni | North Carolina A&T State University | 融合VV与VH极化SAR观测数据，提升深度学习洪水制图的空间精度与边界清晰度 | [#467](https://github.com/thinson/RS-PaperClaw/issues/467) |

## 🔎 观察

- 基础模型研究从'规模竞赛'转向'效率优化'，模型蒸馏与轻量化成为新焦点
- 遥感应用持续下沉至发展中国家本地化场景，众源数据与开放工具链降低技术门槛

---

Powered by OpenClaw🦞

---
