# Kistler 9107B 3성분 힘 센서 / Kistler 9107B 3-Component Force Sensor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [키슬러 (Kistler) / Kistler](../companies/company_kistler.md) |
| **제품 카테고리** | 압전식 3성분 힘 센서 |
| **출시 시기** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Kistler 9107B 3성분 힘 센서 제품/자료 페이지](https://www.kistler.com/en/products/force-sensors/9107b) |

## 제품 개요

9107B는 Kistler가 출시한 소형 압전식 3성분 힘 센서로, Fx, Fy 및 Fz 세 개의 직교 방향 동적 힘을 동시에 측정할 수 있습니다. 높은 강성, 높은 고유 진동수 및 매우 낮은 크로스토크로 인해 기계 가공 절삭력 모니터링, 로봇 말단 힘 제어 및 구조 테스트에 적합합니다.

## 제품 이미지

> Kistler 9107B 3성분 힘 센서: [공식 자료](https://www.kistler.com/en/products/force-sensors/9107b)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 압전식 3성분 힘 센서 | 공식 홈페이지 |
| 측정 방향 | Fx / Fy / Fz | 공식 홈페이지/데이터시트 |
| 힘 측정 범위 (Fx/Fy) | 미공개 | - |
| 힘 측정 범위 (Fz) | 미공개 | - |
| 감도 | 미공개 | - |
| 강성 | 고강성 설계 | 공식 홈페이지/데이터시트 |
| 고유 진동수 | 미공개 | - |
| 크로스토크 | < ±1% (일반적) | 공식 홈페이지/데이터시트 |
| 작동 온도 | 미공개 | - |
| 보호 등급 | 미공개 | - |
| 출력 인터페이스 | 압전 전하 출력 + 전용 전하 증폭기 | 공식 홈페이지/데이터시트 |
| 크기 | 소형 플랜지 장착 | 공식 홈페이지/데이터시트 |
| 무게 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [키슬러 (Kistler) / Kistler](../companies/company_kistler.md)
- **핵심 부품/기술 출처**: 압전 석영 결정 감지 소자, 예압 기구, 스테인리스 스틸 하우징, 차폐 케이블, 전하 증폭기.
- **하위 응용/고객**: 공작 기계 및 공구 제조사, 자동차 테스트 연구소, 로봇 OEM, 항공우주 연구 기관, 휴머노이드 로봇 완성차 제조사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_kistler_9107b`
- 부품 엔터티: `ent_component_kistler_9107b_sensor`
- 제조사 엔터티: `ent_company_kistler`
- 주요 관계:
  - `rel_ent_company_kistler_manufactures_ent_product_kistler_9107b` (`ent_company_kistler` → `manufactures` → `ent_product_kistler_9107b`)
  - `rel_ent_company_kistler_manufactures_ent_component_kistler_9107b_sensor` (`ent_company_kistler` → `manufactures` → `ent_component_kistler_9107b_sensor`)
  - `rel_ent_product_kistler_9107b_uses_ent_component_kistler_9107b_sensor` (`ent_product_kistler_9107b` → `uses` → `ent_component_kistler_9107b_sensor`)

## 응용 시나리오

- **기계 가공 절삭력 모니터링**: 실시간 3방향 절삭력 분석, 공구 수명 및 가공 품질 최적화.
- **로봇 말단 힘 제어**: 조립, 프레스 및 연삭 과정의 동적 힘 피드백.
- **구조 동적 테스트**: 고강성 센서가 과도 충격 및 진동 하중 포착.
- **휴머노이드 로봇 발끝**: 보행 및 균형 제어 중 지면 반력 측정.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 압전 3성분 힘 센서 | ATI Mini 시리즈 | Kunwei KWR36 |
| 기술 원리 | 압전 석영 | 실리콘 스트레인 게이지 | 금속 스트레인 게이지 |
| 적용 주파수 대역 | 고주파 동적 | 중저주파 힘 제어 | 중저주파 힘 제어 |
| 핵심 장점 | 고주파 동적, 낮은 크로스토크 | 로봇 통합 성숙도 | 소형 고정밀 |

## 구매 및 배포 권장 사항

- 목표 응용 분야의 분해능, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위 일치 여부를 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 키슬러 (Kistler) / Kistler](../companies/company_kistler.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Kistler 공식 홈페이지](https://www.kistler.com)
2. [Kistler 9107B 3성분 힘 센서 제품/자료 페이지](https://www.kistler.com/en/products/force-sensors/9107b)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
