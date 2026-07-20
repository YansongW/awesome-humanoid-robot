# 우수 G1 / Unitree G1

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [우수 테크놀로지 / Unitree Robotics](../companies/company_unitree.md) |
| **제품 카테고리** | 컴팩트 휴머노이드 로봇 |
| **출시일** | 2024년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Unitree G1 제품 페이지](https://www.unitree.com/g1) |

## 제품 개요

우수 G1은 Unitree가 교육, 연구 및 개발자를 위해 출시한 컴팩트 휴머노이드 로봇으로, 공격적인 가격과 높은 접근성으로 유명합니다. G1의 키는 약 127cm, 무게는 약 35kg이며, 기본 버전은 23개의 자유도를 가지고 있고, EDU 버전은 43 DOF로 확장 가능하며 Dex3-1 다섯 손가락 정교한 손과 NVIDIA Jetson Orin 컴퓨팅 모듈을 갖추고 있습니다.

G1은 3D LiDAR, 깊이 카메라 및 8코어 CPU(EDU 버전은 Jetson Orin 추가)를 채택하며, ROS2, Python/C++ SDK 및 OTA 업그레이드를 지원합니다. 접이식 설계로 운송 및 배치가 용이하여 전 세계 출하량이 가장 많은 휴머노이드 개발 플랫폼 중 하나가 되었습니다.

## 제품 이미지

> Unitree G1: [공식 자료](https://www.unitree.com/g1)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 127cm(높이) | 공개 사양 |
| 무게 | 약 35kg | 공개 사양 |
| 자유도(전체) | 23–43 DOF | 기본 버전/EDU 버전 구성 차이 |
| 주요 성능 지표 | 관절 최대 토크 90–120 N·m; 탑재 하중 약 2kg | 공개 사양 |
| 보행 속도 | 약 2m/s | 공개 사양 |
| 배터리 지속 시간 | 약 1.5–2시간(9,000mAh 퀵 릴리스 배터리) | 공개 사양 |
| 컴퓨팅 플랫폼 | 8코어 CPU; EDU 버전은 NVIDIA Jetson Orin 선택 가능 | 공개 사양 |
| 가격 | 약 16,000 USD / 국내 9.9만 위안부터 | 미디어 보도 |

## 공급망 위치

- **제조사**: [우수 테크놀로지 / Unitree Robotics](../companies/company_unitree.md)
- **핵심 부품/기술 출처**: 자체 개발 관절 모터 및 드라이버, 3D LiDAR, Intel RealSense 깊이 카메라, NVIDIA Jetson Orin(EDU 버전).
- **하위 응용/고객**: 대학, 교육 기관, 개발자, AI 연구 및 상용 전시.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_unitree_g1`
- 제조사 엔터티: `ent_company_unitree`
- 주요 관계:
  - `rel_ent_company_unitree_manufactures_ent_product_unitree_g1`(`ent_company_unitree` → `manufactures` → `ent_product_unitree_g1`)

## 응용 시나리오

- **교육 시연**: 대학, 초중등학교 및 과학관에서 로봇 강의, 전시 및 경진대회에 사용.
- **AI 및 로봇 연구**: 개발자 커뮤니티에서 모방 학습, 강화 학습 및 다중 모드 상호 작용 실험 수행.
- **경량 상업**: 소매 전시, 안내 접객 및 소량 물류 시범 운영.

## 경쟁 비교

| 비교 항목 | Unitree G1 | Unitree H1 | Unitree R1 |
|--------|------------|------------|------------|
| 포지셔닝 | 컴팩트 개발 플랫폼 | 풀사이즈 고다이나믹 플랫폼 | 입문형 개발 플랫폼 |
| 키 | 127cm | 180cm | 121cm |
| 가격 | 약 16,000 USD | 약 90,000 USD | 약 5,900 USD |
| 핵심 장점 | 가성비 우수, EDU 버전 기능 완전 | 고다이나믹 운동, 높은 탑재 하중 | 초저가 진입 장벽, 개발자 친화적 |

## 구매 및 배치 권장 사항

- 교육/연구 기관은 SDK, ROS2 및 Jetson Orin 컴퓨팅 지원을 위해 G1 EDU 버전을 우선 선택하는 것을 권장합니다.
- 배치 시 현장에 충분한 안전 공간을 확보하고, 비상 정지 장치 및 보호 펜스를 설치해야 합니다.

## 참고 자료

1. [Unitree G1 제품 페이지](https://www.unitree.com/g1)
2. [Robozaps – Unitree G1 Review](https://blog.robozaps.com/b/unitree-g1-review)
3. [Humanoid.Guide – Unitree G1](https://humanoid.guide/product/g1/)
4. [Humanoid Index – G1](https://humanoidindex.org/robots/g1)
