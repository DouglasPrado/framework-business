# AGENTS  AI Agent Operating Instructions

## Purpose

This document provides specific instructions for AI agents (like Claude, ChatGPT, or other LLMs) working within this operational framework. Follow these guidelines to ensure consistency, quality, and alignment with the business system defined in this repository.

## Core Principles

1. **Always read before writing**: Before creating or updating any file, read the relevant models and existing documentation
2. **Use models as source of truth**: All deliverables must follow the templates in `models/`
3. **Maintain consistency**: Use established vocabulary, structure, and patterns from existing files
4. **Update dependencies**: When changing one file, verify and update all related files in the same session
5. **Work in English with CamelCase**: All file names and process folders use CamelCase format (`<ProcessName>`)

## Operating Workflow

### When creating a new process

1. **Read foundation documents**:
   - [README.MD](README.MD) - System overview
   - [process/README.MD](process/README.MD) - Process structure standards
   - `models/process/README.MD` - Official templates

2. **Check for reusable artifacts across processes**:
   - **First, check `process/_SHARED/`** for existing shared templates and references
   - Search all existing processes in `process/` for similar tasks or artifacts
   - Review `_DATA/` folders of related processes for reusable templates, examples, or outputs
   - Identify tasks that have already been executed in other processes
   - **Reference shared artifacts from `_SHARED/`** instead of duplicating work
   - If artifact is used by 2+ processes, consider moving it to `_SHARED/templates/` or `_SHARED/references/`
   - Document shared artifacts in `knowledge.MD` with references to source processes or `_SHARED/`
   - Avoid creating redundant tasks - reuse and adapt existing ones when possible

3. **Copy and customize templates**:
   - Create folder: `process/<ProcessName>/`
   - Create subfolder: `process/<ProcessName>/_DATA/` for storing all process artifacts
   - Copy models: `process.MD`, `knowledge.MD`, `tasks.MD`, `validator.MD`
   - Customize each file according to the specific process requirements

4. **Document comprehensively**:
   - `process.MD`: objectives, scope, steps, expected outputs, indicators, warnings
   - `knowledge.MD`: references, support materials, FAQs, checkpoints
   - `tasks.MD`: operational sequence following process.MD structure
   - `validator.MD`: quality checks and validation criteria

5. **Verify consistency**:
   - Cross-reference Process � Tasks � Validator � Models
   - Ensure terminology alignment across all files
   - Update dependencies in the same session

### When updating existing content

1. **Identify scope**: Understand what needs to change and why
2. **Read dependencies**: Review all related files before editing
3. **Update atomically**: Make all necessary changes in a single session
4. **Document changes**: If models change, update all processes built from them

### When referencing tools or resources

- Only reference tools listed in `tools/`
- Do not suggest external solutions not mapped in the approved catalog
- If a new tool is needed, document the requirement for manual approval

### When working with strategies

- Strategies in `strategies/` define which processes should be created or revised
- Consult relevant playbooks and triggers before proposing new processes
- Align process objectives with strategic theses

### During process execution

1. Request a clear context from the requester before starting any process, capturing objectives, assumptions, and constraints.
2. Convert the context into a short English title and apply CamelCase; this becomes the folder name in `drive/` (e.g., `drive/MarketEntryDiagnostics`).
3. Check whether the CamelCase folder already exists in `drive/`; if not, create it following the naming guidance in `drive/README.MD`.
4. For each process executed within that context, create a subfolder named exactly after the process (e.g., `drive/MarketEntryDiagnostics/ProblemHypothesisExpress`).
5. Copy every relevant artifact from `process/<Process>/_DATA/` into the corresponding subfolder, preserving structure and sequence; rename files to the numeric `01-`, `02-`, etc. pattern when needed, and place them directly in the process folder without recreating `_DATA` inside `drive/`.
6. Update the copied files with execution-specific results while keeping the text in Portuguese, aligned with the process model, and referencing the recorded context.

## File Conventions

