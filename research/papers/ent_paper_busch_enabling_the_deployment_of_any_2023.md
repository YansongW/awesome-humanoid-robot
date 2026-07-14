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
  zh: 本文提出了基于微服务架构的ROS/ROS 2机器人应用容器化部署流程，并开源了工具套件（docker-ros、docker-ros-ml-images、docker-run），实现ROS包的最小化Docker镜像自动构建、提供机器学习基础镜像并简化容器驱动开发，同时进行了定性比较并在自动驾驶研究车辆上部署验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.06611v3.
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
In an increasingly automated world -- from warehouse robots to self-driving cars -- streamlining the development and deployment process and operations of robotic applications becomes ever more important. Automated DevOps processes and microservice architectures have already proven successful in other domains such as large-scale customer-oriented web services (e.g., Netflix). We recommend to employ similar microservice architectures for the deployment of small- to large-scale robotic applications in order to accelerate development cycles, loosen functional dependence, and improve resiliency and elasticity. In order to facilitate involved DevOps processes, we present and release a tooling suite for automating the development of microservices for robotic applications based on the Robot Operating System (ROS). Our tooling suite covers the automated minimal containerization of ROS applications, a collection of useful machine learning-enabled base container images, as well as a CLI tool for simplified interaction with container images during the development phase. Within the scope of this paper, we embed our tooling suite into the overall context of streamlined robotics deployment and compare it to alternative solutions. We release our tools as open-source software at https://github.com/ika-rwth-aachen/dorotos.

## 核心内容
In an increasingly automated world -- from warehouse robots to self-driving cars -- streamlining the development and deployment process and operations of robotic applications becomes ever more important. Automated DevOps processes and microservice architectures have already proven successful in other domains such as large-scale customer-oriented web services (e.g., Netflix). We recommend to employ similar microservice architectures for the deployment of small- to large-scale robotic applications in order to accelerate development cycles, loosen functional dependence, and improve resiliency and elasticity. In order to facilitate involved DevOps processes, we present and release a tooling suite for automating the development of microservices for robotic applications based on the Robot Operating System (ROS). Our tooling suite covers the automated minimal containerization of ROS applications, a collection of useful machine learning-enabled base container images, as well as a CLI tool for simplified interaction with container images during the development phase. Within the scope of this paper, we embed our tooling suite into the overall context of streamlined robotics deployment and compare it to alternative solutions. We release our tools as open-source software at https://github.com/ika-rwth-aachen/dorotos.

## 参考
- http://arxiv.org/abs/2309.06611v3

