---
$id: ent_paper_darup_encrypted_control_for_networke_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Encrypted control for networked systems: An illustrative introduction and current
    challenges'
  zh: 网络化系统的加密控制：示例性介绍与当前挑战
  ko: '네트워크된 시스템을 위한 암호화된 제어: 설명적 소개와 현재 과제'
summary:
  en: A tutorial-style paper that unifies encrypted controller architectures and derives
    encrypted formulations for linear state-feedback, model predictive, and distributed
    controllers using homomorphic encryption and secure multi-party computation.
  zh: 一篇教程式论文，统一了加密控制器架构，并基于同态加密与安全多方计算推导了线性状态反馈、模型预测和分布式控制器的加密形式。
  ko: 동형 암호화와 안전한 다자간 계산을 사용하여 선형 상태 피드백, 모델 예측 및 분산 제어기의 암호화된 형식을 도출하고 암호화된 제어기 아키텍처를
    통합한 튜토리얼 형식의 논문이다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'Encrypted control for networked systems: An illustrative introduction and
    current challenges'
  url: https://arxiv.org/abs/2010.00268
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper provides a tutorial-style introduction to encrypted control for networked dynamical systems. It explains how to reformulate standard control algorithms so that sensitive states, inputs, controller parameters, and model data remain encrypted during transmission over public networks and computation on untrusted or third-party platforms. The discussion covers the conceptual steps, changes in computation flows, and quantization issues that arise when moving from unencrypted to encrypted controller realizations.

The authors unify several encrypted controller types and architectures, targeting readers without deep cryptography backgrounds. They focus on linear state-feedback controllers, model predictive control, and cooperative control for multi-agent systems, showing how cryptographic primitives such as homomorphic encryption and secure multi-party computation can be embedded into the control loop. The paper also surveys practical challenges including computational and communication overhead, latency, stability guarantees, and continuous operation.

The work concludes with a list of open problems and future directions. These include the need for efficient fully homomorphic schemes, handling of active attacks on integrity and availability, and robustness to network latency and packet loss in realistic deployments.

## Key Contributions

- Tutorial-style unification of encrypted controller types, architectures, and cryptographic tools for non-cryptographers.
- Derivation of encrypted formulations for linear state-feedback controllers using ElGamal, Paillier, and secret-sharing/two-party computation.
- Presentation of encrypted model predictive control via offline explicit solutions, real-time projected-gradient iterations, and multi-party computation.
- Presentation of encrypted cooperative control for multi-agent systems with privacy-preserving control shares.
- Discussion of quantization effects, stability guarantees, continuous operation, and a list of open problems and future directions.

## Relevance to Humanoid Robotics

Humanoid robots are increasingly deployed in fleets that rely on cloud-based computation, distributed controllers, and multi-agent coordination for fleet management and mass production. This paper's methods for computing control actions on encrypted data can help keep operational states, inputs, controller gains, and model parameters confidential from third-party compute platforms or curious agents in such deployments. The software-middleware focus aligns with building trustworthy control backbones for humanoid systems at scale.
