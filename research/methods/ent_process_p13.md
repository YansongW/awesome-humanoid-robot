---
$id: ent_process_p13
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Electronics & Power Systems
  zh: 电子电气与能源系统（Electronics & Power）
  ko: 电子电气与能源系统（Electronics & Power）
summary:
  en: Electronics & Power Systems—Phase 13 of the full lifecycle for humanoid robot product development, encompassing system
    design, implementation and validation, and document delivery.
  zh: 电子电气与能源系统（Electronics & Power）是人形机器人产品开发全流程中的第 13 个阶段，在 WBS V3 中展开为若干三级子任务。
  ko: 电子电气与能源系统（Electronics & Power）
domains:
- 02_components
- 08_software_middleware
layers:
- intelligence
- upstream
functional_roles:
- process
- knowledge
tags: []
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body restructured into standard sections by scripts/restructure_entry_bodies.py. English name/summary machine-translated
    from Chinese by scripts/backfill_en_translations.py.
sources:
- id: wbs_v3_report
  type: report
  title: 全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）
  date: '2026-06-27'
theoretical_depth:
- system
---



## 概述
电子电气与能源系统（Electronics & Power）是人形机器人产品开发全流程中的第 13 个阶段，在 WBS V3 中展开为若干三级子任务。
## 核心内容
该阶段覆盖输入梳理、方案设计、实施/原型、验证闭环与文档交付等完整工程动作，是确保下游依赖方获得合格输入的关键节点。

## 关键子任务与技术内容
#### 计算与通信硬件

##### 计算平台架构与选型
- **方法 / 工具**：Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布
- **设计思考逻辑**：AI 任务用 GPU，实时控制用 MCU/FPGA，安全监控独立
- **关键约束**：功耗、散热、重量、实时性、功能安全
- **完成标准 / 输出物**：计算架构图、各节点算力/功耗预算、安全分区
**三级子任务：**
- **P13.1.1.1 输入梳理与目标量化**：整理「计算平台架构与选型」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.1.1.2 候选方案建立与评估**：针对「计算平台架构与选型」建立候选方案库，使用「Jetson / Intel NUC / 自研载板 / FPGA / MCU 分布」进行量化评估，考虑成本、性能、供应链、可维护性后确定最终方案。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.1.1.3 实施/原型/样件制作**：根据设计方案执行「计算平台架构与选型」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.1.1.4 验证与问题闭环**：对「计算平台架构与选型」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.1.1.5 文档输出与下游交付**：输出「计算平台架构与选型」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 自研/外购 PCB 设计
- **方法 / 工具**：载板、关节驱动板、传感器接口板、安全监控板
- **设计思考逻辑**：将计算、通信、电源、安全功能固化到可靠硬件
- **关键约束**：EMC、SI/PI、热、空间、可制造性
- **完成标准 / 输出物**：原理图、PCB、BOM、DFM 报告
**三级子任务：**
- **P13.1.2.1 输入梳理与目标量化**：整理「自研/外购 PCB 设计」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.1.2.2 概念与详细设计**：完成「自研/外购 PCB 设计」的概念设计、详细设计与接口定义，使用「载板、关节驱动板、传感器接口板、安全监控板」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.1.2.3 实施/原型/样件制作**：根据设计方案执行「自研/外购 PCB 设计」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.1.2.4 验证与问题闭环**：对「自研/外购 PCB 设计」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.1.2.5 文档输出与下游交付**：输出「自研/外购 PCB 设计」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 通信网络与同步
- **方法 / 工具**：CAN-FD、EtherCAT、Ethernet、TSN、PTP 时间同步
- **设计思考逻辑**：关节控制需要高实时性，视觉/AI 需要高带宽；关键信号冗余
- **关键约束**：线缆数量、EMC、成本、可扩展性
- **完成标准 / 输出物**：通信拓扑图、协议分配、带宽/延迟预算、同步精度
**三级子任务：**
- **P13.1.3.1 输入梳理与目标量化**：整理「通信网络与同步」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.1.3.2 方案/方法设计**：针对「通信网络与同步」制定实施方法或候选方案，使用「CAN-FD、EtherCAT、Ethernet、TSN、PTP 时间同步」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.1.3.3 实施/原型/样件制作**：根据设计方案执行「通信网络与同步」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.1.3.4 验证与问题闭环**：对「通信网络与同步」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.1.3.5 文档输出与下游交付**：输出「通信网络与同步」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 电源与能源

