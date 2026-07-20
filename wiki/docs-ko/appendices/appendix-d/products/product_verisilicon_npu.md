# VeriSilicon VIP9000 NPU IP / VeriSilicon VIP9000

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [VeriSilicon](../companies/company_verisilicon.md) |
| **제품 카테고리** | 신경망 프로세서 IP (NPU IP) |
| **출시일** | VIP9000 시리즈 지속적 업데이트 |
| **상태** | 상용 라이선스 |
| **공식 홈페이지/출처** | VeriSilicon 공식 홈페이지, 제품 매뉴얼 |

## 제품 개요

VeriSilicon VIP9000 시리즈는 구성 가능하고 확장 가능한 신경망 프로세서 IP로, 엣지 AI, 스마트 자동차, 소비자 가전 및 로봇 칩에 고효율 AI 가속 성능을 제공합니다.

VIP9000은 INT8/INT16/FP16/BFloat16 등의 정밀도를 지원하며, CNN, Transformer 및 대규모 언어 모델 등 주요 네트워크를 실행할 수 있습니다. 고도로 구성 가능한 하드웨어 아키텍처를 통해 고객은 연산 성능, 전력 소비 및 면적 목표에 따라 유연하게 맞춤 설정할 수 있으며, VeriSilicon의 ISP, GPU, 비디오 코덱 IP와 협력하여 종단 간 비전 및 AI 솔루션을 구축할 수 있습니다.

## 제품 이미지

> VeriSilicon VIP9000: [공식 자료](https://www.verisilicon.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| IP 이름 | VeriSilicon VIP9000 시리즈 NPU | VeriSilicon 공식 홈페이지 |
| 유형 | 신경망 프로세서 IP | VeriSilicon 공개 자료 |
| 연산 성능 범위 | 0.5–수백 TOPS (구성에 따라 다름) | VeriSilicon 공개 자료 |
| 정밀도 지원 | INT8 / INT16 / FP16 / BFloat16 | VeriSilicon 공개 자료 |
| 모델 지원 | TensorFlow / PyTorch / ONNX 등 | VeriSilicon 공개 자료 |
| 버스 인터페이스 | AXI / AHB | VeriSilicon 공개 자료 |
| 공정 | 고객 선택 가능 | 공개 보도 |
| 전력 소비 | 고객 구현에 따라 다름 | VeriSilicon 공개 자료 |
| 라이선스 모드 | IP 라이선스 + 칩 맞춤 서비스 | VeriSilicon 공개 자료 |
| 가격 | IP 라이선스, 미공개 | - |

## 공급망 위치

- **제조사**: [VeriSilicon](../companies/company_verisilicon.md)
- **핵심 부품/기술 출처**: 자체 개발 NPU 마이크로아키텍처, EDA 도구, 고객 웨이퍼 파운드리/패키징 및 테스트.
- **하위 응용 분야/고객**: 칩 설계 회사, IDM, 팹리스, 자동차 전자, 소비자 가전, 로봇 칩 제조사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_verisilicon_vip9000`
- 부품 엔터티: `ent_component_verisilicon_vip9000_npu`
- 제조사 엔터티: `ent_company_verisilicon`
- 주요 관계:
  - `rel_ent_company_verisilicon_manufactures_ent_product_verisilicon_vip9000` (`ent_company_verisilicon` → `manufactures` --> `ent_product_verisilicon_vip9000`)
  - `rel_ent_company_verisilicon_manufactures_ent_component_verisilicon_vip9000_npu` (`ent_company_verisilicon` → `manufactures` --> `ent_component_verisilicon_vip9000_npu`)
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## 응용 시나리오

- **로봇 엣지 인식**: 로봇 SoC에 통합되어 비전, 음성 및 멀티모달 AI 추론 구현.
- **스마트 자동차 ADAS**: 전방 시야, 서라운드 뷰 및 차량 내 인식 시스템에 사용.
- **스마트 보안 및 AIoT**: IPC, 초인종, 웨어러블 기기의 고효율 AI 비전 지원.

## 경쟁 비교

| 비교 항목 | VeriSilicon VIP9000 | ARM Ethos | Synopsys ARC NPU |
|--------|------|------|------|
| 유형 | NPU IP | NPU IP | NPU IP |
| 구성 가능성 | 높음 | 중간 | 높음 |
| 생태계 협력 | ISP/GPU/비디오 IP 협력 | ARM 생태계 | Synopsys 생태계 |
| 라이선스 모드 | IP 라이선스 | IP 라이선스 | IP 라이선스 |

## 구매 및 배포 권장 사항

- 대상 모델, 연산 성능 및 전력 소비 예산에 따라 VIP9000 구성과 버스 인터페이스를 선택하세요.
- 모델 양자화 및 컴파일 도구 체인이 대상 네트워크에 대한 적응 효과를 평가하세요.
- VeriSilicon 공식 채널을 통해 IP 평가 패키지, 참조 설계 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: VeriSilicon](../companies/company_verisilicon.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [VeriSilicon 공식 홈페이지](https://www.verisilicon.com)
2. [VeriSilicon AI 프로세서 IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. VeriSilicon 2024 연례 보고서
