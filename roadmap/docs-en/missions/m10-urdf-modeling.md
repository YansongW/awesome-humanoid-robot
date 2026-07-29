# M10 · URDF Modeling and Export: Turning a Hunk of Metal into a Computable Model

**Global Position**: After the full machine is assembled (M09) or the structure is finalized, before simulation (M11–M13). The input is your mechanical design (CAD or physical object), and the output is a **validated URDF model package** (urdf file + mesh + inertial parameters). It is the common foundation for M11 simulation conversion, M12 standing, and M13 reinforcement learning.

**Prerequisites**: Able to understand the URDF structure ([Stage 0](../stage-0-foundations.md) simulation first experience); structural dimensions and mass distribution are determined.

Theoretical background: [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) card and [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/), [Chapter 23: Simulation and Physics Engines](/wiki/chapters/chapter-23/).

## Step 1: Define the Link/Joint Tree and Naming Convention

【What to Do】First, sketch the kinematic tree on paper: base_link → hip → leg → ankle → foot, torso → shoulder → arm → wrist. Then establish three naming rules and follow them throughout:

1. Side prefix: `l_` / `r_` (left/right leg and arm);
2. Joint type suffix: `_pitch` / `_roll` / `_yaw` (rotation axis);
3. Coordinate system for each link: **Origin on the joint axis, z-axis along the joint axis** (consistent with the exporter default, avoiding pitfalls later).

【Why】90% of URDF problems are not format errors but **inconsistent coordinate system conventions**: axis drawn in reverse, origin offset, left-right mirroring written incorrectly. Freeze the conventions on paper first, then open the software. Specifications for joint types (revolute/prismatic/fixed) and axis directions are detailed in the [URDF Robot Description Format](/entry/ent_technology_urdf_robot_description_format_2024/) card.

【How to Analyze Your Situation】For replicating an open-source platform (M08): Use the official URDF directly; this task only requires Step 4 (inertia verification) and Step 6 (validation); skip the rest. For a self-developed structure: Follow all six steps thoroughly.

## Step 2: Export the Skeleton from CAD

【What to Do】Choose one of three routes:

| Route | Tool | Suitable For |
|---|---|---|
| SolidWorks Export | `sw_urdf_exporter` plugin | Structure designed in SolidWorks |
| Onshape Export | `onshape-to-robot` | Cloud-based CAD, multi-user collaboration |
| Hand-write URDF/xacro | Text editor + xacro macros | Simple structure or need for parameterization (e.g., adjustable leg length) |

First thing after export: Open it in RViz or `urdf-viz`, **manually drag each joint** to confirm that the axis direction and positive/negative orientation match the conventions from Step 1.

【Why】Exporter-generated skeletons often have redundant fixed joints and nested frames, and the axis conventions may not match your specifications; xacro macros can condense 20 similar joints into a parameterized template, allowing one change to take effect globally. Before hand-writing the skeleton, ensure you can mentally describe the `origin rpy` for each joint.

【How to Analyze Your Situation】If you have no CAD model, only the physical object: Use calipers to measure joint distances, hand-write xacro directly; for a desktop robot with a dozen links, this can be done in half a day; mesh files (Step 5) can initially be placeholder geometries (box/cylinder).

## Step 3: Fill in Inertial Parameters—The Soul of the Model

【What to Do】Every link must have `<inertial>`: `mass`, `origin` (center of mass), `inertia` (3×3 inertia tensor). Three acquisition paths, ordered by accuracy:

1. **Read from CAD after material assignment**: Assign real material density to each part; CAD directly outputs the center of mass and inertia tensor;
2. **Physical weighing + geometric approximation**: Weigh to get mass, estimate using equivalent geometry (cuboid/cylinder) inertia formulas;
3. **Swing method to measure period**: Suspend and swing to measure period, then back-calculate inertia (highest accuracy, most labor-intensive; see [Chapter 9: Key Subsystem Design](/wiki/chapters/chapter-09/) and the [System Identification](/entry/ent_method_system_identification/) card).

Actuators account for the bulk of mass: Enter the mass of the motor/reducer selected in M02 into the corresponding link according to the datasheet; do not distribute evenly.

【Why】80% of "mysterious falls" in simulation stem from incorrect inertial parameters: a 20% mass error ruins controller tuning; an order-of-magnitude error in the inertia tensor completely changes dynamic response. In M14 sim-to-real, you will return to refine these numbers using system identification.

【How to Analyze Your Situation】For 3D-printed parts, use CAD density × print infill ratio (PLA ~1.24 g/cm³ × infill ratio). A 10–15% error is acceptable for the first version, but **the center of mass position must be verified experimentally**: Suspend the physical link with a string; the intersection of the vertical lines is the center of mass. If it doesn't match the model, adjust.

## Step 4: Joint Limits, Transmission Ratios, and Safety Boundaries

