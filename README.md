# Machine Learning project template

The objective of this repository is to serve as a template for machine learning projects.

## Getting Started

To set up the project, the easiest way is to copy the all the folders into an empty GitHub repository. Make sure you change the name of the library `miguellib`.

## Structure

- .github: CI/CD with GitHub Actions. It runs the tests every time there is a pull request to the repository.
- docs: Documentation of the project.
- examples: Jupyter notebooks with machine learning experiments. Here is where you would do data exploration, try different machine learning models, etc.
- miguellib: Libraries with common functions that you use in the project. 
- tests: Python tests of the libraries.

## Setup

    pip install -e .
    python -c "import miguellib; print(miguellib.__version__)"

## Coding Principles

Next there are a few coding principles that I follow when working on machine learning projects.

### Start from something that works

Here is one of the most practical tips I know about working on machine learning. **Instead of starting from scratch, start with something that works and adapt it to your problem.**

For example, let's say you want to build a recommendation system with data from your company. What I would do is something as simple as this:

1. Go to [Recommenders](https://github.com/recommenders-team/recommenders) and look at an example that a similar dataset structure and compute. For example, if your data is text-based and you want to use GPU, explore the examples of LSTUR or NPA.
2. Install the dependencies and run the example. Make sure that it works.
3. Change the data of the example to your data. If your data is different or more extensive, just forget about it and use the part of your data that is similar to the example. Make sure that it works.
4. Change the code to adapt it to your specific data and problem.

### Notebooks that call a library

One of the main differences between a professional and an amateur machine learning project is this. Don't put your functions and classes in the notebooks, instead, create libraries and call them from the notebooks. This is the only way to reuse your code and make it scalable. 

Most of the time, notebooks are not deployed, they are used for experimentation and visualization. You deploy the libraries. In addition, if you create libraries, you can test them.

### Why tests are important?

Tests solve one of the most expensive problems in development: maintenance. The way I see testing is like the immune system of your project. It protects your project from bugs and errors and makes sure your project is healthy. 

A strong test pipeline minimizes maintenance. It is one of the best investments you can do in your project, because it will avoid new buggy code in the project, and it will detect breaking changes when using dependencies.

## Agents & Skills

### Recommended Structure

```
├── skills/
│   ├── <name>/
│   │   ├── SKILL.md            ← Instructions (required)
│   │   ├── references/         ← Extended documentation (optional)
│   │   │   ├── reference1.md
│   │   │   └── reference2.md
│   │   ├── scripts/            ← Code scripts (optional)
│   │   │   └── generate.py
│   │   └── resources/          ← Binary files (optional)
│   │       └── template.pptx
│   └── ...
├── agents/
│   └── <name>.md               ← Frontmatter + system prompt
```

### Skills

Each skill lives in its own directory under `skills/` and must contain a `SKILL.md` file with YAML frontmatter and the instructions body.

#### Frontmatter

```yaml
---
name: my-skill
description: >
  What this skill does and when agents should use it.
  Include trigger phrases so agents know when to load the skill.
metadata:
  version: 1.0.0
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier for the skill. |
| `description` | Yes | Domain, capabilities, and trigger phrases the agent uses to decide whether to load the skill. |
| `metadata` | Yes | Custom block for organizing and versioning (see [`metadata` block](#metadata-block) below). |
| `disable-model-invocation` | No | Set to `true` so only the user can invoke it (not Claude automatically). |
| `user-invocable` | No | Set to `false` so only Claude can load it (does not appear in the `/` menu). |
| `allowed-tools` | No | Tools allowed without asking permission when the skill is active. E.g. `Read Grep Edit`. |
| `model` | No | Model to use (`sonnet`, `opus`, `haiku`). |
| `effort` | No | Reasoning level: `low`, `medium`, `high`, `max`. |
| `context` | No | Set to `fork` to run in an isolated subagent. |
| `agent` | No | Subagent type when `context: fork`. E.g. `Explore`, `Plan`, `general-purpose`. |
| `paths` | No | Globs that limit when the skill auto-activates. E.g. `src/**,tests/**`. |
| `shell` | No | Shell for inline commands: `bash` (default) or `powershell`. |
| `argument-hint` | No | Autocomplete hint. E.g. `[issue-number]`. |
| `hooks` | No | Lifecycle hooks, scoped to the skill. |

#### `metadata` Block

Custom block (not interpreted by Claude Code) for organizing and versioning skills.

```yaml
metadata:
  version: 1.0.0
```

| Field | Required | Description |
|-------|----------|-------------|
| `version` | Yes | Semantic version of the skill. |
| `<custom>` | No | Any additional custom metadata. |

#### Full `SKILL.md` Example

```yaml
---
name: data-validation
description: >
  Validate dataframes against a schema before training.
  Use when the user mentions "validate", "schema check", or "data quality".
---

# Data Validation

1. Load the schema from `config/schema.yaml`.
2. Run `scripts/validate.py --input <path>`.
3. Report mismatches as a markdown table.
```

The system uses **progressive disclosure**: at startup only the frontmatter is parsed to keep context small. The full body is loaded only when a task matches the skill's domain. Files in `references/`, `scripts/`, and `resources/` are fetched on demand.

### Agents

Each agent is a single Markdown file under `agents/` with YAML frontmatter and a system prompt body.

#### Frontmatter

```yaml
---
name: my-agent
description: >
  What this agent does and when it should be invoked.
tools: Read, Write, Glob, Grep, Bash
skills:
  - my-skill
metadata:
  version: 1.0.0
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier (kebab-case). |
| `description` | Yes | When and why to delegate to this agent. |
| `metadata` | Yes | Custom block for organizing and versioning (see [`metadata` block](#metadata-block) above). |
| `tools` | No | Tools available to the agent. |
| `skills` | No | Skills preloaded when the agent starts. |
| `model` | No | Model to use (`sonnet`, `opus`, `haiku`). Inherits from parent by default. |
| `maxTurns` | No | Maximum number of turns allowed. |
| `effort` | No | Reasoning level: `low`, `medium`, `high`. |
| `license` | No | License of the agent. |

#### Full Agent Example

```yaml
---
name: test-runner
description: >
  Run the project test suite and report failures.
  Use when the user asks to run tests or validate changes.
tools: Read, Bash, Grep
skills:
  - test-helpers
maxTurns: 20
metadata:
  version: 1.0.0
---

You are a test-runner agent. Your job is to:

1. Identify the test framework configured in `pyproject.toml`.
2. Run the test suite with `pytest -v`.
3. Report a summary of passed/failed tests as a markdown table.
4. If any test fails, read the failing test file and suggest a fix.
```
