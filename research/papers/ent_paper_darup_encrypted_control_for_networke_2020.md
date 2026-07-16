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
  zh: Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids,
    building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages
    of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability,
    and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing
    of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eave
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.00268v1.
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
Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids, building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability, and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eavesdropping and manipulation of data. Encrypted control addresses this security gap and provides confidentiality of the processed data in the entire control loop. This paper presents a tutorial-style introduction to this young but emerging field in the framework of secure control for networked dynamical systems.

## 核心内容
Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids, building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability, and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eavesdropping and manipulation of data. Encrypted control addresses this security gap and provides confidentiality of the processed data in the entire control loop. This paper presents a tutorial-style introduction to this young but emerging field in the framework of secure control for networked dynamical systems.

## 参考
- http://arxiv.org/abs/2010.00268v1

## Overview
Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids, building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability, and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eavesdropping and manipulation of data. Encrypted control addresses this security gap and provides confidentiality of the processed data in the entire control loop. This paper presents a tutorial-style introduction to this young but emerging field in the framework of secure control for networked dynamical systems.

## Content
Cloud computing and distributed computing are becoming ubiquitous in many modern control systems such as smart grids, building automation, robot swarms or intelligent transportation systems. Compared to "isolated" control systems, the advantages of cloud-based and distributed control systems are, in particular, resource pooling and outsourcing, rapid scalability, and high performance. However, these capabilities do not come without risks. In fact, the involved communication and processing of sensitive data via public networks and on third-party platforms promote, among other cyberthreats, eavesdropping and manipulation of data. Encrypted control addresses this security gap and provides confidentiality of the processed data in the entire control loop. This paper presents a tutorial-style introduction to this young but emerging field in the framework of secure control for networked dynamical systems.

## 개요
클라우드 컴퓨팅과 분산 컴퓨팅은 스마트 그리드, 빌딩 자동화, 로봇 군집, 지능형 교통 시스템 등 많은 현대 제어 시스템에서 보편화되고 있습니다. "고립된" 제어 시스템과 비교할 때, 클라우드 기반 및 분산 제어 시스템의 장점은 특히 자원 풀링 및 아웃소싱, 빠른 확장성, 높은 성능에 있습니다. 그러나 이러한 기능에는 위험이 따릅니다. 실제로 공용 네트워크와 타사 플랫폼을 통한 민감한 데이터의 통신 및 처리는 다른 사이버 위협 중에서도 도청 및 데이터 조작을 촉진합니다. 암호화된 제어는 이러한 보안 격차를 해결하고 전체 제어 루프에서 처리된 데이터의 기밀성을 제공합니다. 본 논문은 네트워크화된 동적 시스템을 위한 안전한 제어 프레임워크에서 이 젊지만 떠오르는 분야에 대한 튜토리얼 스타일의 소개를 제공합니다.

## 핵심 내용
클라우드 컴퓨팅과 분산 컴퓨팅은 스마트 그리드, 빌딩 자동화, 로봇 군집, 지능형 교통 시스템 등 많은 현대 제어 시스템에서 보편화되고 있습니다. "고립된" 제어 시스템과 비교할 때, 클라우드 기반 및 분산 제어 시스템의 장점은 특히 자원 풀링 및 아웃소싱, 빠른 확장성, 높은 성능에 있습니다. 그러나 이러한 기능에는 위험이 따릅니다. 실제로 공용 네트워크와 타사 플랫폼을 통한 민감한 데이터의 통신 및 처리는 다른 사이버 위협 중에서도 도청 및 데이터 조작을 촉진합니다. 암호화된 제어는 이러한 보안 격차를 해결하고 전체 제어 루프에서 처리된 데이터의 기밀성을 제공합니다. 본 논문은 네트워크화된 동적 시스템을 위한 안전한 제어 프레임워크에서 이 젊지만 떠오르는 분야에 대한 튜토리얼 스타일의 소개를 제공합니다.
