# 芯原股份 / VeriSilicon

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 芯原股份 |
| **영문명** | VeriSilicon Holdings |
| **본사** | 중국 상하이시 푸동신구 |
| **설립일** | 2001년 |
| **공식 홈페이지** | [https://www.verisilicon.com](https://www.verisilicon.com) |
| **공급망 단계** | 칩 설계 서비스, 반도체 IP, AI/비디오/디스플레이 IP |
| **기업 속성** | 상장 기업 (科创板: 688521) |
| **모회사/소속 그룹** | 없음 (독립 상장 주체) |
| **데이터 출처** | VeriSilicon 공식 홈페이지, 연례 보고서, 제품 매뉴얼, 공개 보도 자료 |

## 회사 소개

VeriSilicon은 중국을 선도하는 칩 설계 서비스 및 반도체 IP 제공업체로, 글로벌 고객에게 원스톱 칩 맞춤 설계 및 IP 라이선스 서비스를 제공합니다.

VeriSilicon은 칩 설계 플랫폼, 비디오/디스플레이 IP, AI 가속 IP, RF/인터페이스 IP에 이르는 완벽한 역량을 보유하고 있으며, VIP9000/VIP9400 시리즈 신경망 프로세서 IP는 엣지 AI, 스마트 자동차, 사물인터넷 및 로봇 칩에 널리 사용됩니다. 회사는 "경량 설계" 모델을 채택하여 칩을 직접 판매하지 않고 IP 라이선스 및 칩 맞춤 설계 서비스를 통해 고객을 지원합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| AI 프로세서 IP | 신경망 가속기 IP | VIP9000 / VIP9400 / NPU IP | 엣지 AI, 자동차, 로봇 |
| 비디오 IP | 비디오 코덱 및 ISP | Hantro / Vivante ISP | 보안, 자동차, 소비자 가전 |
| 디스플레이 IP | GPU/디스플레이 컨트롤러 | Vivante GPU / DC | 모바일, 자동차, IoT |
| 칩 맞춤 설계 서비스 | 원스톱 칩 설계 | 고객 맞춤형 SoC | 다양한 산업 |

## 대표 제품

### VeriSilicon VIP9000 시리즈 NPU IP

> VeriSilicon VIP9000: [공식 자료](https://www.verisilicon.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 아키텍처 | 구성 가능한 신경망 프로세서 IP | VeriSilicon 공개 자료 |
| 연산 성능 | 0.5–수백 TOPS (구성에 따라 다름) | VeriSilicon 공개 자료 |
| 정밀도 지원 | INT8 / INT16 / FP16 / BFloat16 | VeriSilicon 공개 자료 |
| 모델 지원 | TensorFlow / PyTorch / ONNX 등 | VeriSilicon 공개 자료 |
| 버스 인터페이스 | AXI / AHB | VeriSilicon 공개 자료 |
| 공정 | 고객 선택 가능 (공개 보도) | 공개 보도 |
| 전력 소비 | 고객 구현에 따라 다름 | VeriSilicon 공개 자료 |
| 가격 | IP 라이선스, 미공개 | - |

**기술적 특징**: 고도로 구성 가능한 NPU IP, Transformer 및 대규모 모델 지원, ISP/GPU와의 협력, 저전력 엣지 AI.

**응용 시나리오**: 스마트폰, 자동차 ADAS, 보안 IPC, 로봇 엣지 인식, AIoT.

### VeriSilicon Vivante GPU IP

> VeriSilicon Vivante GPU: [공식 자료](https://www.verisilicon.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 아키텍처 | 확장 가능한 GPU / GPGPU IP | VeriSilicon 공개 자료 |
| 성능 | 저사양부터 차량용 고성능까지 구성에 따라 다름 | VeriSilicon 공개 자료 |
| API 지원 | OpenGL ES / Vulkan / OpenCL 등 | VeriSilicon 공개 자료 |
| 기능 안전 | 일부 IP는 ASIL-B/D 지원 | VeriSilicon 공개 자료 |
| 응용 시나리오 | 디스플레이, 그래픽 렌더링, 범용 컴퓨팅 | VeriSilicon 공개 자료 |
| 가격 | IP 라이선스, 미공개 | - |

**기술적 특징**: 소면적 저전력, 자동차 기능 안전 인증, NPU/ISP와 결합하여 완벽한 비주얼 컴퓨팅 솔루션 제공.

**응용 시나리오**: 차량용 인포테인먼트, 계기판, 로봇 HMI, 산업용 디스플레이.

## 공급망 위치

- **상류 핵심 부품/재료**: EDA 도구, IP 라이선스, 웨이퍼 파운드리 파트너, 패키징 및 테스트.
- **하류 고객/응용 시나리오**: 칩 설계 회사, IDM, 팹리스, 자동차 전자, 소비자 가전, 로봇 칩 제조사.
- **주요 경쟁사/벤치마크**: ARM Mali/Immortalis, Imagination PowerVR, Synopsys ARC NPU, Cadence Tensilica.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_verisilicon`
- 제품 엔터티: `ent_product_verisilicon_vip9000`
- 부품 엔터티: `ent_component_verisilicon_vip9000_npu`
- 주요 관계:
  - `ent_company_verisilicon` -- `manufactures` --> `ent_product_verisilicon_vip9000`
  - `ent_company_verisilicon` -- `manufactures` --> `ent_component_verisilicon_vip9000_npu`
  - `ent_product_verisilicon_vip9000` -- `uses` --> `ent_component_verisilicon_vip9000_npu`

## 참고 자료

1. [VeriSilicon 공식 홈페이지](https://www.verisilicon.com)
2. [VeriSilicon AI 프로세서 IP](https://www.verisilicon.com/IPPortfolio/Artificial-Intelligence-IP.html)
3. VeriSilicon 2024년 연례 보고서
