# Formant / Formant

> 이 용어는 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Formant |
| **영문명** | Formant |
| **본사** | 미국 캘리포니아주 샌프란시스코 |
| **설립일** | 2017년 |
| **공식 웹사이트** | [https://formant.io](https://formant.io) |
| **공급망 단계** | 로봇 데이터 플랫폼, 원격 운영, 차량 관리, 원격 조작 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Formant 공식 웹사이트, BMW i Ventures 투자 뉴스, The Robot Report |

## 회사 소개

Formant는 로봇 운영(Robot Operations, RobOps)에 특화된 클라우드 컴퓨팅 회사로, 로봇 개발자와 최종 기업에 통합 데이터, 모니터링, 분석 및 원격 운영 플랫폼을 제공합니다.

플랫폼은 ROS/ROS2 및 모든 로봇 SDK를 지원하며, 단일 명령 또는 경량 Agent를 통해 로봇을 클라우드에 연결할 수 있습니다. Formant는 실시간 원격 측정 시각화, 알림, 데이터 기록, 원격 제어(teleoperation), 작업 스케줄링 및 차량 단위 분석을 제공하여 기업이 더 적은 엔지니어링 리소스로 대규모 배포를 실현할 수 있도록 지원합니다. 고객은 농업, 창고, 순찰, 청소 및 제조 등 여러 분야에 걸쳐 있습니다.

Formant는 2022년 1,800만 달러의 시리즈 A 투자를 유치했으며, 2024년에는 BMW i Ventures가 주도하는 2,100만 달러의 투자를 추가로 유치하여 차량 운영 및 데이터 플랫폼 역량을 더욱 확장했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| 로봇 데이터 플랫폼 | 실시간 원격 측정, 로그, 시각화 | Formant Observe | 차량 모니터링, 장애 진단 |
| 원격 운영 플랫폼 | 저지연 원격 조작 및 인간-로봇 협업 | Formant Operate | 이상 상황 개입, 복잡한 환경 제어 |
| 데이터 분석 플랫폼 | 차량 단위 인사이트 및 KPI | Formant Analyze | 운영 최적화, ROI 보고서 |
| 애플리케이션 구축 프레임워크 | 화이트 라벨/맞춤형 로봇 애플리케이션 | Formant Platform SDK | 다중 브랜드 차량 통합 |

## 대표 제품

### Formant 데이터 및 운영 플랫폼

> Formant Platform: [공식 자료](https://formant.io)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / 프라이빗 배포 | Formant 공식 웹사이트 |
| 연결 방식 | Formant Agent (단일 명령 설치) | Formant 문서 |
| 지원 미들웨어 | ROS 1 / ROS 2, MQTT, REST API | 공개 자료 |
| 데이터 유형 | 원격 측정, 로그, 비디오, 포인트 클라우드, 지도 | Formant 문서 |
| 원격 조작 지연 시간 | 미공개 (네트워크 및 에지 에이전트에 따라 다름) | - |
| 차량 규모 | 수천 대 로봇 지원 | BMW i Ventures 뉴스 |
| 보안 규정 준수 | SOC 2, GDPR, 암호화 전송 | Formant 공식 웹사이트 |
| 가격 | 장치/데이터량 기준 구독 | 공식 문의 |

**기술적 강점**: 즉시 사용 가능한 로봇 데이터 시각화, 로우 코드 알림 및 자동화 워크플로우, 브랜드 간 차량 통합 관리, 원격 제어 및 원클릭 인계, PickNik MoveIt 등 생태계와의 통합.

**적용 시나리오**: AMR 창고 차량 모니터링, 농업 로봇 원격 진단, 순찰 로봇 이상 상황 인계, 청소 서비스 로봇 대규모 운영.

### Formant Teleoperation

> Formant Teleoperation: [공식 자료](https://formant.io)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 제어 방식 | 키보드, 게임패드, 터치스크린, 맞춤형 API | Formant 문서 |
| 비디오 스트림 | 다중 카메라 실시간 전송 | 공개 자료 |
| 지도 및 내비게이션 | 2D/3D 지도 오버레이, 목표 지점 클릭 내비게이션 | Formant 문서 |
| 보안 메커니즘 | 긴급 정지, 권한 관리, 감사 로그 | 공개 자료 |
| 네트워크 적응성 | 약한 네트워크/네트워크 끊김 재연결, 에지 캐싱 | Formant 문서 |
| 가격 | 기업 구독에 포함 | 공식 문의 |

**기술적 강점**: 브라우저 기반 저지연 원격 제어, 다중 카메라 및 센서 융합 뷰, Formant 데이터 플랫폼과의 기본 연동, 권한 등급 및 운영 감사.

**적용 시나리오**: 창고 혼잡 상황에서의 수동 인계, 야외 순찰 이상 상황 처리, 반자율 로봇의 원격 지원 작업, 신규 직원 교육 및 로봇 시연.

## 공급망 위치

- **상류 핵심 부품/소재**: AWS/Google Cloud/Azure 클라우드 인프라, 에지 컴퓨팅 모듈, ROS/ROS2, 비디오 코덱 및 네트워크 전송 기술.
- **하류 고객/적용 시나리오**: SoftBank Robotics, BP, Blue River Technology (John Deere), Burro, Knightscope, Scythe 등 로봇 제조사 및 최종 기업.
- **주요 경쟁사/대상**: InOrbit, Freedom Robotics, AWS RoboMaker, Google Cloud Robotics, Boston Dynamics Orbit.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_formant`
- 제품/플랫폼 엔터티: `ent_product_formant_platform`, `ent_product_formant_teleoperation`
- 주요 관계:
  - `rel_ent_company_formant_manufactures_ent_product_formant_platform` (`ent_company_formant` → `manufactures` → `ent_product_formant_platform`)
  - `rel_ent_company_formant_manufactures_ent_product_formant_teleoperation` (`ent_company_formant` → `manufactures` → `ent_product_formant_teleoperation`)

## 참고 자료

1. [Formant 공식 웹사이트](https://formant.io)
2. [BMW i Ventures – Formant 투자 뉴스](https://www.bmwiventures.com/news/operationalizing-robot-fleets-at-scale-our-lead-investment-in-formant)
3. [The Robot Report – Formant와 SoftBank 협력](https://www.therobotreport.com/formants-data-platform-comes-to-softbanks-cleaning-robots/)
4. [SignalFire – Formant 투자 블로그](https://www.signalfire.com/blog/formant-robotics-investor)
