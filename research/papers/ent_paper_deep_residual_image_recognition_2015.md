---
$id: ent_paper_deep_residual_image_recognition_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Residual Learning for Image Recognition
  zh: Deep Residual Learning for Image Recognition
  ko: Deep Residual Learning for Image Recognition
summary:
  en: 'Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of
    networks that are substantially deeper than those used previously. Institutions per source list: Microsoft Research.'
  zh: 何恺明等人提出深度残差学习框架（ResNet），通过引入残差函数（residual function）解决深层网络训练困难问题。核心贡献在于证明152层残差网络在ImageNet上以更低复杂度超越VGG，并在ILSVRC 2015分类任务中取得3.57%错误率夺冠。该框架同时推动COCO检测任务提升28%相对性能。
  ko: 'Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of
    networks that are substantially deeper than those used previously. Institutions per source list: Microsoft Research.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- deep
- residual
- image
- recognition
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 747 (.staging/ingest_yuanxq). Tier C->full. arXiv id 1512.03385 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (1512.03385v1); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:1512.03385 Deep Residual Learning for Image Recognition
  url: https://arxiv.org/abs/1512.03385
  accessed_at: '2026-07-31'
  date: '2015-12-10'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

传统深层神经网络面临梯度消失/爆炸导致的训练退化问题。ResNet创新性地将网络层重构为学习输入与输出的残差映射，通过恒等捷径连接（identity shortcut connections）使梯度可直接反向传播。实验表明，152层ResNet的复杂度低于VGG-16/19，但ImageNet top-5错误率降至3.57%。在CIFAR-10上验证了100层与1000层网络的可行性，且深度增加持续提升精度。该架构成为2015年ILSVRC与COCO五项冠军的基础。

## 核心内容
### 核心方法
- **残差学习**：将期望的底层映射H(x)重构为F(x)+x，其中F(x)=H(x)-x为残差函数。通过前馈神经网络实现F(x)，恒等映射x通过捷径连接（shortcut connections）直接传递。
- **捷径连接实现**：当输入输出维度匹配时直接相加；维度不匹配时通过零填充或1×1卷积投影调整。所有捷径连接不引入额外参数。

### 网络架构
- **ImageNet基准**：34层plain网络与34层ResNet对比，后者在18层基础上每两层添加残差连接。152层ResNet采用bottleneck设计（1×1→3×3→1×1卷积），参数量低于VGG-19。
- **CIFAR-10实验**：构建20层至1202层网络，使用3×3卷积核，特征图尺寸32×32→8×8时通道数倍增。1001层网络测试误差4.62%，但1202层因过拟合误差略高。

### 实验设置
- **训练参数**：ImageNet使用随机裁剪（224×224）、水平翻转、颜色增强，SGD优化器（batch size=256，momentum=0.9，weight decay=0.0001）。学习率从0.1开始，每30个epoch除以10，总迭代60万次。
- **测试策略**：标准10-crop测试（224×224），集成6个152层ResNet模型。

### 关键结果
- **ImageNet分类**：152层ResNet单模型top-5错误率4.49%，集成模型3.57%（ILSVRC 2015冠军）。相比VGG-16（7.4%）、GoogleNet（6.7%）显著提升。
- **深度影响**：34层ResNet（top-5错误率5.71%）优于18层ResNet（5.91%），而plain网络34层（7.51%）反而不如18层（5.60%），证明残差学习消除退化。
- **COCO检测**：基于Faster R-CNN框架，将VGG-16替换为101层ResNet，mAP从21.1%提升至27.0%（相对提升28%）。

### 结论
残差学习框架使网络深度突破传统限制，验证了深度表示对视觉任务的核心作用。该工作为后续DenseNet、ResNeXt等架构奠定基础，并推动计算机视觉进入超深网络时代。

## Overview
Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from considerably increased depth. On the ImageNet dataset we evaluate residual nets with a depth of up to 152 layers---8x deeper than VGG nets but still having lower complexity. An ensemble of these residual nets achieves 3.57% error on the ImageNet test set. This result won the 1st place on the ILSVRC 2015 classification task. We also present analysis on CIFAR-10 with 100 and 1000 layers. The depth of representations is of central importance for many visual recognition tasks. Solely due to our extremely deep representations, we obtain a 28% relative improvement on the COCO object detection dataset. Deep residual nets are foundations of our submissions to ILSVRC & COCO 2015 competitions, where we also won the 1st places on the tasks of ImageNet detection, ImageNet localization, COCO detection, and COCO segmentation.

