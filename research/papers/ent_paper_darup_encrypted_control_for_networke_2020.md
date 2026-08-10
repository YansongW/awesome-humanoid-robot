---
$id: ent_paper_darup_encrypted_control_for_networke_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Encrypted control for networked systems: An illustrative introduction and current challenges'
  zh: 网络化系统的加密控制：示例性介绍与当前挑战
  ko: '네트워크된 시스템을 위한 암호화된 제어: 설명적 소개와 현재 과제'
summary:
  en: A tutorial-style paper that unifies encrypted controller architectures and derives encrypted formulations for linear
    state-feedback, model predictive, and distributed controllers using homomorphic encryption and secure multi-party computation.
  zh: 本文是一篇教程式论文，由多位作者共同撰写，旨在为网络化动态系统的安全控制领域提供加密控制的入门介绍。核心贡献在于统一了加密控制器架构，并利用同态加密和安全多方计算，推导了线性状态反馈、模型预测和分布式控制器的加密公式。
  ko: 동형 암호화와 안전한 다자간 계산을 사용하여 선형 상태 피드백, 모델 예측 및 분산 제어기의 암호화된 형식을 도출하고 암호화된 제어기 아키텍처를 통합한 튜토리얼 형식의 논문이다.
domains:
- 08_software_middleware
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- encrypted_control
- homomorphic_encryption
- secure_multi_party_computation
- secret_sharing
- cloud_computing
- networked_control_systems
- privacy_preserving_control
- distributed_control
- model_predictive_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.00268v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (931 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Encrypted control for networked systems: An illustrative introduction and current challenges'
  url: https://arxiv.org/abs/2010.00268
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
随着云计算和分布式计算在智能电网、楼宇自动化、机器人集群和智能交通系统等现代控制系统中日益普及，其带来的资源池化、快速扩展和高性能等优势也伴随着数据被窃听和篡改的风险。加密控制技术正是为了解决这一安全漏洞而生，它能确保整个控制回路中处理数据的机密性。本文以教程形式，系统性地介绍了这一新兴领域，并重点展示了如何将同态加密和安全多方计算应用于线性状态反馈、模型预测和分布式控制器，从而构建安全的加密控制方案。

## 核心内容
### 核心动机与问题
- 现代控制系统（如智能电网、机器人集群）越来越多地依赖云计算和分布式计算，以实现资源池化、快速扩展和高性能。
- 然而，通过公共网络和第三方平台传输和处理敏感数据，带来了严重的网络安全威胁，尤其是数据窃听和篡改。
- 加密控制技术旨在填补这一安全空白，为整个控制回路中处理的数据提供机密性保护。

### 方法与架构
- 本文以教程风格，统一了多种加密控制器架构。
- 核心方法包括：
  - **同态加密 (Homomorphic Encryption, HE)**：允许在加密数据上直接进行计算，无需解密。
  - **安全多方计算 (Secure Multi-Party Computation, SMPC)**：允许多个参与方在不泄露各自私有输入的情况下，共同计算一个函数。
- 基于上述方法，论文推导了三种关键控制器的加密公式：
  - **线性状态反馈控制器**：展示了如何对基本的线性控制律进行加密实现。
  - **模型预测控制器 (Model Predictive Control, MPC)**：探讨了在加密环境下实现优化问题的求解。
  - **分布式控制器**：解决了多个控制器节点在加密状态下进行协作与通信的问题。

### 实验设置与关键结论
- 论文作为教程，侧重于概念介绍和架构统一，并未提供具体的实验数据集或数值结果。
- 关键结论在于，通过同态加密和安全多方计算的结合，可以构建出能够保护数据机密性的网络化控制系统，从而有效抵御针对控制数据的窃听和篡改攻击。
- 论文同时指出了该领域当前面临的挑战，例如计算开销、通信延迟以及加密方案与实时控制需求的兼容性问题。

## Overview
Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids, building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability, and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eavesdropping and manipulation of data. Encrypted control addresses this security gap and provides confidentiality of the processed data in the entire control loop. This paper presents a tutorial-style introduction to this young but emerging field in the framework of secure control for networked dynamical systems.

## 参考
- http://arxiv.org/abs/2010.00268v1

## 개요
클라우드 컴퓨팅과 분산 컴퓨팅이 스마트 그리드, 빌딩 자동화, 로봇 군집, 지능형 교통 시스템과 같은 현대 제어 시스템에서 점점 더 보편화됨에 따라, 자원 풀링, 빠른 확장, 고성능과 같은 이점은 데이터 도청 및 변조 위험을 동반합니다. 암호화 제어 기술은 바로 이러한 보안 취약점을 해결하기 위해 등장했으며, 전체 제어 루프에서 처리되는 데이터의 기밀성을 보장할 수 있습니다. 본 논문은 튜토리얼 형식으로 이 신흥 분야를 체계적으로 소개하며, 특히 동형 암호화와 안전한 다자간 계산을 선형 상태 피드백, 모델 예측 및 분산 제어기에 적용하여 안전한 암호화 제어 방안을 구축하는 방법을 중점적으로 보여줍니다.

## 핵심 내용
### 핵심 동기와 문제
- 현대 제어 시스템(예: 스마트 그리드, 로봇 군집)은 자원 풀링, 빠른 확장, 고성능을 위해 점점 더 클라우드 컴퓨팅과 분산 컴퓨팅에 의존합니다.
- 그러나 공용 네트워크와 제3자 플랫폼을 통한 민감 데이터의 전송 및 처리는 심각한 사이버 보안 위협, 특히 데이터 도청 및 변조를 초래합니다.
- 암호화 제어 기술은 이러한 보안 공백을 메우고, 전체 제어 루프에서 처리되는 데이터에 기밀성 보호를 제공하는 것을 목표로 합니다.

### 방법과 아키텍처
- 본 논문은 튜토리얼 스타일로 다양한 암호화 제어기 아키텍처를 통합합니다.
- 핵심 방법은 다음과 같습니다:
  - **동형 암호화 (Homomorphic Encryption, HE)**: 복호화 없이 암호화된 데이터에 대해 직접 계산을 수행할 수 있게 합니다.
  - **안전한 다자간 계산 (Secure Multi-Party Computation, SMPC)**: 여러 참여자가 각자의 비공개 입력을 노출하지 않고 공동으로 함수를 계산할 수 있게 합니다.
- 위 방법을 기반으로, 논문은 세 가지 핵심 제어기의 암호화 공식을 도출합니다:
  - **선형 상태 피드백 제어기**: 기본 선형 제어 법칙을 암호화하여 구현하는 방법을 보여줍니다.
  - **모델 예측 제어기 (Model Predictive Control, MPC)**: 암호화 환경에서 최적화 문제 해결을 탐구합니다.
  - **분산 제어기**: 여러 제어기 노드가 암호화 상태에서 협력 및 통신하는 문제를 해결합니다.

### 실험 설정과 핵심 결론
- 본 논문은 튜토리얼로서 개념 소개와 아키텍처 통합에 중점을 두며, 구체적인 실험 데이터셋이나 수치 결과를 제공하지 않습니다.
- 핵심 결론은 동형 암호화와 안전한 다자간 계산의 결합을 통해 데이터 기밀성을 보호할 수 있는 네트워크화된 제어 시스템을 구축할 수 있으며, 이를 통해 제어 데이터에 대한 도청 및 변조 공격을 효과적으로 방어할 수 있다는 점입니다.
- 논문은 또한 계산 오버헤드, 통신 지연, 암호화 방식과 실시간 제어 요구 사항 간의 호환성 문제 등 현재 이 분야가 직면한 과제를 지적합니다.
