# 지푸 AI / Zhipu AI

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 智谱 AI |
| **영문명** | Zhipu AI |
| **본사** | 중국 베이징 |
| **설립 시간** | 2019 |
| **공식 사이트** | [https://www.zhipuai.cn / https://open.bigmodel.cn](https://www.zhipuai.cn) |
| **공급망环节** | 대규모 언어 모델, 멀티모달 모델, 구현 지능, AI Agent |
| **기업 속성** | 유니콘 기업, 칭화 계열, GLM 대모델 팀 |
| **모회사/소속 그룹** | 독립 운영 (베이징 지푸 화장 과기 유한공사) |
| **데이터 출처** | 지푸 AI 공식 사이트, 오픈 플랫폼 문서, GitHub 기술 보고서 |

## 회사 소개

지푸 AI (Zhipu AI)는 칭화대학교 컴퓨터과학과 지식공학 연구실의 기술 성과 전환을 통해 설립되었으며, 국산 자주 제어 가능한 범용 인공지능 대규모 모델 개발에 주력하고 있습니다. 회사는 GLM (General Language Model) 아키텍처를 기반으로 GLM-4 시리즈 대규모 모델을 출시하고, 시각 언어 모델 GLM-4V, 코드 모델 CodeGeeX, 비디오 생성 CogVideo 및 구현 지능 Agent 플랫폼 AutoGLM으로 확장했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| GLM 대규모 언어 모델 | 범용 대화 및 추론 | GLM-4 / GLM-4-Plus / GLM-4-Long | 기업 응용, 연구 |
| 멀티모달 모델 | 이미지/텍스트/비디오 이해 및 생성 | GLM-4V / CogView / CogVideo | 콘텐츠 제작, 로봇 VLA |
| 코드 및 Agent | 코드 생성 및 자율 Agent | CodeGeeX / AutoGLM | 소프트웨어 개발, 구현 지능 |
| 오픈 플랫폼 | API 및 업종 솔루션 | BigModel | 금융, 교육, 에너지, 로봇 |

## 대표 제품

### 지푸 AI GLM-4 대규모 모델

> 지푸 AI GLM-4 대규모 모델: [공식 자료](https://www.zhipuai.cn)를 방문하여 확인하세요.

| 규격 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 범용 대규모 언어 모델 / 멀티모달 대규모 모델 | 지푸 AI 공식 사이트 |
| 아키텍처 | GLM (General Language Model) | 지푸 AI 공식 사이트 |
| 매개변수 수 | 미공개 (수백억/수천억 규모) | 지푸 AI 공식 사이트 |
| 컨텍스트 길이 | 128K (표준판) / 최대 1M (GLM-4-Long) | 지푸 AI 공식 사이트 |
| 멀티모달 | GLM-4V 이미지/비디오 이해 지원 | 지푸 AI 공식 사이트 |
| 추론 능력 | GLM-4-Plus 심층 추론 지원 | 지푸 AI 공식 사이트 |
| 도구 호출 | Function Call, 코드 인터프리터, 인터넷 연결 지원 | 지푸 AI 공식 사이트 |
| Agent 능력 | AutoGLM 자율 작업 실행 지원 | 지푸 AI 공식 사이트 |
| 인터페이스 | REST API / SSE 스트리밍 | 지푸 오픈 플랫폼 |
| 배포 방식 | 클라우드 API / 프라이빗 배포 | 지푸 오픈 플랫폼 |
| 오픈소스 버전 | GLM-4-9B 시리즈 (HuggingFace/GitHub) | GitHub THUDM/GLM-4 |
| 가격 | 사용량 기반 과금 (API) / 미공개 (프라이빗) | - |

**기술亮点**: 국산 자주 GLM 아키텍처, 긴 텍스트/멀티모달/심층 추론, Agent 및 도구 호출 능력, 오픈소스 9B 생태계.

**응용 시나리오**: 스마트 고객 서비스, 지식 Q&A, 콘텐츠 제작, 코드 생성, 로봇 VLA, 구현 지능 의사 결정, 금융/교육/에너지 업종 솔루션.

### 지푸 AI CodeGeeX 코드 대규모 모델

> 지푸 AI CodeGeeX 코드 대규모 모델: [공식 자료](https://www.zhipuai.cn)를 방문하여 확인하세요.

| 규격 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 코드 생성 대규모 모델 | 지푸 AI 공식 사이트 |
| 기능 | 코드 완성, 주석, 수정, 번역 | 지푸 AI 공식 사이트 |
| 버전 | CodeGeeX-4 | 지푸 AI 공식 사이트 |
| 가격 | 미공개 | - |

**기술亮点**: 다국어 코드 생성 및 지능형 에이전트 프로그래밍 지원, 소프트웨어 개발 효율성 향상.

**응용 시나리오**: IDE 플러그인, 소프트웨어 공학, 자동화 프로그래밍.

## 공급망 위치

- **상류 핵심 부품/소재**: GPU/AI 연산 클러스터, 훈련 데이터, RLHF 레이블링, 추론 프레임워크
- **하류 고객/응용 시나리오**: 기업 개발자, 로봇 제조사, 인터넷 기업, 연구 기관, 수직 업종 ISV
- **주요 경쟁사/대상**: OpenAI GPT-4, Anthropic Claude, 알리바바 통이첸원, 바이두 원신이옌, 바이트 도우바오

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_zhipu_ai`
- 제품 엔터티: `ent_product_zhipu_glm4`
- 부품 엔터티: `ent_component_zhipu_glm4_model_core`
- 주요 관계:
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_product_zhipu_glm4`
  - `ent_company_zhipu_ai` -- `manufactures` --> `ent_component_zhipu_glm4_model_core`
  - `ent_product_zhipu_glm4` -- `uses` --> `ent_component_zhipu_glm4_model_core`

## 참고 자료

1. [지푸 AI 공식 사이트](https://www.zhipuai.cn)
2. [지푸 AI GLM-4 대규모 모델 제품/자료 페이지](https://open.bigmodel.cn/dev/api/normal-model/glm-4)
3. 회사 연례 보고서, 제품 데이터시트 및 공개 보도자료
4. [부록 D 제품 목록](../index-products.md)