##### 电池包设计与 BMS
- **方法 / 工具**：锂电池选型、模组设计、SOC/SOH 估算、快充策略、热失控防护
- **设计思考逻辑**：续航与重量平衡；BMS 需过充/过放/过温保护
- **关键约束**：安全认证、热失控、循环寿命、成本
- **完成标准 / 输出物**：电池包方案、BMS 规格、续航估算、安全测试
**三级子任务：**
- **P13.2.1.1 输入梳理与目标量化**：整理「电池包设计与 BMS」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.2.1.2 概念与详细设计**：完成「电池包设计与 BMS」的概念设计、详细设计与接口定义，使用「锂电池选型、模组设计、SOC/SOH 估算、快充策略、热失控防护」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.2.1.3 实施/原型/样件制作**：根据设计方案执行「电池包设计与 BMS」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.2.1.4 验证与问题闭环**：对「电池包设计与 BMS」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.2.1.5 文档输出与下游交付**：输出「电池包设计与 BMS」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 电源分配与 DC-DC
- **方法 / 工具**：母线电压选择、DC-DC 模块、滤波、OR-ing、冗余
- **设计思考逻辑**：电机母线与逻辑电源隔离；故障时安全断电
- **关键约束**：压降、效率、EMI、安全标准
- **完成标准 / 输出物**：电源分配图、DC-DC 选型、效率/热测试
**三级子任务：**
- **P13.2.2.1 输入梳理与目标量化**：整理「电源分配与 DC-DC」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.2.2.2 方案/方法设计**：针对「电源分配与 DC-DC」制定实施方法或候选方案，使用「母线电压选择、DC-DC 模块、滤波、OR-ing、冗余」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.2.2.3 实施/原型/样件制作**：根据设计方案执行「电源分配与 DC-DC」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.2.2.4 验证与问题闭环**：对「电源分配与 DC-DC」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.2.2.5 文档输出与下游交付**：输出「电源分配与 DC-DC」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 充电与能源管理
- **方法 / 工具**：充电桩/座、无线充电、充电协议、能量回收
- **设计思考逻辑**：补能体验影响可用性；需兼容目标场景
- **关键约束**：安全、标准、成本、空间
- **完成标准 / 输出物**：充电方案、充电时间、BMS 通信协议
**三级子任务：**
- **P13.2.3.1 输入梳理与目标量化**：整理「充电与能源管理」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.2.3.2 方案/方法设计**：针对「充电与能源管理」制定实施方法或候选方案，使用「充电桩/座、无线充电、充电协议、能量回收」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.2.3.3 实施/原型/样件制作**：根据设计方案执行「充电与能源管理」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.2.3.4 验证与问题闭环**：对「充电与能源管理」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.2.3.5 文档输出与下游交付**：输出「充电与能源管理」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

#### 安全与 EMC

