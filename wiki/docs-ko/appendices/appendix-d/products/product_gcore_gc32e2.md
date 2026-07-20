# 格科微 GC32E2 CMOS 이미지 센서 / GalaxyCore GC32E2 CMOS Image Sensor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [格科微 / GalaxyCore](../companies/company_gcore.md) |
| **제품 카테고리** | 32MP CMOS 이미지 센서 |
| **출시일** | 2024년 양산 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [格科微 GC32E2 CMOS 이미지 센서 제품/자료 페이지](https://en.gcoreinc.com/news/detail-67) |

## 제품 개요

格科微 GC32E2는 2세대 고성능 단일 칩 32MP CMOS 이미지 센서로, 후면 조사식(BSI) 공정과 단일 프레임 DAG HDR 기술을 채택하여 프리뷰, 촬영 및 녹화 시 하이라이트와 어두운 부분의 디테일을 보존합니다. 센서는 PDAF 위상차 검출 자동 초점과 AON 저전력 모드를 지원하며, 스마트폰 전면 카메라 및 로봇 비전 등에 적합합니다.

## 제품 이미지

> 格科微 GC32E2 CMOS 이미지 센서: [공식 자료](https://en.gcoreinc.com/news/detail-67)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 32MP CMOS 이미지 센서 | 格科微 공식 사이트 |
| 유효 화소 | 32 MP | 格科微 공식 사이트 |
| 화소 크기 | 0.7 µm | 格科微 공식 사이트 |
| 광학 크기 | 1/3.1" | 格科微 공식 사이트 |
| 공정 | 후면 조사식(BSI) | 格科微 공식 사이트 |
| 셔터 | 롤링 셔터 | 格科微 공식 사이트 |
| HDR | 단일 프레임 DAG HDR | 格科微 공식 사이트 |
| 초점 | PDAF 위상차 검출 자동 초점 | 格科微 공식 사이트 |
| 출력 형식 | RAW 10 / 12 | 格科微 공식 사이트 |
| 인터페이스 | MIPI D-PHY | 格科微 공식 사이트 |
| 패키지 | COB / COM | 格科微 공식 사이트 |
| 프레임 속도 | 최대 15fps(전체 해상도) | 格科微 공식 사이트 |
| 작동 온도 | -20℃ – +70℃ | 格科微 공식 사이트 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [格科微 / GalaxyCore](../companies/company_gcore.md)
- **핵심 부품/기술 출처**: 웨이퍼 파운드리, 패키징 및 테스트, 컬러 필터, 마이크로렌즈, 캐리어 기판
- **하위 응용/고객**: 스마트폰 OEM, ODM, 태블릿, 로봇, IoT 카메라 제조사

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_gcore_gc32e2`
- 부품 엔터티: `ent_component_gcore_gc32e2_sensor`
- 제조사 엔터티: `ent_company_gcore`
- 주요 관계:
  - `rel_ent_company_gcore_manufactures_ent_product_gcore_gc32e2` (`ent_company_gcore` → `manufactures` → `ent_product_gcore_gc32e2`)
  - `rel_ent_company_gcore_manufactures_ent_component_gcore_gc32e2_sensor` (`ent_company_gcore` → `manufactures` → `ent_component_gcore_gc32e2_sensor`)
  - `ent_product_gcore_gc32e2` -- `uses` --> `ent_component_gcore_gc32e2_sensor`

## 응용 시나리오

- **스마트폰 전면 카메라, 태블릿 PC, 로봇 비전, 웨어러블 기기, 화상 통화**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 성능 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 格科微 / GalaxyCore](../companies/company_gcore.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [格科微 공식 사이트](https://www.gcoreinc.com)
2. [格科微 GC32E2 CMOS 이미지 센서 제품/자료 페이지](https://en.gcoreinc.com/news/detail-67)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
