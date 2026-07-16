---
$id: ent_paper_reuss_multimodal_diffusion_transform_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
  zh: MDT
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals'
summary:
  en: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
  zh: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
  ko: 'Multimodal Diffusion Transformer: Learning Versatile Behavior from Multimodal Goals (MDT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Karlsruhe Institute of Technology, and published at Robotics - Science and
    Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- mdt
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.05996v1.
sources:
- id: src_001
  type: website
  title: MDT source
  url: https://doi.org/10.15607/RSS.2024.XX.121
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 核心内容
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 参考
- http://arxiv.org/abs/2407.05996v1

## Overview
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## Content
This work introduces the Multimodal Diffusion Transformer (MDT), a novel diffusion policy framework, that excels at learning versatile behavior from multimodal goal specifications with few language annotations. MDT leverages a diffusion-based multimodal transformer backbone and two self-supervised auxiliary objectives to master long-horizon manipulation tasks based on multimodal goals. The vast majority of imitation learning methods only learn from individual goal modalities, e.g. either language or goal images. However, existing large-scale imitation learning datasets are only partially labeled with language annotations, which prohibits current methods from learning language conditioned behavior from these datasets. MDT addresses this challenge by introducing a latent goal-conditioned state representation that is simultaneously trained on multimodal goal instructions. This state representation aligns image and language based goal embeddings and encodes sufficient information to predict future states. The representation is trained via two self-supervised auxiliary objectives, enhancing the performance of the presented transformer backbone. MDT shows exceptional performance on 164 tasks provided by the challenging CALVIN and LIBERO benchmarks, including a LIBERO version that contains less than $2\%$ language annotations. Furthermore, MDT establishes a new record on the CALVIN manipulation challenge, demonstrating an absolute performance improvement of $15\%$ over prior state-of-the-art methods that require large-scale pretraining and contain $10\times$ more learnable parameters. MDT shows its ability to solve long-horizon manipulation from sparsely annotated data in both simulated and real-world environments. Demonstrations and Code are available at https://intuitive-robots.github.io/mdt_policy/.

## 개요
본 연구는 다중 모달 확산 트랜스포머(MDT)를 소개합니다. 이는 새로운 확산 정책 프레임워크로, 적은 언어 주석으로 다중 모달 목표 사양으로부터 다양한 행동을 학습하는 데 탁월합니다. MDT는 확산 기반 다중 모달 트랜스포머 백본과 두 가지 자기 지도 보조 목표를 활용하여 다중 모달 목표에 기반한 장기 조작 작업을 마스터합니다. 대부분의 모방 학습 방법은 언어 또는 목표 이미지와 같은 개별 목표 모달리티에서만 학습합니다. 그러나 기존의 대규모 모방 학습 데이터셋은 언어 주석이 부분적으로만 레이블링되어 있어, 현재 방법들이 이러한 데이터셋에서 언어 조건화된 행동을 학습하는 것을 방해합니다. MDT는 다중 모달 목표 명령에 동시에 학습되는 잠재 목표 조건화 상태 표현을 도입하여 이 문제를 해결합니다. 이 상태 표현은 이미지 및 언어 기반 목표 임베딩을 정렬하고 미래 상태를 예측하기에 충분한 정보를 인코딩합니다. 표현은 두 가지 자기 지도 보조 목표를 통해 학습되어 제시된 트랜스포머 백본의 성능을 향상시킵니다. MDT는 까다로운 CALVIN 및 LIBERO 벤치마크에서 제공되는 164개 작업에서 뛰어난 성능을 보여주며, 여기에는 언어 주석이 $2\%$ 미만인 LIBERO 버전도 포함됩니다. 또한 MDT는 CALVIN 조작 챌린지에서 새로운 기록을 세워, 대규모 사전 학습이 필요하고 $10\times$ 더 많은 학습 가능한 매개변수를 포함하는 이전 최첨단 방법보다 절대 성능이 $15\%$ 향상되었음을 입증합니다. MDT는 시뮬레이션 및 실제 환경 모두에서 희소 주석 데이터로 장기 조작을 해결하는 능력을 보여줍니다. 데모 및 코드는 https://intuitive-robots.github.io/mdt_policy/에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 다중 모달 확산 트랜스포머(MDT)를 소개합니다. 이는 새로운 확산 정책 프레임워크로, 적은 언어 주석으로 다중 모달 목표 사양으로부터 다양한 행동을 학습하는 데 탁월합니다. MDT는 확산 기반 다중 모달 트랜스포머 백본과 두 가지 자기 지도 보조 목표를 활용하여 다중 모달 목표에 기반한 장기 조작 작업을 마스터합니다. 대부분의 모방 학습 방법은 언어 또는 목표 이미지와 같은 개별 목표 모달리티에서만 학습합니다. 그러나 기존의 대규모 모방 학습 데이터셋은 언어 주석이 부분적으로만 레이블링되어 있어, 현재 방법들이 이러한 데이터셋에서 언어 조건화된 행동을 학습하는 것을 방해합니다. MDT는 다중 모달 목표 명령에 동시에 학습되는 잠재 목표 조건화 상태 표현을 도입하여 이 문제를 해결합니다. 이 상태 표현은 이미지 및 언어 기반 목표 임베딩을 정렬하고 미래 상태를 예측하기에 충분한 정보를 인코딩합니다. 표현은 두 가지 자기 지도 보조 목표를 통해 학습되어 제시된 트랜스포머 백본의 성능을 향상시킵니다. MDT는 까다로운 CALVIN 및 LIBERO 벤치마크에서 제공되는 164개 작업에서 뛰어난 성능을 보여주며, 여기에는 언어 주석이 $2\%$ 미만인 LIBERO 버전도 포함됩니다. 또한 MDT는 CALVIN 조작 챌린지에서 새로운 기록을 세워, 대규모 사전 학습이 필요하고 $10\times$ 더 많은 학습 가능한 매개변수를 포함하는 이전 최첨단 방법보다 절대 성능이 $15\%$ 향상되었음을 입증합니다. MDT는 시뮬레이션 및 실제 환경 모두에서 희소 주석 데이터로 장기 조작을 해결하는 능력을 보여줍니다. 데모 및 코드는 https://intuitive-robots.github.io/mdt_policy/에서 확인할 수 있습니다.