##### 硬件急停与安全链
- **方法 / 工具**：硬件急停、看门狗、熔断、安全 PLC/继电器、双通道
- **设计思考逻辑**：任何软件失效都能通过硬件切断动力；符合功能安全
- **关键约束**：响应时间、可靠性、误触发
- **完成标准 / 输出物**：安全系统原理图、FMEA、急停响应时间 < 目标
**三级子任务：**
- **P13.3.1.1 输入梳理与目标量化**：整理「硬件急停与安全链」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.3.1.2 方案/方法设计**：针对「硬件急停与安全链」制定实施方法或候选方案，使用「硬件急停、看门狗、熔断、安全 PLC/继电器、双通道」进行论证，明确技术路线与资源需求。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.3.1.3 实施/原型/样件制作**：根据设计方案执行「硬件急停与安全链」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.3.1.4 验证与问题闭环**：对「硬件急停与安全链」输出进行验证，检查是否满足完成标准，记录问题并跟踪至关闭。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.3.1.5 文档输出与下游交付**：输出「硬件急停与安全链」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### EMC/EMI 设计与测试
- **方法 / 工具**：屏蔽、滤波、接地、PCB 布局、辐射/传导测试
- **设计思考逻辑**：大功率电机驱动与高速计算共存，EMC 风险高
- **关键约束**：CE/FCC/UL 标准、重量、成本
- **完成标准 / 输出物**：EMC 设计规范、预测试报告、整改记录
**三级子任务：**
- **P13.3.2.1 输入梳理与目标量化**：整理「EMC/EMI 设计与测试」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确 Owner 与里程碑。
**四级关键动作：**
1. 列出所有上游输入清单并确认版本
2. 将验收标准转化为可量化 KPI
3. 建立任务 Owner、时间节点与风险登记
- **P13.3.2.2 概念与详细设计**：完成「EMC/EMI 设计与测试」的概念设计、详细设计与接口定义，使用「屏蔽、滤波、接地、PCB 布局、辐射/传导测试」验证可行性，输出图纸/算法/逻辑框架。
**四级关键动作：**
1. 形成不少于 2 个候选方案
2. 建立评估矩阵并量化打分
3. 组织评审并冻结方案
- **P13.3.2.3 实施/原型/样件制作**：根据设计方案执行「EMC/EMI 设计与测试」的实施工作，制作原型、样件或完成关键步骤，记录过程数据。
**四级关键动作：**
1. 建立模型/样机并记录关键参数
2. 执行仿真或原型验证
3. 记录异常与偏差
- **P13.3.2.4 测试执行与结果分析**：按照验收标准执行「EMC/EMI 设计与测试」测试，统计通过率/误差/偏差，进行根因分析并形成改进清单。
**四级关键动作：**
1. 制定测试/评审计划与通过准则
2. 执行测试并记录原始数据
3. 输出问题清单与改进措施
- **P13.3.2.5 文档输出与下游交付**：输出「EMC/EMI 设计与测试」最终报告/图纸/规范，更新 ICD/BOM/SOP/需求追溯链，完成向下游环节的正式交付。
**四级关键动作：**
1. 按模板编写文档并引用原始数据
2. 完成内部评审与版本控制
3. 发布并通知下游依赖方

##### 网络安全架构设计
- **方法 / 工具**：Secure Boot、通信加密（TLS/AES）、访问控制、OTA 签名、漏洞管理流程
- **设计思考逻辑**：联网机器人面临固件篡改、数据窃取、远程攻击风险，需要纵深防御
- **关键约束**：实时性、算力、密钥管理、法规（如 UN R155）
- **完成标准 / 输出物**：安全启动链、OTA 签名验证、漏洞响应流程
**三级子任务：**
- **P13.3.3.1 输入梳理与目标量化**：整理「网络安全架构设计」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P13.3.3.2 方案/方法设计**：针对「网络安全架构设计」制定实施方法或候选方案，使用「Secure Boot、通信加密（TLS/AES）、访问控制、OTA 签名、漏洞管理流程」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P13.3.3.3 实施/建模/实验**：根据方案执行「网络安全架构设计」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P13.3.3.4 验证与优化**：对「网络安全架构设计」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P13.3.3.5 文档输出与下游交付**：输出「网络安全架构设计」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

##### 功能安全详细设计
- **方法 / 工具**：安全 PLC/安全继电器、双通道编码器、STO（Safe Torque Off）、故障安全状态机
- **设计思考逻辑**：将功能安全概念落地为硬件与软件的故障检测、响应与降级机制
- **关键约束**：SIL/PL 等级、响应时间、成本
- **完成标准 / 输出物**：FUSA 详细设计文档、故障注入测试通过、STO 响应时间达标
**三级子任务：**
- **P13.3.4.1 输入梳理与目标量化**：整理「功能安全详细设计」所需输入、参考标准，将验收标准转化为可量化 KPI。
**四级关键动作：**
1. 列出上游输入与验收指标
2. 确认版本与责任人
3. 建立追踪表
- **P13.3.4.2 方案/方法设计**：针对「功能安全详细设计」制定实施方法或候选方案，使用「安全 PLC/安全继电器、双通道编码器、STO（Safe Torque Off）、故障安全状态机」论证。
**四级关键动作：**
1. 形成候选方案
2. 建立评估矩阵
3. 组织评审并冻结方案
- **P13.3.4.3 实施/建模/实验**：根据方案执行「功能安全详细设计」的实施工作，建立模型、样机或完成实验。
**四级关键动作：**
1. 明确输入/方法/输出
2. 执行并记录关键数据
3. 与上下游确认接口
- **P13.3.4.4 验证与优化**：对「功能安全详细设计」结果进行验证，分析偏差并迭代优化。
**四级关键动作：**
1. 制定测试计划
2. 执行测试并记录
3. 输出问题清单与改进
- **P13.3.4.5 文档输出与下游交付**：输出「功能安全详细设计」最终报告/规范，更新 ICD/BOM/SOP/需求追溯链。
**四级关键动作：**
1. 按模板编写
2. 内部评审
3. 发布并通知下游

