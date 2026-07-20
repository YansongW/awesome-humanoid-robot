# Sony IMX500 지능형 비전 센서 / Sony IMX500 Intelligent Vision Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [소니 반도체 솔루션(Sony Semiconductor Solutions) / Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md) |
| **제품 카테고리** | 적층형 CMOS 이미지 센서(AI 추론 통합) |
| **출시일** | 2020년부터 상용화 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Sony IMX500 지능형 비전 센서 제품/자료 페이지](https://www.sony-semicon.co.jp/products/common/IMX500.html) |

## 제품 개요

IMX500은 픽셀 칩과 로직 칩의 적층 구조에 AI 처리 유닛을 통합한 세계 최초의 이미지 센서입니다. 센서 단에서 이미지 인식 및 추론을 완료하고 메타데이터만 출력하여 시스템 전력 소모와 데이터 대역폭을 크게 줄이며, 로봇 비전, 지능형 감시 및 임베디드 지능형 엣지 디바이스에 적합합니다.

## 제품 이미지

> Sony IMX500 지능형 비전 센서: [공식 자료](https://www.sony-semicon.co.jp/products/common/IMX500.html)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 적층형 CMOS 이미지 센서 + AI 추론 | 공식 사이트/datasheet |
| 유효 화소 | 약 1230만(4056 × 3040) | 공식 사이트/datasheet |
| 광학 크기 | 1/2.3형 | 공식 사이트/datasheet |
| 픽셀 크기 | 미공개 | - |
| 셔터 | 롤링 셔터 | 공식 사이트/datasheet |
| 최대 프레임 속도 | 미공개 | - |
| AI 성능 | 센서 단 AI 모델 추론 | 공식 사이트/datasheet |
| 출력 형식 | 메타데이터 / 이미지 + 메타데이터 | 공식 사이트/datasheet |
| 인터페이스 | MIPI D-PHY / SLVS-EC | 공식 사이트/datasheet |
| 전원 공급 | 미공개 | - |
| 전력 소모 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 패키지 | COB / CSP | 공식 사이트/datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [소니 반도체 솔루션(Sony Semiconductor Solutions) / Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md)
- **핵심 부품/기술 출처**: 자체 개발 적층형 픽셀 칩, AI 처리 로직 칩, DRAM, ISP 알고리즘, 레퍼런스 디자인 및 모델 툴체인.
- **하위 응용/고객**: 로봇 OEM, 스마트 카메라 제조사, 보안 감시, 산업 비전 통합업체, 자동차 Tier 1, 소비자 전자 브랜드.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_sony_semiconductor_imx500`
- 부품 엔터티: `ent_component_sony_semiconductor_imx500_sensor`
- 제조사 엔터티: `ent_company_sony_semiconductor`
- 주요 관계:
  - `rel_ent_company_sony_semiconductor_manufactures_ent_product_sony_semiconductor_imx500`(`ent_company_sony_semiconductor` → `manufactures` → `ent_product_sony_semiconductor_imx500`)
  - `rel_ent_company_sony_semiconductor_manufactures_ent_component_sony_semiconductor_imx500_sensor`(`ent_company_sony_semiconductor` → `manufactures` → `ent_component_sony_semiconductor_imx500_sensor`)
  - `rel_ent_product_sony_semiconductor_imx500_uses_ent_component_sony_semiconductor_imx500_sensor`(`ent_product_sony_semiconductor_imx500` → `uses` → `ent_component_sony_semiconductor_imx500_sensor`)

## 응용 시나리오

- **로봇 비전 인식**: 저지연 객체 인식 및 위치 파악, 메인 컨트롤러 연산 부담 감소.
- **지능형 감시**: 이벤트 메타데이터만 출력하여 프라이버시 보호 및 저장 비용 절감.
- **산업 품질 검사**: 엣지 AI 실시간 결함 분류 및 조립 검증.
- **임베디드 지능형**: 엔드 사이드 인식-의사 결정 폐쇄 루프, 시스템 응답 지연 감소.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 지능형 비전 센서 | 갤럭시코어 GC32E2 | OmniVision OX08D10 |
| AI 위치 | 센서 내 추론 | ISP/SoC 측 | ISP/SoC 측 |
| 출력 | 메타데이터/이미지+메타데이터 | RAW 이미지 | RAW 이미지 |
| 핵심 장점 | 저전력, 저대역폭, 프라이버시 | 고화소, 저비용 | 차량용 고다이내믹 |

## 구매 및 배포 권장 사항

- 대상 응용 프로그램의 해상도, 범위, 정밀도 또는 연산 성능 요구 사항에 따라 특정 모델을 선택하세요.
- 배포 전 인터페이스, 전원 공급, 방열, 기계 설치 및 환경 온도 범위가 일치하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 소니 반도체 솔루션(Sony Semiconductor Solutions) / Sony Semiconductor Solutions](../companies/company_sony_semiconductor.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Sony Semiconductor Solutions 공식 사이트](https://www.sony-semicon.co.jp)
2. [Sony IMX500 지능형 비전 센서 제품/자료 페이지](https://www.sony-semicon.co.jp/products/common/IMX500.html)
3. 제품 datasheet 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
