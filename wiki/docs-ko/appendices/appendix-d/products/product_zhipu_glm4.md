# 지푸 AI GLM-4 대규모 언어 모델 / Zhipu AI GLM-4 Large Language Model

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [지푸 AI / Zhipu AI](../companies/company_zhipu_ai.md) |
| **제품 카테고리** | 범용 대규모 언어 모델 / 멀티모달 대규모 모델 |
| **출시일** | 2024년 출시, 지속적 반복 (GLM-4-Plus 등) |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [지푸 AI GLM-4 대규모 모델 제품/자료 페이지](https://open.bigmodel.cn/dev/api/normal-model/glm-4) |

## 제품 개요

GLM-4는 지푸 AI가 출시한 차세대 범용 대규모 언어 모델로, 자체 개발 GLM 아키텍처를 기반으로 훈련되었으며 강력한 언어 이해, 명령 수행, 장문 처리, 논리 추론 및 다중 턴 대화 능력을 갖추고 있습니다. GLM-4 시리즈는 표준 버전, Plus 추론 버전, Long 장문 버전, Flash 경량 버전 및 9B 오픈소스 버전을 포함하며, BigModel 오픈 플랫폼을 통해 API 서비스를 제공하여 스마트 고객 서비스, 지식 Q&A, 코드 생성 및 로봇 VLA 등의 애플리케이션을 지원할 수 있습니다.

## 제품 이미지

> 지푸 AI GLM-4 대규모 모델: [공식 자료](https://open.bigmodel.cn/dev/api/normal-model/glm-4)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 범용 대규모 언어 모델 / 멀티모달 대규모 모델 | 지푸 AI 공식 홈페이지 |
| 아키텍처 | GLM (General Language Model) | 지푸 AI 공식 홈페이지 |
| 매개변수 수 | 미공개 (수백억/수천억 규모) | 지푸 AI 공식 홈페이지 |
| 컨텍스트 길이 | 128K (표준 버전) / 최대 1M (GLM-4-Long) | 지푸 AI 공식 홈페이지 |
| 멀티모달 | GLM-4V 이미지/비디오 이해 지원 | 지푸 AI 공식 홈페이지 |
| 추론 능력 | GLM-4-Plus 심층 추론 지원 | 지푸 AI 공식 홈페이지 |
| 도구 호출 | Function Call, 코드 인터프리터, 인터넷 연결 지원 | 지푸 AI 공식 홈페이지 |
| Agent 능력 | AutoGLM 자율 작업 실행 지원 | 지푸 AI 공식 홈페이지 |
| 인터페이스 | REST API / SSE 스트리밍 | 지푸 오픈 플랫폼 |
| 배포 방식 | 클라우드 API / 프라이빗 배포 | 지푸 오픈 플랫폼 |
| 오픈소스 버전 | GLM-4-9B 시리즈 (HuggingFace/GitHub) | GitHub THUDM/GLM-4 |
| 가격 | 사용량 기반 과금 (API) / 미공개 (프라이빗) | - |

## 공급망 위치

- **제조사**: [지푸 AI / Zhipu AI](../companies/company_zhipu_ai.md)
- **핵심 부품/기술 출처**: GPU/AI 연산 클러스터, 훈련 데이터, RLHF 레이블링, 추론 프레임워크
- **하위 애플리케이션/고객**: 기업 개발자, 로봇 제조사, 인터넷 기업, 연구 기관, 수직 산업 ISV

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_zhipu_glm4`
- 부품 엔터티: `ent_component_zhipu_glm4_model_core`
- 제조사 엔터티: `ent_company_zhipu_ai`
- 주요 관계:
  - `rel_ent_company_zhipu_ai_manufactures_ent_product_zhipu_glm4` (`ent_company_zhipu_ai` → `manufactures` → `ent_product_zhipu_glm4`)
  - `rel_ent_company_zhipu_ai_manufactures_ent_component_zhipu_glm4_model_core` (`ent_company_zhipu_ai` → `manufactures` → `ent_component_zhipu_glm4_model_core`)
  - `ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`

## 애플리케이션 시나리오

- **스마트 고객 서비스, 지식 Q&A, 콘텐츠 제작, 코드 생성, 로봇 VLA, 구현 지능 의사 결정, 금융/교육/에너지 산업 솔루션**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 제안

- 대상 애플리케이션의 해상도, 측정 범위, 정밀도 또는 연산 요구 사항에 따라 특정 모델을 선택하세요.
- 배포 전 인터페이스, 전원 공급, 방열, 기계 장착 및 환경 온도 범위가 일치하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 지푸 AI / Zhipu AI](../companies/company_zhipu_ai.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [지푸 AI 공식 홈페이지](https://www.zhipuai.cn)
2. [지푸 AI GLM-4 대규모 모델 제품/자료 페이지](https://open.bigmodel.cn/dev/api/normal-model/glm-4)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 디렉토리](../index-companies.md)
