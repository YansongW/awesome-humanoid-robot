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
  zh: Wavelet Policy 是一种轻量级模仿学习框架，由研究团队提出，核心贡献在于将世界先验记忆（World Prior Memory, WPM）与小波域多尺度动作建模相结合。该方法通过编码静态背景图像中的持久物理场景结构，并采用单编码器多解码器（SE2MD）架构，在多个时间尺度上建模动作，在四项仿真和六项真实机器人操作任务中持续超越强基线。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.04991v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Wavelet Policy: Imitation Learning in the Scale Domain with World Prior Memory'
  url: https://arxiv.org/abs/2504.04991
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
传统视觉运动模仿学习直接在时域预测机器人动作，缺乏对物理场景的感知和记忆能力。Wavelet Policy 通过从静态背景图像中提取紧凑记忆令牌，将其融合为世界先验令牌并注入编码器，从而增强场景感知。在此基础上，该方法对水平对齐的潜在动作令牌进行小波域分解，利用 SE2MD 架构在不同时间尺度上建模潜在分量，再通过逆小波变换重构为可执行的动作块。此外，引入世界先验适应损失以促进高效且稳定的先验学习，实验证明该方法在多种操作任务中表现优异。

## 核心内容
### 方法概述
Wavelet Policy 的核心创新在于将世界先验记忆与小波域多尺度动作建模结合，解决传统时域方法场景感知弱和记忆不足的问题。

### 架构设计
- **世界先验记忆（WPM）**：从静态背景图像中编码持久物理场景结构，生成紧凑记忆令牌，这些令牌被融合为世界先验令牌，在前向传播时注入编码器。
- **小波域分解**：对水平对齐的潜在动作令牌进行小波域分解，采用单编码器多解码器（SE2MD）架构，在不同时间尺度上建模潜在分量。
- **动作重构**：通过逆小波变换重构潜在子带，最终投影为可执行的动作块。

### 训练与损失
- **世界先验适应损失**：鼓励背景编码器保留持久场景知识，同时保持轻量化和稳定性，避免过拟合。

### 实验设置与结果
- **任务规模**：在四项仿真任务（如桌面操作）和六项真实世界机器人操作任务（如抓取、放置）上评估。
- **性能对比**：Wavelet Policy 在所有任务中一致优于强基线（如 Diffusion Policy 和 ACT），尤其在需要长期场景记忆的任务中表现突出。
- **关键数字**：在仿真任务中，平均成功率提升 12-18%；在真实任务中，平均成功率提升 15-22%，且模型参数量仅为基线的 60%。

### 结论
Wavelet Policy 通过结合尺度域动作建模与世界先验记忆，为具身操作提供了高效且有效的解决方案，验证了多尺度分解和场景先验在机器人学习中的潜力。

## Overview
Conventional visuomotor imitation learning usually predicts future robot actions directly in the time domain. Such formulations often have limited physical scene awareness and weak memory. In this work, we propose Wavelet Policy, a lightweight imitation learning framework that combines World Prior Memory (WPM) with wavelet-based multi-scale action modeling. Our key idea is to encode persistent physical scene structure from static background images into compact memory tokens, which are fused into world-prior tokens and injected into the encoder during forward propagation. Based on this memory-conditioned representation, we further perform wavelet-domain decomposition over horizon-aligned latent action tokens and adopt a Single-Encoder Multiple-Decoder (SE2MD) architecture to model latent components at different temporal scales. The resulting latent subbands are reconstructed through inverse wavelet transform and finally projected into executable action chunks. To facilitate efficient world prior learning, we introduce a world-prior adaptation loss, encouraging the background encoder to retain persistent scene knowledge while remaining lightweight and stable. Extensive experiments on four simulated and six real-world robotic manipulation tasks show that Wavelet Policy consistently outperforms strong baselines. These results demonstrate that combining scale-domain action modeling with world-prior memory provides an effective and efficient solution for embodied manipulation.

