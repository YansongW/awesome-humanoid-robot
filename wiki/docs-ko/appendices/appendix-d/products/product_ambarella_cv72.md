# Ambarella CV72 비전 AI SoC

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [앰바렐라 / Ambarella](../companies/company_ambarella.md) |
| **제품 카테고리** | 엣지 AI 비전 SoC / 보안 및 로봇 비전 프로세서 |
| **출시일** | 2023년 (CV72S) |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Ambarella CV72 Product Page](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/) |

## 제품 개요

Ambarella CV72 시리즈는 5 nm 공정 기반의 엣지 AI 비전 SoC로, 3세대 CVflow AI 가속기와 통합 ISP를 탑재했습니다. AI 연산 성능은 약 12 TOPS로, 최신 CNN 및 Transformer 네트워크를 로컬에서 실행할 수 있으며, 3 W 미만의 전력 소비로 다중 4K/8K 비디오 인코딩을 지원합니다. CV72는 레이더-비전 센서 융합 및 AI-ISP 강화 야간 투시도 지원하여 보안 카메라, 로봇 비전 및 산업 검사에 이상적인 플랫폼입니다.

## 제품 이미지

> Ambarella CV72 비전 AI SoC: [공식 자료](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 공정 | 5 nm (공개 보도) | Ambarella 공개 자료 |
| CPU | 듀얼 코어 / 쿼드 코어 Arm Cortex-A76 (버전에 따라 최대 1.8 GHz) | Ambarella 공개 자료 |
| AI 가속기 | 3세대 CVflow AI 가속기 | Ambarella 공개 자료 |
| AI 연산 성능 | 약 12 TOPS (CV72, 공개 보도) | Ambarella 공개 자료 |
| ISP | 통합 고성능 ISP, 저조도 HDR, AI-ISP (AISP) 지원 | Ambarella 공개 자료 |
| 비디오 | 4Kp120 / 8Kp30 인코딩, 다중 비디오 동시 처리 | Ambarella 공개 자료 |
| 메모리 | LPDDR4x / LPDDR5 / LPDDR5x 지원 | Ambarella 공개 자료 |
| 인터페이스 | PCIe, USB 3.2, GbE, MIPI CSI, 레이더 융합 인터페이스 | Ambarella 공개 자료 |
| 전력 소비 | 일반 < 3 W (CV72S, 공개 보도) | Ambarella 공개 자료 |
| 패키지 | 미공개 | Ambarella 공개 자료 |
| 가격 | 미공개 | Ambarella 공개 자료 |

## 공급망 위치

- **제조사**: [앰바렐라 / Ambarella](../companies/company_ambarella.md)
- **핵심 부품/기술 출처**: 삼성 5 nm 위탁 생산, ARM CPU IP, 자체 개발 CVflow/ISP, LPDDR5x, 패키징/테스트, 기판
- **하위 응용/고객**: 보안 OEM, 스마트 카메라 솔루션 업체, 로봇 및 드론 제조사, 교통 감시 통합 업체

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ambarella_cv72`
- 부품 엔터티: `ent_component_ambarella_cv72_chip`
- 제조사 엔터티: `ent_company_ambarella`
- 주요 관계:
  - `rel_ent_company_ambarella_manufactures_ent_product_ambarella_cv72` (`ent_company_ambarella` → `manufactures` --> `ent_product_ambarella_cv72`)
  - `rel_ent_company_ambarella_manufactures_ent_component_ambarella_cv72_chip` (`ent_company_ambarella` → `manufactures` --> `ent_component_ambarella_cv72_chip`)
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`

## 응용 시나리오

- **로봇 비전**: 다중 카메라 실시간 객체 감지, 의미론적 분할 및 내비게이션 지원
- **스마트 보안 카메라**: 엣지 4K AI 분석, 저조도 컬러 야간 투시, 얼굴/번호판 인식
- **산업 비전 검사**: 고속 결함 감지, 치수 측정, OCR 및 바코드 인식

## 경쟁 비교

| 비교 항목 | Ambarella CV72 | Qualcomm QCS8550 | NVIDIA Jetson Orin NX |
|---|---|---|---|
| 공정 | 5 nm | 4 nm | 8 nm |
| AI 연산 성능 | 약 12 TOPS | 약 15 TOPS | 최대 100 TOPS |
| 전력 소비 | < 3 W | 약 5–10 W | 10–25 W |

## 구매 및 배포 권장 사항

Ambarella SDK가 대상 Transformer/CNN 모델을 지원하는지 평가하고, CVflow 툴체인을 활용하여 모델을 양자화 및 최적화하며, 카메라 및 레이더 인터페이스에 따라 해당 CV72 버전 및 레퍼런스 디자인을 선택하세요.

## 관련 항목

- [제조사: 앰바렐라 / Ambarella](../companies/company_ambarella.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Ambarella CV72 제품 페이지](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
2. [Ambarella CV72S 보도 자료](https://www.ambarella.com/news/ambarella-launches-4k-5nm-edge-ai-soc-mainstream-security/)
3. [Ambarella 공식 사이트](https://www.ambarella.com)
