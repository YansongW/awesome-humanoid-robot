---
$id: ent_paper_ceola_fast_object_segmentation_learn_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Fast Object Segmentation Learning with Kernel-based Methods for Robotics
  zh: 基于核方法的机器人快速目标分割学习
  ko: 커널 기반 방법을 활용한 로보틱스용 빠른 객체 분할 학습
summary:
  en: A 2021 paper proposing a hybrid object-segmentation architecture that replaces output layers of a pre-trained Mask R-CNN
    with FALKON kernel-based classifiers and RLS regressors to enable fast online training for robotic vision.
  zh: 2021年发表的论文，提出了一种混合目标分割架构，使用FALKON核分类器和RLS回归器替换预训练Mask R-CNN的输出层，以实现机器人视觉的快速在线训练。
  ko: 2021년 발표된 논문으로, 사전 학습된 Mask R-CNN의 출력 층을 FALKON 커널 기반 분류기와 RLS 회귀기로 대체하여 로봇 비전을 위한 빠른 온라인 학습을 가능하게 하는 하이브리드 객체 분할 아키텍처를
    제안한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- object_segmentation
- instance_segmentation
- kernel_methods
- falkon
- mask_rcnn
- online_learning
- robotic_vision
- ycb_video
- fast_training
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2011.12805v2.
sources:
- id: src_001
  type: paper
  title: Fast Object Segmentation Learning with Kernel-based Methods for Robotics
  url: https://arxiv.org/abs/2011.12805
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Object segmentation is a key component in the visual system of a robot that performs tasks like grasping and object manipulation, especially in presence of occlusions. Like many other computer vision tasks, the adoption of deep architectures has made available algorithms that perform this task with remarkable performance. However, adoption of such algorithms in robotics is hampered by the fact that training requires large amount of computing time and it cannot be performed on-line. In this work, we propose a novel architecture for object segmentation, that overcomes this problem and provides comparable performance in a fraction of the time required by the state-of-the-art methods. Our approach is based on a pre-trained Mask R-CNN, in which various layers have been replaced with a set of classifiers and regressors that are re-trained for a new task. We employ an efficient Kernel-based method that allows for fast training on large scale problems. Our approach is validated on the YCB-Video dataset which is widely adopted in the computer vision and robotics community, demonstrating that we can achieve and even surpass performance of the state-of-the-art, with a significant reduction (${\sim}6\times$) of the training time. The code to reproduce the experiments is publicly available on GitHub.

## 核心内容
Object segmentation is a key component in the visual system of a robot that performs tasks like grasping and object manipulation, especially in presence of occlusions. Like many other computer vision tasks, the adoption of deep architectures has made available algorithms that perform this task with remarkable performance. However, adoption of such algorithms in robotics is hampered by the fact that training requires large amount of computing time and it cannot be performed on-line. In this work, we propose a novel architecture for object segmentation, that overcomes this problem and provides comparable performance in a fraction of the time required by the state-of-the-art methods. Our approach is based on a pre-trained Mask R-CNN, in which various layers have been replaced with a set of classifiers and regressors that are re-trained for a new task. We employ an efficient Kernel-based method that allows for fast training on large scale problems. Our approach is validated on the YCB-Video dataset which is widely adopted in the computer vision and robotics community, demonstrating that we can achieve and even surpass performance of the state-of-the-art, with a significant reduction (${\sim}6\times$) of the training time. The code to reproduce the experiments is publicly available on GitHub.

## 参考
- http://arxiv.org/abs/2011.12805v2

## Overview
Object segmentation is a key component in the visual system of a robot that performs tasks like grasping and object manipulation, especially in presence of occlusions. Like many other computer vision tasks, the adoption of deep architectures has made available algorithms that perform this task with remarkable performance. However, adoption of such algorithms in robotics is hampered by the fact that training requires large amount of computing time and it cannot be performed on-line. In this work, we propose a novel architecture for object segmentation, that overcomes this problem and provides comparable performance in a fraction of the time required by the state-of-the-art methods. Our approach is based on a pre-trained Mask R-CNN, in which various layers have been replaced with a set of classifiers and regressors that are re-trained for a new task. We employ an efficient Kernel-based method that allows for fast training on large scale problems. Our approach is validated on the YCB-Video dataset which is widely adopted in the computer vision and robotics community, demonstrating that we can achieve and even surpass performance of the state-of-the-art, with a significant reduction (${\sim}6\times$) of the training time. The code to reproduce the experiments is publicly available on GitHub.

