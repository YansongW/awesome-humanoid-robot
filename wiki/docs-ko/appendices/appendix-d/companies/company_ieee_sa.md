# IEEE 표준 협회 / IEEE Standards Association (IEEE SA)

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | IEEE 표준 협회 |
| **영문명** | IEEE Standards Association (IEEE SA) |
| **본사** | 미국 뉴저지주 피스카타웨이 |
| **설립일** | 1963 (IEEE 표준 업무는 1960년대까지 거슬러 올라감) |
| **공식 웹사이트** | [https://standards.ieee.org](https://standards.ieee.org) |
| **공급망 단계** | 로봇 표준, 시스템 아키텍처, 윤리적 자율 시스템 표준 |
| **기업 속성** | IEEE 산하 표준 기관, 비영리 전문 기관 |
| **모회사/소속 그룹** | IEEE (Institute of Electrical and Electronics Engineers) |
| **데이터 출처** | IEEE SA 공식 웹사이트, IEEE 표준 데이터베이스 |

## 회사 소개

IEEE SA는 전기, 전자 및 정보 기술 분야의 글로벌 선도 표준 제정 기관으로, IEEE 표준의 전체 수명 주기(입안, 초안 검토, 발행 및 유지보수)를 관리합니다. 로봇 분야에서 IEEE SA는 온톨로지, 상호 운용성, 윤리 및 자율 시스템 관련 표준을 발행했으며, 이는 연구, 산업 및 규제에서 인용되고 있습니다.

IEEE 1872 로봇 온톨로지 표준, IEEE 7000 윤리 설계 프로세스 표준 등은 IEEE가 로봇 분야에서 기여한 핵심 성과입니다. IEEE SA는 Industry Connections 활동을 통해 로봇, 자율 주행 및 인공지능의 교차 분야 표준화를 추진하고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 로봇 온톨로지 및 상호 운용성 표준 | 용어, 온톨로지 및 데이터 교환 규격 | [IEEE 로봇 표준군](../products/product_ieee_sa_robotics_standards.md) | 로봇 연구개발, 시뮬레이션, 지식 베이스 |
| 윤리 및 신뢰 시스템 표준 | 시스템 공학 윤리 위험 처리 | IEEE 7000 시리즈 | 자율 주행, 의료 로봇, 휴머노이드 로봇 |
| 산업 연결 및 가이드 | 사전 표준화 연구 및 구현 가이드 | IEEE Industry Connections 보고서 | 산업 연합, 학술 기관 |

## 대표 제품

### IEEE 로봇 표준군

> IEEE 로봇 표준군: [공식 자료](https://standards.ieee.org)를 방문하여 확인하세요.

| 규격 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 표준 시리즈 | IEEE 1872, IEEE 7000 등 | IEEE SA |
| 핵심 표준 | IEEE 1872-2015, IEEE 7000-2021 | IEEE 표준 데이터베이스 |
| 적용 범위 | 로봇 온톨로지, 시스템 상호 운용성, 윤리 설계 | 공개 자료 |
| 발행 상태 | 현행/지속 유지보수 | IEEE SA |
| 표준 유형 | IEEE 표준, IEEE 가이드/권장 규정 | IEEE |
| 가격 | 미공개 | IEEE 표준 스토어 |
| 인증 속성 | 비강제, 산업 및 규제 참조용 | IEEE SA |

**기술 하이라이트**: 로봇 지식 표현, 온톨로지 모델링 및 윤리 설계 프로세스를 대상으로 하며, 시스템 수준의 안전성, 투명성 및 설명 가능성을 강조합니다.

**적용 시나리오**: 로봇 지식 그래프 구축, 플랫폼 간 상호 운용성, 윤리 위험 평가, 휴머노이드 로봇 행동 설계 규범.

## 공급망 위치

- **상류 핵심 부품/재료**: IEEE 회원 및 기술 전문가, 연구 기관, 기업 워킹 그룹, 학술 성과
- **하류 고객/적용 시나리오**: 로봇 제조사, 자율 주행 기업, 의료 로봇 기업, 연구 기관, 입법 및 규제 기관
- **주요 경쟁사/대상**: ISO/IEC 공동 표준, ANSI/RIA R15.06, OMG 로봇 표준, 각국 국가 표준

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_ieee_sa`
- 제품 엔터티: `ent_product_ieee_sa_robotics_standards`
- 부품 엔터티: `ent_component_ieee_sa_robotics_standards_core`
- 주요 관계:
  - `ent_company_ieee_sa` -- `manufactures` --> `ent_product_ieee_sa_robotics_standards`
  - `ent_company_ieee_sa` -- `manufactures` --> `ent_component_ieee_sa_robotics_standards_core`
  - `ent_product_ieee_sa_robotics_standards` -- `uses` --> `ent_component_ieee_sa_robotics_standards_core`

## 참고 자료

1. [IEEE SA 공식 웹사이트](https://standards.ieee.org)
2. [IEEE 1872-2015 표준 페이지](https://standards.ieee.org/standard/1872-2015.html)
3. [IEEE 7000-2021 표준 페이지](https://standards.ieee.org/standard/7000-2021.html)
4. [부록 D 기업 디렉토리](../index-companies.md)
5. 공개 산업 보고서 및 시장 자료
6. 데이터 업데이트 비고: 2026-07-01