## 完成标准
本阶段所有三级子任务均通过验收评审，关键输出物版本受控并正式交付给下游依赖方。

## 参考
- 《全尺寸双足人形机器人产品开发全流程报告（V3 / 三四级任务展开版）》

## Overview
Electronics & Power is the 13th stage in the full-process development of humanoid robots, expanded into several Level-3 sub-tasks in WBS V3.
## Content
This stage covers complete engineering actions including input review, solution design, implementation/prototyping, verification closure, and documentation delivery, serving as a critical node to ensure downstream dependencies receive qualified inputs.

## Key Sub-tasks and Technical Content
#### Computing and Communication Hardware

##### Computing Platform Architecture and Selection
- **Methods/Tools**: Jetson / Intel NUC / Custom carrier board / FPGA / MCU distribution
- **Design Logic**: GPU for AI tasks, MCU/FPGA for real-time control, independent safety monitoring
- **Key Constraints**: Power consumption, heat dissipation, weight, real-time performance, functional safety
- **Completion Criteria/Deliverables**: Computing architecture diagram, compute/power budget per node, safety partitioning
**Level-3 Sub-tasks:**
- **P13.1.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Computing Platform Architecture and Selection," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.1.1.2 Candidate Solution Development and Evaluation**: Build a candidate solution library for "Computing Platform Architecture and Selection," perform quantitative evaluation using "Jetson / Intel NUC / Custom carrier board / FPGA / MCU distribution," and finalize the solution considering cost, performance, supply chain, and maintainability.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.1.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Computing Platform Architecture and Selection" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.1.1.4 Verification and Issue Closure**: Verify the output of "Computing Platform Architecture and Selection," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.1.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Computing Platform Architecture and Selection," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Custom/Off-the-Shelf PCB Design
- **Methods/Tools**: Carrier board, joint driver board, sensor interface board, safety monitoring board
- **Design Logic**: Consolidate computing, communication, power, and safety functions into reliable hardware
- **Key Constraints**: EMC, SI/PI, thermal, space, manufacturability
- **Completion Criteria/Deliverables**: Schematic, PCB, BOM, DFM report
**Level-3 Sub-tasks:**
- **P13.1.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Custom/Off-the-Shelf PCB Design," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.1.2.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Custom/Off-the-Shelf PCB Design," verify feasibility using "Carrier board, joint driver board, sensor interface board, safety monitoring board," and output drawings/algorithms/logic frameworks.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.1.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Custom/Off-the-Shelf PCB Design" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.1.2.4 Verification and Issue Closure**: Verify the output of "Custom/Off-the-Shelf PCB Design," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.1.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Custom/Off-the-Shelf PCB Design," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Communication Network and Synchronization
- **Methods/Tools**: CAN-FD, EtherCAT, Ethernet, TSN, PTP time synchronization
- **Design Logic**: Joint control requires high real-time performance; vision/AI requires high bandwidth; critical signal redundancy
- **Key Constraints**: Cable count, EMC, cost, scalability
- **Completion Criteria/Deliverables**: Communication topology diagram, protocol allocation, bandwidth/latency budget, synchronization accuracy
**Level-3 Sub-tasks:**
- **P13.1.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Communication Network and Synchronization," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.1.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Communication Network and Synchronization," demonstrate using "CAN-FD, EtherCAT, Ethernet, TSN, PTP time synchronization," and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.1.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Communication Network and Synchronization" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.1.3.4 Verification and Issue Closure**: Verify the output of "Communication Network and Synchronization," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.1.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Communication Network and Synchronization," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Power and Energy