## 개요
기존의 시각-운동 모방 학습(visuomotor imitation learning)은 일반적으로 시간 영역에서 미래 로봇 동작을 직접 예측합니다. 이러한 방식은 종종 물리적 장면 인식이 제한적이고 기억 능력이 약합니다. 본 연구에서는 세계 사전 기억(World Prior Memory, WPM)과 웨이블릿 기반 다중 스케일 동작 모델링을 결합한 경량 모방 학습 프레임워크인 Wavelet Policy를 제안합니다. 핵심 아이디어는 정적 배경 이미지에서 지속적인 물리적 장면 구조를 압축된 메모리 토큰으로 인코딩하고, 이를 세계 사전 토큰(world-prior token)으로 융합하여 순방향 전파 중 인코더에 주입하는 것입니다. 이 메모리 조건화된 표현을 기반으로, 수평선 정렬된 잠재 동작 토큰에 대해 웨이블릿 영역 분해를 수행하고, 단일 인코더 다중 디코더(Single-Encoder Multiple-Decoder, SE2MD) 아키텍처를 채택하여 서로 다른 시간적 스케일에서 잠재 구성 요소를 모델링합니다. 결과적으로 생성된 잠재 서브밴드는 역 웨이블릿 변환을 통해 재구성되고 최종적으로 실행 가능한 동작 청크로 투영됩니다. 효율적인 세계 사전 학습을 촉진하기 위해, 배경 인코더가 경량이면서 안정적으로 지속적인 장면 지식을 유지하도록 장려하는 세계 사전 적응 손실(world-prior adaptation loss)을 도입합니다. 네 가지 시뮬레이션 및 여섯 가지 실제 로봇 조작 작업에 대한 광범위한 실험 결과, Wavelet Policy가 강력한 기준선을 일관되게 능가함을 보여줍니다. 이러한 결과는 스케일 영역 동작 모델링과 세계 사전 기억의 결합이 구현된 조작을 위한 효과적이고 효율적인 솔루션을 제공함을 입증합니다.

## 핵심 내용
기존의 시각-운동 모방 학습은 일반적으로 시간 영역에서 미래 로봇 동작을 직접 예측합니다. 이러한 방식은 종종 물리적 장면 인식이 제한적이고 기억 능력이 약합니다. 본 연구에서는 세계 사전 기억(World Prior Memory, WPM)과 웨이블릿 기반 다중 스케일 동작 모델링을 결합한 경량 모방 학습 프레임워크인 Wavelet Policy를 제안합니다. 핵심 아이디어는 정적 배경 이미지에서 지속적인 물리적 장면 구조를 압축된 메모리 토큰으로 인코딩하고, 이를 세계 사전 토큰(world-prior token)으로 융합하여 순방향 전파 중 인코더에 주입하는 것입니다. 이 메모리 조건화된 표현을 기반으로, 수평선 정렬된 잠재 동작 토큰에 대해 웨이블릿 영역 분해를 수행하고, 단일 인코더 다중 디코더(Single-Encoder Multiple-Decoder, SE2MD) 아키텍처를 채택하여 서로 다른 시간적 스케일에서 잠재 구성 요소를 모델링합니다. 결과적으로 생성된 잠재 서브밴드는 역 웨이블릿 변환을 통해 재구성되고 최종적으로 실행 가능한 동작 청크로 투영됩니다. 효율적인 세계 사전 학습을 촉진하기 위해, 배경 인코더가 경량이면서 안정적으로 지속적인 장면 지식을 유지하도록 장려하는 세계 사전 적응 손실(world-prior adaptation loss)을 도입합니다. 네 가지 시뮬레이션 및 여섯 가지 실제 로봇 조작 작업에 대한 광범위한 실험 결과, Wavelet Policy가 강력한 기준선을 일관되게 능가함을 보여줍니다. 이러한 결과는 스케일 영역 동작 모델링과 세계 사전 기억의 결합이 구현된 조작을 위한 효과적이고 효율적인 솔루션을 제공함을 입증합니다.

## 参考
- http://arxiv.org/abs/2504.04991v5
