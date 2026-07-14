---
$id: ent_algorithm_sac
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Soft Actor-Critic (SAC)
  zh: 软演员-评论家（SAC）
  ko: 소프트 액터-크리틱(SAC)
summary:
  en: An off-policy actor-critic reinforcement-learning algorithm that maximizes expected return while also maximizing policy
    entropy for exploration.
  zh: 在最大化期望回报的同时最大化策略熵以促进探索的异策演员-评论家强化学习算法。
  ko: 기대 보상을 최대화하면서도 정책 엔트로피를 최대화해 탐색을 장려하는 오프폴리시 액터-크리틱 강화학습 알고리즘.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- algorithm
- chapter_15
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#Python 示例：八点法 + RANSAC + 三角测量 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
软演员-评论家（SAC）是人形机器人领域的重要algorithm。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
以下代码演示一个简化 VO 前端：用归一化 8 点法估计本质矩阵，用 RANSAC 剔除外点，再分解出位姿并三角测量恢复三维点。实际系统应使用 ORB/SIFT 等真实特征检测与匹配。

```python
"""
Simplified visual odometry frontend:
random correspondences -> normalized 8-point -> RANSAC -> E decomposition -> triangulation.
"""
import numpy as np


def skew(v):
    """Return 3x3 skew-symmetric matrix of vector v."""
    return np.array([[0, -v[2], v[1]],
                     [v[2], 0, -v[0]],
                     [-v[1], v[0], 0]])


def estimate_eight_point(pts1, pts2):
    """Estimate essential matrix from N>=8 normalized correspondences."""
    A = []
    for (x1, y1), (x2, y2) in zip(pts1, pts2):
        A.append([x2*x1, x2*y1, x2, y2*x1, y2*y1, y2, x1, y1, 1])
    A = np.array(A)
    _, _, Vt = np.linalg.svd(A)
    E = Vt[-1].reshape(3, 3)
    # Enforce singular-value constraint
    U, S, Vt = np.linalg.svd(E)
    S = np.diag([1, 1, 0])
    E = U @ S @ Vt
    return E


def decompose_essential(E):
    """Decompose E into 4 possible (R, t)."""
    U, _, Vt = np.linalg.svd(E)
    W = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    R1 = U @ W @ Vt
    R2 = U @ W.T @ Vt
    t = U[:, 2]
    if np.linalg.det(R1) < 0:
        R1 = -R1
    if np.linalg.det(R2) < 0:
        R2 = -R2
    return [(R1, t), (R1, -t), (R2, t), (R2, -t)]


def triangulate_point(P1, P2, x1, x2):
    """Linear triangulation of a single point."""
    A = np.vstack([
        x1[0] * P1[2] - P1[0],
        x1[1] * P1[2] - P1[1],
        x2[0] * P2[2] - P2[0],
        x2[1] * P2[2] - P2[1]
    ])
    _, _, Vt = np.linalg.svd(A)
    X = Vt[-1]
    return X[:3] / X[3]


def ransac_essential(pts1, pts2, threshold=1e-3, max_iter=500, p=0.99):
    """RANSAC for essential matrix."""
    best_E, best_inliers = None, []
    n = len(pts1)
    for _ in range(max_iter):
        idx = np.random.choice(n, 8, replace=False)
        E = estimate_eight_point(pts1[idx], pts2[idx])
        # Sampson distance as error metric
        errs = []
        for x1, x2 in zip(pts1, pts2):
            Ex1 = E @ x1
            Etx2 = E.T @ x2
            num = (x2.T @ E @ x1) ** 2
            den = Ex1[0]**2 + Ex1[1]**2 + Etx2[0]**2 + Etx2[1]**2
            errs.append(num / (den + 1e-12))
        inliers = np.where(np.array(errs) < threshold)[0]
        if len(inliers) > len(best_inliers):
            best_inliers = inliers
            best_E = E
        # Adaptively update iterations
        if len(best_inliers) > 8:
            eps = len(best_inliers) / n
            k = np.log(1 - p) / np.log(1 - eps**8)
            max_iter = min(max_iter, int(k))
    return best_E, best_inliers

## 参考
- Wiki extraction
- 项目 Wiki：chapter-06.md#Python 示例：八点法 + RANSAC + 三角测量

