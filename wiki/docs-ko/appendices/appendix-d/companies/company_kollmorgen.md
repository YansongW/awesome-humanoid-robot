---
id: ent_company_kollmorgen
schema_version: 1
type: company
title: Kollmorgen
domain: 02_components
theoretical_depth: system
names:
  zh: Kollmorgen
  en: Kollmorgen
status: active
sources:
  - id: src_kollmorgen_official
    type: website
    title: Kollmorgen 공식 웹사이트
    url: https://www.kollmorgen.com
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# Kollmorgen / Kollmorgen

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Kollmorgen |
| **영문명** | Kollmorgen |
| **본사** | 미국 Radford, Virginia |
| **설립 연도** | 1916 |
| **공식 웹사이트** | [https://www.kollmorgen.com](https://www.kollmorgen.com) |
| **공급망 단계** | 서보 모터 / 프레임리스 토크 모터 / 모션 컨트롤 |
| **기업 속성** | 외국계 브랜드, Regal Rexnord 산하 |
| **모회사/소속 그룹** | Regal Rexnord |
| **데이터 출처** | 공식 웹사이트, 제품 매뉴얼, 공개 연구 보고서, WAIC 2026 보도 |

## 회사 소개

글로벌 모션 컨트롤 분야 선도 브랜드로, TBM/KBM 프레임리스 토크 모터는 로봇 관절 및 정밀 회전 테이블에 널리 사용됩니다.

Kollmorgen은 프레임리스 토크 모터, 서보 모터, 드라이버 및 모션 컨트롤러를 제공합니다. TBM2G 시리즈는 협동 로봇 및 휴머노이드 로봇 관절용으로 설계되었으며, 낮은 코깅, 높은 토크 밀도 및 48V 이하 저전압 작동 기능을 갖추고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| TBM2G 프레임리스 모터 | 차세대 로봇 관절 모터 | TBM2G-050 / TBM2G-115 | 협동/휴머노이드 로봇 관절 |
| AKM 서보 모터 | 고성능 서보 모터 | AKM24 / AKM32 | 산업 자동화, CNC |

## 대표 제품

### TBM2G-050 프레임리스 모터 / TBM2G-050 Frameless Motor

> TBM2G-050 프레임리스 모터: [공식 자료](https://www.kollmorgen.com)를 방문하여 확인하십시오.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 외경 | 50 mm | Kollmorgen / INMOCO |
| 무게 | 미공개 | - |
| 연속 토크 | 0.27 N·m | INMOCO 2022 |
| 정격 속도 | 8000 rpm | INMOCO 2022 |
| 출력 전력 | 0.205 kW | INMOCO 2022 |
| 전압 | ≤ 48 VDC | Kollmorgen |
| 피드백 | 선택적 통합 Hall 센서 | Kollmorgen |
| 모터 상수 | 0.061 N·m/√W | INMOCO 2022 |

**기술적 특징**: 3–15 kg 협동 로봇용으로 설계, 낮은 코깅, 높은 응답성, 하모닉 드라이브 감속기 치수에 적합.

**적용 분야**: 협동 로봇 관절, 휴머노이드 로봇 팔/손목, 정밀 회전 테이블.

### TBM2G-115 프레임리스 모터 / TBM2G-115 Frameless Motor

> TBM2G-115 프레임리스 모터: [공식 자료](https://www.kollmorgen.com)를 방문하여 확인하십시오.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 외경 | 115 mm | Kollmorgen / INMOCO |
| 무게 | 미공개 | - |
| 연속 토크 | 6.03 N·m | INMOCO 2022 |
| 정격 속도 | 3100 rpm | INMOCO 2022 |
| 출력 전력 | 1.43 kW | INMOCO 2022 |
| 전압 | ≤ 48 VDC | Kollmorgen |
| 피드백 | 선택적 통합 Hall 센서 | Kollmorgen |
| 모터 상수 | 0.802 N·m/√W | INMOCO 2022 |

**기술적 특징**: 고토크 프레임리스 모터, 로봇 어깨/엉덩이 관절에 직접 내장 가능, 고부하 동적 운동 지원.

**적용 분야**: 산업용 로봇 대형 관절, 휴머노이드 로봇 허리/엉덩이, 중부하 협동 로봇.

## 공급망 위치

- **상류 핵심 부품/재료**: 희토류 자석, 규소 강판, 구리선, 절연 재료, 베어링
- **하류 고객/적용 분야**: 협동 로봇, 휴머노이드 로봇, 항공우주, 의료 장비 OEM
- **주요 경쟁사/대상**: Maxon, 汇川技术, 禾川科技, Parker

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_kollmorgen`
- 제품 엔터티: `ent_component_kollmorgen_tbm2g_050`, `ent_component_kollmorgen_tbm2g_115`
- 주요 관계:
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_050`
  - `ent_company_kollmorgen` -- `manufactures` --> `ent_component_kollmorgen_tbm2g_115`

## 참고 자료

1. [공식 웹사이트](https://www.kollmorgen.com)
2. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인하십시오)