##### Battery Pack Design and BMS
- **Methods/Tools**: Lithium battery selection, module design, SOC/SOH estimation, fast charging strategy, thermal runaway protection
- **Design Logic**: Balance between range and weight; BMS requires overcharge/overdischarge/overtemperature protection
- **Key Constraints**: Safety certification, thermal runaway, cycle life, cost
- **Completion Criteria/Deliverables**: Battery pack solution, BMS specifications, range estimation, safety testing
**Level-3 Sub-tasks:**
- **P13.2.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Battery Pack Design and BMS," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.2.1.2 Concept and Detailed Design**: Complete concept design, detailed design, and interface definition for "Battery Pack Design and BMS," verify feasibility using "Lithium battery selection, module design, SOC/SOH estimation, fast charging strategy, thermal runaway protection," and output drawings/algorithms/logic frameworks.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.2.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Battery Pack Design and BMS" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.2.1.4 Verification and Issue Closure**: Verify the output of "Battery Pack Design and BMS," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.2.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Battery Pack Design and BMS," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Power Distribution and DC-DC
- **Methods/Tools**: Bus voltage selection, DC-DC modules, filtering, OR-ing, redundancy
- **Design Logic**: Isolate motor bus from logic power; safe power-off during faults
- **Key Constraints**: Voltage drop, efficiency, EMI, safety standards
- **Completion Criteria/Deliverables**: Power distribution diagram, DC-DC selection, efficiency/thermal testing
**Level-3 Sub-tasks:**
- **P13.2.2.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Power Distribution and DC-DC," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.2.2.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Power Distribution and DC-DC," demonstrate using "Bus voltage selection, DC-DC modules, filtering, OR-ing, redundancy," and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.2.2.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Power Distribution and DC-DC" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.2.2.4 Verification and Issue Closure**: Verify the output of "Power Distribution and DC-DC," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.2.2.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Power Distribution and DC-DC," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

##### Charging and Energy Management
- **Methods/Tools**: Charging pile/dock, wireless charging, charging protocol, energy recovery
- **Design Logic**: Charging experience affects usability; must be compatible with target scenarios
- **Key Constraints**: Safety, standards, cost, space
- **Completion Criteria/Deliverables**: Charging solution, charging time, BMS communication protocol
**Level-3 Sub-tasks:**
- **P13.2.3.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Charging and Energy Management," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.2.3.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Charging and Energy Management," demonstrate using "Charging pile/dock, wireless charging, charging protocol, energy recovery," and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.2.3.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Charging and Energy Management" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.2.3.4 Verification and Issue Closure**: Verify the output of "Charging and Energy Management," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.2.3.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Charging and Energy Management," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

#### Safety and EMC

##### Hardware Emergency Stop and Safety Chain
- **Methods/Tools**: Hardware emergency stop, watchdog, fuse, safety PLC/relay, dual-channel
- **Design Logic**: Any software failure can be cut off by hardware; comply with functional safety
- **Key Constraints**: Response time, reliability, false triggering
- **Completion Criteria/Deliverables**: Safety system schematic, FMEA, emergency stop response time < target
**Level-3 Sub-tasks:**
- **P13.3.1.1 Input Review and Target Quantification**: Organize upstream inputs, reference standards, and resources required for "Hardware Emergency Stop and Safety Chain," convert completion criteria into quantifiable acceptance indicators, and define Owner and milestones.
**Level-4 Key Actions:**
1. List all upstream input items and confirm versions
2. Convert acceptance criteria into quantifiable KPIs
3. Establish task Owner, timeline, and risk register
- **P13.3.1.2 Solution/Method Design**: Develop implementation methods or candidate solutions for "Hardware Emergency Stop and Safety Chain," demonstrate using "Hardware emergency stop, watchdog, fuse, safety PLC/relay, dual-channel," and clarify technical route and resource requirements.
**Level-4 Key Actions:**
1. Form at least 2 candidate solutions
2. Establish an evaluation matrix and score quantitatively
3. Organize review and freeze the solution
- **P13.3.1.3 Implementation/Prototype/Sample Fabrication**: Execute implementation work for "Hardware Emergency Stop and Safety Chain" according to the design plan, produce prototypes, samples, or complete key steps, and record process data.
**Level-4 Key Actions:**
1. Build models/prototypes and record key parameters
2. Perform simulation or prototype verification
3. Record anomalies and deviations
- **P13.3.1.4 Verification and Issue Closure**: Verify the output of "Hardware Emergency Stop and Safety Chain," check if completion criteria are met, record issues, and track until closure.
**Level-4 Key Actions:**
1. Develop test/review plan and pass criteria
2. Execute tests and record raw data
3. Output issue list and improvement measures
- **P13.3.1.5 Documentation Output and Downstream Delivery**: Output final reports/drawings/specifications for "Hardware Emergency Stop and Safety Chain," update ICD/BOM/SOP/requirements traceability chain, and complete formal delivery to downstream stages.
**Level-4 Key Actions:**
1. Write documents per template and reference raw data
2. Complete internal review and version control
3. Release and notify downstream dependencies

