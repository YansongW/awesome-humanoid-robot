# UL Solutions(미국 보험사 연구소)

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | UL Solutions(미국 보험사 연구소) |
| **영문명** | UL Solutions LLC |
| **본사** | 미국 일리노이주 노스브룩 |
| **설립 연도** | 1894 |
| **공식 사이트** | [https://www.ul.com](https://www.ul.com) |
| **공급망 단계** | 로봇 안전 표준, 안전 인증, 북미 시장 진입 |
| **기업 속성** | 제3자 안전 인증 기관(NRTL), 상장 기업 |
| **모회사/소속 그룹** | UL Solutions LLC(NYSE: UL) |
| **데이터 출처** | UL 공식 사이트, UL 1740 표준 페이지, 로봇 안전 인증 서비스 페이지 |

## 회사 소개

UL Solutions는 세계적으로 유명한 독립 안전 과학 회사로, UL 마크는 북미 시장에서 높은 신뢰도를 가지고 있습니다. 이 회사는 UL 1740《산업용 로봇 안전 표준》을 제정 및 발표하며, 산업용 로봇, 협동 로봇 및 인간형 로봇에 대한 안전 평가, 테스트, 인증 및 지속적인 감독 서비스를 제공합니다.

UL Solutions는 미국 OSHA 국가 인정 시험소(NRTL) 체계에서 중요한 위치를 차지하며, 그 인증 결과는 미국, 캐나다 및 많은 라틴 아메리카, 아시아 태평양 국가에서 인정받아 로봇 제품이 북미 시장에 진입하기 위한 핵심 규정 준수 통로입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 로봇 안전 표준 | 북미 산업용 로봇 안전 요구 사항 | [UL 1740 산업용 로봇 안전 표준](../products/product_ul_solutions_ul_1740.md) | 산업용 로봇, 협동 로봇, 인간형 로봇 |
| 안전 인증 서비스 | NRTL 안전 인증 | UL 마크 인증 서비스 | 전자 전기, 로봇, 산업 장비 |
| 기능 안전 및 사이버 보안 | 제어 시스템 및 네트워크 연결 안전 평가 | UL 기능 안전 서비스, IEC 62443 서비스 | 로봇 컨트롤러, IoT 장치 |

## 대표 제품

### UL 1740 산업용 로봇 안전 표준

> UL 1740: [공식 자료](https://www.ul.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 표준 번호 | UL 1740 | UL Solutions |
| 표준 명칭 | Standard for Safety for Industrial Robots | UL 표준 카탈로그 |
| 적용 범위 | 산업용 로봇, 로봇 시스템, 협동 응용 | UL 1740 |
| 발행 상태 | 현행/지속 유지 | UL 표준 카탈로그 |
| 대응 표준 | ANSI/RIA R15.06, ISO 10218 | 공개 자료 |
| 인증 속성 | 북미 시장 진입 및 보험 근거로 사용 가능 | UL Solutions |
| 가격 | 미공개 | UL 표준 스토어 |

**기술적 특징**: 북미 시장에서 높은 인정을 받는 로봇 안전 표준으로, 위험 평가, 안전 기능, 전기 및 기계적 보호를 강조하며 ANSI/RIA R15.06과 조화를 이룹니다.

**적용 시나리오**: 산업용 로봇 북미 판매, 자동차/전자 제조 라인, 협동 로봇 작업 셀, 인간형 로봇 산업 현장 규정 준수.

## 공급망 위치

- **상류 핵심 부품/재료**: ANSI/RIA 표준 입력, 테스트 장비, NRTL 자격, 안전 엔지니어, 사고 데이터
- **하류 고객/적용 시나리오**: 북미 로봇 OEM, 시스템 통합업체, 수입업체, 보험사, 규제 기관
- **주요 경쟁사/대상**: TÜV SÜD, SGS, Intertek, CSA Group, ETL(Intertek)

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_ul_solutions`
- 제품 엔터티: `ent_product_ul_solutions_ul_1740`
- 부품 엔터티: `ent_component_ul_solutions_ul_1740_core`
- 주요 관계:
  - `ent_company_ul_solutions` -- `manufactures` --> `ent_product_ul_solutions_ul_1740`
  - `ent_company_ul_solutions` -- `manufactures` --> `ent_component_ul_solutions_ul_1740_core`
  - `ent_product_ul_solutions_ul_1740` -- `uses` --> `ent_component_ul_solutions_ul_1740_core`

## 참고 자료

1. [UL Solutions 공식 사이트](https://www.ul.com)
2. [UL Product iQ](https://www.ul.com/piq)
3. [부록 D 기업 디렉토리](../index-companies.md)
4. 공개 업계 보고서 및 시장 자료
5. 데이터 업데이트 비고: 2026-07-01
