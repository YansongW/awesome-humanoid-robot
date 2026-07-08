#!/usr/bin/env python3
"""Rewrite seed queries and add relevance_context to generated workstream stubs.

Targets YAMLs created by generate_missing_workstreams.py (metadata.generated_from
== "WORKSTREAM_TREE.md") that do not yet have a relevance_context. Curated
foundational/economics/CS/OR/physics/chemistry query sets are used where
available; other generated stubs get a broadened generic query set.

Usage:
    source .venv/bin/activate
    python scripts/refine_generated_workstreams.py \
        --root scripts/ai4sci_workstreams [--dry-run]
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


# Curated query sets for generated stubs with historically low hit rates.
# Each entry is (seed_queries, relevance_context).
CURATED: dict[str, tuple[list[str], str]] = {
    "cost_analysis": (
        [
            "robot manufacturing cost model",
            "humanoid robot total cost of ownership",
            "robotics bill of materials cost analysis",
            "automation production cost breakdown",
            "humanoid robot mass production cost",
        ],
        "Relevant if it presents cost modeling, TCO, BOM, or manufacturing "
        "economics methods applicable to humanoid or general robot production, "
        "even when examples use industrial robots or automation.",
    ),
    "game_theory": (
        [
            "game theory robotics",
            "multi-agent game theory human robot interaction",
            "strategic interaction robots",
            "cooperative game theory robot teams",
            "negotiation game theory humanoid robot",
        ],
        "Relevant if it develops or applies game-theoretic models (strategic, "
        "cooperative, or negotiation) to robotics, multi-agent systems, or "
        "human-robot interaction, even if not exclusively humanoid.",
    ),
    "industrial_organization": (
        [
            "robotics industry structure",
            "industrial robot market competition",
            "robotics platform economics",
            "robotics ecosystem industrial organization",
            "automation supply chain industrial organization",
        ],
        "Relevant if it analyzes market structure, platform economics, "
        "ecosystems, supply chains, or competition in robotics/automation, "
        "even when examples are industrial robots or automation firms.",
    ),
    "algorithms_data_structures": (
        [
            "motion planning algorithms robotics",
            "collision detection algorithms robot",
            "real-time path planning humanoid robot",
            "trajectory optimization data structures",
            "graph search robot motion planning",
        ],
        "Relevant if it introduces algorithms or data structures for robot "
        "motion planning, collision detection, trajectory optimization, or "
        "real-time planning that can apply to humanoid robots.",
    ),
    "distributed_systems": (
        [
            "distributed control multi robot systems",
            "edge cloud robotics",
            "robot fleet coordination distributed",
            "distributed perception robot system",
            "humanoid robot distributed computing",
        ],
        "Relevant if it covers distributed control, edge-cloud computing, fleet "
        "coordination, or distributed perception for robotics; humanoid "
        "relevance is accepted if the architecture scales to humanoids.",
    ),
    "machine_learning_theory": (
        [
            "reinforcement learning theory robotics",
            "imitation learning theory robot",
            "sim to real theory transfer robotics",
            "sample efficiency robot learning",
            "humanoid robot learning generalization",
        ],
        "Relevant if it presents learning-theory results (RL, imitation, "
        "sim-to-real, generalization, sample efficiency) with robotics "
        "applications or direct humanoid-robot focus.",
    ),
    "real_time_systems": (
        [
            "real-time control robotics",
            "real-time operating system robot",
            "deterministic control humanoid robot",
            "low latency control robotics",
            "ROS2 real-time robot control",
        ],
        "Relevant if it addresses real-time/deterministic/low-latency control, "
        "RTOS, or scheduling for robotics; direct humanoid relevance is "
        "preferred, but general robot control is accepted if transferable.",
    ),
    "differential_geometry": (
        [
            "differential geometry robotics",
            "Lie group robot kinematics",
            "manifold learning robot motion",
            "Riemannian geometry robot control",
            "differential geometry humanoid robot",
        ],
        "Relevant if it applies differential geometry, Lie groups, manifolds, or "
        "Riemannian geometry to robot kinematics, motion, or control, with "
        "humanoid applicability.",
    ),
    "graph_theory": (
        [
            "graph theory robot planning",
            "graph search motion planning",
            "topological graph robotics",
            "graph neural network robot",
            "graph theory multi robot coordination",
        ],
        "Relevant if it uses graph theory, graph search, graph neural networks, "
        "or topological methods for robot planning, coordination, or reasoning.",
    ),
    "linear_algebra": (
        [
            "linear algebra robotics",
            "matrix methods robot control",
            "numerical linear algebra robotics",
            "linear algebra humanoid robot dynamics",
            "linear algebra robot learning",
        ],
        "Relevant if it covers linear algebra or matrix methods with direct "
        "robotics applications (dynamics, control, learning); generic math "
        "without robot relevance should be rejected.",
    ),
    "multivariable_calculus": (
        [
            "multivariable calculus robotics",
            "gradient methods robot optimization",
            "calculus of variations robot control",
            "differential calculus humanoid robot",
            "multivariable calculus robot kinematics",
        ],
        "Relevant if it applies multivariable calculus, gradients, or "
        "variational methods to robot optimization, control, or kinematics.",
    ),
    "numerical_analysis": (
        [
            "numerical analysis robotics",
            "numerical optimization robot control",
            "numerical integration humanoid dynamics",
            "simulation numerical methods robotics",
            "numerical linear algebra robot",
        ],
        "Relevant if it presents numerical methods (integration, optimization, "
        "linear algebra) used in robot simulation, dynamics, or control.",
    ),
    "optimal_control": (
        [
            "optimal control robotics",
            "model predictive control humanoid robot",
            "LQR legged robot",
            "trajectory optimization robot",
            "optimal control manipulation robotics",
        ],
        "Relevant if it covers optimal control, MPC, LQR, or trajectory "
        "optimization for robotics; legged/humanoid examples are preferred, "
        "but general robot optimal control is accepted.",
    ),
    "probability_statistics": (
        [
            "probabilistic robotics",
            "statistical learning robot",
            "uncertainty quantification robot",
            "Bayesian methods humanoid robot",
            "probability statistics robotics perception",
        ],
        "Relevant if it applies probability/statistics/Bayesian methods to "
        "robotics perception, learning, or state estimation; generic statistics "
        "without robot relevance should be rejected.",
    ),
    "inventory_management": (
        [
            "robot inventory management",
            "humanoid robot spare parts supply chain",
            "robot fleet inventory optimization",
            "automated warehouse inventory robotics",
            "service robot inventory management",
        ],
        "Relevant if it addresses inventory management, spare parts, or supply "
        "chain for robot fleets/warehouses, or service-humanoid robot operations.",
    ),
    "reliability_engineering": (
        [
            "robot reliability engineering",
            "humanoid robot reliability prediction",
            "failure analysis robot system",
            "reliability testing robotics",
            "component reliability humanoid robot",
        ],
        "Relevant if it covers reliability engineering, failure analysis, or "
        "reliability testing for robotic systems/components applicable to "
        "humanoids.",
    ),
    "scheduling_optimization": (
        [
            "robot task scheduling",
            "humanoid robot planning scheduling",
            "multi robot scheduling optimization",
            "robot fleet optimization",
            "manufacturing scheduling humanoid robot",
        ],
        "Relevant if it addresses task scheduling, planning, or optimization for "
        "robots/fleets/manufacturing with applicability to humanoid workflows.",
    ),
    "statistical_process_control": (
        [
            "statistical process control robotics",
            "quality control robot manufacturing",
            "SPC assembly process humanoid robot",
            "manufacturing process monitoring robot",
            "robot production quality statistical control",
        ],
        "Relevant if it applies statistical process control or quality control "
        "to robotics manufacturing/assembly; direct humanoid relevance is "
        "preferred.",
    ),
    "contact_mechanics": (
        [
            "robot contact mechanics",
            "legged robot contact dynamics",
            "humanoid foot ground contact",
            "friction cone robotics locomotion",
            "impact dynamics humanoid robot",
        ],
        "Relevant if it models robot contact/impact/friction, legged locomotion "
        "contacts, or humanoid foot-ground interaction.",
    ),
    "electromagnetism": (
        [
            "robot motor electromagnetic design",
            "actuator electromagnetic modeling",
            "humanoid robot electromagnetic compatibility",
            "permanent magnet motor robotics",
            "brushless motor torque ripple robot",
        ],
        "Relevant if it concerns electromagnetic design/modeling of robot "
        "actuators/motors, or EMC in humanoid/robot systems.",
    ),
    "materials_mechanics": (
        [
            "robot materials mechanics",
            "lightweight materials humanoid robot",
            "composite materials robotics",
            "structural mechanics robot limb",
            "material fatigue robot actuator",
        ],
        "Relevant if it studies mechanics, lightweight/composite materials, "
        "structural behavior, or fatigue of robot components applicable to "
        "humanoids.",
    ),
    "thermodynamics": (
        [
            "robot thermal management",
            "humanoid robot heat dissipation",
            "actuator thermal modeling robotics",
            "motor thermodynamics humanoid robot",
            "power electronics thermal robot",
        ],
        "Relevant if it addresses thermal management, heat dissipation, or "
        "thermal modeling of robot actuators/motors/power electronics.",
    ),
    "battery_electrochemistry": (
        [
            "lithium ion battery electrochemistry",
            "solid state battery robotics",
            "battery kinetics humanoid robot",
            "electrolyte transport battery modeling",
            "high energy density battery robot",
        ],
        "Relevant if it covers battery electrochemistry/kinetics/modeling for "
        "high-energy mobile robots, including humanoids.",
    ),
    "polymer_materials": (
        [
            "polymer composite lightweight robot",
            "thermoplastic humanoid robot structure",
            "polymer materials robotics",
            "soft robot polymer material",
            "wear resistant polymer robot component",
        ],
        "Relevant if it develops or applies polymer/composite/thermoplastic "
        "materials for lightweight, wear-resistant, or soft robot/humanoid "
        "components.",
    ),
    "rare_earth_magnet_chemistry": (
        [
            "rare earth magnet robot actuator",
            "NdFeB magnet motor robotics",
            "permanent magnet material humanoid robot",
            "magnet corrosion protection robotics",
            "high performance magnet actuator robot",
        ],
        "Relevant if it concerns rare-earth/NdFeB permanent magnet chemistry, "
        "processing, or performance for robot actuators/motors.",
    ),
    "surface_treatment": (
        [
            "surface treatment robot component",
            "coating wear resistance robotics",
            "corrosion protection humanoid robot",
            "tribological coating robot actuator",
            "surface engineering robot parts",
        ],
        "Relevant if it covers surface treatment, coatings, corrosion/wear "
        "protection, or tribology for robot/humanoid components.",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refine generated workstream YAMLs with better seed queries "
                    "and relevance_context."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path("scripts/ai4sci_workstreams"),
        help="Root directory containing workstream YAMLs.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print changes without writing files.",
    )
    return parser.parse_args()


def generic_queries_and_context(name: str) -> tuple[list[str], str]:
    topic = name.replace("_", " ")
    return (
        [
            f"{topic} robotics",
            f"humanoid robot {topic}",
            f"{topic} robots survey",
            f"{topic} automation manufacturing",
            f"{topic} applied to humanoid robots",
        ],
        f"Relevant if it addresses {topic} in a robotics or automation context, "
        f"or develops foundational methods/principles applicable to humanoid "
        f"robots, even when examples are not explicitly humanoid.",
    )


def refine_workstream(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    data: dict[str, Any] = yaml.safe_load(text)

    metadata = data.get("metadata") or {}
    if metadata.get("generated_from") != "WORKSTREAM_TREE.md":
        return False
    if data.get("relevance_context"):
        return False

    name = data["name"]
    if name in CURATED:
        queries, context = CURATED[name]
    else:
        queries, context = generic_queries_and_context(name)

    data["seed_queries"] = queries
    data["relevance_context"] = context

    # Bump description to note refinement.
    desc = data.get("description", "")
    if isinstance(desc, str) and "Query set refined" not in desc:
        data["description"] = desc.rstrip() + "\nQuery set refined for broader robotics relevance and relevance_context added."

    if dry_run:
        print(f"[dry-run] Would refine {path}")
        return True

    with open(path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[refine] Updated {path}")
    return True


def main() -> int:
    args = parse_args()
    count = 0
    for path in sorted(args.root.rglob("*.yaml")):
        if refine_workstream(path, args.dry_run):
            count += 1
    print(f"\n[refine] {'Would refine' if args.dry_run else 'Refined'} {count} workstream(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