## 개요
전자 전기 및 에너지 시스템(Electronics & Power)은 휴머노이드 로봇 제품 개발 전 과정 중 13번째 단계이며, WBS V3에서 여러 3레벨 하위 작업으로 전개됩니다.
## 핵심 내용
이 단계는 입력 정리, 설계, 구현/프로토타입, 검증 폐쇄 및 문서 전달 등 완전한 엔지니어링 작업을 포함하며, 하위 의존 부서가 적격한 입력을 확보할 수 있도록 하는 핵심 지점입니다.

## 주요 하위 작업 및 기술 내용
#### 컴퓨팅 및 통신 하드웨어

##### 컴퓨팅 플랫폼 아키텍처 및 선정
- **방법 / 도구**: Jetson / Intel NUC / 자체 개발 캐리어 보드 / FPGA / MCU 분포
- **설계 사고 논리**: AI 작업은 GPU, 실시간 제어는 MCU/FPGA, 안전 모니터링은 독립적으로
- **핵심 제약 조건**: 전력 소모, 방열, 무게, 실시간성, 기능 안전
- **완료 기준 / 산출물**: 컴퓨팅 아키텍처 다이어그램, 각 노드의 연산 능력/전력 소모 예산, 안전 분할
**3레벨 하위 작업:**
- **P13.1.1.1 입력 정리 및 목표 정량화**: 「컴퓨팅 플랫폼 아키텍처 및 선정」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.1.1.2 후보 설계 수립 및 평가**: 「컴퓨팅 플랫폼 아키텍처 및 선정」에 대한 후보 설계 라이브러리를 구축하고, 「Jetson / Intel NUC / 자체 개발 캐리어 보드 / FPGA / MCU 분포」를 사용하여 정량적 평가를 수행하며, 비용, 성능, 공급망, 유지보수성을 고려하여 최종 설계를 결정합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.1.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「컴퓨팅 플랫폼 아키텍처 및 선정」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.1.1.4 검증 및 문제 폐쇄**: 「컴퓨팅 플랫폼 아키텍처 및 선정」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.1.1.5 문서 출력 및 하위 전달**: 「컴퓨팅 플랫폼 아키텍처 및 선정」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 자체 개발/외주 PCB 설계
- **방법 / 도구**: 캐리어 보드, 관절 구동 보드, 센서 인터페이스 보드, 안전 모니터링 보드
- **설계 사고 논리**: 컴퓨팅, 통신, 전원, 안전 기능을 신뢰할 수 있는 하드웨어에 고정
- **핵심 제약 조건**: EMC, SI/PI, 열, 공간, 제조 가능성
- **완료 기준 / 산출물**: 회로도, PCB, BOM, DFM 보고서
**3레벨 하위 작업:**
- **P13.1.2.1 입력 정리 및 목표 정량화**: 「자체 개발/외주 PCB 설계」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.1.2.2 개념 및 상세 설계**: 「자체 개발/외주 PCB 설계」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「캐리어 보드, 관절 구동 보드, 센서 인터페이스 보드, 안전 모니터링 보드」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.1.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「자체 개발/외주 PCB 설계」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.1.2.4 검증 및 문제 폐쇄**: 「자체 개발/외주 PCB 설계」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.1.2.5 문서 출력 및 하위 전달**: 「자체 개발/외주 PCB 설계」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 통신 네트워크 및 동기화
- **방법 / 도구**: CAN-FD, EtherCAT, Ethernet, TSN, PTP 시간 동기화
- **설계 사고 논리**: 관절 제어는 높은 실시간성 필요, 비전/AI는 높은 대역폭 필요; 핵심 신호 이중화
- **핵심 제약 조건**: 케이블 수량, EMC, 비용, 확장성
- **완료 기준 / 산출물**: 통신 토폴로지 다이어그램, 프로토콜 할당, 대역폭/지연 예산, 동기화 정밀도
**3레벨 하위 작업:**
- **P13.1.3.1 입력 정리 및 목표 정량화**: 「통신 네트워크 및 동기화」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.1.3.2 설계/방법 설계**: 「통신 네트워크 및 동기화」에 대한 구현 방법 또는 후보 설계를 수립하고, 「CAN-FD, EtherCAT, Ethernet, TSN, PTP 시간 동기화」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.1.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「통신 네트워크 및 동기화」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.1.3.4 검증 및 문제 폐쇄**: 「통신 네트워크 및 동기화」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.1.3.5 문서 출력 및 하위 전달**: 「통신 네트워크 및 동기화」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 전원 및 에너지

