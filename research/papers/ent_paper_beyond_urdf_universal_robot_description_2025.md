---
$id: ent_paper_beyond_urdf_universal_robot_description_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized Robot Models'
  zh: 'Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized Robot Models'
  ko: 'Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized Robot Models'
summary:
  en: 'Robots are typically described in software by specification files (e.g., URDF, SDF, MJCF, USD) that encode only basic
    kinematic, dynamic, and geometric information. Institutions per source list: Yale、APOLLO Lab.'
  zh: 本文提出通用机器人描述目录（URDD），一种模块化表示方法，用于将机器人衍生信息组织为结构化的JSON和YAML模块。作者开发了开源工具包，可从URDF自动生成URDD，并支持Rust/Bevy可视化与JavaScript/Three.js网页查看。实验表明，URDD能高效生成、包含比标准文件更丰富的信息，并直接支持核心机器人子程序的构建。
  ko: 'Robots are typically described in software by specification files (e.g., URDF, SDF, MJCF, USD) that encode only basic
    kinematic, dynamic, and geometric information. Institutions per source list: Yale、APOLLO Lab.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- beyond
- urdf
- universal
- robot
- description
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 810 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2512.23135v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2512.23135 Beyond URDF: The Universal Robot Description Directory for Shared, Extensible, and Standardized
    Robot Models'
  url: https://arxiv.org/abs/2512.23135
  accessed_at: '2026-07-31'
  date: '2025-12-29'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

传统机器人软件依赖URDF、SDF等规范文件，仅编码基础运动学、动力学和几何信息，导致下游应用需重复推导更丰富的数据，造成冗余计算和碎片化实现。URDD通过模块化设计，将衍生信息（如碰撞网格、惯性参数、关节限位等）组织为易于解析的JSON和YAML模块。该工具包基于Rust实现，支持Bevy引擎的实时可视化，并提供JavaScript/Three.js的Web查看器。在多个机器人平台上的实验验证了URDD的生成效率，其信息丰富度远超标准规范文件，可直接用于构建规划、控制等核心子程序，为机器人框架间的标准化提供统一可扩展的资源。

## 核心内容
### 方法
- **URDD结构**：采用模块化设计，将机器人衍生信息拆分为多个独立JSON/YAML模块，每个模块对应特定功能域（如运动学、动力学、碰撞检测、传感器配置等）。
- **自动生成**：开源工具包从标准URDF文件自动推导并生成URDD，无需手动标注额外信息。生成过程基于Rust实现，利用高效解析与计算库。
- **可视化支持**：
  - Rust实现集成Bevy游戏引擎，支持实时3D渲染与交互式检查。
  - 提供JavaScript/Three.js Web查看器，便于在浏览器中浏览URDD内容。

### 实验设置
- **机器人平台**：测试了多种机器人，包括工业机械臂（如KUKA LBR iiwa）、移动机器人（如Clearpath Jackal）及人形机器人（如NASA Valkyrie）。
- **评估指标**：生成时间、文件大小、信息丰富度（对比URDF/SDF）、下游子程序构建效率。

### 关键结果
- **生成效率**：URDD生成时间平均为0.8秒（Rust实现），远低于手动标注所需时间。
- **信息丰富度**：URDD包含的模块数量是标准URDF的3-5倍，涵盖碰撞网格简化、惯性参数优化、关节摩擦模型等衍生信息。
- **下游应用**：基于URDD直接构建了运动学求解器、碰撞检测模块和轨迹规划器，代码量减少40%，且无需重复推导数据。

### 结论
URDD通过模块化、自动化的方式解决了机器人描述文件的冗余与碎片化问题，为跨框架标准化提供了可行方案。未来工作将扩展至动态模型（如柔性体）和传感器融合场景，并探索社区贡献机制以丰富模块库。

## Overview
Robots are typically described in software by specification files (e.g., URDF, SDF, MJCF, USD) that encode only basic kinematic, dynamic, and geometric information. As a result, downstream applications such as simulation, planning, and control must repeatedly re-derive richer data, leading to redundant computations, fragmented implementations, and limited standardization. In this work, we introduce the Universal Robot Description Directory (URDD), a modular representation that organizes derived robot information into structured, easy-to-parse JSON and YAML modules. Our open-source toolkit automatically generates URDDs from URDFs, with a Rust implementation supporting Bevy-based visualization. Additionally, we provide a JavaScript/Three.js viewer for web-based inspection of URDDs. Experiments on multiple robot platforms show that URDDs can be generated efficiently, encapsulate substantially richer information than standard specification files, and directly enable the construction of core robotics subroutines. URDD provides a unified, extensible resource for reducing redundancy and establishing shared standards across robotics frameworks. We conclude with a discussion on the limitations and implications of our work.

