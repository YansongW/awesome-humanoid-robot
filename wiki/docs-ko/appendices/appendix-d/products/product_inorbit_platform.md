# InOrbit 로봇 운영 플랫폼 / InOrbit RobOps Platform

> 본 용어는 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [InOrbit](../companies/company_inorbit.md) |
| **제품 카테고리** | 로봇 운영(RobOps) / 로봇 오케스트레이션 플랫폼 |
| **출시 시간** | 2017년부터 지속적 업데이트 |
| **상태** | 상용 / 무료 버전 + 엔터프라이즈 버전 |
| **공식 사이트/출처** | [InOrbit 공식 사이트](https://inorbit.ai) |

## 제품 개요

InOrbit 로봇 운영 플랫폼은 업계 선도적인 RobOps 솔루션으로, 로봇 개발자와 기업이 이기종 로봇 차량군에서 관측 가능성, 원격 운영, 최적화 및 오케스트레이션을 실현할 수 있도록 지원합니다. 플랫폼은 "4개의 O"를 철학으로 합니다: Observability(관측 가능), Operations(운영), Optimization(최적화), Orchestration(오케스트레이션).

InOrbit는 로봇 독립적인 Agent, 적응형 진단(Adaptive Diagnostics™), 실시간 지도 추적, 원클릭 이벤트 대응, Time Capsule™ 과거 데이터 재생, 그리고 VDA 5050, MassRobotics AMR 상호운용 표준을 지원하는 InOrbit Connect 인증 프로그램을 제공합니다. 2025년 InOrbit는 Space Intelligence를 추가로 출시하여 오케스트레이션 기능을 로봇에서 사람, 수동 차량 및 고정 설비로 확장했습니다.

InOrbit는 Gartner가 2024년 물류 및 로봇 기술 Cool Vendor로 선정했으며, 고객으로는 Colgate-Palmolive, Genentech/Roche 등 대형 기업이 있습니다.

## 제품 이미지

> InOrbit RobOps Platform: [공식 자료](https://inorbit.ai)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 배포 형태 | 퍼블릭 클라우드 SaaS / 프라이빗 배포 | InOrbit 공식 사이트 |
| 접속 방식 | InOrbit Agent / Robot SDK / VDA 5050 | InOrbit 문서 |
| 지원 로봇 유형 | AMR, AGV, 로봇 팔, 서비스 로봇 | 공개 자료 |
| 관측 가능성 | 원격 측정, 지도 위치, 알림, 진단 | InOrbit 문서 |
| 적응형 진단 | Adaptive Diagnostics™ | 공식 자료 |
| 과거 재생 | Time Capsule™ | InOrbit 뉴스 |
| 상호운용 표준 | VDA 5050, MassRobotics AMR | InOrbit 문서 |
| 무료 버전 | 무제한 로봇 Free Edition | Automate.org |
| 가격 | Free / Standard / Developer / Enterprise | InOrbit 공식 사이트 |

## 공급망 위치

- **제조사**: [InOrbit](../companies/company_inorbit.md)
- **핵심 부품/기술 출처**: AWS/Google Cloud 클라우드 인프라, ROS/ROS2, SICK Tag-LOC 등 위치 시스템, VDA 5050 / MassRobotics 상호운용 표준.
- **하위 응용/고객**: Colgate-Palmolive, Genentech/Roche, 물류 3PL, 제조 및 소매 기업.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_inorbit_robops_platform`
- 제조사 엔터티: `ent_company_inorbit`
- 주요 관계:
  - `rel_ent_company_inorbit_manufactures_ent_product_inorbit_robops_platform` (`ent_company_inorbit` → `manufactures` → `ent_product_inorbit_robops_platform`)

## 응용 시나리오

- **다중 브랜드 AMR 혼합 차량군**: 다양한 제조사의 AMR/AGV를 통합 오케스트레이션하여 교통 충돌 방지.
- **창고 내 사람-로봇 혼합 관리**: 규칙 엔진을 통해 사람, 지게차, 로봇에 통행 우선순위 할당.
- **로봇 이상 대응**: 적응형 진단이 자동으로 고장 분류, 원클릭 인계 또는 작업 티켓 트리거.
- **생산 시설 로봇 오케스트레이션**: WMS/ERP/MES와 통합하여 자재 배송 및 생산 라인 협업 구현.

## 경쟁 비교

| 비교 항목 | InOrbit | Formant | Freedom Robotics |
|--------|---------|---------|------------------|
| 포지셔닝 | RobOps 및 로봇 오케스트레이션 | 데이터 및 운영 플랫폼 | 원격 제어 및 차량군 관리 |
| 핵심 강점 | 오케스트레이션, 상호운용 표준, 무료 버전 | 데이터 시각화, 원격 조작 | 빠른 접속, 개발자 친화적 |
| 상호운용 인증 | InOrbit Connect | 비교적 유연 | 비교적 유연 |
| 기업 통합 | WMS/ERP/MES | 타사 통합 | 타사 통합 |
| 타겟 고객 | 대형 기업 혼합 차량군 | 로봇 제조사 + 최종 기업 | 스타트업 로봇 회사 |

## 구매 및 배포 권장 사항

- 다중 브랜드, 다중 시나리오 로봇 차량군을 보유하고 통합 오케스트레이션 및 기업 시스템 통합이 필요한 대형 기업에 적합.
- 무료 버전은 소규모 파일럿에 사용하여 Agent 안정성 및 데이터 시각화 효과를 검증할 수 있음.
- 배포 전 기존 로봇 인터페이스 표준을 정리하고, VDA 5050 또는 InOrbit Robot SDK를 지원하는 장비를 우선 선택하는 것이 좋음.

## 참고 자료

1. [InOrbit 공식 사이트](https://inorbit.ai)
2. [Automate.org – InOrbit Free Edition 출시](https://www.automate.org/news/inorbit-launches-free-edition-to-democratize-robot-operations)
3. [Automate.org – SICK와 InOrbit 협력](https://www.automate.org/news/sick-and-inorbit-ai-achieve-groundbreaking-advances-in-robot-and-facility-operations)
4. [Robotics 247 – InOrbit 시리즈 A 투자 유치](https://www.robotics247.com/article/inorbit.ai_closes_series_a_funding_round_to_scale_robot_orchestration_platform/designer)
