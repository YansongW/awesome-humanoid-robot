# Freedom Robotics / Freedom Robotics

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Freedom Robotics |
| **영문명** | Freedom Robotics |
| **본사** | 미국 캘리포니아주 샌프란시스코 |
| **설립일** | 2018년 |
| **공식 웹사이트** | [https://freedomrobotics.ai](https://freedomrobotics.ai) |
| **공급망 단계** | 로봇 원격 제어, 차량 관리, 소프트웨어 개발 인프라 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Freedom Robotics 공식 웹사이트, The Robot Report, Built In SF |

## 회사 소개

Freedom Robotics는 "로봇 관리 소프트웨어 인프라"를 제공하여 로봇 기업이 로봇 차량을 신속하게 구축, 운영, 지원 및 확장할 수 있도록 돕습니다. 플랫폼은 "한 줄의 코드로 연결 가능"하다는 점으로 유명하며, ROS/ROS2 및 다양한 로봇 SDK를 지원합니다.

핵심 제품인 Mission Control은 실시간 원격 측정 시각화, 원격 제어, 데이터 기록, OTA 업데이트, 차량 관리를 통합된 클라우드-엣지 협업 플랫폼으로 제공합니다. Freedom Robotics는 플랫폼 독립성(platform-agnostic)을 강조하여 기업이 단일 클라우드 공급업체에 완전히 의존하지 않고 로봇을 관리할 수 있도록 합니다.

2019년, Freedom Robotics는 Initialized Capital이 주도하고 Toyota AI Ventures, Liquid 2 Ventures 및 Twitch 공동 창업자 Justin Kan 등이 참여한 660만 달러의 시드 투자를 완료했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 로봇 임무 통제 센터 | 실시간 시각화 및 원격 제어 | Mission Control | 개발 디버깅, 현장 운영 |
| 차량 관리 소프트웨어 | 다중 로봇 상태, 로그, 알림 | Freedom Fleet Management | 대규모 배포 |
| 데이터 수집 및 진단 | 센서 로그, 비디오 재생, 근본 원인 분석 | Freedom Data Logging | 장애 해결, 모델 반복 |
| 로봇 개발 도구 | 클라우드 IDE, CI/CD, OTA | Freedom Dev Tools | 로봇 소프트웨어 개발 |

## 대표 제품

### Freedom Robotics Mission Control

> Freedom Robotics Mission Control: [공식 자료](https://freedomrobotics.ai)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / 프라이빗 배포 | Freedom Robotics 공식 웹사이트 |
| 연결 방식 | 한 명령으로 Freedom Agent 설치 | The Robot Report |
| 지원 미들웨어 | ROS 1 / ROS 2, 사용자 정의 SDK | 공개 자료 |
| 시각화 | 2D/3D 뷰, LiDAR, 주행 거리계, 카메라 | Freedom Robotics 문서 |
| 원격 제어 방식 | 키보드, 게임패드, API | 공개 자료 |
| 데이터 기록 | 센서 로그, 비디오, 원격 측정 동기화 | Freedom Robotics 문서 |
| 차량 규모 | 단일 대부터 수천 대까지 | 공개 자료 |
| 가격 | 장치별 구독 | 공식 문의 |

**기술적 특징**: 분 단위 연결, 통합된 실시간 원격 측정 및 비디오 스트리밍, 원격 안전 인계, 과거 데이터 재생 및 근본 원인 분석, 크로스 플랫폼 호환성.

**적용 시나리오**: 농업 로봇 원격 진단, 창고 AMR 이상 처리, 청소 로봇 차량 모니터링, 로봇 스타트업의 신속한 제품화.

### Freedom Robotics Fleet Management

> Freedom Robotics Fleet Management: [공식 자료](https://freedomrobotics.ai)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 관리 범위 | 장치 상태, 소프트웨어 버전, 구성, 알림 | Freedom Robotics 문서 |
| OTA 업데이트 | 소프트웨어 및 펌웨어 원격 업데이트 지원 | 공개 자료 |
| 권한 관리 | 다중 역할, 다중 팀 접근 제어 | Freedom Robotics 문서 |
| 알림 메커니즘 | 사용자 정의 임계값, Slack/Email/Webhook | 공개 자료 |
| API | REST API 및 SDK | 공개 자료 |
| 가격 | 기업 구독에 포함 | 공식 문의 |

**기술적 특징**: 차량 수준 상태 모니터링, 소프트웨어 버전 일관성 관리, 자동화된 알림 및 워크플로우, Mission Control 데이터 시각화와의 원활한 통합.

**적용 시나리오**: 다중 사이트 로봇 차량 운영, 소프트웨어 버전 단계적 배포, 대규모 장애 대응, 팀 간 협업 및 감사.

## 공급망 위치

- **상류 핵심 부품/재료**: AWS/Google Cloud 클라우드 인프라, ROS/ROS2, 비디오 스트리밍 및 네트워크 전송 기술, 엣지 컴퓨팅 모듈.
- **하류 고객/적용 시나리오**: 농업, 창고, 식음료 자동화, 라스트 마일 물류, 로봇 스타트업.
- **주요 경쟁사/대상**: Formant, InOrbit, AWS RoboMaker, Google Cloud Robotics, Rocos(전신).

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_freedom_robotics`
- 제품/플랫폼 엔터티: `ent_product_freedom_robotics_mission_control`, `ent_product_freedom_robotics_fleet_management`
- 주요 관계:
  - `rel_ent_company_freedom_robotics_manufactures_ent_product_freedom_robotics_mission_control` (`ent_company_freedom_robotics` → `manufactures` → `ent_product_freedom_robotics_mission_control`)
  - `rel_ent_company_freedom_robotics_manufactures_ent_product_freedom_robotics_fleet_management` (`ent_company_freedom_robotics` → `manufactures` → `ent_product_freedom_robotics_fleet_management`)

## 참고 자료

1. [Freedom Robotics 공식 웹사이트](https://freedomrobotics.ai)
2. [The Robot Report – Freedom Robotics 시드 투자](https://www.therobotreport.com/freedom-robotics-raises-seed-funding-robotic-fleet-controls/)
3. [Built In SF – Freedom Robotics 회사 소개](https://www.builtinsf.com/company/freedom-robotics)
4. [Freedom Robotics 블로그 및 문서](https://freedomrobotics.ai/resources)
