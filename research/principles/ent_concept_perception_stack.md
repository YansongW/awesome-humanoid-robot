---
$id: ent_concept_perception_stack
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Perception Stack
  zh: 感知栈
  ko: 인식 스택
summary:
  en: The software subsystem that processes sensor data to estimate states, detect objects, and build environmental representations
    for decision-making.
  zh: 处理传感器数据以估计状态、检测物体并构建环境表示，为决策提供输入的软件子系统。
  ko: 센서 데이터를 처리하여 상태를 추정·물체를 검출·환경 표현을 구축하고 의사결정에 입력을 제공하는 소프트웨어 하위 시스템.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- concept
- chapter_24
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-05.md#5.1.3 人形机器人感知系统的整体架构 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
感知栈是人形机器人领域的重要concept。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
一个典型的人形机器人感知系统可以分为四层：

1. **传感层（sensor layer）**：物理换能器与前端模拟电路，输出原始电信号。
2. **数据采集层（data acquisition layer）**：对模拟信号进行滤波、采样、量化和时间戳对齐。
3. **状态与感知层（state & perception layer）**：运行 SLAM、视觉里程计、力/位估计、物体检测、语义分割等算法。
4. **决策与控制层（decision & control layer）**：把感知结果用于步态规划、操作规划、人机交互与安全保障。

```mermaid
flowchart TD
    subgraph 传感层
    A1["相机 / LiDAR / 雷达 / 超声"]
    A2["编码器 / 力矩传感器 / F/T"]
    A3["IMU / 触觉 / 麦克风"]
    end
    subgraph 数据采集层
    B1["模拟前端 / ADC"]
    B2["时间同步 / 触发"]
    B3["预处理 / 去噪"]
    end
    subgraph 状态与感知层
    C1["状态估计 EKF / VIO"]
    C2["SLAM / 地图"]
    C3["检测 / 分割 / 跟踪"]
    end
    subgraph 决策与控制层
    D1["运动规划"]
    D2["力/位控制"]
    D3["安全监控"]
    end
    A1 --> B1
    A2 --> B1
    A3 --> B1
    B1 --> B2 --> B3 --> C1
    B3 --> C2
    B3 --> C3
    C1 --> D1
    C2 --> D1
    C3 --> D2
    C1 --> D2
    D1 --> D3
    D2 --> D3
```

---

## 参考
- Wiki extraction
- 项目 Wiki：chapter-05.md#5.1.3 人形机器人感知系统的整体架构

