---
$id: ent_component_zed_stereo_camera_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: ZED Stereo Camera
  zh: ZED 立体相机
  ko: ZED 스테레오 칩차
summary:
  en: Stereo vision camera with onboard depth estimation and spatial AI used in robot navigation.
  zh: '核心内容 ### ZED 立体相机的定义与定位 ZED 立体相机属于 **component** 类型。 所属领域包括：02_components, 06_design_engineering。 价值链层级：midstream,
    upstream。 具有 onboard 深度估计和空间AI的立体视觉相机，用于机器人导航。 英文名称为 *ZED Stereo Camera*。 韩文名称为 *ZED 스테레오 칩차*。'
  ko: 온보드 깊이 추정 및 공간 AI를 갖춘 스테레오 비전 칩차, 로봇 납치에 사용.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- camera
- component
- sensor
- stereo
- zed
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-02'
  confidence: medium
  notes: Imported via ingestion framework from source_type=website. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: ZED Stereo Camera
  url: https://www.stereolabs.com/zed/
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
具有 onboard 深度估计和空间AI的立体视觉相机，用于机器人导航。

## 核心内容
### ZED 立体相机的定义与定位
ZED 立体相机属于 **component** 类型。 所属领域包括：02_components, 06_design_engineering。 价值链层级：midstream, upstream。 具有 onboard 深度估计和空间AI的立体视觉相机，用于机器人导航。 英文名称为 *ZED Stereo Camera*。 韩文名称为 *ZED 스테레오 칩차*。

### ZED 立体相机的工作原理与技术架构
ZED 立体相机的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用ZED 立体相机需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
ZED 立体相机已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- camera
- component
- sensor
- stereo
- zed

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键component之一，ZED 立体相机在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [ZED Stereo Camera](https://www.stereolabs.com/zed/)


