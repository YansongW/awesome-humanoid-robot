# {{company_name_zh}} / {{company_name_en}}

> 이 항목은 [부록 D 기업/제품 Wiki](../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | {{company_name_zh}} |
| **영문명** | {{company_name_en}} |
| **본사** | {{hq}} |
| **설립일** | {{founded}} |
| **공식 웹사이트** | `{{website}}` |
| **공급망 단계** | {{tags}} |
| **기업 속성** | {{attributes}} |
| **모회사/소속 그룹** | {{parent}} |
| **데이터 출처** | {{sources}} |

## 회사 개요

{{one_sentence_positioning}}

{{company_description}}

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|-----------|----------|-----------|-----------|
| {{product_line_1}} | {{positioning_1}} | {{representative_1}} | {{application_1}} |
| {{product_line_2}} | {{positioning_2}} | {{representative_2}} | {{application_2}} |

## 대표 제품

### {{product_name_1}}

> 이미지: 공식 공개 자료를 참조하십시오.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | {{dimension_1}} | {{source_1}} |
| 무게 | {{weight_1}} | {{source_1}} |
| 자유도 | {{dof_1}} | {{source_1}} |
| 부하/토크 | {{payload_1}} | {{source_1}} |
| 속도/회전수 | {{speed_1}} | {{source_1}} |
| 지속 시간 | {{endurance_1}} | {{source_1}} |
| 인터페이스/통신 | {{interface_1}} | {{source_1}} |
| 가격 | {{price_1}} | {{source_1}} |

**기술적 특징**: {{highlights_1}}

**응용 시나리오**: {{applications_1}}

### {{product_name_2}}

> 이미지: 공식 공개 자료를 참조하십시오.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | {{dimension_2}} | {{source_2}} |
| 무게 | {{weight_2}} | {{source_2}} |
| 자유도 | {{dof_2}} | {{source_2}} |
| 부하/토크 | {{payload_2}} | {{source_2}} |
| 속도/회전수 | {{speed_2}} | {{source_2}} |
| 지속 시간 | {{endurance_2}} | {{source_2}} |
| 인터페이스/통신 | {{interface_2}} | {{source_2}} |
| 가격 | {{price_2}} | {{source_2}} |

**기술적 특징**: {{highlights_2}}

**응용 시나리오**: {{applications_2}}

## 공급망 위치

- **상류 핵심 부품/소재**: {{upstream}}
- **하류 고객/응용 시나리오**: {{downstream}}
- **주요 경쟁사/대상**: {{competitors}}

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_{{company_id}}`
- 제품 엔터티: `ent_product_{{product_id_1}}`, `ent_product_{{product_id_2}}`
- 주요 관계:
  - `ent_company_{{company_id}}` -- `manufactures` --> `ent_product_{{product_id_1}}`
  - `ent_product_{{product_id_1}}` -- `uses` --> `ent_component_xxx`
  - `ent_company_{{company_id}}` -- `supplies` --> `ent_company_xxx`

## 참고 자료

1. 공식 웹사이트: `{{website}}`
2. WAIC 2026 참가 보도: `{{waic_source}}`
3. 기타 공개 자료: `{{other_source}}`
