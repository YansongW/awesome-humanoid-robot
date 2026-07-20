# 오비중광 Gemini 335 / Orbbec Gemini 335

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [오비중광 / Orbbec](../companies/company_orbbec.md) |
| **제품 카테고리** | 양안 깊이 카메라 |
| **출시일** | 2024년 4월 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Orbbec Gemini 335 제품 페이지](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/) |

## 제품 개요

오비중광 Gemini 335는 Gemini 330 시리즈 양안 3D 카메라의 표준 버전으로, 실내 및 반실외 로봇 시나리오를 위해 설계되었습니다. Gemini 335는 오비중광 자체 개발 MX6800 깊이 엔진 ASIC을 탑재하고, 능동 + 수동 융합 입체 시야 기술을 채택하여 강한 직사광선, 저조도, 흰 벽 등 약한 텍스처 환경에서도 안정적으로 고품질 깊이 데이터를 출력할 수 있습니다.

Gemini 335는 소형 본체(90×25×30 mm, 97 g)로, USB 3.0 Type-C 인터페이스와 UVC 드라이버를 지원하여 AMR, 휴머노이드 로봇, 로봇 팔, 드론 등에 신속하게 통합할 수 있습니다. 깊이 대각 FOV는 100° 이상이며, 최대 측정 범위는 10m 이상이고, IMU 및 다기기 동기화 기능을 통합하여 로봇 3D 비전의 주요 선택지 중 하나입니다.

## 제품 이미지

> Orbbec Gemini 335: [공식 자료](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 90 mm × 25 mm × 30 mm | Orbbec Store |
| 무게 | 97 g | Orbbec Store |
| 깊이 기술 | 능동 + 수동 입체 시야 | Orbbec 공식 홈페이지 |
| 깊이 해상도 | 최대 1280×800 @ 30 fps | Orbbec Store |
| RGB 해상도 | 최대 1920×1080 @ 30 fps | Orbbec Store |
| 깊이 FOV | 90° × 65° (대각 >100°) | Orbbec Store |
| 깊이 측정 범위 | 0.1 m – 20 m+ (이상적 0.26–3.0 m) | Orbbec Store |
| 공간 정밀도 | ≤1.5% @ 2 m | Orbbec Store |
| 인터페이스 | USB 3.0 Type-C | Orbbec Store |
| 소비 전력 | <3 W | Orbbec Store |
| 보호 등급 | IP5X | Orbbec Store |
| 가격 | 약 CNY 1,950 | 딜러 참고 |

## 공급망 위치

- **제조사**: [오비중광 / Orbbec](../companies/company_orbbec.md)
- **핵심 부품/기술 출처**: 자체 개발 MX6800 깊이 엔진 ASIC, 광학 모듈, 깊이 알고리즘; 이미지 센서, 레이저 프로젝터는 외부 구매.
- **하위 응용/고객**: AMR, 휴머노이드 로봇, 협동 로봇 팔, 드론, 3D 스캐닝 및 인체 재구성.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_orbbec_gemini_335`
- 제조사 엔터티: `ent_company_orbbec`
- 주요 관계:
  - `rel_ent_company_orbbec_manufactures_ent_component_orbbec_gemini_335` (`ent_company_orbbec` → `manufactures` → `ent_component_orbbec_gemini_335`)

## 응용 시나리오

- **AMR/AGV 내비게이션 및 장애물 회피**: 실내외 넓은 FOV 깊이 인식 및 동적 장애물 감지.
- **휴머노이드 로봇 비전**: 머리 또는 몸통 비전 모듈, VSLAM, 제스처 및 객체 인식 지원.
- **협동 로봇 팔**: 상자 피킹, 부품 위치 파악, 치수 측정 및 그리핑 가이드.
- **드론 및 야외 장비**: 강한 빛에서도 사용 가능한 깊이 데이터로 저고도 장애물 회피 및 지형 매핑 지원.

## 경쟁 비교

| 비교 항목 | 오비중광 Gemini 335 | Intel RealSense D435i | Stereolabs ZED 2i |
|--------|---------------------|-----------------------|-------------------|
| 깊이 기술 | 능동+수동 양안 | 능동 적외선 입체 시야 | 수동 양안 |
| 측정 범위 | 0.1–20 m+ | 0.3–10 m | 0.3–20 m |
| 소비 전력 | <3 W | 약 3 W | 약 4 W |
| 핵심 장점 | 야외 강한 빛, MX6800 ASIC, 저지연 | 생태계 성숙, ROS 지원 우수 | 고정밀 및 3D 재구성 |

## 참고 자료

1. [Orbbec Gemini 335 제품 페이지](https://www.orbbec.com/products/stereo-vision-camera/gemini-335/)
2. [Orbbec Store – Gemini 335](https://store.orbbec.com/products/gemini-335)
3. [오비중광 중국어 공식 홈페이지 – Gemini 330 시리즈 출시](https://www.orbbec.com.cn/index/News/info.html?cate=31&id=273)
4. [CSDN – ROS2 + Gemini 335L 사용](https://blog.csdn.net/imwaters/article/details/156425172)
