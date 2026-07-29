# M01 · Mathematizing the Requirement Scenario: Translating "I Want to Build a Robot" into Numbers

**Global Position**: This is the first task of the entire 0→1 roadmap. The input is the vague desire in your mind ("I want to build a robot that can walk/grasp things"), and the output is a **specification sheet filled with numbers** — every subsequent task (motor selection, reduction ratio, structure, budget) will be based on this sheet, and no decisions are allowed based on gut feeling.

**Prerequisites**: None (you can start directly). Mathematical tools themselves are not a prerequisite for this task. If you cannot calculate something clearly, mark it first and go back to [Stage 0 Foundations](../stage-0-foundations.md) to catch up.

## Step 1: Write the Scenario as a One-Sentence Mission Statement

[What to do] Write down the **most demanding task** your robot must complete in one sentence, using the format: "In [environment], at [frequency], perform [action] on [load]." Three reference tiers:

| Tier | Mission Statement Example | Corresponding Platform Scale |
|---|---|---|
| Desktop Learning Machine | "On a desktop, once per minute, move a 200 g block from point A to point B" | 5–10 DOF arm or small humanoid, servo/QDD hybrid |
| Bipedal Walking Platform | "On indoor flat ground, walk continuously for 10 minutes without falling" | 10–16 DOF biped, total weight 5–30 kg |
| Full Humanoid Operation | "After hearing a command, walk to a table, pick up a 500 g cup, and place it at a designated spot" | 20+ DOF full body, walking + manipulation + perception |

[Why] All downstream numbers are derived from this task: torque comes from load and leverage, speed from action tempo, endurance from duty cycle, cost from the number of DOFs. Skipping this step and buying motors directly is like buying bricks without a blueprint. For a perceptual anchor of whole-machine scale, see [Chapter 26: Whole System Case Studies](/wiki/chapters/chapter-26/) and the cards for [Tesla Optimus](/entry/ent_robot_system_tesla_optimus/), [Unitree H1](/entry/ent_robot_unitree_h1_humanoid_robot_2024/).

[How to analyze your situation] After writing down the mission statement, make two cuts: ① Remove any "while I'm at it" functions — the first machine should do only one thing; ② Simplify the environment as much as possible (indoor, flat ground, fixed lighting). Proving a complete chain on one machine is far more valuable than stacking five half-finished features.

## Step 2: From Mission to Load Spectrum — Calculate Peak Torque

[What to do] For each joint, use the **lever equation** to estimate the lower bound of peak torque:

```
τ_joint ≥ m_load × g × L_arm × S
```

- `m_load`: Total mass to be lifted downstream of the joint (including arm self-weight + end-effector load), in kg
- `g = 9.81 m/s²`, `L_arm`: Horizontal distance from the center of mass to the joint axis, in m
- `S`: Safety factor, 1.5 for static, 2–3 for dynamic (walking/running/catching/throwing)

Example (desktop arm shoulder flexion/extension joint): Arm + hand total 1.2 kg, end-effector grasps 0.5 kg, equivalent center-of-mass arm length 0.25 m, dynamic safety factor 2:

```
τ ≥ (1.2 + 0.5) × 9.81 × 0.25 × 2 ≈ 8.3 N·m
```

Fill the results for each joint into the specification sheet (template in Step 4). For bipedal hip/knee joints in the stance phase, they must bear **total robot weight × single-leg support impact**; when estimating, take `m_load` as the total robot mass and start with `S` = 2.5.

[Why] Peak torque is the primary constraint that determines the motor and reducer. Underestimating it means the system cannot drive the load; overestimating it wastes money and adds weight. The [Frameless Torque Motor](/entry/ent_component_frameless_torque_motor_2024/) card shows the physical root is τ ∝ r²l (torque scales with the square of the radius) — doubling the torque requirement only requires a ×1.41 increase in motor diameter, which is why joint motors are often made like "pancakes." For a systematic discussion of the actuator layer, see [Chapter 4: Actuators](/wiki/chapters/chapter-04/).

[How to analyze your situation] When CAD weight data is unavailable, use the analogy method: The Berkeley Humanoid Lite weighs about 16 kg with 12 DOFs (`data/roadmap/research/berkeley-humanoid-lite.md`). Scale the joint torque of your desktop machine according to the weight ratio. Joints with calculated torque < 3 N·m can use smart servos ([XM430 stall torque 3.0 N·m](/entry/ent_component_dynamixel_xm430_w210_t/)); 3–15 N·m consider custom QDD (M02); anything larger enters the world of industrial frameless motors.

## Step 3: From Mission to Speed and Duty Cycle — Calculate RPM and Heat

[What to do] Fill in two more columns:

1. **Rated Output Speed**: Derived from action time. "Swing the arm 90° in 0.5 s" → 90°/0.5 s = 180°/s ≈ 30 rpm at the output. Motor speed = output speed × reduction ratio; this number will be used in M03.
2. **Duty Cycle**: The proportion of time the joint is exerting force within the task cycle. For a walking platform, support legs are about 50–70%; for a desktop arm, pick-and-place is about 20–30%. Duty cycle × stall heat generation = average thermal load, which determines the continuous current rating rather than the peak.

[Why] A motor's peak torque can only be sustained for a few seconds (limited by heat). What it can continuously output depends on the duty cycle and thermal design. Speed, in turn, constrains the reduction ratio — [Harmonic Drives](/entry/ent_component_harmonic_reducer_2024/) are commonly 50–100:1, paired with a 3000 rpm motor yielding 30–60 rpm output, which is sufficient; but to achieve 120 rpm with the same reduction ratio, a lower ratio solution is needed. For heat and continuous rating, see [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/) and the [Thermal Simulation](/entry/ent_method_thermal_simulation/) card.

