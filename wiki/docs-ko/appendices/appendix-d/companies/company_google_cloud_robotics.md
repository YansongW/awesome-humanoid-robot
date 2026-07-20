# Google Cloud Robotics / Google Cloud Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Google Cloud Robotics |
| **영문명** | Google Cloud Robotics |
| **본사** | 미국 캘리포니아주 마운틴뷰 |
| **설립 시간** | 2018년 발표, 2019년 개발자 프리뷰 |
| **공식 사이트** | [https://cloud.google.com/solutions/robotics](https://cloud.google.com/solutions/robotics) |
| **공급망 단계** | 클라우드 로봇 플랫폼, 로봇-클라우드 페더레이션 오케스트레이션, AI/ML 서비스 |
| **기업 속성** | 퍼블릭 클라우드 부문 서비스 |
| **모회사/소속 그룹** | Google Cloud / Alphabet Inc. |
| **데이터 출처** | Google Cloud 공식 사이트, Cloud Robotics Core GitHub, The Robot Report |

## 회사 소개

Google Cloud Robotics는 Google Cloud가 로봇 개발자와 기업을 위해 출시한 클라우드 로봇 플랫폼입니다. 핵심 목표는 Kubernetes, Google AI/ML 서비스 및 오픈 소스 ROS 생태계를 활용하여 확장 가능한 로봇 차량 관리 및 자동화 솔루션을 구축하는 것입니다.

이 플랫폼은 Cloud Robotics Core를 핵심 오픈 소스 프로젝트로 사용하여 로봇-클라우드 안전 양방향 통신, 애플리케이션 패키지 관리, 페더레이션 구성 및 Google Cloud 서비스(Vertex AI, BigQuery, Cloud Storage, Cartographer SLAM, TensorFlow)와의 심층 통합을 제공합니다. "객체 지능" 및 "공간 지능" 서비스는 그리핑 계획, 재고 관리 및 동적 환경에서의 로봇 인식을 지원할 수 있습니다.

Google Cloud Robotics의 완전한 상업화 경로는 AWS RoboMaker에 비해 더 조용하지만, 오픈 소스 코어와 Kubernetes 네이티브 아키텍처는 멀티 클라우드/하이브리드 클라우드 배포 및 DevOps 친화적인 로봇 애플리케이션 배포에서 대표성을 가집니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 클라우드 로봇 핵심 플랫폼 | 오픈 소스 로봇-클라우드 페더레이션 프레임워크 | Cloud Robotics Core | 산업 자동화, AMR 차량 |
| AI/ML 서비스 | 객체 인식, 자세 추정, SLAM | Vertex AI + Cartographer | 그리핑, 내비게이션, 디지털 트윈 |
| 로봇 애플리케이션 마켓 | Kubernetes 애플리케이션 패키지 배포 | Cloud Robotics App Management | 다중 브랜드 로봇 통합 |
| 데이터 및 모니터링 | 로그, 모니터링, 알림 | Google Cloud Operations Suite | 원격 운영, 차량 분석 |

## 대표 제품

### Google Cloud Robotics Platform

> Google Cloud Robotics Platform: [공식 자료](https://cloud.google.com/solutions/robotics)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 PaaS / 오픈 소스 코어 | Google Cloud 공식 사이트 |
| 오픈 소스 코어 | Cloud Robotics Core (GitHub) | Google Cloud Robotics GitHub |
| 오케스트레이션 엔진 | Kubernetes / GKE | Google Cloud 문서 |
| 미들웨어 지원 | ROS / ROS2 | Cloud Robotics Core 문서 |
| 통신 프로토콜 | gRPC, MQTT, HTTPS | 공개 자료 |
| AI 서비스 | Vertex AI, AutoML, TensorFlow | Google Cloud 공개 자료 |
| 공간 지능 | Cartographer (2D/3D SLAM) | Google 오픈 소스 프로젝트 |
| 가격 | Google Cloud 리소스 사용량 기준 과금 | Google Cloud 가격 페이지 |

**기술 하이라이트**: Kubernetes 네이티브 로봇 애플리케이션 관리, 안전한 양방향 로봇-클라우드 통신, Vertex AI와 연동된 인식 및 의사 결정, 오픈 소스 Cloud Robotics Core, 이식 가능한 데이터 소유권 모델.

**적용 시나리오**: 다중 브랜드 AMR 차량 오케스트레이션, 산업 디지털 트윈, 클라우드 기반 SLAM 및 지도 공유, Gemini/Vertex AI 기반 로봇 비전-언어-행동 모델.

### Cloud Robotics Core

> Cloud Robotics Core: [공식 자료](https://cloud.google.com/solutions/robotics)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 코드 저장소 | github.com/googlecloudrobotics/core | GitHub |
| 오픈 소스 라이선스 | Apache 2.0 | GitHub |
| 주요 언어 | Go, Bazel, Terraform | GitHub |
| 핵심 기능 | 페더레이션 구성, 애플리케이션 패키지, 안전 통신 | GitHub README |
| 배포 방식 | 클라우드 클러스터 + 로봇 엣지 클러스터 | 문서 |
| 인증 방식 | OAuth / Workload Identity | 문서 |
| 가격 | 오픈 소스 무료; 클라우드 리소스는 Google Cloud 기준 과금 | GitHub / Google Cloud |

**기술 하이라이트**: 선언적 로봇-클라우드 리소스 구성, 애플리케이션 수명 주기 관리, 장치 ID 및 인증서 관리, Google Cloud 서비스와의 통합 인증.

**적용 시나리오**: 기업 프라이빗 클라우드 로봇 플랫폼 구축, 지역 간 로봇 차량 관리, 높은 수준의 맞춤화가 필요한 클라우드-엣지 협업 로봇 시스템.

## 공급망 위치

- **상류 핵심 부품/소재**: Google Cloud 인프라, Kubernetes 생태계, ROS/ROS2, Edge TPU, NVIDIA/Intel 컴퓨팅 플랫폼, 오픈 소스 SLAM/인식 알고리즘.
- **하류 고객/적용 시나리오**: 산업용 로봇 OEM, AMR 제조사, 시스템 통합업체, 물류 및 제조 기업, 연구 기관.
- **주요 경쟁사/대상**: AWS RoboMaker, Microsoft Azure IoT / ROS, Formant, InOrbit, Freedom Robotics.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_google_cloud_robotics`
- 제품/플랫폼 엔터티: `ent_product_google_cloud_robotics_platform`, `ent_product_google_cloud_robotics_core`
- 주요 관계:
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`)
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_core` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_core`)

## 참고 자료

1. [Google Cloud Robotics 공식 사이트](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core 문서](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform 보도](https://www.therobotreport.com/google-cloud-robotics-platform/)
