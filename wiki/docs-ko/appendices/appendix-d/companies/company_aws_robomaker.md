# AWS RoboMaker / AWS RoboMaker

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 아마존 웹 서비스 RoboMaker |
| **영문명** | AWS RoboMaker |
| **본사** | 미국 워싱턴주 시애틀 |
| **설립 시간** | 2018년 출시 (2019년 정식 상용화) |
| **공식 사이트** | [https://aws.amazon.com/robomaker](https://aws.amazon.com/robomaker) |
| **공급망 단계** | 클라우드 로봇 플랫폼, 로봇 시뮬레이션, 차량 관리 |
| **기업 속성** | 퍼블릭 클라우드 부문 서비스 |
| **모회사/소속 그룹** | Amazon Web Services (AWS) / Amazon.com Inc. |
| **데이터 출처** | AWS 공식 사이트, AWS RoboMaker 제품 페이지, AWS 블로그 및 공지 |

## 회사 소개

AWS RoboMaker는 Amazon Web Services가 출시한 클라우드 로봇 개발 플랫폼으로, 로봇 개발자에게 클라우드 기반 시뮬레이션, 머신러닝, 차량 관리 및 지속적 통합/지속적 배포(CI/CD) 기능을 제공하는 것을 목표로 합니다.

플랫폼은 Robot Operating System (ROS/ROS2)을 기본적으로 통합하며, 개발자는 클라우드에서 대규모로 Gazebo 시뮬레이션을 실행하고, Amazon SageMaker를 활용하여 모델을 훈련시키며, AWS IoT Greengrass를 통해 모델을 엣지 로봇에 배포할 수 있습니다. RoboMaker는 또한 Small Warehouse World와 같은 샘플 애플리케이션과 월드 파일을 제공하여 AMR, 창고 로봇 및 실외 이동 로봇의 프로토타입 검증을 가속화합니다.

2024년부터 AWS는 RoboMaker의 일부 관리형 기능을 오픈 소스 ROS 생태계와 더 광범위한 AWS 서비스 포트폴리오(예: IoT, SageMaker, SimSpace Weaver)로 점진적으로 이전하고 있으며, 신규 고객에게는 오픈 소스 도구 체인과 AWS 서비스를 기반으로 자체 클라우드 로봇 솔루션을 구축할 것을 권장합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 클라우드 로봇 개발 플랫폼 | 클라우드 기반 ROS/ROS2 개발 및 시뮬레이션 | AWS RoboMaker | AMR, 창고, 서비스 로봇 |
| 시뮬레이션 및 디지털 트윈 | 대규모 병렬 물리 시뮬레이션 | RoboMaker Simulation | 알고리즘 검증, 시나리오 회귀 테스트 |
| 차량 및 엣지 관리 | 로봇 OTA, 모니터링, 작업 스케줄링 | AWS IoT Greengrass + RoboMaker Fleet Management | 현장 배포, 원격 운영 |
| 머신러닝 서비스 | 클라우드 모델 훈련 및 엣지 추론 | Amazon SageMaker + RoboMaker ML | 인식, 내비게이션, 조작 |

## 대표 제품

### AWS RoboMaker 클라우드 로봇 플랫폼

> AWS RoboMaker: [공식 자료](https://aws.amazon.com/robomaker)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / PaaS | AWS 공식 사이트 |
| 지원 미들웨어 | ROS 1 / ROS 2 | AWS RoboMaker 문서 |
| 시뮬레이션 엔진 | Gazebo / Ignition | AWS 공개 자료 |
| 최대 동시 시뮬레이션 | 필요에 따라 확장 (AWS 컴퓨팅 리소스) | AWS 공식 사이트 |
| 엣지 배포 | AWS IoT Greengrass | AWS 문서 |
| ML 훈련 통합 | Amazon SageMaker | AWS 공개 자료 |
| 데이터 스토리지 | Amazon S3, Amazon CloudWatch | AWS 문서 |
| 가격 | 시뮬레이션 시간, 스토리지 및 데이터 전송에 따라 과금 | AWS 가격 페이지 |

**기술 하이라이트**: 클라우드 기반 ROS 개발 환경, 대규모 병렬 시뮬레이션, SageMaker 연동 모델 훈련, Greengrass 엣지 배포, 샘플 창고 월드 및 내비게이션 스택.

**적용 시나리오**: AMR 내비게이션 알고리즘 검증, 창고 로봇 디지털 트윈, 서비스 로봇 원격 모니터링, 로봇 모델 OTA 업데이트.

### AWS IoT Greengrass (로봇 엣지 배포)

> AWS IoT Greengrass: [공식 자료](https://aws.amazon.com/robomaker)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 엣지 런타임 + 클라우드 관리 | AWS 공식 사이트 |
| 지원 프로토콜 | MQTT, HTTP, 로컬 Lambda | AWS 문서 |
| 보안 메커니즘 | 디바이스 인증서, IAM, TLS 암호화 | AWS 공개 자료 |
| 오프라인 실행 | 로컬 컴퓨팅 및 메시지 큐 지원 | AWS 문서 |
| 지원 하드웨어 | ARM / x86 엣지 게이트웨이, NVIDIA Jetson 등 | AWS 공개 자료 |
| 컨테이너 지원 | Docker 호환 | AWS 문서 |
| 가격 | 디바이스 연결 및 메시지에 따라 과금 | AWS 가격 페이지 |

**기술 하이라이트**: 엣지-클라우드 협업, 로컬 Lambda 컴퓨팅, 안전한 OTA, 디바이스 섀도우 및 상태 동기화, RoboMaker 차량 관리 연동.

**적용 시나리오**: 로봇 현장 작업 실행, 오프라인/취약 네트워크 환경에서의 로컬 의사 결정, 공장 라인 엣지 추론, 차량 단위 구성 배포.

## 공급망 위치

- **상류 핵심 부품/소재**: AWS 자체 개발 클라우드 인프라, NVIDIA/Intel 엣지 컴퓨팅 모듈, ROS/ROS2 오픈 소스 생태계, Gazebo 시뮬레이션 엔진.
- **하류 고객/적용 시나리오**: 창고 물류 AMR, 서비스 로봇 제조사, 자율 주행 연구 개발, 교육 및 연구 기관.
- **주요 경쟁사/대상**: Google Cloud Robotics, Microsoft Azure IoT + ROS, Formant, InOrbit, Freedom Robotics.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_aws_robomaker`
- 제품/플랫폼 엔터티: `ent_product_aws_robomaker_cloud`, `ent_product_aws_iot_greengrass`
- 주요 관계:
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`)
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_iot_greengrass` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_iot_greengrass`)

## 참고 자료

1. [AWS RoboMaker 공식 사이트](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker 문서](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass 제품 페이지](https://aws.amazon.com/greengrass/)
4. [AWS 블로그 – RoboMaker 마이그레이션 공지](https://aws.amazon.com/blogs/robotics/)