## 参考
- https://arxiv.org/abs/1512.03385
- https://github.com/ImChong/Robotics_Notebooks

## 개요

전통적인 심층 신경망은 기울기 소실/폭발로 인한 훈련 저하 문제에 직면합니다. ResNet은 네트워크 계층을 입력과 출력의 잔차 매핑을 학습하도록 재구성하고, 항등 지름길 연결(identity shortcut connections)을 통해 기울기를 직접 역전파할 수 있게 합니다. 실험 결과, 152층 ResNet의 복잡도는 VGG-16/19보다 낮지만, ImageNet top-5 오류율은 3.57%로 감소했습니다. CIFAR-10에서는 100층 및 1000층 네트워크의 실행 가능성을 검증했으며, 깊이가 증가할수록 정확도가 지속적으로 향상되었습니다. 이 아키텍처는 2015년 ILSVRC 및 COCO 5개 부문 우승의 기반이 되었습니다.

## 핵심 내용
### 핵심 방법
- **잔차 학습**: 기대하는 기본 매핑 H(x)를 F(x)+x로 재구성하며, 여기서 F(x)=H(x)-x는 잔차 함수입니다. 순방향 신경망을 통해 F(x)를 구현하고, 항등 매핑 x는 지름길 연결(shortcut connections)을 통해 직접 전달됩니다.
- **지름길 연결 구현**: 입력과 출력 차원이 일치할 때는 직접 더하고, 차원이 일치하지 않을 때는 제로 패딩 또는 1×1 컨볼루션 프로젝션으로 조정합니다. 모든 지름길 연결은 추가 매개변수를 도입하지 않습니다.

### 네트워크 아키텍처
- **ImageNet 기준**: 34층 plain 네트워크와 34층 ResNet을 비교했으며, 후자는 18층을 기반으로 2층마다 잔차 연결을 추가했습니다. 152층 ResNet은 bottleneck 설계(1×1→3×3→1×1 컨볼루션)를 사용하며, 매개변수 수는 VGG-19보다 적습니다.
- **CIFAR-10 실험**: 20층에서 1202층까지의 네트워크를 구축했으며, 3×3 컨볼루션 커널을 사용하고, 특징 맵 크기가 32×32→8×8일 때 채널 수가 두 배로 증가합니다. 1001층 네트워크의 테스트 오류율은 4.62%였지만, 1202층은 과적합으로 인해 오류율이 약간 높았습니다.

### 실험 설정
- **훈련 매개변수**: ImageNet은 무작위 자르기(224×224), 수평 뒤집기, 색상 증강을 사용했으며, SGD 최적화기(batch size=256, momentum=0.9, weight decay=0.0001)를 사용했습니다. 학습률은 0.1에서 시작하여 30 에포크마다 10으로 나누었으며, 총 60만 번 반복했습니다.
- **테스트 전략**: 표준 10-crop 테스트(224×224)를 사용했으며, 6개의 152층 ResNet 모델을 앙상블했습니다.

### 주요 결과
- **ImageNet 분류**: 152층 ResNet 단일 모델의 top-5 오류율은 4.49%, 앙상블 모델은 3.57%였습니다(ILSVRC 2015 우승). VGG-16(7.4%), GoogleNet(6.7%)에 비해 크게 향상되었습니다.
- **깊이 영향**: 34층 ResNet(top-5 오류율 5.71%)은 18층 ResNet(5.91%)보다 우수했지만, plain 네트워크 34층(7.51%)은 18층(5.60%)보다 성능이 낮아, 잔차 학습이 저하를 제거함을 증명했습니다.
- **COCO 검출**: Faster R-CNN 프레임워크를 기반으로 VGG-16을 101층 ResNet으로 교체했을 때, mAP가 21.1%에서 27.0%로 향상되었습니다(상대적 28% 향상).

### 결론
잔차 학습 프레임워크는 네트워크 깊이의 전통적인 한계를 돌파했으며, 시각 작업에서 깊은 표현의 핵심 역할을 검증했습니다. 이 작업은 이후 DenseNet, ResNeXt 등의 아키텍처를 위한 기반을 마련했으며, 컴퓨터 비전을 초심층 네트워크 시대로 이끌었습니다.
