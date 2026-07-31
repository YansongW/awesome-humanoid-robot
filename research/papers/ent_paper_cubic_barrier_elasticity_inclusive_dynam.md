---
$id: ent_paper_cubic_barrier_elasticity_inclusive_dynam
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness
  zh: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness
  ko: A Cubic Barrier with Elasticity-Inclusive Dynamic Stiffness
summary:
  en: '# ZOZO''s Contact Solver 🫶


    A contact solver for physics-based simulations

    involving 👚 shells, 🪵 solids, 🪢 rods, 🧱 rigid bodies and ⏳ sand. Institutions per source list: Ryoichi Ando 等、ZOZO、Inc.（st-tech）.'
  zh: ZOZO, Inc. 提出了一种名为“包含弹性动态刚度的立方体屏障”的接触求解器，用于物理仿真。其核心贡献在于开发了一个鲁棒、可扩展且完全在 GPU 上运行的接触与弹性求解器，能够处理超过 1.8 亿个接触点，并确保无穿透接触。该求解器采用有限元方法处理可变形体，并提供了经过校准的织物预设参数。
  ko: '# ZOZO''s Contact Solver 🫶


    A contact solver for physics-based simulations

    involving 👚 shells, 🪵 solids, 🪢 rods, 🧱 rigid bodies and ⏳ sand. Institutions per source list: Ryoichi Ando 等、ZOZO、Inc.（st-tech）.'
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
- cubic
- barrier
- elasticity
- inclusive
- dynam
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: Full ingest from Yuanxq lab paper list row 741 (.staging/ingest_yuanxq). Tier B->page. Content compiled by DeepSeek
    from the fetched project page (https://raw.githubusercontent.com/st-tech/ppf-contact-solver/HEAD/README.md). Institutions
    as given in the source list, not verified.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://github.com/st-tech/ppf-contact-solver
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: Project page (fetched)
  url: https://raw.githubusercontent.com/st-tech/ppf-contact-solver/HEAD/README.md
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该接触求解器由日本最大的时尚电商公司 ZOZO, Inc. 开发，最初作为内部物理引擎，现已开源。它支持对壳、实体、杆、刚体和沙粒等多种物理对象的仿真。求解器的主要特点包括：鲁棒的无穿透接触解析、出色的可扩展性（可处理超过 1.8 亿个接触点）、完全在 GPU 上以单精度运行的高缓存效率、以及使用有限元方法（FEM）处理可变形体并计算符号力雅可比矩阵。此外，它还提供了经过实际测量校准的织物预设参数，并支持通过 Blender 插件、JupyterLab 和 Docker 等多种方式进行使用和部署。

## 核心内容
### 方法概述

该求解器是一个基于物理的接触求解器，专门为涉及多种物理对象的仿真而设计。其核心算法确保了接触解析的鲁棒性，能够实现无穿透接触，避免出现卡顿或交叉现象。

### 核心架构与特性

- **鲁棒性**：接触解析保证无穿透，不会产生卡顿的交叉点。
- **可扩展性**：极端情况下可处理超过 1.8 亿个接触点，而不仅仅是百万级别。
- **缓存效率**：所有计算均在 GPU 上以单精度运行，无需双精度。
- **有限元方法 (FEM)**：对可变形体使用 FEM，并计算符号力雅可比矩阵。
- **参数校准**：提供了与实际测量结果匹配的织物预设参数。
- **大规模并行**：接触求解器和弹性求解器均在 GPU 上运行。
- **支持多种对象**：包括壳、实体、杆、刚体和沙粒。

### 实验设置与关键数字

- **极端规模**：能够处理超过 1.8 亿个接触点。
- **三角形变形限制**：三角形面片不会超出严格的上限（例如 1%）。
- **压力测试**：通过 GitHub Actions 连续运行 10 次压力测试。
- **Docker 镜像**：大小约为 1GB，便于快速部署。
- **许可证**：采用 Apache 2.0 许可证，允许商业和专有用途。

### 使用与部署方式

- **Blender 插件**：支持从 Blender 远程仿真，并在本地获取结果，甚至可在 macOS 上使用。
- **JupyterLab**：内置 JupyterLab，用户可通过浏览器直接运行示例。
- **Docker**：提供 Docker 镜像，支持在 Linux 和 Windows 上快速部署。
- **Windows 原生可执行文件**：提供无需安装的 Windows 可执行文件，解压即可运行。
- **云就绪**：可无缝部署在主流云平台上，如 vast.ai、Scaleway 和 Amazon Web Services。
- **MCP 支持**：允许大型语言模型使用自然语言运行仿真。

### 结论

ZOZO 的接触求解器是一个功能强大、鲁棒且可扩展的物理仿真工具，特别适合处理大规模接触问题。其开源、易于部署和丰富的功能使其成为研究和工业应用的理想选择。

## 参考
- https://github.com/st-tech/ppf-contact-solver
- https://raw.githubusercontent.com/st-tech/ppf-contact-solver/HEAD/README.md
- https://github.com/ImChong/Robotics_Notebooks

## Overview

This contact solver was developed by ZOZO, Inc., Japan's largest fashion e-commerce company, originally as an internal physics engine and has now been open-sourced. It supports simulation of various physical objects including shells, solids, rods, rigid bodies, and sand particles. Key features of the solver include: robust non-penetration contact resolution, excellent scalability (handling over 180 million contact points), high cache efficiency running entirely on GPU with single precision, and the use of the Finite Element Method (FEM) for deformable bodies with computation of symbolic force Jacobians. Additionally, it provides fabric preset parameters calibrated against real-world measurements and supports multiple usage and deployment methods including Blender plugins, JupyterLab, and Docker.

## Content
### Method Overview

This solver is a physics-based contact solver specifically designed for simulations involving multiple physical objects. Its core algorithm ensures robust contact resolution, enabling non-penetration contact without jitter or intersection.

### Core Architecture and Features

- **Robustness**: Contact resolution guarantees non-penetration without jittering intersections.
- **Scalability**: Handles over 180 million contact points in extreme cases, not just millions.
- **Cache Efficiency**: All computations run on GPU with single precision, no double precision required.
- **Finite Element Method (FEM)**: Uses FEM for deformable bodies and computes symbolic force Jacobians.
- **Parameter Calibration**: Provides fabric preset parameters matching real-world measurements.
- **Massive Parallelism**: Both contact solver and elasticity solver run on GPU.
- **Support for Multiple Objects**: Includes shells, solids, rods, rigid bodies, and sand particles.

### Experimental Setup and Key Figures

- **Extreme Scale**: Capable of handling over 180 million contact points.
- **Triangle Deformation Limit**: Triangular facets do not exceed strict upper bounds (e.g., 1%).
- **Stress Testing**: Runs 10 consecutive stress tests via GitHub Actions.
- **Docker Image**: Approximately 1GB in size for rapid deployment.
- **License**: Licensed under Apache 2.0, permitting commercial and proprietary use.

### Usage and Deployment Methods

- **Blender Plugin**: Supports remote simulation from Blender with local result retrieval, even on macOS.
- **JupyterLab**: Built-in JupyterLab allows users to run examples directly via browser.
- **Docker**: Provides Docker images for quick deployment on Linux and Windows.
- **Windows Native Executable**: Offers a no-install Windows executable that runs after extraction.
- **Cloud-Ready**: Seamlessly deployable on major cloud platforms such as vast.ai, Scaleway, and Amazon Web Services.
- **MCP Support**: Allows large language models to run simulations using natural language.

### Conclusion

ZOZO's contact solver is a powerful, robust, and scalable physics simulation tool, particularly suited for handling large-scale contact problems. Its open-source nature, ease of deployment, and rich feature set make it an ideal choice for both research and industrial applications.

## 개요

이 접촉 솔버는 일본 최대 패션 전자상거래 기업 ZOZO, Inc.가 개발했으며, 처음에는 내부 물리 엔진으로 사용되다가 현재 오픈소스로 공개되었습니다. 쉘, 솔리드, 로드, 강체 및 모래 입자 등 다양한 물리 객체의 시뮬레이션을 지원합니다. 솔버의 주요 특징으로는 강건한 비관통 접촉 해석, 뛰어난 확장성(1억 8천만 개 이상의 접촉점 처리 가능), 완전히 GPU에서 단정밀도로 실행되는 높은 캐시 효율성, 그리고 유한 요소법(FEM)을 사용하여 변형체를 처리하고 기호 힘 야코비 행렬을 계산하는 점이 있습니다. 또한 실제 측정을 통해 보정된 직물 사전 설정 파라미터를 제공하며, Blender 플러그인, JupyterLab 및 Docker 등 다양한 방식을 통해 사용 및 배포할 수 있습니다.

## 핵심 내용
### 방법 개요

이 솔버는 다양한 물리 객체를 포함하는 시뮬레이션을 위해 설계된 물리 기반 접촉 솔버입니다. 핵심 알고리즘은 접촉 해석의 강건성을 보장하여 끊김이나 교차 현상 없이 비관통 접촉을 구현합니다.

### 핵심 아키텍처 및 특징

- **강건성**: 접촉 해석이 비관통을 보장하며, 끊기는 교차점이 발생하지 않습니다.
- **확장성**: 극한 상황에서 수백만 수준이 아닌 1억 8천만 개 이상의 접촉점을 처리할 수 있습니다.
- **캐시 효율성**: 모든 계산이 GPU에서 단정밀도로 실행되며, 배정밀도가 필요하지 않습니다.
- **유한 요소법(FEM)**: 변형체에 FEM을 사용하고 기호 힘 야코비 행렬을 계산합니다.
- **파라미터 보정**: 실제 측정 결과와 일치하는 직물 사전 설정 파라미터를 제공합니다.
- **대규모 병렬 처리**: 접촉 솔버와 탄성 솔버가 모두 GPU에서 실행됩니다.
- **다양한 객체 지원**: 쉘, 솔리드, 로드, 강체 및 모래 입자를 포함합니다.

### 실험 설정 및 주요 수치

- **극한 규모**: 1억 8천만 개 이상의 접촉점을 처리할 수 있습니다.
- **삼각형 변형 제한**: 삼각형 패치가 엄격한 상한(예: 1%)을 초과하지 않습니다.
- **스트레스 테스트**: GitHub Actions를 통해 연속 10회 스트레스 테스트를 실행합니다.
- **Docker 이미지**: 크기가 약 1GB로 빠른 배포가 가능합니다.
- **라이선스**: Apache 2.0 라이선스를 채택하여 상업 및 독점 용도를 허용합니다.

### 사용 및 배포 방식

- **Blender 플러그인**: Blender에서 원격 시뮬레이션을 지원하고 로컬에서 결과를 가져올 수 있으며, macOS에서도 사용 가능합니다.
- **JupyterLab**: JupyterLab이 내장되어 있어 사용자가 브라우저를 통해 직접 예제를 실행할 수 있습니다.
- **Docker**: Docker 이미지를 제공하여 Linux 및 Windows에서 빠르게 배포할 수 있습니다.
- **Windows 네이티브 실행 파일**: 설치가 필요 없는 Windows 실행 파일을 제공하며, 압축을 풀면 바로 실행 가능합니다.
- **클라우드 준비**: vast.ai, Scaleway 및 Amazon Web Services와 같은 주요 클라우드 플랫폼에 원활하게 배포할 수 있습니다.
- **MCP 지원**: 대규모 언어 모델이 자연어를 사용하여 시뮬레이션을 실행할 수 있도록 합니다.

### 결론

ZOZO의 접촉 솔버는 대규모 접촉 문제를 처리하는 데 특히 적합한 강력하고 강건하며 확장 가능한 물리 시뮬레이션 도구입니다. 오픈소스, 쉬운 배포 및 풍부한 기능 덕분에 연구 및 산업 응용 분야에 이상적인 선택입니다.