## Content
Object segmentation is a key component in the visual system of a robot that performs tasks like grasping and object manipulation, especially in presence of occlusions. Like many other computer vision tasks, the adoption of deep architectures has made available algorithms that perform this task with remarkable performance. However, adoption of such algorithms in robotics is hampered by the fact that training requires large amount of computing time and it cannot be performed on-line. In this work, we propose a novel architecture for object segmentation, that overcomes this problem and provides comparable performance in a fraction of the time required by the state-of-the-art methods. Our approach is based on a pre-trained Mask R-CNN, in which various layers have been replaced with a set of classifiers and regressors that are re-trained for a new task. We employ an efficient Kernel-based method that allows for fast training on large scale problems. Our approach is validated on the YCB-Video dataset which is widely adopted in the computer vision and robotics community, demonstrating that we can achieve and even surpass performance of the state-of-the-art, with a significant reduction (${\sim}6\times$) of the training time. The code to reproduce the experiments is publicly available on GitHub.

## 개요
객체 분할은 특히 폐색이 있는 상황에서 물체를 잡거나 조작하는 작업을 수행하는 로봇의 시각 시스템에서 핵심 구성 요소입니다. 다른 많은 컴퓨터 비전 작업과 마찬가지로, 심층 아키텍처의 도입으로 이 작업을 놀라운 성능으로 수행하는 알고리즘을 사용할 수 있게 되었습니다. 그러나 로봇 공학에서 이러한 알고리즘을 채택하는 것은 훈련에 많은 계산 시간이 필요하고 온라인으로 수행할 수 없다는 사실로 인해 방해를 받습니다. 본 연구에서는 이 문제를 극복하고 최신 방법에 비해 훨씬 짧은 시간 내에 유사한 성능을 제공하는 새로운 객체 분할 아키텍처를 제안합니다. 우리의 접근 방식은 사전 훈련된 Mask R-CNN을 기반으로 하며, 다양한 레이어를 새로운 작업을 위해 재훈련되는 분류기와 회귀기 세트로 대체합니다. 대규모 문제에서 빠른 훈련을 가능하게 하는 효율적인 커널 기반 방법을 사용합니다. 우리의 접근 방식은 컴퓨터 비전 및 로봇 공학 커뮤니티에서 널리 채택된 YCB-Video 데이터셋에서 검증되었으며, 훈련 시간을 크게 줄이면서(${\sim}6\times$) 최신 기술의 성능을 달성하거나 심지어 능가할 수 있음을 보여줍니다. 실험을 재현하기 위한 코드는 GitHub에서 공개적으로 제공됩니다.

## 핵심 내용
객체 분할은 특히 폐색이 있는 상황에서 물체를 잡거나 조작하는 작업을 수행하는 로봇의 시각 시스템에서 핵심 구성 요소입니다. 다른 많은 컴퓨터 비전 작업과 마찬가지로, 심층 아키텍처의 도입으로 이 작업을 놀라운 성능으로 수행하는 알고리즘을 사용할 수 있게 되었습니다. 그러나 로봇 공학에서 이러한 알고리즘을 채택하는 것은 훈련에 많은 계산 시간이 필요하고 온라인으로 수행할 수 없다는 사실로 인해 방해를 받습니다. 본 연구에서는 이 문제를 극복하고 최신 방법에 비해 훨씬 짧은 시간 내에 유사한 성능을 제공하는 새로운 객체 분할 아키텍처를 제안합니다. 우리의 접근 방식은 사전 훈련된 Mask R-CNN을 기반으로 하며, 다양한 레이어를 새로운 작업을 위해 재훈련되는 분류기와 회귀기 세트로 대체합니다. 대규모 문제에서 빠른 훈련을 가능하게 하는 효율적인 커널 기반 방법을 사용합니다. 우리의 접근 방식은 컴퓨터 비전 및 로봇 공학 커뮤니티에서 널리 채택된 YCB-Video 데이터셋에서 검증되었으며, 훈련 시간을 크게 줄이면서(${\sim}6\times$) 최신 기술의 성능을 달성하거나 심지어 능가할 수 있음을 보여줍니다. 실험을 재현하기 위한 코드는 GitHub에서 공개적으로 제공됩니다.