##### 배터리 팩 설계 및 BMS
- **방법 / 도구**: 리튬 배터리 선정, 모듈 설계, SOC/SOH 추정, 급속 충전 전략, 열 폭주 방지
- **설계 사고 논리**: 주행 거리와 무게 균형; BMS는 과충전/과방전/과온 보호 필요
- **핵심 제약 조건**: 안전 인증, 열 폭주, 사이클 수명, 비용
- **완료 기준 / 산출물**: 배터리 팩 설계, BMS 사양, 주행 거리 추정, 안전 테스트
**3레벨 하위 작업:**
- **P13.2.1.1 입력 정리 및 목표 정량화**: 「배터리 팩 설계 및 BMS」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.2.1.2 개념 및 상세 설계**: 「배터리 팩 설계 및 BMS」의 개념 설계, 상세 설계 및 인터페이스 정의를 완료하고, 「리튬 배터리 선정, 모듈 설계, SOC/SOH 추정, 급속 충전 전략, 열 폭주 방지」를 사용하여 타당성을 검증하며, 도면/알고리즘/논리 프레임워크를 출력합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.2.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「배터리 팩 설계 및 BMS」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.2.1.4 검증 및 문제 폐쇄**: 「배터리 팩 설계 및 BMS」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.2.1.5 문서 출력 및 하위 전달**: 「배터리 팩 설계 및 BMS」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 전원 분배 및 DC-DC
- **방법 / 도구**: 모선 전압 선택, DC-DC 모듈, 필터링, OR-ing, 이중화
- **설계 사고 논리**: 모터 모선과 로직 전원 분리; 고장 시 안전 전원 차단
- **핵심 제약 조건**: 전압 강하, 효율, EMI, 안전 표준
- **완료 기준 / 산출물**: 전원 분배 다이어그램, DC-DC 선정, 효율/열 테스트
**3레벨 하위 작업:**
- **P13.2.2.1 입력 정리 및 목표 정량화**: 「전원 분배 및 DC-DC」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.2.2.2 설계/방법 설계**: 「전원 분배 및 DC-DC」에 대한 구현 방법 또는 후보 설계를 수립하고, 「모선 전압 선택, DC-DC 모듈, 필터링, OR-ing, 이중화」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.2.2.3 구현/프로토타입/시제품 제작**: 설계에 따라 「전원 분배 및 DC-DC」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.2.2.4 검증 및 문제 폐쇄**: 「전원 분배 및 DC-DC」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.2.2.5 문서 출력 및 하위 전달**: 「전원 분배 및 DC-DC」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

