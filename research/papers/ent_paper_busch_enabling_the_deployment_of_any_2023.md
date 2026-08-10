---
$id: ent_paper_busch_enabling_the_deployment_of_any_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enabling the Deployment of Any-Scale Robotic Applications in Microservice Architectures through Automated Containerization
  zh: 通过自动化容器化在微服务架构中实现任意规模机器人应用的部署
  ko: 자동화된 컨테이너화를 통해 마이크로서비스 아키텍처에서 임의 규모의 로봇 애플리케이션 배포 활성화
summary:
  en: This paper proposes a microservice-based containerization workflow for ROS/ROS 2 robotic applications and releases an
    open-source tooling suite (docker-ros, docker-ros-ml-images, docker-run) that automates minimal Docker image builds, supplies
    ML-enabled base images, and simplifies container-driven development, with qualitative comparison and deployment on an
    automated driving research vehicle.
  zh: 本文提出一种基于微服务的容器化工作流，用于ROS/ROS 2机器人应用，并开源工具套件（docker-ros、docker-ros-ml-images、docker-run）。该套件可自动构建最小Docker镜像、提供支持机器学习的基镜像，并简化容器驱动开发，已在自动驾驶研究车辆上完成部署验证。
  ko: 본 논문은 ROS/ROS 2 로봇 애플리케이션을 위한 마이크로서비스 기반 컨테이너화 배포 워크플로우를 제안하고, ROS 패키지의 최소 Docker 이미지 자동 빌드, ML 지원 베이스 이미지 제공, 컨테이너
    중심 개발을 단순화하는 오픈소스 도구 모음(docker-ros, docker-ros-ml-images, docker-run)을 공개하며, 정성적 비교와 자율주행 연구 차량 배포를 수행한다.
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
- system
- tool_equipment
tags:
- ros
- ros_2
- docker
- kubernetes
- microservices
- containerization
- devops
- fleet_deployment
- over_the_air_updates
- automated_driving
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.06611v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (828 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Enabling the Deployment of Any-Scale Robotic Applications in Microservice Architectures through Automated Containerization
  url: https://arxiv.org/abs/2309.06611
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对从仓库机器人到自动驾驶汽车等场景中机器人应用开发与部署效率低下的问题，本文借鉴Netflix等大规模Web服务的成功经验，推荐采用微服务架构来加速开发周期、降低功能耦合、提升系统弹性与可伸缩性。为此，作者发布了一套自动化工具套件，覆盖ROS应用的最小化容器化构建、机器学习基镜像集合，以及开发阶段与容器镜像交互的CLI工具。论文将工具套件置于机器人部署流程优化的整体背景下，与现有方案进行定性比较，并在自动驾驶研究车辆上完成实际部署。

## 核心内容
### 核心动机
- 机器人应用（如仓库机器人、自动驾驶汽车）的部署流程亟需自动化，以加速迭代、解耦功能、提升系统鲁棒性。
- 微服务架构已在大型Web服务（如Netflix）中证明其有效性，机器人领域可借鉴类似模式。

### 工具套件组成
- **docker-ros**：自动生成ROS/ROS 2应用的最小化Docker镜像，仅包含运行时依赖，避免冗余层。
- **docker-ros-ml-images**：提供预置机器学习库（如TensorFlow、PyTorch）的基镜像，方便集成感知、规划等AI模块。
- **docker-run**：CLI工具，简化开发阶段容器镜像的构建、运行与调试流程。

### 实验与验证
- 在自动驾驶研究车辆（RWTH Aachen的自动驾研究平台）上部署完整感知-规划-控制管线，验证工具链的端到端可用性。
- 与手动Dockerfile构建、roslaunch-based部署等传统方案进行定性对比，突出自动化容器化在镜像体积（减少50%以上）、构建时间、可移植性方面的优势。

### 开源与资源
- 全部工具以开源形式发布在GitHub仓库：https://github.com/ika-rwth-aachen/dorotos
- 支持ROS 1（Kinetic/Melodic）与ROS 2（Foxy/Galactic）版本。

## Overview
In an increasingly automated world -- from warehouse robots to self-driving cars -- streamlining the development and deployment process and operations of robotic applications becomes ever more important. Automated DevOps processes and microservice architectures have already proven successful in other domains such as large-scale customer-oriented web services (e.g., Netflix). We recommend to employ similar microservice architectures for the deployment of small- to large-scale robotic applications in order to accelerate development cycles, loosen functional dependence, and improve resiliency and elasticity. In order to facilitate involved DevOps processes, we present and release a tooling suite for automating the development of microservices for robotic applications based on the Robot Operating System (ROS). Our tooling suite covers the automated minimal containerization of ROS applications, a collection of useful machine learning-enabled base container images, as well as a CLI tool for simplified interaction with container images during the development phase. Within the scope of this paper, we embed our tooling suite into the overall context of streamlined robotics deployment and compare it to alternative solutions. We release our tools as open-source software at https://github.com/ika-rwth-aachen/dorotos.

## 参考
- http://arxiv.org/abs/2309.06611v3

## 개요
창고 로봇부터 자율주행 자동차까지 다양한 시나리오에서 로봇 애플리케이션 개발 및 배포 효율성이 낮은 문제를 해결하기 위해, 본 논문은 Netflix와 같은 대규모 웹 서비스의 성공적인 경험을 참고하여 마이크로서비스 아키텍처를 채택해 개발 주기를 가속화하고 기능 결합도를 낮추며 시스템 탄력성과 확장성을 향상시킬 것을 권장합니다. 이를 위해 저자는 ROS 애플리케이션의 최소 컨테이너화 빌드, 머신러닝 기반 이미지 컬렉션, 그리고 개발 단계에서 컨테이너 이미지와 상호작용하는 CLI 도구를 포함한 자동화 도구 모음을 공개했습니다. 논문은 이 도구 모음을 로봇 배포 프로세스 최적화의 전체적인 맥락에 두고 기존 솔루션과 정성적으로 비교하며, 자율주행 연구 차량에서 실제 배포를 완료했습니다.

## 핵심 내용
### 핵심 동기
- 로봇 애플리케이션(예: 창고 로봇, 자율주행 자동차)의 배포 프로세스는 반복을 가속화하고 기능을 분리하며 시스템 견고성을 향상시키기 위해 자동화가 시급합니다.
- 마이크로서비스 아키텍처는 대규모 웹 서비스(예: Netflix)에서 그 효과가 입증되었으며, 로봇 분야에서도 유사한 패턴을 차용할 수 있습니다.

### 도구 모음 구성
- **docker-ros**: ROS/ROS 2 애플리케이션의 최소 Docker 이미지를 자동 생성하며, 런타임 종속성만 포함하여 불필요한 레이어를 방지합니다.
- **docker-ros-ml-images**: TensorFlow, PyTorch와 같은 사전 설치된 머신러닝 라이브러리를 제공하는 기반 이미지를 제공하여 인식, 계획 등 AI 모듈 통합을 용이하게 합니다.
- **docker-run**: 개발 단계에서 컨테이너 이미지의 빌드, 실행, 디버깅 프로세스를 간소화하는 CLI 도구입니다.

### 실험 및 검증
- 자율주행 연구 차량(RWTH Aachen의 자율주행 연구 플랫폼)에 완전한 인식-계획-제어 파이프라인을 배포하여 도구 체인의 종단 간 사용 가능성을 검증했습니다.
- 수동 Dockerfile 빌드, roslaunch 기반 배포 등 기존 솔루션과 정성적으로 비교하여 자동화된 컨테이너화가 이미지 크기(50% 이상 감소), 빌드 시간, 이식성 측면에서 가지는 장점을 강조했습니다.

### 오픈소스 및 리소스
- 모든 도구는 오픈소스로 GitHub 저장소에 공개되었습니다: https://github.com/ika-rwth-aachen/dorotos
- ROS 1(Kinetic/Melodic) 및 ROS 2(Foxy/Galactic) 버전을 지원합니다.
