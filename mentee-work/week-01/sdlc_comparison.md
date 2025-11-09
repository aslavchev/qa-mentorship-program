# SDLC Model Comparison

## Part A: SDLC Comparison Matrix

| Criteria | Waterfall | Agile | V-Model | DevOps |
|----------|-----------|-------|---------|--------|
| **Best suited for** | Projects with well-defined requirements and minimal changes | Projects with evolving requirements and fast delivery needs | Projects requiring rigorous validation and verification | Projects with continuous delivery, automation, and rapid deployment |
| **Project size** | Medium to large | Small to medium, can scale | Medium to large | Any size, often medium to large |
| **Requirement stability** | Stable requirements | Changing/flexible requirements | Stable requirements | Changing requirements with continuous feedback |
| **Customer involvement** | Low during development, higher at milestones | High, frequent feedback | Moderate, mainly at verification stages | High, continuous collaboration and monitoring |
| **When testing occurs** | After development phase | Continuous testing in each iteration | At each corresponding development phase (verification) | Continuous testing and integration throughout lifecycle |
| **Documentation level** | High | Moderate | High | Moderate to high, often automated |
| **Flexibility to change** | Low | High | Low to moderate | High, supports continuous changes |
| **Risk level** | Moderate to high if changes occur | Lower due to adaptability | Low if validation is strict | Lower due to automated pipelines and early detection |

## Part B: QA Role by Model

### Waterfall:
- Key activities: Requirement reviews, test plan creation, test case design, system testing after development.
- Challenges: Late discovery of defects, inflexible to requirement changes.
- When QA is most active: After development phase and during system integration testing.

### Agile:
- Key activities: Continuous testing in sprints, collaboration with developers, automated tests, regression testing.
- Challenges: Keeping pace with fast iterations, ensuring coverage.
- When QA is most active: Throughout each sprint, from planning to review.

### V-Model:
- Key activities: Requirement validation, test planning aligned with development phases, unit, integration, system, and acceptance testing.
- Challenges: High upfront effort in documentation, less flexibility to changes.
- When QA is most active: During each corresponding testing phase aligned with development.

### DevOps:
- Key activities: Continuous integration and delivery, automated testing, monitoring, deployment validation.
- Challenges: Tooling complexity, maintaining quality in fast-paced releases.
- When QA is most active: Continuously throughout development, integration, and deployment.

## Part C: Scenario Matching

1. A startup building a new social media app with evolving features
   - **Best Model:** Agile
   - **Justification:** Agile supports rapid iterations and adapts to changing requirements, allowing the startup to continuously improve the app.

2. A medical device with strict regulatory requirements
   - **Best Model:** V-Model
   - **Justification:** V-Model ensures rigorous validation and verification at each stage, which is critical for regulatory compliance and safety.

3. A government contract with fixed requirements and timeline
   - **Best Model:** Waterfall
   - **Justification:** Waterfall works well for projects with stable, well-defined requirements and clear deadlines, typical in government contracts.

4. A SaaS product requiring weekly releases
   - **Best Model:** DevOps
   - **Justification:** DevOps enables continuous integration, automated testing, and frequent deployments, ideal for weekly release cycles.