### Naming
- Folders: `CamelCase` (e.g., `ContentProduction`, `LeadQualification`)
- Files: `lowercase.MD` (e.g., `process.MD`, `knowledge.MD`)
- Data folder: `_DATA` (uppercase with underscore prefix)
- No spaces, special characters, or non-ASCII in file names

### Structure
- Use markdown formatting consistently
- Include section headers following model templates
- Keep plain text format (no external spreadsheets)
- **Do NOT use markdown tables** - use bullet lists, numbered lists, or plain text instead
- **Do NOT use emojis** - keep all content professional and text-only
- Use relative links for internal references
- Store all process artifacts (templates, examples, outputs, references) in `_DATA/` folder

### Data Folder (`_DATA/`)
Every process must include a `_DATA/` folder to store all artifacts:
- **Templates**: Document templates, email templates, content templates
- **Examples**: Sample outputs, reference materials, best practices
- **Outputs**: Generated deliverables, reports, analysis results
- **References**: External documents, images, diagrams, supporting files
- **Assets**: Any binary files, spreadsheets, or non-markdown resources
- Keep `_DATA/` organized with subfolders if needed (e.g., `_DATA/templates/`, `_DATA/examples/`)

### Shared Artifacts Folder (`process/_SHARED/`)
For artifacts used by multiple processes:
- **Location**: `process/_SHARED/templates/` and `process/_SHARED/references/`
- **Purpose**: Avoid duplication, maintain consistency across processes
- **Usage**: Reference shared artifacts instead of copying to local `_DATA/`
- **Criteria**: Move artifact to `_SHARED/` when used by 2+ processes
- **Documentation**: See [process/_SHARED/README.MD](process/_SHARED/README.MD) for complete guidelines
- **Examples**: Template de declaração de hipótese, checklists padrão, referências comuns

### Language
- **Write all markdown content in Portuguese (pt-BR)**
- File names remain in English with CamelCase format
- Use clear, simple, actionable language
- Align vocabulary with existing documentation
- Avoid jargon unless defined in knowledge.MD
- **No emojis** - maintain professional, text-only documentation

## Response Patterns

### When asked to create a process

 **DO**:
- Read README.MD and relevant models first
- **Check `process/_SHARED/` first for existing shared templates**
- **Search all existing processes for reusable artifacts before creating new tasks**
- Ask clarifying questions if scope is unclear
- Use TodoWrite to track creation steps
- Create all required files (process.MD, knowledge.MD, tasks.MD, validator.MD)
- Create `_DATA/` folder for storing process artifacts
- **Reference shared artifacts from `_SHARED/` instead of duplicating**
- Reference existing artifacts in knowledge.MD when reusing from other processes or `_SHARED/`
- **If creating artifact used by 2+ processes, place in `_SHARED/` and update README**
- Verify completeness before finishing

L **DON'T**:
- Create processes without reading models
- Skip any required file (including `_DATA/` folder)
- Use custom templates instead of official models
- Use markdown tables (use bullet/numbered lists instead)
- Use emojis in any process files
- Leave inconsistencies between files

### When asked to update documentation

 **DO**:
- Read the current file before editing
- Identify all dependencies
- Update all affected files in the same session
- Maintain existing structure and style
- Preserve formatting and conventions

L **DON'T**:
- Make isolated changes without checking dependencies
- Change file structure without updating models
- Mix languages or naming conventions
- Create new files when updating existing ones is sufficient

### When asked to generate tasks

 **DO**:
- Base tasks on process.MD structure
- Follow the model in `models/process/tasks.MD`
- Include clear, actionable steps
- Reference specific tools from `tools/`
- Align with validator.MD criteria

L **DON'T**:
- Create tasks without reading process.MD
- Skip steps or assume implicit knowledge
- Reference unapproved tools
- Ignore validation requirements

## Quality Checklist

Before completing any work, verify:

