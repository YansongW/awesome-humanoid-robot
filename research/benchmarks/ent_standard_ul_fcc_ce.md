---
$id: ent_standard_ul_fcc_ce
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: Regional Market Certifications (UL / FCC / CE)
  zh: 区域准入认证
  ko: 지역별 시장 인증(UL/FCC/CE)
summary:
  en: The set of mandatory or voluntary certifications required to sell robots in specific regions, such as UL for North America,
    CE for Europe, and FCC for electromagnetic compatibility.
  zh: 在特定区域销售机器人所需的强制性或自愿性认证，如北美UL、欧洲CE及电磁兼容FCC等。
  ko: 특정 지역에서 로봇을 판매하기 위해 필요한 강제 또는 자발적 인증; 북미 UL, 유럽 CE, 전자기 적합성 FCC 등.
domains:
- 12_policy_regulation_ethics
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- standard
- chapter_12
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-07.md#7.9.7 Python 算例：关节壳体 should-cost 计算器 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
区域准入认证是人形机器人领域的重要standard。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
下面的代码以铝合金关节壳体为例，逐项计算 should-cost，并展示改变良率与批量对单位成本的影响。

```python
import numpy as np
import matplotlib.pyplot as plt

class ShouldCostModel:
    def __init__(self, annual_volume):
        self.N = annual_volume
        # 材料
        self.blank_weight = 0.35      # kg
        self.al_price = 28.0          # 元/kg
        self.blank_yield = 0.97       # 毛坯良率
        # 压铸
        self.cycle_time = 90 / 3600   # h/件
        self.die_cast_rate = 180.0    # 元/h
        self.die_investment = 350_000 # 元
        self.die_life = 200_000       # 件
        # CNC
        self.cnc_time = 25 / 60       # h/件
        self.cnc_rate = 120.0         # 元/h
        self.tool_cost = 4.5          # 元/件（已按寿命摊销）
        # 表面处理
        self.surface_area = 0.045     # m²
        self.surface_price = 220.0    # 元/m²
        # 间接费用与利润
        self.overhead_rate = 0.25     # 占直接成本的 25%
        self.profit_rate = 0.12       # 占成本加费用的 12%

    def cost(self):
        C_mat = self.blank_weight * self.al_price / self.blank_yield
        C_die_cast = self.cycle_time * self.die_cast_rate + self.die_investment / min(self.N, self.die_life)
        C_cnc = self.cnc_time * self.cnc_rate + self.tool_cost
        C_surface = self.surface_area * self.surface_price
        direct = C_mat + C_die_cast + C_cnc + C_surface
        overhead = direct * self.overhead_rate
        profit = (direct + overhead) * self.profit_rate
        return {
            "材料": C_mat,
            "压铸": C_die_cast,
            "CNC": C_cnc,
            "表面处理": C_surface,
            "制造费用": overhead,
            "利润": profit,
            "should_cost": direct + overhead + profit,
        }

## 参考
- Wiki extraction
- 项目 Wiki：chapter-07.md#7.9.7 Python 算例：关节壳体 should-cost 计算器

