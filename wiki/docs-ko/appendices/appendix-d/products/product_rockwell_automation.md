# 록웰 오토메이션 Integrated Architecture / ControlLogix

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [록웰 오토메이션 / Rockwell Automation, Inc.](../companies/company_rockwell.md) |
| **제품 카테고리** | 프로그래머블 자동화 컨트롤러 / 산업 자동화 플랫폼 |
| **출시일** | 미공개 |
| **상태** | 출시/상용 |
| **공식 홈페이지/출처** | [https://www.rockwellautomation.com](https://www.rockwellautomation.com) |

## 제품 개요

ControlLogix 5580은 록웰 오토메이션 Integrated Architecture 플랫폼의 핵심 PAC로, 통합 Logix 제어 엔진을 사용하여 표준, 안전, 모션 및 프로세스 제어를 통합합니다.

## 제품 이미지

> ControlLogix 5580: [공식 자료](https://www.rockwellautomation.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 컨트롤러 유형 | 프로그래머블 자동화 컨트롤러 (PAC) | Rockwell 공식 홈페이지 |
| 프로세서 | 미공개 | Rockwell 공식 홈페이지 |
| I/O 확장 | 모듈식, 로컬 및 분산 I/O 지원 | Rockwell 공식 홈페이지 |
| 통신 프로토콜 | EtherNet/IP, ControlNet, DeviceNet | Rockwell 공식 홈페이지 |
| 프로그래밍 환경 | Studio 5000 Logix Designer | Rockwell 공식 홈페이지 |
| 보호 등급 | IP20 (제어 캐비닛 내) | Rockwell 공식 홈페이지 |
| 설치 방식 | DIN 레일 / 패널 설치 | Rockwell 공식 홈페이지 |
| 가격 | 미공개 | 견적 문의 필요 |

## 공급망 위치

- **제조사**: [록웰 오토메이션 / Rockwell Automation, Inc.](../companies/company_rockwell.md)
- **핵심 부품/기술 출처**: 자체 개발 Logix 제어 엔진 및 FactoryTalk 소프트웨어; 외부 조달 반도체 칩, PCB, 커넥터, 전원 모듈.
- **하위 응용/고객**: 자동차 OEM, 소비재, 생명 과학, 석유 및 가스, 자동화 시스템 통합업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_rockwell_automation`
- 제조사 엔터티: `ent_company_rockwell`
- 주요 관계:
  - `rel_ent_company_rockwell_manufactures_ent_product_rockwell_automation` (`ent_company_rockwell` → `manufactures` → `ent_product_rockwell_automation`)

## 응용 시나리오

- **생산 라인 제어, 로봇 셀 통합, 휴머노이드 로봇 테스트 및 조립 라인, 디지털 팩토리 MES/OT 융합.**
- **상업 서비스**: 안내, 접객, 전시 및 브랜드 상호작용에 사용.
- **산업 제조**: 유연 생산 라인에서 운반, 조립, 검사 등의 작업 수행.
- **연구 및 교육**: 로봇 제어, AI 훈련 및 임베디드 인텔리전스 연구를 위한 하드웨어 플랫폼으로 활용.

## 확장 및 생태계

- 제조사는 공식 SDK, 시뮬레이션 도구 및 애프터서비스 교육을 제공하며, 구체적인 세부 사항은 공식 채널을 통해 확인해야 합니다.
- 주요 MES/WMS/PLC 시스템과 연동 가능하지만, 인터페이스 프로토콜은 공식 문서를 기준으로 해야 합니다.
- 배포 전 시나리오 기반 검증 및 호환성 테스트를 권장합니다.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 |
|--------|--------|----------|
| 포지셔닝 | 미공개 | 유사 제품은 특정 시나리오에 따라 다름 |
| 핵심 장점 | 통합 Logix 제어 엔진, 표준, 안전, 모션 및 프로세스 제어 통합; EtherNet/IP를 통해 로봇, 서보 및 정보화 시스템과의 원활한 연결 구현. | 미공개 |
| 가격 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

- 공식 채널을 통해 최신 소프트웨어 버전, SDK 지원 및 애프터서비스 교육을 확인하는 것이 좋습니다.
- 연구 및 교육 사용자는 2차 개발 인터페이스, 시뮬레이션 플랫폼 호환성 및 커뮤니티 활동성을 우선 평가해야 합니다.
- 산업 사용자는 특정 공정에 따라 부하, 정밀도, 보호 등급 및 통합 인터페이스를 검증해야 합니다.

## 참고 자료

1. [ControlLogix 5580 제품 페이지](https://www.rockwellautomation.com/en-us/products/hardware/allen-bradley/controllers/programmable-automation-controllers.html)
2. [록웰 오토메이션 공식 홈페이지](https://www.rockwellautomation.com)
3. [공개 자료 및 업계 보고서](https://www.rockwellautomation.com)
