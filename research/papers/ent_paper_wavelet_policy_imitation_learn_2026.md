---
$id: ent_paper_wavelet_policy_imitation_learn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  zh: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  ko: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
summary:
  en: 'arXiv:2504.04991v5 Announce Type: replace Abstract: Conventional visuomotor imitation learning usually predicts future
    robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory.
    In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM)
    with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static
    background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during
    forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition
    over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent
    components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform
    and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior
    adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and
    stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy
    consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with
    world-prior memory provides an effective and efficient solution for embodied manipulation.'
  zh: 'arXiv:2504.04991v5 Announce Type: replace Abstract: Conventional visuomotor imitation learning usually predicts future
    robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory.
    In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM)
    with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static
    background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during
    forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition
    over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent
    components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform
    and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior
    adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and
    stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy
    consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with
    world-prior memory provides an effective and efficient solution for embodied manipulation.'
  ko: 'arXiv:2504.04991v5 Announce Type: replace Abstract: Conventional visuomotor imitation learning usually predicts future
    robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory.
    In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM)
    with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static
    background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during
    forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition
    over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent
    components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform
    and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior
    adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and
    stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy
    consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with
    world-prior memory provides an effective and efficient solution for embodied manipulation.'
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
- robotics
- wavelet_policy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.04991v5.
sources:
- id: src_001
  type: paper
  title: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  url: https://arxiv.org/abs/2504.04991
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.

## 核心内容
Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.

## 参考
- http://arxiv.org/abs/2504.04991v5

## Overview
Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.

## Content
Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.

## 개요
기존의 시각-운동 모방 학습(visuomotor imitation learning)은 일반적으로 시간 영역에서 미래 로봇 동작을 직접 예측합니다. 이러한 방식은 종종 물리적 장면 인식이 제한적이고 기억 능력이 약합니다. 본 연구에서는 세계 사전 기억(World Prior Memory, WPM)과 웨이블릿 기반 다중 스케일 동작 모델링을 결합한 경량 모방 학습 프레임워크인 Wavelet Policy를 제안합니다. 핵심 아이디어는 정적 배경 이미지에서 지속적인 물리적 장면 구조를 압축된 메모리 토큰으로 인코딩하고, 이를 세계 사전 토큰(world-prior token)으로 융합하여 순방향 전파 중 인코더에 주입하는 것입니다. 이 메모리 조건화된 표현을 기반으로, 수평선 정렬된 잠재 동작 토큰에 대해 웨이블릿 영역 분해를 수행하고, 단일 인코더 다중 디코더(Single-Encoder Multiple-Decoder, SE2MD) 아키텍처를 채택하여 서로 다른 시간적 스케일에서 잠재 구성 요소를 모델링합니다. 결과적으로 생성된 잠재 서브밴드는 역 웨이블릿 변환을 통해 재구성되고 최종적으로 실행 가능한 동작 청크로 투영됩니다. 효율적인 세계 사전 학습을 촉진하기 위해, 배경 인코더가 경량이면서 안정적으로 지속적인 장면 지식을 유지하도록 장려하는 세계 사전 적응 손실(world-prior adaptation loss)을 도입합니다. 네 가지 시뮬레이션 및 여섯 가지 실제 로봇 조작 작업에 대한 광범위한 실험 결과, Wavelet Policy가 강력한 기준선을 일관되게 능가함을 보여줍니다. 이러한 결과는 스케일 영역 동작 모델링과 세계 사전 기억의 결합이 구현된 조작을 위한 효과적이고 효율적인 솔루션을 제공함을 입증합니다.

## 핵심 내용
기존의 시각-운동 모방 학습은 일반적으로 시간 영역에서 미래 로봇 동작을 직접 예측합니다. 이러한 방식은 종종 물리적 장면 인식이 제한적이고 기억 능력이 약합니다. 본 연구에서는 세계 사전 기억(World Prior Memory, WPM)과 웨이블릿 기반 다중 스케일 동작 모델링을 결합한 경량 모방 학습 프레임워크인 Wavelet Policy를 제안합니다. 핵심 아이디어는 정적 배경 이미지에서 지속적인 물리적 장면 구조를 압축된 메모리 토큰으로 인코딩하고, 이를 세계 사전 토큰(world-prior token)으로 융합하여 순방향 전파 중 인코더에 주입하는 것입니다. 이 메모리 조건화된 표현을 기반으로, 수평선 정렬된 잠재 동작 토큰에 대해 웨이블릿 영역 분해를 수행하고, 단일 인코더 다중 디코더(Single-Encoder Multiple-Decoder, SE2MD) 아키텍처를 채택하여 서로 다른 시간적 스케일에서 잠재 구성 요소를 모델링합니다. 결과적으로 생성된 잠재 서브밴드는 역 웨이블릿 변환을 통해 재구성되고 최종적으로 실행 가능한 동작 청크로 투영됩니다. 효율적인 세계 사전 학습을 촉진하기 위해, 배경 인코더가 경량이면서 안정적으로 지속적인 장면 지식을 유지하도록 장려하는 세계 사전 적응 손실(world-prior adaptation loss)을 도입합니다. 네 가지 시뮬레이션 및 여섯 가지 실제 로봇 조작 작업에 대한 광범위한 실험 결과, Wavelet Policy가 강력한 기준선을 일관되게 능가함을 보여줍니다. 이러한 결과는 스케일 영역 동작 모델링과 세계 사전 기억의 결합이 구현된 조작을 위한 효과적이고 효율적인 솔루션을 제공함을 입증합니다.
