# AWS RoboMaker 클라우드 로보틱스 플랫폼 / AWS RoboMaker Cloud Robotics Platform

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 파라미터는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [AWS RoboMaker](../companies/company_aws_robomaker.md) |
| **제품 카테고리** | 클라우드 로보틱스 개발 / 시뮬레이션 / 차량 관리 플랫폼 |
| **출시일** | 2018년 출시, 2019년 정식 상용화 |
| **상태** | 점진적으로 오픈소스 및 AWS 서비스 조합으로 이전 중 |
| **공식 사이트/출처** | [AWS RoboMaker 공식 사이트](https://aws.amazon.com/robomaker) |

## 제품 개요

AWS RoboMaker는 Amazon Web Services가 제공하는 엔드투엔드 클라우드 로보틱스 플랫폼으로, 개발자가 클라우드에서 로봇 애플리케이션을 개발, 시뮬레이션, 테스트 및 배포할 수 있도록 지원합니다. 플랫폼은 ROS/ROS2를 기본적으로 통합하며, AWS IoT Greengrass, Amazon SageMaker, Amazon S3, Amazon CloudWatch 등 AWS 서비스와 깊이 연결됩니다.

RoboMaker의 핵심 가치는 기존의 로컬 로봇 개발 환경을 확장 가능한 클라우드로 이전하는 데 있습니다. 개발자는 병렬 시뮬레이션에서 수천 번의 시나리오 회귀 테스트를 실행하고, SageMaker를 통해 인식 및 내비게이션 모델을 훈련한 후, Greengrass를 통해 모델을 엣지 로봇에 안전하게 푸시할 수 있습니다. 또한 플랫폼은 Small Warehouse World 등 예제 시나리오를 제공하여 AMR 및 창고 로봇의 빠른 프로토타입 검증을 지원합니다.

2024년부터 AWS는 신규 사용자에게 오픈소스 ROS 툴체인과 AWS 서비스를 결합하여 클라우드 로보틱스 솔루션을 구축할 것을 권장하며, RoboMaker의 일부 관리형 기능은 이전되었거나 오픈소스화되었습니다.

## 제품 이미지

> AWS RoboMaker Cloud: [공식 자료](https://aws.amazon.com/robomaker)를 방문하여 확인하세요.

## 사양 파라미터 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / PaaS | AWS 공식 사이트 |
| 지원 미들웨어 | ROS 1 / ROS 2 | AWS 문서 |
| 시뮬레이션 엔진 | Gazebo / Ignition | AWS 공개 자료 |
| 동시 시뮬레이션 | 온디맨드 확장 (EC2/SimSpace Weaver) | AWS 문서 |
| 엣지 배포 | AWS IoT Greengrass | AWS 문서 |
| ML 훈련 | Amazon SageMaker | AWS 공개 자료 |
| 데이터 저장 | Amazon S3, CloudWatch Logs | AWS 문서 |
| 네트워크 | VPC, IAM, TLS 암호화 | AWS 문서 |
| 가격 | 시뮬레이션 시간, 스토리지 및 트래픽 기준 과금 | AWS 가격 페이지 |

## 공급망 위치

- **제조사**: [AWS RoboMaker](../companies/company_aws_robomaker.md)
- **핵심 부품/기술 출처**: AWS 클라우드 인프라, NVIDIA/Intel 엣지 컴퓨팅 플랫폼, ROS/ROS2 오픈소스 생태계, Gazebo 시뮬레이션 엔진, SageMaker ML 프레임워크.
- **하위 응용/고객**: AMR 제조사, 창고 물류 로봇, 서비스 로봇, 자율주행 연구개발, 대학 및 연구 기관.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_aws_robomaker_cloud`
- 제조사 엔터티: `ent_company_aws_robomaker`
- 주요 관계:
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`)

## 응용 시나리오

- **AMR 내비게이션 알고리즘 검증**: Small Warehouse World 등 시뮬레이션 환경에서 SLAM, 경로 계획 및 장애물 회피 테스트.
- **디지털 트윈 및 시나리오 회귀**: 수천 번의 시뮬레이션을 병렬 실행하여 소프트웨어 업데이트가 로봇 동작에 미치는 영향 검증.
- **클라우드 모델 훈련**: SageMaker를 활용한 객체 탐지, 의미론적 분할 또는 강화 학습 정책 모델 훈련.
- **엣지 OTA 배포**: Greengrass를 통해 업데이트된 모델과 소프트웨어를 물리적 로봇에 안전하게 전달.

## 경쟁 비교

| 비교 항목 | AWS RoboMaker | Google Cloud Robotics | Microsoft Azure IoT + ROS |
|--------|---------------|----------------------|---------------------------|
| 포지셔닝 | 엔드투엔드 클라우드 로보틱스 플랫폼 | Kubernetes 네이티브 클라우드 로보틱스 프레임워크 | 엔터프라이즈 IoT 및 ROS 통합 |
| 시뮬레이션 | Gazebo 관리형 시뮬레이션 | 자체 개발/타사 시뮬레이션 통합 | 타사 시뮬레이션 통합 |
| 미들웨어 | ROS/ROS2 | ROS/ROS2 | ROS/ROS2 |
| 엣지 | AWS IoT Greengrass | Cloud Robotics Core | Azure IoT Edge |
| 비즈니스 모델 | 사용량 기반 과금 | 오픈소스 + 클라우드 리소스 과금 | 클라우드 리소스 기반 과금 |

## 구매 및 배포 권장 사항

- 신규 사용자는 단일 관리형 서비스에 대한 의존도를 낮추기 위해 오픈소스 ROS + AWS 서비스 조합을 직접 사용할지 평가해야 합니다.
- 대규모 시뮬레이션 요구 사항은 SimSpace Weaver 또는 자체 관리 EC2 클러스터를 결합하여 비용을 최적화할 수 있습니다.
- 배포 전 VPC, IAM 권한, Greengrass 디바이스 인증서 및 OTA 파이프라인을 계획해야 합니다.

## 참고 자료

1. [AWS RoboMaker 공식 사이트](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker 개발자 가이드](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass 제품 페이지](https://aws.amazon.com/greengrass/)
4. [AWS 로봇 블로그](https://aws.amazon.com/blogs/robotics/)
