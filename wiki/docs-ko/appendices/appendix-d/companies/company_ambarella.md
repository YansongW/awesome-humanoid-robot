# 앰바렐라 / Ambarella

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 앰바렐라 |
| **영문명** | Ambarella |
| **본사** | 미국 캘리포니아주 산타클라라 |
| **설립일** | 2004년 |
| **공식 웹사이트** | [https://www.ambarella.com](https://www.ambarella.com) |
| **공급망 단계** | 비전 AI SoC, ISP, 비디오 인코딩, ADAS/로봇/보안 |
| **기업 속성** | 상장 기업 (NASDAQ: AMBA) |
| **모회사/소속 그룹** | 없음 (독립 상장 주체) |
| **데이터 출처** | Ambarella 공식 웹사이트, 제품 매뉴얼, 투자자 보도자료, 업계 보고서 |

## 회사 소개

Ambarella(앰바렐라)는 저전력, 고해상도 비디오 및 엣지 AI 비전 처리를 전문으로 하는 반도체 기업입니다. CVflow 아키텍처 AI 가속기는 ISP, 비디오 코덱 및 다중 센서 융합 기능을 통합하여 보안 카메라, ADAS, 드론, 로봇 및 산업용 비전에 널리 사용됩니다. CV72, CV7 등 차세대 SoC는 5/4 nm 공정을 채택하고 Transformer와 CNN 혼합 네트워크를 지원하며, 업계 선도적인 AI 성능 대비 전력 효율을 자랑합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| CV72 / CV72S 시리즈 | 5 nm 주류 엣지 AI 비전 SoC | CV72S | 전문 보안, 스마트 카메라, 로봇 비전, 산업 검사 |
| CV7 시리즈 | 4 nm 플래그십 8K 비전 AI SoC | CV7 | 고급 보안, 드론, 자율주행 인식, 8K 카메라 |

## 대표 제품

### Ambarella CV72

> Ambarella CV72: [공식 자료](https://www.ambarella.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 5 nm (공개 보도) | Ambarella 공개 자료 |
| CPU | 듀얼 코어 / 쿼드 코어 Arm Cortex-A76 (버전에 따라 최대 1.8 GHz) | Ambarella 공개 자료 |
| AI 가속기 | 3세대 CVflow AI 가속기 | Ambarella 공개 자료 |
| AI 연산 성능 | 약 12 TOPS (CV72, 공개 보도) | Ambarella 공개 자료 |
| ISP | 통합 고성능 ISP, 저조도 HDR, AI-ISP (AISP) 지원 | Ambarella 공개 자료 |
| 비디오 | 4Kp120 / 8Kp30 인코딩, 다중 채널 비디오 동시 처리 | Ambarella 공개 자료 |
| 메모리 | LPDDR4x / LPDDR5 / LPDDR5x 지원 | Ambarella 공개 자료 |
| 인터페이스 | PCIe, USB 3.2, GbE, MIPI CSI, 레이더 융합 인터페이스 | Ambarella 공개 자료 |
| 전력 소비 | 일반 < 3 W (CV72S, 공개 보도) | Ambarella 공개 자료 |
| 패키지 | 미공개 | Ambarella 공개 자료 |
| 가격 | 미공개 | Ambarella 공개 자료 |

**기술적 특징**: CVflow 3.0은 Transformer와 CNN 동시 처리, AI 강화 ISP, 레이더-비전 융합, 초저전력, 다중 채널 고화질 카메라 지향.

**응용 시나리오**: **로봇 비전**: 다중 카메라 실시간 객체 탐지, 의미론적 분할 및 내비게이션 보조; **스마트 보안 카메라**: 엣지 4K AI 분석, 저조도 컬러 나이트 비전, 얼굴/번호판 인식; **산업용 비전 검사**: 고속 결함 검출, 치수 측정, OCR 및 바코드 인식

### Ambarella CV7

> Ambarella CV7: [공식 자료](https://www.ambarella.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 4 nm (공개 보도) | Ambarella 공개 자료 |
| CPU | 쿼드 코어 Arm Cortex-A73 | Ambarella 공개 자료 |
| AI 가속기 | 3세대 CVflow AI 가속기 | Ambarella 공개 자료 |
| AI 연산 성능 | 이전 세대 대비 2.5배 이상 향상 | Ambarella 공개 자료 |
| 비디오 | 8Kp60 다중 채널 비디오, 4Kp240 인코딩 | Ambarella 공개 자료 |
| 전력 소비 | 미공개 | Ambarella 공개 자료 |
| 가격 | 미공개 | Ambarella 공개 자료 |

**기술적 특징**: 8K 비전 AI, 4 nm 공정, 더 높은 CPU 성능, 플래그십 AI 인식 애플리케이션 지향.

**응용 시나리오**: 8K 액션 카메라, 고급 보안, 자율주행 인식, 드론, 화상 회의.

## 공급망 위치

- **상류 핵심 부품/소재**: 삼성 5/4 nm 웨이퍼 파운드리, ARM IP, ISP/비디오 IP, LPDDR5x 스토리지, 패키징 및 테스트, 모듈
- **하류 고객/응용 시나리오**: 보안 카메라 제조사, 드론 기업, 자동차 Tier1/OEM, 로봇 완제품 제조사, 화상 회의 장비 업체
- **주요 경쟁사/대상**: Qualcomm QCS, NVIDIA Jetson, Horizon Robotics Journey, HiSilicon, Novatek

## 지식 그래프 노드 및 관계

- 기업 엔터티: `ent_company_ambarella`
- 제품 엔터티: `ent_product_ambarella_cv72`, `ent_product_ambarella_cv7`
- 부품 엔터티: `ent_component_ambarella_cv72_chip`, `ent_component_ambarella_cv7_chip`
- 주요 관계:
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv72`
  - `ent_company_ambarella` -- `manufactures` --> `ent_product_ambarella_cv7`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv72_chip`
  - `ent_company_ambarella` -- `manufactures` --> `ent_component_ambarella_cv7_chip`
  - `ent_product_ambarella_cv72` -- `uses` --> `ent_component_ambarella_cv72_chip`
  - `ent_product_ambarella_cv7` -- `uses` --> `ent_component_ambarella_cv7_chip`

## 참고 자료

1. [Ambarella 공식 웹사이트](https://www.ambarella.com)
2. [Ambarella CV72 제품 페이지](https://www.ambarella.com/products/aiot-industrial-robotics/cv72-ai-soc/)
3. [Ambarella CV7 보도자료](https://www.ambarella.com/news/ambarella-launches-powerful-edge-ai-8k-vision-soc-with-industry-leading-ai-and-multi-sensor-perception-performance/)
