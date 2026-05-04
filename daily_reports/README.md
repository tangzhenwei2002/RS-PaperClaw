# Daily Reports

最近三天日报（最新在前）：

# [20260501](./202605/20260501.md)
## 📌 今日概况

今日共检索候选论文 3 篇；关键词+LLM 智能匹配遥感交叉论文 3 篇；最终纳入日报 2 篇。

今日遥感AI研究聚焦两大方向：一是基础模型在气溶胶光学厚度反演中的创新应用，利用PACE卫星高光谱数据探索Vision Transformer的潜力；二是生成式AI技术在遥感影像超分辨率重建中的新进展，Flow Matching方法为Sentinel-2数据增强提供了新思路。

## ✨ 今日亮点

- 基础AI模型首次应用于PACE卫星气溶胶光学厚度估算，拓展高光谱遥感应用边界
- Flow Matching生成模型引入Sentinel-2超分辨率任务，为扩散模型提供高效替代方案
- 跨机构合作凸显遥感AI研究的多学科融合趋势，涵盖大气科学与精准农业领域

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260501] Foundation AI Models for Aerosol Optical Depth Estimation from PACE Satellite Data | Zahid Hassan Tushar, Purushotham Sanjay | University of Maryland, Baltimore County | 该研究基于PACE卫星高光谱数据，构建Vision Transformer基础模型实现气溶胶光学厚度精准估算。 | [#454](https://github.com/thinson/RS-PaperClaw/issues/454) |
| [20260501] Flow matching for Sentinel-2 super-resolution: implementation, application, and implications | Hester Dakota, Vitor S. Martins, Lucas B. Ferreira, Thainara M. A. Lima, Juliana A. Araújo | Department of Agricultural and Biological Engineering, Mississippi State University；North Mississippi Research and Extension Center, Mississippi State University | 该研究将Flow Matching生成模型应用于Sentinel-2影像超分辨率，系统评估其实现细节与应用效果。 | [#455](https://github.com/thinson/RS-PaperClaw/issues/455) |

## 🔎 观察

- 基础模型向地球科学专用领域渗透，高光谱卫星数据成为新的模型训练与验证资源
- 扩散模型替代方案在遥感影像生成任务中受关注，计算效率与重建质量的权衡成为关键考量

---

Powered by OpenClaw🦞

---

# [20260430](./202604/20260430.md)
## 📌 今日概况

今日共检索候选论文 15 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 8 篇。

今日遥感AI研究呈现多模态融合与高效架构两大主线。高光谱分类与超分辨率持续深化光谱-空间联合建模；扩散模型、对比学习等自监督范式向语义分割、表格数据等场景扩展；轻量化设计与预训练策略优化成为工程落地关键。

## ✨ 今日亮点

- 扩散模型Noise2Map实现语义分割与变化检测端到端统一框架
- 超光谱超分辨率引入频域动态注意力机制突破重建瓶颈
- 多源数据融合网络协同挖掘SAR、高光谱与LiDAR互补信息

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260430] Hyperspectral Image Classification via Efficient Global Spectral Supertoken Clustering | Liu Peifu, Xu Tingfa, Wang Jie, Chen Huan, Bai Huiyan, Li Jianan | Beijing Institute of Technology；Beijing Institute of Technology Chongqing Innovation Center；Key Laboratory of Photoelectronic Imaging Technology and System, Ministry of Education of China | 提出全局光谱超像素聚类方法，通过超令牌机制提升高光谱分类边界 delineation 效率。 | [#443](https://github.com/thinson/RS-PaperClaw/issues/443) |
| [20260430] Noise2Map: End-to-End Diffusion Model for Semantic Segmentation and Change Detection | Shibli Ali, Nascetti Andrea, Ban Yifang | KTH Royal Institute of Technology；Delft University of Technology | Noise2Map将扩散模型用于遥感语义分割与变化检测，实现噪声到地图的直接生成。 | [#446](https://github.com/thinson/RS-PaperClaw/issues/446) |
| [20260430] Multi-wavelength polarisation imaging with inverse designed metasurfaces | Sarah E. Dean, Li Neuton, Munro Josephine, Laudert Benjamin, Siefke Thomas, Ngo Quyet, Sharp Robert, Dragomir N. Neshev, Eilenberger Falk, Andrey A. Sukhorukov | ARC Centre of Excellence for Transformative Meta-Optical Systems (TMOS), Department of Electronic Materials Engineering, Research School of Physics, The Australian National University；Fraunhofer-Institute for Applied Optics and Precision Engineering IOF；Friedrich Schiller University Jena, Abbe Center of Photonics, Institute of Applied Physics；Ernst-Abbe-Hochschule Jena University of Applied Sciences；Research School of Astronomy & Astrophysics, The Australian National University | 逆设计超表面实现多波长偏振成像，为计算成像硬件提供新范式。 | [#447](https://github.com/thinson/RS-PaperClaw/issues/447) |
| [20260430] A generalised pre-training strategy for deep learning networks in semantic segmentation of remotely sensed images | Fang Yuan, Cai Yuanzhi, Aryal Jagannath, Zhu Qinfeng, Huang Hong, Zhang Cheng, Fan Lei | Xi'an Jiaotong-Liverpool University；CSIRO Mineral Resources；The University of Melbourne | 提出通用预训练策略缓解遥感语义分割中的域间隙问题，提升跨场景泛化能力。 | [#448](https://github.com/thinson/RS-PaperClaw/issues/448) |
| [20260430] Robust Lightweight Crack Classification for Real-Time UAV Bridge Inspection | Li Wei, Li Haisheng, Li Weijie, Wang Jiandong, Ma Kaichen, Yang Luming | Bay Area Super Bridge Maintenance Technology Center, Guangdong Provincial Highway Construction Co., Ltd.；Guangdong AIHISUN Technology Co., Ltd. | 面向无人机桥梁巡检的轻量级裂缝分类网络，兼顾实时性与鲁棒性需求。 | [#449](https://github.com/thinson/RS-PaperClaw/issues/449) |
| [20260430] ZAYAN: Disentangled Contrastive Transformer for Tabular Remote Sensing Data | Al Zadid Sultan Bin Habib, Tasnim Tanpia, Md. Ekramul Islam, Tabasum Muntasir | Lane Dept. of Computer Science and Electrical Engineering, West Virginia University；Dept. of Geology & Geography, West Virginia University；Department of Computer Science and Engineering, Green University of Bangladesh；Department of Computer Science and Engineering, Stamford University Bangladesh | ZAYAN解耦对比Transformer专为遥感表格数据设计，拓展自监督学习应用边界。 | [#450](https://github.com/thinson/RS-PaperClaw/issues/450) |
| [20260430] Spectral Dynamic Attention Network for Hyperspectral Image Super-Resolution | Zhang Tengya, Gao Feng, Qi Lin, Dong Junyu, Du Qian | the Sanya Oceanographic Institution, Ocean Univer- conventional FFN follows a simple linear；State Key Laboratory of spectral；the Department of Electrical and Computer Engineering, recover fine-grained details and leads to suboptimal recon- | 频域动态注意力网络针对高光谱超分辨率，通过通道稀疏注意力捕获光谱相关性。 | [#451](https://github.com/thinson/RS-PaperClaw/issues/451) |
| [20260430] Representative Spectral Correlation Network for Multi-source Remote Sensing Image Classification | Gong Chuanzheng, Gao Feng, Lin Junyan, Dong Junyu, Du Qian | the Department of Computing, The Hong Kong SAR/LiDAR data lacks sufficient spectral information, limit-；the Department of Electrical and Computer Engineering, ing its ability to distinguish objects with similar appearances；the State Key Laboratory of Physical Oceanography, Ocean University of China, Qingdao | 代表性光谱相关网络融合SAR、高光谱与LiDAR，解决多源遥感分类光谱选择难题。 | [#452](https://github.com/thinson/RS-PaperClaw/issues/452) |

## 🔎 观察

- 扩散模型正从生成任务向判别任务渗透，Noise2Map或预示遥感分割新范式。
- 高光谱研究密集涌现，光谱-空间联合建模与频域分析成为竞争焦点。

---

Powered by OpenClaw🦞

---

# [20260429](./202604/20260429.md)
## 📌 今日概况

今日共检索候选论文 14 篇；关键词+LLM 智能匹配遥感交叉论文 11 篇；最终纳入日报 10 篇。

今日遥感AI研究呈现多模态融合与基础模型迁移两大主线。无人机RGBT语义分割、开放词汇变化检测等任务聚焦跨模态对齐；高光谱基础模型跨域迁移、量子机器学习特征映射等探索新型表征学习。3D视觉与点云配准等几何任务持续受到关注，扩散模型与拓扑学习方法为降维与半监督学习提供新思路。

## ✨ 今日亮点

- MemOVCD提出免训练开放词汇变化检测，通过跨时序记忆推理实现自适应修正
- AirZoo构建大规模合成数据集，统一支撑航空几何三维视觉的地面真值研究
- 高光谱扩散框架将噪声映射至低维流形，解决退化图像分类的维度灾难问题

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260429] Graph-based Semantic Calibration Network for Unaligned UAV RGBT Image Semantic Segmentation and A Large-scale Benchmark | Fan Fangqiang, Zhao Zhicheng, Ma Xiaoliang, Li Chenglong, Tang Jin | Key Laboratory of Intelligent Comput-；the School of Computer Science and Technology, Anhui the modality gap is reduced, deriving geometric corrections；the Anhui Provincial Key Laboratory of Multimodal | 图神经网络实现无人机RGBT图像语义分割的跨模态对齐与几何校正，构建大规模基准数据集。 | [#435](https://github.com/thinson/RS-PaperClaw/issues/435) |
| [20260429] MemOVCD: Training-Free Open-Vocabulary Change Detection via Cross-Temporal Memory Reasoning and Global-Local Adaptive Rectification | Kuang Zuzheng, Chang Honghao, Liang Boqiang, Wang Haoqian, He Lijun, Li Fan, Bi Haixia | Xi'an Jiaotong University | 免训练开放词汇变化检测方法MemOVCD，利用跨时序记忆推理与全局-局部自适应修正提升检测精度。 | [#436](https://github.com/thinson/RS-PaperClaw/issues/436) |
| [20260429] Parameterized Quantum Circuits as Feature Maps: Representation Quality and Readout Effects in Multispectral Land-Cover Classification | Komini Ralntion, Mandilara Aikaterini, Maragkopoulos Georgios, Syvridis Dimitris | Department of Informatics and Telecommunications, National and Kapodistrian University of Athens；Eulambia Advanced Technologies Ltd | 参数化量子电路作为特征映射，评估多光谱土地覆盖分类中的表示质量与读出效应影响。 | [#437](https://github.com/thinson/RS-PaperClaw/issues/437) |
| [20260429] AirZoo: A Unified Large-Scale Dataset for Grounding Aerial Geometric 3D Vision | Cheng Xiaoya, Wu Rouwan, Liu Xinyi, Cui Zeyu, Liu Yan, Zhao Na, Liu Yu, Zhang Maojun, Yan Shen | National University of Defense Technology；Singapore University of Technology and Design | AirZoo统一大规模合成数据集，为航空几何三维视觉任务提供摄影测量级网格真值。 | [#438](https://github.com/thinson/RS-PaperClaw/issues/438) |
| [20260429] 3D-LENS: A 3D Lifting-based Elevated Novel-view Synthesis method for Single-View Aerial-Ground Re-Identification | Grolleau William, Sabourin Astrid, Lapouge Guillaume, Achard Catherine | Université Paris-Saclay, CEA, List；Sorbonne University, CNRS, Institute of Intelligent Systems and Robotics (ISIR) | 3D-LENS基于单视图三维提升，实现空中-地面跨视角重识别的新视角合成。 | [#439](https://github.com/thinson/RS-PaperClaw/issues/439) |
| [20260429] Cross-Domain Transfer of Hyperspectral Foundation Models | Theisen Nick, Neubert Peer | Intelligent Autonomous Systems, University of Koblenz | 高光谱基础模型跨域迁移研究，探索预训练表征在不同地理场景间的可迁移性。 | [#440](https://github.com/thinson/RS-PaperClaw/issues/440) |
| [20260429] Topology-Aware Representation Alignment for Semi-Supervised Vision-Language Learning | You Junwon, Jang Mihyun, Mo Sangwoo, Jung Jae-Hun | KAIST；POSTECH | 拓扑感知表征对齐方法，利用持续同调优化半监督视觉-语言学习的多模态表征。 | [#441](https://github.com/thinson/RS-PaperClaw/issues/441) |
| [20260429] Point Cloud Registration via Probabilistic Self-Update Local Correspondence and Line Vector Sets | Chung Kuo-Liang, Lin Yu-Cheng, Chen Wu-Chi | Department of Computer Science and Information Engineering, National Taiwan University of Science and Technology | 概率自更新局部对应与线向量集方法，提升点云配准的鲁棒性与精度。 | [#442](https://github.com/thinson/RS-PaperClaw/issues/442) |
| [20260429] High-Dimensional Noise to Low-Dimensional Manifolds: A Manifold-Space Diffusion Framework for Degraded Hyperspectral Image Classification | Yang Boxiang, Chen Ning, Yue Xia, Luo Yichang, Fan Yingbo, Zhang Haoyuan, Ma Haoyu, Yue Jun, Mao Shanjun | School of Computer Science and Engineering, Central；the Aerospace Information Research a higher-dimensional observation space, thereby introducing；the Institute of energy, Peking University, Beijing, China mation；the School of Mechanics and Engineering Science, observations away from a compact spectral manifold into a；the School of Automation, Central South University, more dispersed high-dimensional space. In such cases, directly；the data, but more fundamentally from the strong sensitivity the Institute of Remote Sensing；Geographic Information System, of its intrinsic structure to external perturbations | 流形空间扩散框架将高维噪声映射至低维流形，解决退化高光谱图像分类问题。 | [#443](https://github.com/thinson/RS-PaperClaw/issues/443) |
| [20260429] Seeking Consensus: Geometric-Semantic On-the-Fly Recalibration for Open-Vocabulary Remote Sensing Semantic Segmentation | Wang Guanchun, Wu Chenxiao, Zhang Xiangrong, Peng Zelin, Lai Jianxun, Zhang Tianyang, Tang Xu | School of Artificial Intelligence, Xidian University；MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University | 几何-语义动态重校准方法，通过双重共识机制提升开放词汇遥感语义分割性能。 | [#444](https://github.com/thinson/RS-PaperClaw/issues/444) |

## 🔎 观察

- 开放词汇学习成为遥感语义分割热点方向，但几何一致性与语义一致性的联合优化仍具挑战。
- 量子机器学习在遥感领域的应用尚处探索期，其表示优势需更多实际任务验证。

---

Powered by OpenClaw🦞

---
