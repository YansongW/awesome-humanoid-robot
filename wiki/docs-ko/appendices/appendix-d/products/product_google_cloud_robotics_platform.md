# Google Cloud Robotics 플랫폼 / Google Cloud Robotics Platform

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Google Cloud Robotics](../companies/company_google_cloud_robotics.md) |
| **제품 카테고리** | 클라우드 로봇 플랫폼 / 로봇-클라우드 연합 오케스트레이션 |
| **출시 시간** | 2018년 발표, 2019년 개발자 프리뷰 |
| **상태** | 오픈소스 코어 + 엔터프라이즈 클라우드 서비스 |
| **공식 사이트/출처** | [Google Cloud Robotics](https://cloud.google.com/solutions/robotics) |

## 제품 개요

Google Cloud Robotics Platform은 Google Cloud가 로봇 개발자와 기업을 위해 출시한 클라우드 로봇 솔루션입니다. 플랫폼은 오픈소스 프로젝트 Cloud Robotics Core를 기반으로 Kubernetes 연합 아키텍처를 통해 로봇과 클라우드를 연결하여 개발자가 클라우드 애플리케이션을 관리하듯 로봇 애플리케이션을 관리할 수 있도록 합니다.

플랫폼은 안전한 양방향 통신, 애플리케이션 패키지 배포, 장치 ID 관리를 제공하며 Vertex AI, Cloud Storage, BigQuery, Cloud Operations Suite 및 Cartographer SLAM 등 Google 서비스와 원활하게 통합됩니다. 설계는 개방성을 강조합니다: 고객이 데이터를 소유하고 필요에 따라 마이그레이션할 수 있으며 핵심 인프라는 오픈소스입니다.

AWS RoboMaker의 관리형 경로와 달리 Google Cloud Robotics는 "플랫폼 + 오픈소스 코어" 모델에 더 가깝고, 높은 수준의 맞춤화, 멀티 클라우드/하이브리드 클라우드 배포 또는 Google AI 기능과의 심층 통합이 필요한 기업에 적합합니다.

## 제품 이미지

> Google Cloud Robotics Platform: [공식 자료](https://cloud.google.com/solutions/robotics)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 배포 형태 | 퍼블릭 클라우드 PaaS / 오픈소스 코어 | Google Cloud 공식 사이트 |
| 오픈소스 코어 | Cloud Robotics Core | GitHub |
| 오케스트레이션 엔진 | Kubernetes / GKE | Google Cloud 문서 |
| 미들웨어 지원 | ROS / ROS2 | Cloud Robotics Core 문서 |
| 통신 프로토콜 | gRPC, MQTT, HTTPS | 공개 자료 |
| AI/ML 서비스 | Vertex AI, AutoML, TensorFlow | Google Cloud 공개 자료 |
| 공간 지능 | Cartographer 2D/3D SLAM | Google 오픈소스 프로젝트 |
| 데이터 서비스 | Cloud Storage, BigQuery | Google Cloud 문서 |
| 가격 | Google Cloud 리소스 사용량 기준 과금 | Google Cloud 가격 페이지 |

## 공급망 위치

- **제조사**: [Google Cloud Robotics](../companies/company_google_cloud_robotics.md)
- **핵심 부품/기술 출처**: Google Cloud 인프라, Kubernetes 생태계, ROS/ROS2, Cartographer, Edge TPU, Vertex AI.
- **하위 애플리케이션/고객**: 산업용 로봇 OEM, AMR 제조사, 시스템 통합업체, 물류 및 제조 기업, 연구 기관.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_google_cloud_robotics_platform`
- 제조사 엔터티: `ent_company_google_cloud_robotics`
- 주요 관계:
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`)

## 적용 시나리오

- **멀티 브랜드 AMR 차량 오케스트레이션**: Kubernetes 애플리케이션 패키지를 통해 다양한 제조사의 로봇 소프트웨어 및 구성을 통합 관리.
- **클라우드 기반 SLAM 및 지도 공유**: Cartographer와 Cloud Storage를 활용한 다중 로봇 지도 업데이트 및 공유.
- **비전-언어-행동 모델**: Vertex AI 및 Gemini API와 결합하여 로봇에 다중 모달 인식 및 추론 기능 제공.
- **산업 디지털 트윈**: Google Cloud 시뮬레이션 및 AI 서비스를 통해 고충실도 디지털 트윈 환경 구축.

## 경쟁 비교

| 비교 항목 | Google Cloud Robotics | AWS RoboMaker | Formant |
|-----------|----------------------|---------------|---------|
| 포지셔닝 | Kubernetes 네이티브 클라우드 로봇 플랫폼 | 엔드투엔드 관리형 클라우드 로봇 서비스 | 로봇 데이터 및 운영 플랫폼 |
| 개방성 | 핵심 오픈소스 | 일부 서비스 점진적 마이그레이션/오픈소스 | 상용 SaaS |
| AI 통합 | Vertex AI / Gemini | SageMaker | 타사 통합 |
| 오케스트레이션 | Kubernetes 연합 | AWS 관리형 서비스 | 플랫폼 내장 |
| 대상 사용자 | DevOps 역량을 갖춘 기업 | 빠른 클라우드 도입을 원하는 개발자 | 운영형 로봇 고객 |

## 구매 및 배포 권장 사항

- Kubernetes/GKE 경험이 있고 클라우드-엣지 협업 아키텍처를 심층 맞춤화하려는 팀에 적합.
- 오픈소스 Cloud Robotics Core는 프라이빗 클라우드 또는 하이브리드 클라우드 배포에 사용 가능하여 벤더 종속 위험 감소.
- 배포 전 장치 인증, 네트워크 정책, 연합 리소스 구성 및 Vertex AI와의 데이터 파이프라인을 계획해야 함.

## 참고 자료

1. [Google Cloud Robotics 공식 사이트](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core 문서](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform 보도](https://www.therobotreport.com/google-cloud-robotics-platform/)