- [ ] All required files created/updated
- [ ] `_DATA/` folder created for process artifacts
- [ ] **`process/_SHARED/` checked for existing shared templates first**
- [ ] **Existing processes checked for reusable artifacts**
- [ ] **No duplicate tasks - existing artifacts referenced when possible**
- [ ] **Shared artifacts from `_SHARED/` referenced instead of duplicated**
- [ ] Models used as templates
- [ ] Dependencies checked and updated
- [ ] Naming conventions followed (CamelCase for folders, lowercase.MD for files)
- [ ] Portuguese language throughout all markdown content
- [ ] Plain text format maintained (no markdown tables, no emojis)
- [ ] Internal links are relative and correct
- [ ] Vocabulary aligns with existing docs
- [ ] No external/unapproved tool references
- [ ] Process ↔ Tasks ↔ Validator consistency verified
- [ ] Artifacts properly stored in `_DATA/` folder

## Common Scenarios

### "Create a new process for [X]"
1. Read README.MD, process/README.MD, and models
2. Use TodoWrite to plan: read models, check _SHARED, check existing processes, create folder, copy templates, customize files, verify
3. **Check `process/_SHARED/` first** for existing shared templates and references
4. **Search existing processes** for reusable artifacts in `process/*/`
5. Review `_DATA/` folders of related processes for templates, examples, and outputs
6. Create `process/<ProcessName>/` folder
7. Create `process/<ProcessName>/_DATA/` folder for artifacts
8. Copy all model files from `models/process/`
9. Customize each file for the specific process
10. **Reference shared artifacts from `_SHARED/`** instead of duplicating tasks
11. If creating new template used by 2+ processes, add to `_SHARED/` and update its README
12. Cross-check all files for consistency

### "Update the [ProcessName] process"
1. Read current `process/<ProcessName>/process.MD`
2. Identify what needs to change
3. Check dependencies (tasks.MD, validator.MD, knowledge.MD)
4. Update all affected files
5. Verify consistency across the process package

### "Add tasks for [ProcessName]"
1. Read `process/<ProcessName>/process.MD`
2. Read `models/process/tasks.MD` for template
3. Read existing `process/<ProcessName>/tasks.MD`
4. Add or update tasks following the model
5. Ensure alignment with process.MD steps
6. Verify validator.MD still applies

### "This process needs a new tool"
1. Check if tool exists in `tools/`
2. If not, document the requirement clearly
3. Explain why existing approved tools are insufficient
4. Wait for manual approval before referencing in processes

## Error Prevention

### Common mistakes to avoid
- Creating files without reading models
- Writing markdown content in English instead of Portuguese
- Skipping required files (validator.MD, knowledge.MD, `_DATA/` folder)
- **Not checking `process/_SHARED/` for existing shared templates first**
- **Not checking existing processes for reusable artifacts before creating new tasks**
- **Duplicating tasks or artifacts that already exist in other processes or `_SHARED/`**
- **Creating duplicate templates when shared version exists in `_SHARED/`**
- Not updating dependencies when changing files
- Referencing external tools not in `tools/`
- Using snake_case or other naming formats
- Creating parallel documentation outside the process folder
- Storing artifacts outside the `_DATA/` folder
- Using markdown tables in process files (use lists instead)
- Using emojis in process documentation

### When uncertain
- Ask clarifying questions
- Read related documentation
- Check existing processes for patterns
- Consult models for template structure
- Verify with user before making structural changes

## Integration with Other Files

- **README.MD**: Overall system guide - consult for structure understanding
- **CLAUDE.MD**: Additional AI-specific instructions for Claude Code integration
- **process/README.MD**: Process structure standards - always follow
- **process/_SHARED/README.MD**: Shared artifacts guidelines - check before creating templates
- **models/README.MD**: Model documentation - source of truth for templates
- **tools/**: Approved tool catalog - only reference these
- **strategies/**: Strategic direction - aligns process creation

## Execution Standards

- Be precise and thorough
- Work systematically through checklists
- Document as you build
- Maintain traceability between strategic decisions and operational tasks
- Prioritize clarity and executability
- Ensure deliverables are immediately usable by human operators

---

**Remember**: This framework exists to enable scalable, consistent business operations. Your role as an agent is to maintain that consistency while being flexible enough to handle unique process requirements. When in doubt, read the models and ask questions.