【What to Do】For each revolute joint, fill in `<limit>`: `lower/upper` (angle limits, degrees → radians), `effort` (torque limit, use the peak torque from the M01 specification table), `velocity` (speed limit, convert the rated speed from M01 to rad/s). For transmissions with reduction ratios, specify `<transmission>` or annotate the reduction ratio in comments (value from M03).

【Why】The simulator constrains motion according to limits; during RL training (M13), action clipping also reads these values—if `effort` is set too high, the policy may learn actions the real machine cannot execute, causing sim-to-real failure. Software limits for safety must be 5–10° smaller than the mechanical hard limits.

【How to Analyze Your Situation】Measure limit angles from structural drawings; if not available, manually rotate the physical joint to its endpoints and measure with an angle gauge. For `effort`, use motor peak torque × reduction ratio × efficiency (0.7–0.9 estimated value, needs verification based on reducer type—M03).

## Step 5: Separate Visual and Collision Geometry

【What to Do】

- `<visual>`: Place fine mesh (STL/DAE), purely for appearance;
- `<collision>`: Place **simplified geometry**—prefer combinations of box/cylinder/sphere, or a convex hull simplified mesh; keep the vertex count of each link's collision body within a few hundred.

Handle the foot sole collision body separately: Use a flat-bottomed box, slightly smaller than the actual foot sole (to avoid edge mis-triggering); leave friction parameters for tuning in M11.

【Why】The physics engine calculates contact based on collision geometry; complex meshes are both slow and unstable (sharp corners, self-intersections); a beautiful visual mesh contributes nothing to simulation. Official documentation for [MuJoCo Physics Engine](/entry/ent_software_mujoco_physics_engine_2022/) and [Gazebo](/entry/ent_software_gazebo/) both list "collision body simplification" as the primary recommendation for performance and stability.

【How to Analyze Your Situation】For 3D-printed parts, use the print STL directly for visual; for collision, manually write the bounding box of the same-named part in CAD—this is more controllable than converting to a convex hull. Pay attention to mesh units: STL in millimeters vs. meters—URDF defaults to meters; scaling errors during export are a classic pitfall.

## Step 6: Validation and Export Delivery

【What to Do】Pass four checks sequentially:

1. `check_urdf model.urdf`: Kinematic tree parses without errors;
2. RViz / urdf-viz visualization: Axes, limits, and mesh scaling are correct;
3. Mass report: Total model mass = physical weight ±10%, overall center of mass position is reasonable (projection within the support polygon when standing);
4. Package delivery: `robot_description/` (urdf + meshes + a README documenting coordinate system conventions and inertia sources), submit to version control.

【Why】These four checks are the entry ticket to M11—model conversion (URDF→MJCF/USD) amplifies small errors into "simulation flies off immediately upon running." The delivery package goes into version control; when you modify the model in M13, you'll know what changed.

【How to Analyze Your Situation】When validation reports errors, prioritize checking: missing units in `origin` (degrees vs. radians), non-positive definite inertia tensor, case sensitivity in mesh paths. These three account for the vast majority of URDF errors.

## Acceptance Criteria

- [ ] Kinematic tree and naming convention documented (one sheet: tree diagram + axis conventions).
- [ ] `check_urdf` passes; RViz manual joint dragging confirms axes/directions are correct.
- [ ] Every link has inertial parameters; total mass deviation from physical weight ≤ 10%; center of mass verified by string suspension.
- [ ] Every revolute joint has limits (angle/effort/velocity), values consistent with the M01 specification table.
- [ ] Visual/collision geometry separated; collision bodies are simplified geometry.
- [ ] Model package committed to repository (including README with coordinate system conventions), ready for direct conversion in M11.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Model "explodes" or flies around in RViz | Joint origin miswritten / mesh unit mismatch (mm mistaken for m) | Comment out joints level by level to isolate; try mesh scaling ×0.001 |
| Slowly topples during simulated standing | Incorrect center of mass position / total mass inconsistent with physical model | Re-measure center of mass using plumb line method; re-weigh and compare |
| MJCF conversion reports inertia tensor error | Inertia matrix not positive definite (manually estimated incorrectly) | Check ixx/iyy/izz satisfy triangle inequality; re-export from CAD |
| RL policy fails to learn standing | Effort/velocity limits set too high | Return to Step 4 and refill according to motor's actual capability |
| Asymmetric left/right leg behavior | Mirror joint axis direction or sign reversed | Check rpy and axis joint by joint against naming conventions |

## Companion Reading

- Previous task: [M09 · Full Assembly, Wiring, and Power Supply](m09-mechanical-assembly.md)
- Next task: [M11 · Simulation Environment and Model Conversion](m11-sim-setup.md)
- Theoretical background: [Chapter 22 · Software Middleware](/wiki/chapters/chapter-22/), [Chapter 23 · Simulation and Physics Engines](/wiki/chapters/chapter-23/)
- [Simulation Environment Setup Guide](../playbooks/sim-setup.md) · [Stage 2 Overview](../stage-2-biped.md)
