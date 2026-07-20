# 중경 PM01 / EngineAI PM01

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [중경 로봇 / EngineAI](../companies/company_engineai.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시 시간** | 2024년 말 / 2025년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [https://www.engineai.com.cn](https://www.engineai.com.cn) |

## 제품 개요

연구 교육 알고리즘 검증, 산업 제조 2차 개발, 상업 전시 및 댄스 공연.

EngineAI PM01은 중경 로봇의 대표 제품입니다. 풀스택 자체 개발 통합 관절, 허리 ＞300° 회전, 오픈소스 학습/배포 코드, 핸드헬드 리모컨, 인터랙션 스크린. 주요 사양은 다음과 같습니다: 서 있을 때 1400(H)×535.55(W)×252.66(D) mm (크기), 상업용 약 42 kg; 교육용 약 43 kg (무게), 상업용 23 DOF; 교육용 24 DOF (자유도).

## 제품 이미지

![EngineAI PM01](https://cn-engineai-1304599088.cos.ap-guangzhou.myqcloud.com/uploads/upload/images/20251029/668bd44456c24b778a8c7d824e42d858.png)

> 이미지 출처: EngineAI 공식 사이트 제품 이미지.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 서 있을 때 1400(H)×535.55(W)×252.66(D) mm | EngineAI 공식 사이트 |
| 무게 | 상업용 약 42 kg; 교육용 약 43 kg | EngineAI 공식 사이트 |
| 자유도 | 상업용 23 DOF; 교육용 24 DOF | EngineAI 공식 사이트 |
| 부하/토크 | 무릎 관절 피크 토크 145 N·m (Q90H 모터) | EngineAI 공식 사이트 |
| 속도/회전 속도 | 이동 속도 ＞2 m/s (하드웨어 지원) | EngineAI 공식 사이트 |
| 배터리 지속 시간 | 약 2시간 (10000 mAh 퀵 릴리스 배터리) | EngineAI 공식 사이트 |
| 인터페이스/통신 | 교육용 2차 개발 지원, NVIDIA Jetson Orin NX (16G) 탑재 | EngineAI 공식 사이트 |
| 가격 | 상업용 8.8만 위안 (세금 포함) | 공식 FAQ |

## 공급망 위치

- **제조사**: [중경 로봇 / EngineAI](../companies/company_engineai.md)
- **핵심 부품/기술 출처**: 자체 개발 Q90H/Q25H 통합 관절 모터, 유성/하모닉 감속기, 모터; Intel RealSense, NVIDIA Jetson, 배터리.
- **하류 응용/고객**: 연구 교육 알고리즘 검증, 산업 제조 2차 개발, 상업 전시 및 댄스 공연.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_engineai_pm01`
- 제조사 엔터티: `ent_company_engineai`
- 주요 관계:
  - `rel_ent_company_engineai_manufactures_ent_product_engineai_pm01` (`ent_company_engineai` → `manufactures` → `ent_product_engineai_pm01`)
  - `ent_product_engineai_pm01` -- `uses` --> `ent_component_engineai_q90h`

## 응용 시나리오

- **연구 교육 알고리즘 검증, 산업 제조 2차 개발, 상업 전시 및 댄스 공연.**
- **산업 제조**: 유연 생산 라인에서 운반, 조립, 검사 등의 작업 수행.
- **상업 서비스**: 안내, 접객, 전시 및 브랜드 인터랙션에 사용.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 |
|--------|--------|----------|
| 포지셔닝 | 범용 휴머노이드 로봇 | 유사 제품은 특정 시나리오에 따라 다름 |
| 핵심 장점 | 풀스택 자체 개발 통합 관절, 허리 ＞300° 회전, 오픈소스 학습/배포 코드, 핸드헬드 리모컨, 인터랙션 스크린 | 미공개 |
| 가격 | 상업용 8.8만 위안 (세금 포함) | 미공개 |

## 구매 및 배포 제안

- 공식 채널을 통해 최신 소프트웨어 버전, SDK 지원 및 사후 교육을 확인하는 것을 권장합니다.
- 연구 및 교육 사용자는 2차 개발 인터페이스, 시뮬레이션 플랫폼 호환성 및 커뮤니티 활동성을 우선 평가해야 합니다.
- 산업 사용자는 구체적인 공정에 따라 부하, 정밀도, 보호 등급 및 통합 인터페이스를 검증해야 합니다.

## 참고 자료

1. [EngineAI PM01 제품 페이지](https://www.engineai.com.cn/product-pm01.html)
2. [EngineAI SE01 제품 페이지](https://en.engineai.com.cn/product-se01)
3. [중경 로봇 FAQ](https://www.engineai.com.cn/about-news-media/23.html)
