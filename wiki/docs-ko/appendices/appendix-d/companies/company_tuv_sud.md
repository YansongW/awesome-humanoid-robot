# 남독일그룹 / TÜV SÜD

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 남독일그룹 |
| **영문명** | TÜV SÜD |
| **본사** | 독일 뮌헨 |
| **설립 연도** | 1866 |
| **공식 웹사이트** | [https://www.tuvsud.com](https://www.tuvsud.com) |
| **공급망 단계** | 로봇 검사, 안전 인증, CE 마크, 기능 안전 평가 |
| **기업 속성** | 제3자 시험인증 기관(TIC), 상장 기업 |
| **모회사/소속 그룹** | TÜV SÜD AG |
| **데이터 출처** | TÜV SÜD 공식 웹사이트, 로봇 인증 서비스 페이지 |

## 회사 개요

TÜV SÜD는 산업 기계, 자동차, 전기전자 및 의료 기기 분야에서 오랜 역사를 가진 세계 최고의 제3자 시험, 검사 및 인증 기관 중 하나입니다. 로봇 안전 인증 서비스는 산업용 로봇, 협동 로봇, 서비스 로봇 및 휴머노이드 로봇을 포괄하며, 기업이 EU 기계 지침, CE 마크, 기능 안전(ISO 13849 / IEC 61508) 및 시장 진입 요구 사항을 충족하도록 지원합니다.

TÜV SÜD는 전 세계에 여러 시험 연구소를 보유하고 있으며, 위험 평가, 형식 시험, 기술 문서 검토, 현장 심사 및 지속적인 감독 등 원스톱 규정 준수 서비스를 제공하여 로봇 제품이 유럽 및 글로벌 고급 시장에 진출하는 데 중요한 파트너입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 로봇 안전 인증 | CE 마크, 기계 지침 규정 준수 | [TÜV SÜD 로봇 안전 인증](../products/product_tuv_sud_robot_certification.md) | 산업용 로봇, 협동 로봇, 휴머노이드 로봇 |
| 기능 안전 평가 | SIL/PL 평가 및 검증 | ISO 13849 / IEC 61508 서비스 | 로봇 제어 시스템, 안전 부품 |
| 사이버 보안 및 신뢰성 | IoT/로봇 네트워크 위험 평가 | IEC 62443 관련 서비스 | 네트워크 연결 로봇, 서비스 로봇 |

## 대표 제품

### TÜV SÜD 로봇 안전 인증 서비스

> TÜV SÜD 로봇 인증: [공식 자료](https://www.tuvsud.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 서비스 유형 | 제3자 안전 인증, 시험, 심사 | TÜV SÜD 공식 웹사이트 |
| 적용 규정 | EU 기계 지침, CE 마크, UKCA, 기능 안전 | 공개 자료 |
| 적용 표준 | ISO 10218, ISO/TS 15066, ISO 13482, ISO 13849, IEC 61508 | TÜV SÜD |
| 시험 내용 | 위험 평가, 형식 시험, 전자기 적합성, 기술 문서 검토 | 공개 자료 |
| 서비스 기간 | 미공개 | 프로젝트 기준 |
| 인증 마크 | TÜV SÜD 마크, CE 적합성 | TÜV SÜD |
| 가격 | 미공개 | 비즈니스 견적 |

**기술적 강점**: 글로벌 시험 네트워크, 학제 간 안전 전문가, 기계/전기/소프트웨어/사이버 보안 전 체인 커버리지, 연구개발부터 양산까지 규정 준수 폐쇄 루프 지원.

**적용 시나리오**: 산업용 로봇 EU 수출, 협동 로봇 CE 인증, 서비스 로봇 시장 진입, 휴머노이드 로봇 안전 평가 및 형식 시험.

## 공급망 위치

- **상류 핵심 부품/재료**: 표준 문서(ISO/IEC), 시험 장비, 연구소 부지, 인증 자격, 안전 전문가
- **하류 고객/적용 시나리오**: 로봇 OEM, 부품 공급업체, 시스템 통합업체, 수출 무역업체, 규제 기관
- **주요 경쟁사/대상**: SGS, UL Solutions, Intertek, DEKRA, Bureau Veritas

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_tuv_sud`
- 제품 엔티티: `ent_product_tuv_sud_robot_certification`
- 부품 엔티티: `ent_component_tuv_sud_robot_certification_core`
- 주요 관계:
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_product_tuv_sud_robot_certification`
  - `ent_company_tuv_sud` -- `manufactures` --> `ent_component_tuv_sud_robot_certification_core`
  - `ent_product_tuv_sud_robot_certification` -- `uses` --> `ent_component_tuv_sud_robot_certification_core`

## 참고 자료

1. [TÜV SÜD 공식 웹사이트](https://www.tuvsud.com)
2. [TÜV SÜD 제품 인증 서비스](https://www.tuvsud.com/en/services/product-certification)
3. [부록 D 기업 디렉토리](../index-companies.md)
4. 공개 업계 보고서 및 시장 자료
5. 데이터 업데이트 비고: 2026-07-01
