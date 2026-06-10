# Daily Reports

最近三天日报（最新在前）：

# [20260609](./202606/20260609.md)
## 📌 今日概况

今日共检索候选论文 13 篇；关键词+LLM 智能匹配遥感交叉论文 9 篇；最终纳入日报 8 篇。

今日遥感研究呈现多模态大模型与无监督学习两大热点。Earth-OneVision将多模态大模型扩展至更多传感器模态与任务；多篇工作聚焦建筑物变化检测，分别采用无监督自训练、地震场景专用网络及内容诱导的空谱聚合方法。此外，零样本检测分割、矢量地图统一表示、视觉语言模型用于海岸线定位、以及物理嵌入的频谱重建等方向亦有新进展。

## ✨ 今日亮点

- 多模态大模型向更多遥感传感器模态扩展
- 无监督自训练方法提升建筑物变化检测性能
- 物理知识嵌入Transformer改善光谱重建

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260609] Earth-OneVision: Extending Remote Sensing Multimodal Large Language Models to More Sensor Modalities and Tasks | Cai Miaoxin, Wang Guanqun, Zhang Wei, Zhou Guangyao, Zhuang Yin, Zhang Tong, Wang Hao, Chen He, Li Jun | the National Key Laboratory of Science and Technology on Space-Born Intelligent Information Processing；the Aerospace Information Research Institute, Chinese Academy of Sciences, Beijing , China；the Key Laboratory of Technology in Geo-Spatial Information Processing and Application System, Chinese Academy of Sciences, Beijing , China；the Advanced Research Institute of Multidisciplinary Sciences, Beijing Institute of Technology, Beijing , China；the School of Mechatronical Engineering, Beijing Institute of Technology, Beijing , China；the School of Earth and Space Sciences, Peking University, Beijing , China；the School of Electronics, Peking University, Beijing , China；the School of Computer Science and Hubei Key Laboratory of Intelligent Geo-Information Processing, China University of Geosciences, Wuhan, , China | Earth-OneVision将多模态大语言模型扩展至更多遥感传感器模态与任务。 | [#699](https://github.com/thinson/RS-PaperClaw/issues/699) |
| [20260609] Spatially Selective Self-Training for Unsupervised Building Change Detection | Wafaa I. M. Hussin, Lu Zhi, Anas M. I. Mohammed, Zhou Xiang, Ratiba A. H. Abubaker, Peng Zhenming | the School of Information and Communication Engineering, University of Electronic Science and Technology of China, Chengdu , China；the Laboratory of Intelligent Collaborative Computing, University of Electronic Science and Technology of China, Chengdu , China；the School of Civil Engineering, University of Khartoum, Khartoum, Sudan；the National Energy Research Center, Ministry of Higher Education and Scientific Research, Khartoum, Sudan | 提出空间选择性自训练方法，实现无监督建筑物变化检测。 | [#700](https://github.com/thinson/RS-PaperClaw/issues/700) |
| [20260609] ZODS-RS -- Zero-training Oriented Detection & Segmentation for Remote Sensing | Gu Zuan, Gao Tianhan, Zhao Langxu | Northeastern University, China | ZODS-RS实现零训练条件下的遥感目标检测与实例分割。 | [#701](https://github.com/thinson/RS-PaperClaw/issues/701) |
| [20260609] Vector Map as Language: Toward Unified Remote Sensing Vector Mapping | Yan Yinglong, Yang Yunkai, Wang Haoyi, Fu Wei, Wu Linshan, Pan Honghu, Xia Shaobo, Zhang Shanghang, Chen Hao, Fang Leyuan | Fang are with the school of Artificial Intelligence and Robotics, Hunan {；University, Changsha 410082, China；• Linshan Wu and Hao Chen are with the Department of Computer Science；and Engineering, The Hong Kong University of Science and Technol-；• Shaobo Xia is in the Department of Geomatics Engineering, Changsha；University of Science and Technology, Changsha 410114, China；• Shanghang Zhang is in State Key Laboratory of Multimedia Information；Processing, School of Computer Science, Peking University | 将矢量地图视为语言，提出统一的遥感矢量映射范式。 | [#702](https://github.com/thinson/RS-PaperClaw/issues/702) |
| [20260609] Geometric Coastline Localization using Vision-Language Models | Malik Rafia, Pfahringer Bernhard, Bryan Karin, Dickson Mark, Frank Eibe | a The University of Waikato, New Zealand；b The University of Auckland, New Zealand | 利用视觉语言模型进行几何海岸线定位与变化分析。 | [#703](https://github.com/thinson/RS-PaperClaw/issues/703) |
| [20260609] PF-Trans: Physics-Embedded Frequency-Aware Transformer for Spectral Reconstruction | Gui Yuzhe, Liu Tianzhu, Gu Yanfeng, Li Xian | Harbin Institute of Technology Harbin Institute of Technology Harbin Institute of Technology Harbin Institute of Technology | PF-Trans通过物理嵌入的频率感知Transformer实现光谱重建。 | [#704](https://github.com/thinson/RS-PaperClaw/issues/704) |
| [20260609] Building Change Detection in Earthquake: A Multi-Scale Interaction Network and A Change Detection Dataset | Liu Yunlong, Zhang Zekai | Science and Engineering, Shandong University, Ji’nan 250061, China ( | 提出多尺度交互网络及专用数据集用于地震建筑物变化检测。 | [#705](https://github.com/thinson/RS-PaperClaw/issues/705) |
| [20260609] Content-Induced Spatial-Spectral Aggregation Network for Change Detection in Remote Sensing Images | Liu Yunlong, Zhang Zekai | Science and Engineering, Shandong University, Ji’nan 250061, China ( | 内容诱导的空谱聚合网络结合图卷积提升变化检测性能。 | [#706](https://github.com/thinson/RS-PaperClaw/issues/706) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Multi-Angular Reflectance Anisotropy Observed from UAV Multispectral Imagery | [2606.10350v1](https://arxiv.org/abs/2606.10350v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 多模态大模型正从通用视觉向遥感专用传感器模态深化，跨传感器融合成为趋势。
- 无监督与零样本方法在变化检测和目标分割中应用增多，降低标注依赖是当前重要方向。

---

Powered by OpenClaw🦞

---

# [20260608](./202606/20260608.md)
## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 10 篇；最终纳入日报 8 篇。

今日遥感AI研究聚焦于无人机平台的多模态融合与目标检测，同时涉及变化检测、数据管理及建筑物提取。DINOv3驱动的语义对齐、信息瓶颈融合去云、零参数几何门控等新方法涌现，体现了对高精度、高效率及跨时相一致性的追求。

## ✨ 今日亮点

- 无人机多模态融合与目标检测成为今日研究热点
- 语义变化检测引入DINOv3实现跨时相对齐
- 零参数几何门控提升无人机视频分割时域稳定性

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260608] SemDINO: A DINOv3-Driven Network for Cross-Temporal Semantic Alignment in Change Detection | Tong Xinyu, Zhou Meihua, Sun Jinxiao, Tang Yingjie, Wang Lei | the Xinjiang Institute of Ecology and Geography, Chinese Academy of Sciences, Urumqi , China；the University of Chinese Academy of Sciences, Beijing , China；the School of Computer Science, Xiangtan University, Xiangtan , China；the College of Information and Communication Engineering, Harbin Engineering University, Harbin , China | SemDINO利用DINOv3实现跨时相语义对齐的变化检测网络 | [#690](https://github.com/thinson/RS-PaperClaw/issues/690) |
| [20260608] AeroMesa: Efficient Data Management System for Multi-Dimensional Spatio-Temporal Trajectories | Zhang Yue, Ding Zizhong, Sun Lin, Chen Haopeng, Jiao Yan, Xu Yongming | Shanghai Jiao Tong University, Shanghai, China | AeroMesa提出高效管理多维时空轨迹的数据系统 | [#691](https://github.com/thinson/RS-PaperClaw/issues/691) |
| [20260608] IB-HFN: Information Bottleneck-Driven SAR-Optical Fusion Network for High-Fidelity Cloud Removal | Guo Haojun, Feng Fan, Wang Ziquan | Geospatial Information Institute, Information Engineering University, Zhengzhou, China | IB-HFN基于信息瓶颈融合SAR与光学图像实现高保真去云 | [#692](https://github.com/thinson/RS-PaperClaw/issues/692) |
| [20260608] Zero-Parameter Geometric Gating for Temporally Stable Low-Altitude UAV Video Semantic Segmentation | Yang Jingpu, Ji Fengxian, Lai Zhengzhao, Wu Juanfan, Cui Mingxuan, Wang Yufeng | Beihang University Northeastern University The Chinese University of Hong；Beijing Institute of Technology Northeastern University Beihang University | 零参数几何门控方法提升低空无人机视频语义分割时域一致性 | [#693](https://github.com/thinson/RS-PaperClaw/issues/693) |
| [20260608] CAMF-Det: Closure-Aware Multimodal Fusion for LiDAR-Camera 3D Object Detection on UAV Platforms | Jiang Yanze, Gu Yanfeng, Li Xian | a School of Electronics and Information Engineering, Harbin Institute of Technology, Harbin 150001, China | CAMF-Det实现无人机平台LiDAR-相机融合的3D目标检测 | [#694](https://github.com/thinson/RS-PaperClaw/issues/694) |
| [20260608] Illumination-Invariant Anomaly Detection for Sub-Canopy UAV Multispectral Point Clouds | Chen Likun, Gu Yanfeng, Li Xian | School of Electronics and Information School of Electronics and Information School of Electronics and Information；Harbin Institute of Technology Harbin Institute of Technology Harbin Institute of Technology | 光照不变异常检测方法用于林下无人机多光谱点云 | [#695](https://github.com/thinson/RS-PaperClaw/issues/695) |
| [20260608] Edge-Constrained UAV Small-Object Detection with P2 Enhancement and Quantum-Inspired Lightweight Structure Search | Lei Wuming, Gao Yanbin, Sun Mingyan, Li Xiaobin, Liang Xuechen | East China Jiaotong University, Nanchang, China | 边缘约束与量子启发搜索提升无人机小目标检测性能 | [#696](https://github.com/thinson/RS-PaperClaw/issues/696) |
| [20260608] PolyBuild: An End-to-End Method for Polygonal Building Contour Extraction from High-Resolution Remote Sensing Images | Zhang Yaoteng, Zhang Julin, Wang Guangshuai, Deng Jiwei, Sheng Hui, Muhammad Yasir, Wei Shiqing | the College of Oceanography and Space Informatics, China University of Petroleum | PolyBuild端到端方法从高分辨率遥感图像提取多边形建筑轮廓 | [#697](https://github.com/thinson/RS-PaperClaw/issues/697) |

## ⚠️ 未纳入日报的匹配论文

以下论文通过关键词/LLM 筛选，但在处理过程中失败未纳入日报。点击 arXiv 链接可查看原文。

| 标题 | arXiv | 失败原因 |
|------|-------|----------|
| Vision-Language Guided Hyperspectral Object Tracking via Semantics Fusion and Contextual Template Updating | [2606.09167v1](https://arxiv.org/abs/2606.09167v1) | 质检未通过: 单位为空或无效 |
| An Enhanced Geometric-Spectral Feature Learning Framework for Airborne Multispectral Point Cloud Classification | [2606.09123v1](https://arxiv.org/abs/2606.09123v1) | 质检未通过: 单位为空或无效 |


## 🔎 观察

- 无人机平台研究占比过半，多模态融合与轻量化设计成主流趋势
- 语义变化检测与建筑物提取方法向端到端、高保真方向演进

---

Powered by OpenClaw🦞

---

# [20260607](./202606/20260607.md)
## 📌 今日概况

今日共检索候选论文 4 篇；关键词+LLM 智能匹配遥感交叉论文 1 篇；最终纳入日报 1 篇。

今日遥感AI研究聚焦于超分辨率任务，提出一种结合N-Gram上下文与混合专家模型的高效方法。该方法通过轻量级Transformer架构，在保持较低计算成本的同时提升遥感图像重建质量，体现了当前遥感领域对高效、高精度模型设计的持续关注。

## ✨ 今日亮点

- 提出N-Gram上下文与混合专家模型结合的遥感超分辨率方法
- 在保持低计算成本下提升遥感图像重建质量
- 轻量级Transformer架构应用于遥感超分辨率任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260607] NGram-MoSE: Efficient Remote Sensing Super-Resolution via N-Gram Context and Mixture-of-Experts | Huang Yun-Hsuan, Bui Trong-An, Chuang Chih-Hung | Institute of Aerospace and Systems Engineering, National Taipei University of Technology, Taipei City, Taiwan | 提出NGram-MoSE方法，结合N-Gram上下文与混合专家模型实现高效遥感超分辨率。 | [#688](https://github.com/thinson/RS-PaperClaw/issues/688) |

## 🔎 观察

- 遥感超分辨率研究正从单纯追求精度转向效率与性能的平衡
- 混合专家模型在遥感任务中的应用显示出提升模型适应性的潜力

---

Powered by OpenClaw🦞

---
