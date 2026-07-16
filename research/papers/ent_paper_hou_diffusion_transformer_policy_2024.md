---
$id: ent_paper_hou_diffusion_transformer_policy_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diffusion Transformer Policy
  zh: Diffusion Transformer Policy
  ko: Diffusion Transformer Policy
summary:
  en: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
  zh: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
  ko: Diffusion Transformer Policy (Diffusion Transformer Policy), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by Shanghai AI Lab, College of Computer Science and Technology, Zhejiang University, MMLab, The
    Chinese University of Hong Kong, Peking University, SenseTime Research, Tsinghua University, Center for Artificial Intelligence
    and Robotics, HKISI, CAS, and published at ICRA 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_transformer_policy
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.15959v6.
sources:
- id: src_001
  type: website
  title: Diffusion Transformer Policy source
  url: https://doi.org/10.1109/ICRA55743.2025.11128074
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## 核心内容
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## 参考
- http://arxiv.org/abs/2410.15959v6

## Overview
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## Content
Recent large vision-language-action models pretrained on diverse robot datasets have demonstrated the potential for generalizing to new environments with a few in-domain data. However, those approaches usually predict individual discretized or continuous action by a small action head, which limits the ability in handling diverse action spaces. In contrast, we model the continuous action sequence with a large multi-modal diffusion transformer, dubbed as Diffusion Transformer Policy, in which we directly denoise action chunks by a large transformer model rather than a small action head for action embedding. By leveraging the scaling capability of transformers, the proposed approach can effectively model continuous end-effector actions across large diverse robot datasets, and achieve better generalization performance. Extensive experiments demonstrate the effectiveness and generalization of Diffusion Transformer Policy on Maniskill2, Libero, Calvin and SimplerEnv, as well as the real-world Franka arm, achieving consistent better performance on Real-to-Sim benchmark SimplerEnv, real-world Franka Arm and Libero compared to OpenVLA and Octo. Specifically, without bells and whistles, the proposed approach achieves state-of-the-art performance with only a single third-view camera stream in the Calvin task ABC->D, improving the average number of tasks completed in a row of 5 to 3.6, and the pretraining stage significantly facilitates the success sequence length on the Calvin by over 1.2.

## 개요
최근 다양한 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동 모델은 소량의 도메인 내 데이터만으로 새로운 환경에 일반화할 수 있는 잠재력을 보여주었습니다. 그러나 이러한 접근 방식은 일반적으로 작은 행동 헤드를 통해 개별적으로 이산화되거나 연속적인 행동을 예측하여 다양한 행동 공간을 처리하는 능력에 한계가 있습니다. 이와 대조적으로, 우리는 연속적인 행동 시퀀스를 대규모 다중 모달 확산 트랜스포머(Diffusion Transformer Policy)로 모델링하며, 여기서는 작은 행동 헤드 대신 대규모 트랜스포머 모델을 사용하여 행동 청크를 직접 노이즈 제거합니다. 트랜스포머의 확장 능력을 활용함으로써 제안된 접근 방식은 다양한 대규모 로봇 데이터셋에서 연속적인 엔드 이펙터 행동을 효과적으로 모델링하고 더 나은 일반화 성능을 달성합니다. 광범위한 실험을 통해 Diffusion Transformer Policy가 Maniskill2, Libero, Calvin, SimplerEnv 및 실제 Franka 암에서 효과성과 일반화를 입증했으며, OpenVLA 및 Octo와 비교하여 Real-to-Sim 벤치마크 SimplerEnv, 실제 Franka Arm 및 Libero에서 일관되게 더 나은 성능을 보였습니다. 특히, 별다른 부가 장치 없이 제안된 접근 방식은 Calvin 작업 ABC->D에서 단일 제3자 시점 카메라 스트림만으로 최첨단 성능을 달성하여 연속적으로 완료된 작업의 평균 개수를 5개에서 3.6개로 향상시켰으며, 사전 학습 단계는 Calvin에서 성공 시퀀스 길이를 1.2 이상 크게 촉진했습니다.

## 핵심 내용
최근 다양한 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동 모델은 소량의 도메인 내 데이터만으로 새로운 환경에 일반화할 수 있는 잠재력을 보여주었습니다. 그러나 이러한 접근 방식은 일반적으로 작은 행동 헤드를 통해 개별적으로 이산화되거나 연속적인 행동을 예측하여 다양한 행동 공간을 처리하는 능력에 한계가 있습니다. 이와 대조적으로, 우리는 연속적인 행동 시퀀스를 대규모 다중 모달 확산 트랜스포머(Diffusion Transformer Policy)로 모델링하며, 여기서는 작은 행동 헤드 대신 대규모 트랜스포머 모델을 사용하여 행동 청크를 직접 노이즈 제거합니다. 트랜스포머의 확장 능력을 활용함으로써 제안된 접근 방식은 다양한 대규모 로봇 데이터셋에서 연속적인 엔드 이펙터 행동을 효과적으로 모델링하고 더 나은 일반화 성능을 달성합니다. 광범위한 실험을 통해 Diffusion Transformer Policy가 Maniskill2, Libero, Calvin, SimplerEnv 및 실제 Franka 암에서 효과성과 일반화를 입증했으며, OpenVLA 및 Octo와 비교하여 Real-to-Sim 벤치마크 SimplerEnv, 실제 Franka Arm 및 Libero에서 일관되게 더 나은 성능을 보였습니다. 특히, 별다른 부가 장치 없이 제안된 접근 방식은 Calvin 작업 ABC->D에서 단일 제3자 시점 카메라 스트림만으로 최첨단 성능을 달성하여 연속적으로 완료된 작업의 평균 개수를 5개에서 3.6개로 향상시켰으며, 사전 학습 단계는 Calvin에서 성공 시퀀스 길이를 1.2 이상 크게 촉진했습니다.