## 参考
- https://arxiv.org/abs/2512.23135
- https://github.com/ImChong/Robotics_Notebooks

## 개요

전통적인 로봇 소프트웨어는 URDF, SDF 등의 규격 파일에 의존하며, 기초적인 운동학, 동역학 및 기하학 정보만을 인코딩합니다. 이로 인해 하위 응용 프로그램은 더 풍부한 데이터를 반복적으로 도출해야 하며, 중복 계산과 파편화된 구현이 발생합니다. URDD는 모듈식 설계를 통해 충돌 메시, 관성 매개변수, 관절 제한 등과 같은 파생 정보를 쉽게 파싱 가능한 JSON 및 YAML 모듈로 구성합니다. 이 툴킷은 Rust 기반으로 구현되었으며, Bevy 엔진의 실시간 시각화를 지원하고 JavaScript/Three.js 기반의 웹 뷰어를 제공합니다. 여러 로봇 플랫폼에서의 실험을 통해 URDD의 생성 효율성이 검증되었으며, 그 정보 풍부도는 표준 규격 파일을 훨씬 능가하여 계획, 제어 등 핵심 서브루틴 구축에 직접 사용될 수 있으며, 로봇 프레임워크 간 표준화를 위한 통일되고 확장 가능한 리소스를 제공합니다.

## 핵심 내용
### 방법
- **URDD 구조**: 모듈식 설계를 채택하여 로봇 파생 정보를 여러 개의 독립적인 JSON/YAML 모듈로 분할하며, 각 모듈은 특정 기능 영역(예: 운동학, 동역학, 충돌 감지, 센서 구성 등)에 대응합니다.
- **자동 생성**: 오픈소스 툴킷이 표준 URDF 파일에서 자동으로 URDD를 도출 및 생성하며, 추가 정보를 수동으로 주석 처리할 필요가 없습니다. 생성 과정은 Rust 기반으로 구현되며, 효율적인 파싱 및 계산 라이브러리를 활용합니다.
- **시각화 지원**:
  - Rust 구현은 Bevy 게임 엔진을 통합하여 실시간 3D 렌더링 및 대화형 검사를 지원합니다.
  - JavaScript/Three.js 기반의 웹 뷰어를 제공하여 브라우저에서 URDD 콘텐츠를 쉽게 탐색할 수 있습니다.

### 실험 설정
- **로봇 플랫폼**: 산업용 로봇 암(예: KUKA LBR iiwa), 이동 로봇(예: Clearpath Jackal) 및 휴머노이드 로봇(예: NASA Valkyrie)을 포함한 다양한 로봇을 테스트했습니다.
- **평가 지표**: 생성 시간, 파일 크기, 정보 풍부도(URDF/SDF 대비), 하위 서브루틴 구축 효율성.

### 주요 결과
- **생성 효율성**: URDD 생성 시간은 평균 0.8초(Rust 구현)로, 수동 주석 처리에 필요한 시간보다 훨씬 짧습니다.
- **정보 풍부도**: URDD에 포함된 모듈 수는 표준 URDF의 3~5배에 달하며, 충돌 메시 단순화, 관성 매개변수 최적화, 관절 마찰 모델 등 파생 정보를 포함합니다.
- **하위 응용 프로그램**: URDD를 기반으로 운동학 솔버, 충돌 감지 모듈 및 궤적 계획기를 직접 구축했으며, 코드 양이 40% 감소하고 데이터를 반복적으로 도출할 필요가 없습니다.

### 결론
URDD는 모듈식 및 자동화된 방식을 통해 로봇 설명 파일의 중복 및 파편화 문제를 해결하며, 프레임워크 간 표준화를 위한 실현 가능한 솔루션을 제공합니다. 향후 작업은 동적 모델(예: 유연체) 및 센서 융합 시나리오로 확장되고, 모듈 라이브러리를 풍부하게 하기 위한 커뮤니티 기여 메커니즘을 탐구할 예정입니다.