##### 충전 및 에너지 관리
- **방법 / 도구**: 충전기/스테이션, 무선 충전, 충전 프로토콜, 에너지 회수
- **설계 사고 논리**: 충전 경험은 사용성에 영향; 대상 시나리오와 호환 필요
- **핵심 제약 조건**: 안전, 표준, 비용, 공간
- **완료 기준 / 산출물**: 충전 설계, 충전 시간, BMS 통신 프로토콜
**3레벨 하위 작업:**
- **P13.2.3.1 입력 정리 및 목표 정량화**: 「충전 및 에너지 관리」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.2.3.2 설계/방법 설계**: 「충전 및 에너지 관리」에 대한 구현 방법 또는 후보 설계를 수립하고, 「충전기/스테이션, 무선 충전, 충전 프로토콜, 에너지 회수」를 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.2.3.3 구현/프로토타입/시제품 제작**: 설계에 따라 「충전 및 에너지 관리」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.2.3.4 검증 및 문제 폐쇄**: 「충전 및 에너지 관리」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.2.3.5 문서 출력 및 하위 전달**: 「충전 및 에너지 관리」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지

#### 안전 및 EMC

##### 하드웨어 비상 정지 및 안전 체인
- **방법 / 도구**: 하드웨어 비상 정지, 워치독, 퓨즈, 안전 PLC/릴레이, 이중 채널
- **설계 사고 논리**: 모든 소프트웨어 오류에도 하드웨어를 통해 동력 차단 가능; 기능 안전 준수
- **핵심 제약 조건**: 응답 시간, 신뢰성, 오작동
- **완료 기준 / 산출물**: 안전 시스템 회로도, FMEA, 비상 정지 응답 시간 < 목표
**3레벨 하위 작업:**
- **P13.3.1.1 입력 정리 및 목표 정량화**: 「하드웨어 비상 정지 및 안전 체인」에 필요한 상위 입력, 참조 표준 및 리소스를 정리하고, 완료 기준을 정량화 가능한 검수 지표로 변환하며, Owner와 마일스톤을 명확히 합니다.
**4레벨 핵심 동작:**
1. 모든 상위 입력 목록을 나열하고 버전을 확인
2. 검수 기준을 정량화 가능한 KPI로 변환
3. 작업 Owner, 시간 노드 및 위험 등록부를 구축
- **P13.3.1.2 설계/방법 설계**: 「하드웨어 비상 정지 및 안전 체인」에 대한 구현 방법 또는 후보 설계를 수립하고, 「하드웨어 비상 정지, 워치독, 퓨즈, 안전 PLC/릴레이, 이중 채널」을 사용하여 논증하며, 기술 경로와 리소스 요구 사항을 명확히 합니다.
**4레벨 핵심 동작:**
1. 2개 이상의 후보 설계를 구성
2. 평가 매트릭스를 구축하고 정량적으로 점수화
3. 검토를 조직하고 설계를 확정
- **P13.3.1.3 구현/프로토타입/시제품 제작**: 설계에 따라 「하드웨어 비상 정지 및 안전 체인」의 구현 작업을 실행하고, 프로토타입, 시제품을 제작하거나 핵심 단계를 완료하며, 과정 데이터를 기록합니다.
**4레벨 핵심 동작:**
1. 모델/시제품을 구축하고 핵심 매개변수를 기록
2. 시뮬레이션 또는 프로토타입 검증을 실행
3. 이상 및 편차를 기록
- **P13.3.1.4 검증 및 문제 폐쇄**: 「하드웨어 비상 정지 및 안전 체인」의 출력을 검증하여 완료 기준 충족 여부를 확인하고, 문제를 기록하여 종료될 때까지 추적합니다.
**4레벨 핵심 동작:**
1. 테스트/검토 계획 및 통과 기준을 수립
2. 테스트를 실행하고 원시 데이터를 기록
3. 문제 목록 및 개선 조치를 출력
- **P13.3.1.5 문서 출력 및 하위 전달**: 「하드웨어 비상 정지 및 안전 체인」의 최종 보고서/도면/사양을 출력하고, ICD/BOM/SOP/요구사항 추적 체인을 업데이트하며, 하위 단계로의 공식 전달을 완료합니다.
**4레벨 핵심 동작:**
1. 템플릿에 따라 문서를 작성하고 원시 데이터를 인용
2. 내부 검토 및 버전 관리를 완료
3. 게시하고 하위 의존 부서에 통지
