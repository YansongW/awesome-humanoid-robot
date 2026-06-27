---
$id: ent_paper_busch_enabling_the_deployment_of_any_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enabling the Deployment of Any-Scale Robotic Applications in Microservice Architectures
    through Automated Containerization
  zh: 通过自动化容器化在微服务架构中实现任意规模机器人应用的部署
  ko: 자동화된 컨테이너화를 통해 마이크로서비스 아키텍처에서 임의 규모의 로봇 애플리케이션 배포 활성화
summary:
  en: This paper proposes a microservice-based containerization workflow for ROS/ROS
    2 robotic applications and releases an open-source tooling suite (docker-ros,
    docker-ros-ml-images, docker-run) that automates minimal Docker image builds,
    supplies ML-enabled base images, and simplifies container-driven development,
    with qualitative comparison and deployment on an automated driving research vehicle.
  zh: 本文提出了基于微服务架构的ROS/ROS 2机器人应用容器化部署流程，并开源了工具套件（docker-ros、docker-ros-ml-images、docker-run），实现ROS包的最小化Docker镜像自动构建、提供机器学习基础镜像并简化容器驱动开发，同时进行了定性比较并在自动驾驶研究车辆上部署验证。
  ko: 본 논문은 ROS/ROS 2 로봇 애플리케이션을 위한 마이크로서비스 기반 컨테이너화 배포 워크플로우를 제안하고, ROS 패키지의 최소 Docker
    이미지 자동 빌드, ML 지원 베이스 이미지 제공, 컨테이너 중심 개발을 단순화하는 오픈소스 도구 모음(docker-ros, docker-ros-ml-images,
    docker-run)을 공개하며, 정성적 비교와 자율주행 연구 차량 배포를 수행한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; requires human review against
    full paper before verification.
sources:
- id: src_001
  type: paper
  title: Enabling the Deployment of Any-Scale Robotic Applications in Microservice
    Architectures through Automated Containerization
  url: https://arxiv.org/abs/2309.06611
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper argues that robotic application deployment—spanning warehouse robots to self-driving cars—can be accelerated by adopting microservice architectures and automated DevOps workflows already proven in large-scale web services. It identifies key obstacles to scalable robotic deployment, including complex dependencies, heterogeneous hardware and software platforms, real-time requirements, and the absence of streamlined ROS deployment tooling. To address these obstacles, the authors present and release an open-source tooling suite comprising docker-ros for automated minimal containerization of ROS/ROS 2 packages, docker-ros-ml-images for machine-learning-enabled base container images, and docker-run for simplified container-driven development.

The authors embed the tooling suite into a broader microservice-based deployment workflow and provide a qualitative feature comparison against alternative ROS CI/CD and containerization solutions. They also report a practical deployment on an automated driving research vehicle, demonstrating the feasibility of the containerized approach in a real robotic system. The tools are released publicly on GitHub (github.com/ika-rwth-aachen/dorotos).

## Key Contributions

- A novel microservice-based workflow for developing and deploying ROS robotic applications using containerization and orchestration.
- An open-source tooling suite (docker-ros, docker-ros-ml-images, docker-run) that automates minimal Docker containerization of ROS packages, provides ML-enabled base images, and offers a CLI for container-driven development.
- A qualitative feature comparison of docker-ros against existing ROS CI/CD and containerization tools, validated through deployment on an automated driving research vehicle.

## Relevance to Humanoid Robotics

Mass production and fleet deployment of humanoid robots requires repeatable, scalable software delivery across heterogeneous compute platforms. The proposed containerized microservice workflow and automated ROS containerization tooling directly address this need by enabling consistent build-test-deploy cycles, over-the-air updates, and orchestrated multi-robot operation. Because humanoid platforms typically integrate perception, planning, control, and interaction software from multiple sources, the decoupling and dependency management offered by containerized microservices is particularly valuable for maintainability and fleet scaling.
