---
$id: ent_paper_mirth_mutual_information_reaso_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  zh: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  ko: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
summary:
  en: 'arXiv:2606.31167v1 Announce Type: new Abstract: VLA models have emerged as a powerful paradigm for transferring semantic
    knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic
    limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level
    motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified
    framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1)
    dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings;
    (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal
    context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with
    vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a
    real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error
    recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.'
  zh: 'arXiv:2606.31167v1 Announce Type: new Abstract: VLA models have emerged as a powerful paradigm for transferring semantic
    knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic
    limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level
    motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified
    framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1)
    dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings;
    (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal
    context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with
    vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a
    real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error
    recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.'
  ko: 'arXiv:2606.31167v1 Announce Type: new Abstract: VLA models have emerged as a powerful paradigm for transferring semantic
    knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic
    limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level
    motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified
    framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1)
    dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings;
    (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal
    context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with
    vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a
    real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error
    recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- mirth
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31167v1.
sources:
- id: src_001
  type: paper
  title: 'MIRTH: Mutual-Information Reasoning with Temporal Hubs for Vision-Language-Action Agents'
  url: https://arxiv.org/abs/2606.31167
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

## 核心内容
VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

## 参考
- http://arxiv.org/abs/2606.31167v1

## Overview
VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

## Content
VLA models have emerged as a powerful paradigm for transferring semantic knowledge from web-scale data to physical robotic control. However, current single-frame architectures suffer from intrinsic limitations: temporal myopia that discards historical dynamics, reasoning gaps between high-level instructions and low-level motor commands, and inference inefficiency due to autoregressive scalar decoding. In this work, we propose MIRTH, a unified framework designed to address these challenges. MIRTH augments a pretrained VLA backbone with three key innovations: (1) dual-scale temporal memory hubs that compress long-term scene evolution and short-term motion trends into compact embeddings; (2) latent reasoning tokens optimized via a mutual-information objective carving out a semantic plan space to align multimodal context with action trajectories; and (3) a parallel action decoding scheme that replaces autoregressive generation with vector-wise prediction to maximize control throughput. Extensive evaluations on the LIBERO simulation benchmark and a real-world LeRobot platform demonstrate that MIRTH achieves state-of-the-art performance and exhibiting emergent error recovery capabilities. The codes and collected datasets are released at http://github.com/kiva12138/mirth.

## 개요
VLA 모델은 웹 규모 데이터의 의미론적 지식을 물리적 로봇 제어로 전이하는 강력한 패러다임으로 부상했습니다. 그러나 현재의 단일 프레임 아키텍처는 본질적인 한계를 가지고 있습니다: 과거 동역학을 무시하는 시간적 근시, 고수준 명령과 저수준 모터 명령 사이의 추론 격차, 그리고 자기회귀적 스칼라 디코딩으로 인한 추론 비효율성입니다. 본 연구에서는 이러한 문제를 해결하기 위해 설계된 통합 프레임워크인 MIRTH를 제안합니다. MIRTH는 사전 훈련된 VLA 백본에 세 가지 핵심 혁신을 추가합니다: (1) 장기 장면 진화와 단기 움직임 추세를 컴팩트 임베딩으로 압축하는 이중 스케일 시간 메모리 허브; (2) 상호 정보 목표를 통해 최적화된 잠재 추론 토큰으로, 다중 모달 컨텍스트를 행동 궤적과 정렬하기 위한 의미론적 계획 공간을 구축; (3) 자기회귀적 생성을 벡터 단위 예측으로 대체하여 제어 처리량을 극대화하는 병렬 행동 디코딩 방식입니다. LIBERO 시뮬레이션 벤치마크와 실제 LeRobot 플랫폼에서의 광범위한 평가를 통해 MIRTH가 최첨단 성능을 달성하고 비상 오류 복구 능력을 나타냄을 입증했습니다. 코드와 수집된 데이터셋은 http://github.com/kiva12138/mirth에서 공개되었습니다.

## 핵심 내용
VLA 모델은 웹 규모 데이터의 의미론적 지식을 물리적 로봇 제어로 전이하는 강력한 패러다임으로 부상했습니다. 그러나 현재의 단일 프레임 아키텍처는 본질적인 한계를 가지고 있습니다: 과거 동역학을 무시하는 시간적 근시, 고수준 명령과 저수준 모터 명령 사이의 추론 격차, 그리고 자기회귀적 스칼라 디코딩으로 인한 추론 비효율성입니다. 본 연구에서는 이러한 문제를 해결하기 위해 설계된 통합 프레임워크인 MIRTH를 제안합니다. MIRTH는 사전 훈련된 VLA 백본에 세 가지 핵심 혁신을 추가합니다: (1) 장기 장면 진화와 단기 움직임 추세를 컴팩트 임베딩으로 압축하는 이중 스케일 시간 메모리 허브; (2) 상호 정보 목표를 통해 최적화된 잠재 추론 토큰으로, 다중 모달 컨텍스트를 행동 궤적과 정렬하기 위한 의미론적 계획 공간을 구축; (3) 자기회귀적 생성을 벡터 단위 예측으로 대체하여 제어 처리량을 극대화하는 병렬 행동 디코딩 방식입니다. LIBERO 시뮬레이션 벤치마크와 실제 LeRobot 플랫폼에서의 광범위한 평가를 통해 MIRTH가 최첨단 성능을 달성하고 비상 오류 복구 능력을 나타냄을 입증했습니다. 코드와 수집된 데이터셋은 http://github.com/kiva12138/mirth에서 공개되었습니다.
