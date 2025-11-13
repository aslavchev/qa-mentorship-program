# Pull Request Workflow Guide

## Overview

This guide explains how to submit your weekly work through Pull Requests (PRs). Following this workflow ensures clean version control, easy reviews, and professional collaboration practices.

## Core Principles

1. **One PR = One Concern** - Never mix corrections with new work
2. **Always address open issues BEFORE starting new work**
3. **Always assign PRs to your mentor (@aslavchev)**
4. **Use proper branch naming conventions**
5. **Follow English language and file naming standards**

---

## Git Commands: Modern vs Traditional

**Modern Git (2.23+) introduced clearer commands:**

### Switching Branches

**Modern way (recommended):**
```bash
git switch main              # Switch to existing branch
git switch -c new-branch     # Create and switch to new branch
```

**Traditional way (still works):**
```bash
git checkout main            # Switch to existing branch
git checkout -b new-branch   # Create and switch to new branch
```

**Why modern commands are better:**
- ✅ Clearer intent (`switch` for branches, `restore` for files)
- ✅ Safer (won't accidentally modify files)
- ✅ Easier to learn and remember

**Note:** Both ways work! This guide uses `git checkout` for now, but you can use `git switch` instead.

---

## Standard Weekly Workflow

### Step 1: Check for Open Issues

Before starting ANY new week, check if there are open issues from previous weeks:

```bash
# Check for open issues
gh issue list --assignee @me --state open

# Example output:
# #1  Week 1 Corrections Needed  (week-01, corrections-needed)
```

**Rule**: If issues exist, you MUST fix them FIRST before starting new work.

---

## Scenario A: No Open Issues - Starting New Week

Use this when previous week is approved and merged.

### 1. Start from Clean Main Branch

```bash
# Ensure you're on main and it's up to date
git checkout main
git pull origin main
```

### 2. Create Properly Named Branch

**Branch naming pattern**: `week-XX-work` (where XX is the week number with leading zero)

```bash
# Example for Week 2:
git checkout -b week-02-work

# Example for Week 10:
git checkout -b week-10-work
```

### 3. Complete Your Weekly Exercises

- Create your deliverables in `mentee-work/week-XX/` directory
- Use **hyphens** in filenames (e.g., `test-levels.md`, NOT `test_levels.md`)
- Write all content in **English**
- Test that all links and references work

### 4. Commit Your Work

```bash
# Add all your week's files
git add mentee-work/week-XX/

# Commit with clear message
git commit -m "Week XX: [brief description of exercises]"

# Examples:
# git commit -m "Week 02: Test levels and integration scenarios"
# git commit -m "Week 03: Functional testing types for SauceDemo"
```

### 5. Push Branch to GitHub

```bash
# Push your branch (first time)
git push -u origin week-XX-work
```

### 6. Create Pull Request with Assignment

```bash
# Create PR and assign to mentor
gh pr create \
  --base main \
  --head week-XX-work \
  --title "Week XX: [Brief Title]" \
  --body "Week XX exercises completed. Ready for review." \
  --assignee aslavchev

# Example:
gh pr create \
  --base main \
  --head week-02-work \
  --title "Week 02: Test Levels and Integration" \
  --body "Week 02 exercises completed. Ready for review." \
  --assignee aslavchev
```

### 7. Wait for Review

- Mentor will review within 24-48 hours
- Address any feedback requested
- Once approved, mentor will merge

---

## Scenario B: Open Issues Exist - Corrections Needed

Use this when your mentor has provided feedback on previous work.

### 1. Review Issue Feedback

```bash
# View issue details
gh issue view [issue-number]

# Example:
gh issue view 1
```

Read ALL feedback carefully and understand what needs to be corrected.

### 2. Create Corrections Branch

**Branch naming pattern**: `week-XX-corrections`

```bash
# Start from clean main
git checkout main
git pull origin main

# Create corrections branch
git checkout -b week-XX-corrections

# Example for Week 1 corrections:
git checkout -b week-01-corrections
```

### 3. Fix ALL Issues Mentioned

Common corrections:

**File Renaming (underscores → hyphens):**
```bash
# Use git mv to rename files
git mv mentee-work/week-01/test_levels.md mentee-work/week-01/test-levels.md
git mv mentee-work/week-01/sdlc_comparison.md mentee-work/week-01/sdlc-comparison.md

# Apply to ALL files that need renaming
```

**Translate Content to English:**
- Open files in your editor
- Translate all Bulgarian/Cyrillic content to English
- Ensure technical terms are correct

**Content Corrections:**
- Address specific feedback about concepts, formatting, or completeness
- Re-read corrected sections to ensure clarity

### 4. Commit Corrections

```bash
# Add all corrected files
git add mentee-work/week-XX/

# Commit with descriptive message
git commit -m "Week XX corrections: [what was fixed]"

# Example:
git commit -m "Week 01 corrections: Translate to English, fix file naming"
```

### 5. Push and Create Corrections PR

```bash
# Push corrections branch
git push -u origin week-XX-corrections

# Create PR referencing the issue
gh pr create \
  --base main \
  --head week-XX-corrections \
  --title "Week XX Corrections" \
  --body "Addresses Issue #[number]: [brief summary of fixes]" \
  --assignee aslavchev

# Example:
gh pr create \
  --base main \
  --head week-01-corrections \
  --title "Week 01 Corrections" \
  --body "Addresses Issue #1: Translated content to English, fixed file naming conventions, moved files to correct directory" \
  --assignee aslavchev
```

### 6. Comment on Original Issue

```bash
# Link your corrections PR to the issue
gh issue comment [issue-number] --body "Corrections submitted in PR #[pr-number]"

# Example:
gh issue comment 1 --body "Corrections submitted in PR #3"
```

### 7. Wait for Corrections Review

- Mentor will review corrections
- Once approved and merged, the issue will be closed
- **THEN** you can start next week's work

---

## Scenario C: Mixed Work (Wrong Approach)

❌ **NEVER DO THIS**: Create one PR with both corrections AND new week work

### If You Already Created Mixed PR:

1. **Close the mixed PR:**
```bash
gh pr close [pr-number] --comment "Closing to split into separate PRs per workflow requirements"
```

2. **Follow Scenario B** to create corrections PR first

3. **After corrections merged**, follow Scenario A for new week

---

## Common Commands Quick Reference

### Checking Status

```bash
# Check current branch
git branch --show-current

# Check what files changed
git status

# Check open issues assigned to you
gh issue list --assignee @me --state open

# Check your open PRs
gh pr list --author @me --state open
```

### Branch Management

```bash
# Switch to main and update
git checkout main
git pull origin main

# Create new branch
git checkout -b branch-name

# List all local branches
git branch

# Delete local branch (after merged)
git branch -d branch-name
```

### Viewing PRs and Issues

```bash
# View PR in terminal
gh pr view [number]

# Open PR in browser
gh pr view [number] --web

# View issue
gh issue view [number]

# Open issue in browser
gh issue view [number] --web
```

---

## File Naming Standards

### ✅ Correct

- `test-levels.md`
- `sdlc-comparison.md`
- `qa-qc-testing-comparison.md`
- `saucedemo-analysis.md`

### ❌ Incorrect

- `test_levels.md` (underscores)
- `testLevels.md` (camelCase)
- `TestLevels.md` (PascalCase)
- `test levels.md` (spaces)

**Rule**: Use lowercase with hyphens for multi-word filenames.

---

## Language Standard

All content must be in **English**:
- Exercise answers
- Documentation
- Code comments
- Commit messages
- PR titles and descriptions

---

## Checklist Before Creating PR

Use this checklist BEFORE running `gh pr create`:

- [ ] I'm on the correct branch (`week-XX-work` or `week-XX-corrections`)
- [ ] All files are in correct directory (`mentee-work/week-XX/`)
- [ ] All filenames use hyphens (not underscores)
- [ ] All content is in English
- [ ] I ran `git status` to verify only intended files are changed
- [ ] My commit message is clear and descriptive
- [ ] I checked for open issues first (for new week work)
- [ ] I will use `--assignee aslavchev` in the gh pr create command

---

## Troubleshooting

### "I created a PR but forgot to assign it"

```bash
# Assign existing PR to mentor
gh pr edit [pr-number] --add-assignee aslavchev
```

### "I committed to wrong branch"

```bash
# Move last commit to new branch
git branch week-XX-work
git reset --hard HEAD~1
git checkout week-XX-work
```

### "I need to update my PR after feedback"

```bash
# Make sure you're on the PR's branch
git checkout week-XX-work

# Make your changes, then:
git add .
git commit -m "Address review feedback: [what you fixed]"
git push origin week-XX-work

# PR automatically updates!
```

### "I pushed to main by accident"

Contact your mentor immediately. They will help fix it.

---

## Example: Complete Week 2 Workflow

```bash
# 1. Check for open issues
gh issue list --assignee @me --state open
# Result: No open issues ✅

# 2. Start from clean main
git checkout main
git pull origin main

# 3. Create week 2 branch
git checkout -b week-02-work

# 4. Do your work (create files in mentee-work/week-02/)
# ... complete exercises ...

# 5. Commit
git add mentee-work/week-02/
git commit -m "Week 02: Test levels and integration scenarios"

# 6. Push
git push -u origin week-02-work

# 7. Create PR
gh pr create \
  --base main \
  --head week-02-work \
  --title "Week 02: Test Levels and Integration" \
  --body "Week 02 exercises completed. Ready for review." \
  --assignee aslavchev

# 8. Wait for review
# ... mentor reviews ...
# ... mentor approves and merges ...

# 9. Start Week 3
git checkout main
git pull origin main
git checkout -b week-03-work
# ... repeat process ...
```

---

## Example: Corrections Workflow

```bash
# 1. Mentor created Issue #1 with feedback

# 2. Review feedback
gh issue view 1

# 3. Create corrections branch
git checkout main
git pull origin main
git checkout -b week-01-corrections

# 4. Fix issues
# - Translate files to English
# - Rename files with hyphens
git mv mentee-work/week-01/test_levels.md mentee-work/week-01/test-levels.md
# ... make other corrections ...

# 5. Commit
git add mentee-work/week-01/
git commit -m "Week 01 corrections: Translate to English, fix file naming"

# 6. Push and create PR
git push -u origin week-01-corrections
gh pr create \
  --base main \
  --head week-01-corrections \
  --title "Week 01 Corrections" \
  --body "Addresses Issue #1: Translated content, fixed naming" \
  --assignee aslavchev

# 7. Link PR to issue
gh issue comment 1 --body "Corrections submitted in PR #2"

# 8. Wait for approval
# ... mentor reviews and merges ...

# 9. NOW you can start Week 2
```

---

## Getting Help

If you're stuck or unsure:

1. **Check this guide first**
2. **Review the specific issue/PR feedback**
3. **Ask in the PR comments**: `gh pr comment [number] --body "Question: ..."`
4. **Create a new issue**: `gh issue create --title "Help: [your question]" --assignee aslavchev`
5. **Discuss in weekly mentor session**

---

**Remember**: Clean git workflow = Professional portfolio. Take your time to do it right! 🎯

---

**Last Updated:** November 13, 2024
**For:** QA Fundamentals Mentees

**Recent additions:**
- Modern git commands section (`git switch` vs `git checkout`)
- Clearer explanations of both traditional and modern workflows
- Note: Both command styles work - use what you're comfortable with!
