---
id: ent_product_rokoko_smartgloves
schema_version: 1
type: product
domain: 11_applications_markets
theoretical_depth: system
names:
  zh: Rokoko Smartgloves 动作捕捉手套
  en: Rokoko Smartgloves Motion Capture Gloves
status: active
sources:
- id: src_rokoko_smartgloves_official
  type: website
  url: https://www.rokoko.com/products/smartgloves
- id: src_rokoko_faq
  type: website
  url: https://support.rokoko.com/hc/en-us/articles/20912004920593-Rokoko-Smartgloves-FAQs
- id: src_cgchannel_launch
  type: website
  url: https://www.cgchannel.com/2020/09/rokoko-launches-smartgloves/
verification:
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-13'
---





# Rokoko Smartgloves 动作捕捉手套

## 概述

Rokoko Smartgloves 是丹麦 Rokoko 公司推出的惯性式手部动作捕捉手套，旨在以较低成本实现专业级手指与手部跟踪。每只手套嵌入 7 个六自由度（6-DoF）运动跟踪器，采用 Rokoko 专有的 IMU（惯性测量单元）与 EMF（电磁场）混合传感融合技术，无需外部摄像头即可在任意空间内完成手指姿态采集。Smartgloves 通过 WiFi 将数据实时传输至 Rokoko Studio 软件，外部流媒体帧率为 $100\,\text{fps}$，传感器内部采样率高达 $400\,\text{Hz}$，无线覆盖范围最高可达 $100\,\text{m}$。产品支持 FBX、BVH、CSV 等标准格式导出，并可实时流式传输至 Blender、Unity、Unreal Engine、Maya、MotionBuilder、iClone 等三维软件与游戏引擎。

## 工作原理 / 技术架构

Smartgloves 的跟踪系统由惯性传感器与电磁场传感器两部分组成。IMU 提供高带宽的角速度与加速度信息，用于快速捕捉手指运动；EMF 传感器则通过手套背部的小型线圈产生局部低频磁场，检测手指相对于手掌的绝对位置，从而抑制纯惯性系统长期运行时的漂移累积。两类数据在手套背部 Hub 内进行 Sensor Fusion 2.0 融合，输出手指关节角度。

设传感器输出的四元数为 $q_{\text{imu}}$，EMF 解算的位置/姿态为 $p_{\text{emf}}$，融合后的姿态 $q_{\text{out}}$ 可表示为卡尔曼滤波形式：

$$
\hat{x}_k = K_k \, z_{\text{imu}} + (I - K_k) \, z_{\text{emf}},
$$

其中 $K_k$ 为时变卡尔曼增益。该混合方案使 Smartgloves 在 $100\,\text{fps}$ 输出帧率下保持约 $\pm 1^\circ$ 的旋转动态精度，且对磁场干扰免疫（因其使用自身线圈产生的局部 EMF，而非地磁计）。

## 关键参数表

| 参数 | 规格 |
|---|---|
| 产品类型 | 惯性 + EMF 混合手部动作捕捉手套 |
| 传感器数量 | 7 个 / 手套（共 14 个） |
| 传感器类型 | IMU + EMF 混合 6-DoF 跟踪器 |
| 内部采样率 | $400\,\text{Hz}$ |
| 外部流媒体帧率 | $100\,\text{fps}$ |
| 旋转动态精度 | 约 $\pm 1^\circ$ |
| 无线连接 | WiFi（802.11ac，2.4/5 GHz） |
| 无线范围 | 最高 $100\,\text{m}$（取决于 WiFi 接入点） |
| 典型延迟 | 标准 WiFi 路由器下约 $20\,\text{ms}$ |
| 续航 | 约 $6$ 小时（使用 $5000\,\text{mAh}$ 移动电源） |
| 尺码 | S、M、L、XL |
| 导出格式 | FBX、BVH、CSV |
| 实时插件 | Unity、Unreal Engine、Blender、Maya、MotionBuilder、iClone 等 |

## 应用场景

Smartgloves 的主要应用领域包括：

- **影视与游戏动画制作**：快速捕获手指级精细动作，显著降低角色手部动画的手工制作量。
- **虚拟制作与数字人**：与 Smartsuit Pro II 动捕服、Face Capture 面部捕捉配合使用，实现全身表演捕捉。
- **虚拟现实（VR）与元宇宙**：提供无摄像头的手指跟踪，支持用户在虚拟环境中自然交互。
- **机器人遥操作（Teleoperation）**：研究者利用 Smartgloves 采集人手动作，作为人形机器人或灵巧手模仿学习的示教数据源。
- **运动分析与康复评估**：记录手部运动学数据，用于手功能评估与康复训练量化。

## 供应链关系

Rokoko 作为动作捕捉设备与软件生态的垂直整合厂商，位于“数字内容/机器人数据”供应链上游。其上游包括惯性传感器芯片、电磁线圈、纺织材料、电池与无线通信模组供应商；中游为 Rokoko 自研的硬件、Rokoko Studio 软件及插件生态；下游面向动画工作室、游戏开发商、VR/AR 内容创作者、机器人研究团队与医疗机构。在机器人产业链中，Smartgloves  increasingly 被用作人形机器人遥操作与模仿学习的数据采集前端，连接“人类动作—数字动作—机器人动作”的数据链条。

## 来源与验证

- Rokoko 官网 Smartgloves 产品页确认每只手套 7 个传感器、IMU+EMF 混合技术、$100\,\text{m}$ 范围、$100\,\text{fps}$ 流媒体、$6$ 小时续航及主要软件集成。
- Rokoko 官方 FAQ 确认传感器内部帧率 $400\,\text{Hz}$、外部帧率 $100\,\text{fps}$、旋转动态精度 $\pm 1^\circ$、WiFi 连接要求及 $20\,\text{ms}$ 典型延迟。
- CG Channel 2020 年发布报道详细描述 Smartgloves 的 $995 美元定价、7 个惯性传感器、$100\,\text{fps}$ 流媒体、$6$ 小时续航及与 Rokoko Studio 的集成。