[How to analyze your situation] Don't pursue redundant speed: humanoid joint outputs rarely exceed 60 rpm. Exceeding the speed target often means the reduction ratio is too low (to be rechecked in M03). If you are unsure about the duty cycle, estimate it at 50%; the M07 bench temperature rise test will verify the actual value.

## Step 4: Deliver the Joint Specification Sheet (Core Deliverable of This Task)

[What to do] Summarize all joints into a single table, filling in numbers or marking "needs confirmation" column by column, and print it out to post at your workstation:

| Joint | DOF | Peak Torque (N·m) | Rated Speed (rpm) | Mass Budget (g) | Backlash Limit | Cost Limit |
|---|---|---|---|---|---|---|
| Example: Shoulder Flex/Ext | 1 Rot | ≥ 8.3 (Step 2 example) | ≥ 30 | ≤ 400 (3–5% of total weight per joint, engineering recommendation) | Precision-grade near-zero (see [Harmonic Drive](/entry/ent_component_harmonic_drive_reducer/) card) | Total budget ÷ DOF |
| … (one row per joint) | | | | | | |

Write down two global constraints simultaneously: **Total DOF** (desktop arm 5–7, biped 10–16, full body 20+) and **Total Machine Weight/Cost Limit**. Anchors: Berkeley 6512 QDD single joint BOM ~$157–188 (`data/roadmap/research/berkeley-humanoid-lite.md`); finished humanoid ROBOTIS OP3 sells for $13,764.35 (snapshot from `data/roadmap/research/robotis-op3-darwin-op.md`).

[Why] This sheet is the "contract" for the next six tasks (M02–M07): motor selection matches the torque column, reduction ratio matches the speed/backlash columns, structure matches the mass column, procurement matches the cost column. Without it, every part will require re-negotiation.

[How to analyze your situation] For cells you cannot fill, do not make up numbers. Mark them as "needs confirmation" and clearly state what data is missing (downstream mass? supplier specs?). Update the sheet each time a subsequent task resolves an issue — this sheet is a living document.

## Step 5: Cost Model and Procurement Boundaries

[What to do] Break down the BOM budget into three layers and specify the upper limit for each:

1. **Actuation Layer** (motor + reducer + encoder + driver board, M02–M04): Typically accounts for 50–70% of the total machine cost;
2. **Structure and Manufacturing Layer** (3D printed parts/machined parts/bearings/fasteners, M05): When using FDM printing, mainly machine time and material cost;
3. **Computing and Power Layer** (main controller/battery/BMS/emergency stop, M09): Refer to the [Compute Platform Selection Guide](../playbooks/compute-selection.md) and the [Battery Management System](/entry/ent_component_battery_management_system/) card.

[Why] Budget overruns almost always occur in the actuation layer — the cost of DOFs × single joint cost is easily underestimated. Calculate the total bill before starting: 20 DOFs × $180 ≈ $3,600, which is the scale of the Berkeley Humanoid Lite's total cost of $3,236–4,312 (from research files).

[How to analyze your situation] Total budget < ¥5,000: Reduce DOFs (build only an arm or only the lower body), do not cut the quality of individual joints; ¥20,000–50,000: Can fully cover a 12–16 DOF biped; Only above ¥100,000 does it become feasible to freely combine industrial components ([Harmonic Drive](/entry/ent_component_harmonic_reducer_2024/) + [Frameless Motor](/entry/ent_component_frameless_torque_motor_2024/)).

## Acceptance Criteria

- [ ] A one-sentence task description is written, containing the four elements of environment/frequency/load/motion, and functional reductions have been made.
- [ ] Each joint's peak torque includes a formula, a numerical value, and a justification for the safety factor selection.
- [ ] Each joint's rated output speed and duty cycle have a numerical value or are marked as "to be confirmed by oneself."
- [ ] The joint specification table is documented: all five columns are complete, including total degrees of freedom, overall machine mass, and cost ceiling.
- [ ] The BOM three-layer budget breakdown is complete, with the total cost of the drive layer ≤ 70% of the total budget.
- [ ] The specification table has been shared/archived (subsequent M02–M07 will update this table with each change).

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Calculated torque is absurdly high | Treating the overall machine mass as the load for each joint | Only calculate the mass **downstream** of that joint; use the full machine weight only during the double-support phase |
| Stuck after filling half the specification table | Pursuing perfect data, leading to analysis paralysis | First fill in the order of magnitude (1/3/10 N·m), mark as "to be verified," M02/M07 will close the loop |
| Degrees of freedom keep increasing | Feature creep | Return to step 1 and re-read the task description; each degree of freedom must serve that sentence |
| Budget table omits wiring/fasteners/failed prints | Only accounting for major components | Add a 15% loss margin to both the structure layer and the drive layer (engineering recommendation) |

## Supporting Reading

- Next task: [M02 · Motor Calculation and Selection](m02-motor-sizing.md)
- Theoretical background: [Chapter 4 Actuators](/wiki/chapters/chapter-04/), [Chapter 8 Humanoid Robot Design Principles](/wiki/chapters/chapter-08/)
- [Stage 1 Overview](../stage-1-actuator.md) · [Roadmap Overview](../index.md)
