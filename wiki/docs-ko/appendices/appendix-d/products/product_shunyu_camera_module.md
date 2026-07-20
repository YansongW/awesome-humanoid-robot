# 순우옵틱스 차량용/로봇 카메라 모듈 / Sunny Optical Automotive / Robot Camera Module

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [순우옵틱스 / Sunny Optical](../companies/company_shunyu.md) |
| **제품 카테고리** | 차량용 카메라 모듈 |
| **출시 시간** | 지속 판매/반복 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [순우옵틱스 차량용/로봇 카메라 모듈 제품/자료 페이지](https://www.sunnyoptical.com/en/pro/009017006/index.html) |

## 제품 개요

순우옵틱스 차량용/로봇 카메라 모듈은 ADAS, 스마트 콕핏 및 임베디드 지능 로봇 비전 시나리오를 대상으로 하며, 자체 개발한 유리-플라스틱 하이브리드 렌즈, CMOS 이미지 센서 및 ISP 튜닝을 통합하여 높은 신뢰성, 넓은 온도 범위 및 IP67/IP69K 보호 등급을 갖추고 있습니다. 모듈은 GMSL2/FPD-Link III 등 고속 직렬 인터페이스를 지원하며, 목표 탐지, 차선 인식, SLAM 및 핸드-아이 조정에 사용되는 고화질 이미지를 출력할 수 있습니다.

## 제품 이미지

> 순우옵틱스 차량용/로봇 카메라 모듈: [공식 자료](https://www.sunnyoptical.com/en/pro/009017006/index.html)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 차량용 카메라 모듈 | 공식 제품 자료 |
| 해상도 | 2MP / 3MP / 8MP 다중 모델 | 공식 제품 자료 |
| 센서 | 1/2.7" – 1/2.3" CMOS | 공식 제품 자료 |
| 화각 | 30° – 120° (모델에 따라 다름) | 공식 제품 자료 |
| 렌즈 | 유리-플라스틱 하이브리드 고해상력 렌즈 | 공식 제품 자료 |
| 인터페이스 | GMSL2 / FPD-Link III / 동축 | 공식 제품 자료 |
| 프레임 속도 | 최대 60 fps (해상도 및 인터페이스에 따라 다름) | 공식 제품 자료 |
| 보호 등급 | IP67 / IP69K | 공식 제품 자료 |
| 작동 온도 | -40℃ – +85℃ | 공식 제품 자료 |
| 전원 공급 | 12 V DC (일반) | 공식 제품 자료 |
| 무게 | 약 50 – 150 g | 공식 제품 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [순우옵틱스 / Sunny Optical](../companies/company_shunyu.md)
- **핵심 부품/기술 출처**: CMOS 이미지 센서, 광학 렌즈, 보이스 코일 모터, FPC/PCB, ISP 칩, 구조 부품
- **하류 응용/고객**: 스마트폰 OEM, 자동차 OEM/Tier1, 로봇 완제품 제조사, AR/VR 제조사

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_shunyu_automotive_camera_module`
- 부품 엔터티: `ent_component_shunyu_camera_module_core`
- 제조사 엔터티: `ent_company_shunyu`
- 주요 관계:
  - `rel_ent_company_shunyu_manufactures_ent_product_shunyu_automotive_camera_module` (`ent_company_shunyu` → `manufactures` → `ent_product_shunyu_automotive_camera_module`)
  - `rel_ent_company_shunyu_manufactures_ent_component_shunyu_camera_module_core` (`ent_company_shunyu` → `manufactures` → `ent_component_shunyu_camera_module_core`)
  - `ent_product_shunyu_automotive_camera_module` -- `uses` --> `ent_component_shunyu_camera_module_core`

## 응용 시나리오

- **휴머노이드 로봇/서비스 로봇 비전 유도, 자율 주행 인식, 스마트 콕핏 DMS/OMS, 산업 검사**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 제안

- 대상 응용 프로그램의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 순우옵틱스 / Sunny Optical](../companies/company_shunyu.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [순우옵틱스 공식 홈페이지](https://www.sunnyoptical.com)
2. [순우옵틱스 차량용/로봇 카메라 모듈 제품/자료 페이지](https://www.sunnyoptical.com/en/pro/009017006/index.html)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
