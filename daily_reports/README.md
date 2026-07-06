# Daily Reports

最近三天日报（最新在前）：

# [20260703](./202607/20260703.md)
## 📌 今日概况

今日共检索候选论文 0 篇；关键词+LLM 智能匹配遥感交叉论文 0 篇；最终纳入日报 0 篇。

当日未检索到符合条件并纳入日报的论文。

## 🔎 观察

- 当日无成功纳入论文，建议优先检查候选筛选结果与失败原因。
- 若连续出现空日报，应复核 arXiv 日期窗口、关键词配置与 LLM 筛选输出。

---

Powered by OpenClaw🦞

---

# [20260702](./202607/20260702.md)
## 📌 今日概况

今日共检索候选论文 8 篇；关键词+LLM 智能匹配遥感交叉论文 5 篇；最终纳入日报 5 篇。

今日遥感研究聚焦于智能解译与数据发现两大方向。云去除结合残差流与地理上下文对齐提升可解释性；多篇工作探索大语言模型与知识图谱在遥感数据检索、假设生成及无人机自主决策中的应用；持续学习框架被引入变化检测以应对域偏移问题。

## ✨ 今日亮点

- 云去除方法引入残差流与地理上下文对齐提升可解释性
- 多篇工作探索LLM与知识图谱驱动遥感数据智能发现
- 持续学习框架被用于域增量变化检测任务

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260702] Interpretation-Oriented Cloud Removal via Observation-Anchored Residual Flow with Geo-Contextual Alignment | Wang Ziyao, Wang Maonan, He Yucheng, Ma Xianping, Wang Ziyi, Zhang Hongyang, Cheng Yirong, Pun Man-on | School of Science and Engineering, The Chinese University of Hong Kong；Shanghai Ai Lab, Shanghai, China；Faculty of Geosciences and Engineering, Southwest Jiaotong University, Chengdu | 提出面向可解释的云去除方法，利用观测锚定残差流与地理上下文对齐。 | [#832](https://github.com/thinson/RS-PaperClaw/issues/832) |
| [20260702] Bringing Agentic Search to Earth Observation Data Discovery | Yu Minghan, Sun Youran, Yi Chugang, Wen Yixin, Yang Haizhao | University of Maryland, College Park University of Maryland, College Park；University of Maryland, College Park University of Florida；University of Maryland, College Park；NASA and its data centers hold thousands of geoscience datasets and tools like；metadata, tools, and access pathways. NASA and its affiliated data centers host thousands of datasets；across dozens of Distributed Active Archive Centers (DAACs), together with tools such as Worldview；domain experts to locate the data that best matches their own research question | 将智能体搜索引入地球观测数据发现，提升数据集检索效率。 | [#833](https://github.com/thinson/RS-PaperClaw/issues/833) |
| [20260702] Dual-Selective Network for Domain-Incremental Change Detection | He Yuzhi, Huang Junxi, Wu Haorui, Qu Jiahui | Xidian University, Xi'an, China | 提出双选择性网络用于域增量变化检测，结合视觉状态空间模型。 | [#834](https://github.com/thinson/RS-PaperClaw/issues/834) |
| [20260702] NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy | Qian Weixian, Yang Tianyi, Schroder Sebastian, Deng Yao, Yao Jiaohong, Cheng Xiao, Han Richard, Zheng Xi | School of Computing, Macquarie University, Sydney, NSW, Australia；Macquarie University, when this work was conducted；Department of Computer Science, University of California, Santa Barbara, CA, USA. tianyi | 神经符号方法实现无人机着陆点评估，支持边缘部署与鲁棒自主。 | [#835](https://github.com/thinson/RS-PaperClaw/issues/835) |
| [20260702] EO-Agents: A Three-Agent LLM Pipeline for Earth Observation Hypothesis Generation | Ghazanfari Mahyar, Tabrizian Amin, Mehrabian Armin, Wei Peng | Earth-observation (EO) research is fundamentally combina-；Washington University, Washington, DC, USA；Space Flight Center, Greenbelt, MD, USA | 构建三智能体LLM流水线，自动生成地球观测科学假设。 | [#836](https://github.com/thinson/RS-PaperClaw/issues/836) |

## 🔎 观察

- 大语言模型正从辅助工具演变为遥感数据发现与假设生成的核心引擎。
- 持续学习与域适应成为变化检测研究新热点，应对多源数据分布漂移。

---

Powered by OpenClaw🦞

---

# [20260701](./202607/20260701.md)
## 📌 今日概况

今日共检索候选论文 17 篇；关键词+LLM 智能匹配遥感交叉论文 6 篇；最终纳入日报 6 篇。

今日遥感研究呈现多模态融合与精细化建模两大趋势。视觉定位任务引入过程监督与锚点引导推理，提升复杂场景理解能力。无人机图像分析聚焦质量评估与高效检测微调，结合视觉-语言模型。三维重建方面，轨道射线条件约束的3D基础模型提升了卫星多视角重建精度。此外，不确定性感知的树高变化回归与极化SAR土壤水分反演，体现了对物理过程与量测不确定性的深入建模。

## ✨ 今日亮点

- 多模态大模型在遥感视觉定位中引入过程监督机制
- 无人机图像分析结合视觉-语言模型实现质量评估与高效检测
- 卫星三维重建与森林动态监测强调物理约束与不确定性建模

## 🗂 今日文章列表

| 标题 | 作者 | 单位 | 一句话概括 | Issue |
|---|---|---|---|---|
| [20260701] GeoSearcher: Anchor-Guided Progressive Reasoning for Remote Sensing Visual Grounding with Process Supervision | Wang Dianyu, Zhang Yidan, Zhang Peirong, Li Xuyang, Liu Xiaoxuan, Wang Lei | School of Electronic, Electrical and Communication Engineering, University of Chinese Academy of Sciences, Beijing, China ( | GeoSearcher提出锚点引导渐进推理，实现遥感视觉定位的过程监督。 | [#825](https://github.com/thinson/RS-PaperClaw/issues/825) |
| [20260701] Uncertainty-aware tree height change regression | Gaber Max, Gominski Dimitri, Jaime C. Revenga, Oehmcke Stefan, Fensholt Rasmus, Brandt Martin | Department of Mathematical Sciences, University of Copenhagen；Department of Computer Science and Electrical Engineering, University of Rostock；Department of Computer Science, University of Copenhagen | 不确定性感知回归模型用于树高变化估计，提升森林动态监测可靠性。 | [#826](https://github.com/thinson/RS-PaperClaw/issues/826) |
| [20260701] EO-VGGT: Orbital Ray-Conditioned 3D Foundation Models for Satellite Multi-View Reconstruction | Luo Qiyan, Pi Yingdong, Wen Lekang, Yang Jie, Wang Xiaoyu, Zhang Haiming, Wang Mi | State Key Laboratory of Information Engineering in Surveying, Mapping and Remote Sensing, Wuhan University；Hubei Luojia Laboratory | EO-VGGT利用轨道射线条件约束，构建卫星多视角重建3D基础模型。 | [#827](https://github.com/thinson/RS-PaperClaw/issues/827) |
| [20260701] DroneIQA-VLE: Multi-Task Drone Image Quality Assessment via Vision-Language Ensemble | Sun Wei, Zhang Weixia, Zhan Hongjian, Lu Mingkai, Gao Yixuan, Zhai Guangtao | East China Normal University；Shanghai Jiao Tong University；To promote research on UAV-oriented quality modeling | DroneIQA-VLE通过视觉-语言集成实现无人机图像多任务质量评估。 | [#828](https://github.com/thinson/RS-PaperClaw/issues/828) |
| [20260701] DroneFINE: Domain-Aware Parameter-Efficient Fine-Tuning of Vision-Language Detectors for Drone Images | Wu Ke, Zhang Yanan, Gao Yingjie, Li Wenhao, Zhou Chenyu, Ma XinZhu, Chen Jiaxin, Huang Di | National College for Excellent Engineers, Beihang University, Beijing, China；School of Computer Science and Engineering, Beihang University, Beijing, China；School of Computer Science and Information Engineering, Hefei University of；State Key Laboratory of Virtual Reality Technology and Systems, Beihang；University, Beijing, China；Innovation Center for Intelligent System Cognition and Decision-Making, Beijing；Information Science Academy of China Electronics Technology Group Corporation | DroneFINE提出域感知参数高效微调，适配无人机图像的视觉语言检测。 | [#829](https://github.com/thinson/RS-PaperClaw/issues/829) |
| [20260701] Polarimetric SAR Model Fitting for Soil Moisture Retrieval: Study of PALSAR-2 data over a Heterogeneous Mine Environment in Finland | Antropov Oleg, Hamedianfar Alireza, Molinier Matthieu, Salmela Ulla, Kukkula Hanna, Seitsonen Lauri, Liwata-Kenttälä Pauliina, Middleton Maarit | VTT Technical Research Centre of Finland, Espoo, Finland | 极化SAR半经验模型用于芬兰矿区土壤水分反演，分析PALSAR-2时序数据。 | [#830](https://github.com/thinson/RS-PaperClaw/issues/830) |

## 🔎 观察

- 视觉-语言模型正从通用场景向遥感垂直领域渗透，驱动定位、检测与质量评估任务革新。
- 遥感基础模型发展更注重物理先验（如轨道几何、极化散射）与不确定性量化，提升可解释性。

---

Powered by OpenClaw🦞

---
