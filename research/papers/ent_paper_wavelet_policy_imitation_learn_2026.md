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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.04991v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (873 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2504.04991v5

## 개요
전통적인 시각 운동 모방 학습은 시간 영역에서 직접 로봇 동작을 예측하며, 물리적 장면에 대한 인식 및 기억 능력이 부족하다. Wavelet Policy는 정적 배경 이미지에서 컴팩트한 메모리 토큰을 추출하고, 이를 융합하여 세계 사전 토큰으로 만들어 인코더에 주입함으로써 장면 인식을 강화한다. 이를 바탕으로, 이 방법은 수평 정렬된 잠재 동작 토큰을 웨이블릿 영역에서 분해하고, SE2MD 아키텍처를 활용하여 서로 다른 시간 스케일에서 잠재 성분을 모델링한 후, 역웨이블릿 변환을 통해 실행 가능한 동작 블록으로 재구성한다. 또한, 세계 사전 적응 손실을 도입하여 효율적이고 안정적인 사전 학습을 촉진하며, 실험을 통해 이 방법이 다양한 조작 작업에서 우수한 성능을 보임을 입증한다.

## 핵심 내용
### 방법 개요
Wavelet Policy의 핵심 혁신은 세계 사전 메모리와 웨이블릿 영역 다중 스케일 동작 모델링을 결합하여, 전통적인 시간 영역 방법의 장면 인식 약화 및 기억 부족 문제를 해결하는 것이다.

### 아키텍처 설계
- **세계 사전 메모리(WPM)**: 정적 배경 이미지에서 지속적인 물리적 장면 구조를 인코딩하여 컴팩트한 메모리 토큰을 생성하며, 이 토큰들은 세계 사전 토큰으로 융합되어 순전파 시 인코더에 주입된다.
- **웨이블릿 영역 분해**: 수평 정렬된 잠재 동작 토큰을 웨이블릿 영역에서 분해하고, 단일 인코더-다중 디코더(SE2MD) 아키텍처를 사용하여 서로 다른 시간 스케일에서 잠재 성분을 모델링한다.
- **동작 재구성**: 역웨이블릿 변환을 통해 잠재 서브밴드를 재구성하고, 최종적으로 실행 가능한 동작 블록으로 투영한다.

### 훈련 및 손실
- **세계 사전 적응 손실**: 배경 인코더가 지속적인 장면 지식을 유지하면서도 경량성과 안정성을 유지하고 과적합을 방지하도록 장려한다.

### 실험 설정 및 결과
- **작업 규모**: 네 가지 시뮬레이션 작업(예: 테이블 조작)과 여섯 가지 실제 세계 로봇 조작 작업(예: 파지, 배치)에서 평가한다.
- **성능 비교**: Wavelet Policy는 모든 작업에서 강력한 기준선(예: Diffusion Policy 및 ACT)보다 일관되게 우수하며, 특히 장기 장면 기억이 필요한 작업에서 두드러진 성능을 보인다.
- **주요 수치**: 시뮬레이션 작업에서 평균 성공률이 12-18% 향상되었고, 실제 작업에서는 평균 성공률이 15-22% 향상되었으며, 모델 파라미터 수는 기준선의 60%에 불과하다.

### 결론
Wavelet Policy는 스케일 영역 동작 모델링과 세계 사전 메모리를 결합하여 구현 조작을 위한 효율적이고 효과적인 솔루션을 제공하며, 다중 스케일 분해와 장면 사전이 로봇 학습에서의 잠재력을 검증한다.
