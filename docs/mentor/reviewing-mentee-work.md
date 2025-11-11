# Mentor Guide: Reviewing Mentee Work

## Overview

This guide documents the systematic approach for reviewing mentee Pull Requests and providing effective feedback. It's based on lessons learned from actual mentoring sessions and follows QA quality gate principles.

---

## Core Principles

### 1. Short, Actionable Feedback
**Lesson learned**: Long, comprehensive feedback can overwhelm and confuse mentees.

- ✅ **DO**: Keep feedback under 50 lines
- ✅ **DO**: Use bullet points and code blocks
- ✅ **DO**: Provide exact commands to fix issues
- ✅ **DO**: Link to detailed guides for "how to"
- ❌ **DON'T**: Write 300-line essays with every detail
- ❌ **DON'T**: Explain everything inline

**Example Pattern:**
```
Issues Found:
1. [Issue description]
2. [Issue description]

What to Do:
- Fix X (see docs/mentor/guide.md#section)
- Run command: `git command here`
- Create PR following [workflow guide](link)
```

### 2. Create Reusable Documentation First
When you encounter a repeatable teaching moment:

1. **Create permanent guide** in `docs/mentor/` or update README
2. **Then reference it** in feedback
3. **Don't repeat instructions** every time

**Benefits:**
- Mentee has single source of truth
- You don't rewrite instructions for each PR
- Other mentees benefit from documentation
- Maintains consistency across reviews

### 3. Separate Content Quality from Process Issues
Review in two dimensions:

**Content Quality** (concepts, completeness, accuracy):
- Document in detailed assessment (e.g., `feedback/week-XX-content-review.md`)
- Provide as GitHub Issue for tracking
- Grade if appropriate (e.g., 85/100)

**Process Issues** (git workflow, file naming, language):
- Address immediately in PR comments
- Block merge until fixed
- Reference workflow guides

---

## Review Workflow

### Step 1: Initial PR Assessment (5 minutes)

```bash
# View PR details
gh pr view [PR-number]

# Check files changed
gh pr diff [PR-number] --name-only

# Check commits
gh pr view [PR-number] --json commits --jq '.commits[] | .messageHeadline'

# Check if assigned correctly
gh pr view [PR-number] --json assignees --jq '.assignees[].login'
```

**Quick checklist:**
- [ ] PR assigned to you?
- [ ] Correct branch naming? (`week-XX-work` or `week-XX-corrections`)
- [ ] Single concern? (not mixing corrections + new work)
- [ ] Files in correct directory? (`mentee-work/week-XX/`)
- [ ] File naming correct? (hyphens, not underscores)
- [ ] Language correct? (English)

### Step 2: Check Prerequisites

**For new week PRs:**
```bash
# Check if previous week has open issues
gh issue list --assignee [mentee-username] --state open --label week-XX
```

**Rule**: New week PRs should NOT be submitted if previous week has open issues.

**For correction PRs:**
- Verify it references the issue: `gh issue view [issue-number]`
- Check all feedback points are addressed

### Step 3: Content Review (15-30 minutes)

**For initial submissions (Week X first PR):**

1. **Create comprehensive content assessment:**
   ```bash
   # Create detailed review
   vim feedback/week-XX-content-review.md
   ```

2. **Assessment structure:**
   ```markdown
   # Week XX Content Review

   ## Overall Assessment
   Grade: [score]/100
   Status: [Excellent/Good/Needs Improvement]

   ## Exercise 1: [Title]
   Grade: XX/100
   - [Strengths]
   - [Areas for improvement]
   - [Specific feedback]

   ## Exercise 2...
   ```

3. **Create GitHub Issue with content feedback:**
   ```bash
   gh issue create \
     --title "Week XX Feedback: [Corrections Required/Approved]" \
     --body-file feedback/week-XX-content-review.md \
     --label "week-XX,feedback" \
     --assignee [mentee-username]
   ```

**For correction PRs:**
- Verify each issue point is addressed
- Check quality of corrections
- Update quality gate status

### Step 4: Provide PR Feedback

**Scenario A: Process Issues Found (Workflow Violations)**

Create short, direct PR comment:

```bash
# Write concise feedback
vim feedback/pr-X-review.md

# Post to PR
gh pr comment [PR-number] --body-file feedback/pr-X-review.md
```

**Template:**
```markdown
## PR #X Review

### ❌ Issues Found
1. [Issue + brief explanation]
2. [Issue + brief explanation]

### ✅ What to Do
[Step-by-step with exact commands]

See [relevant workflow guide](link) for details.
```

**Scenario B: Corrections Look Good**

```bash
gh pr comment [PR-number] --body "✅ Corrections look good! All Issue #X points addressed. Approving and merging."

gh pr review [PR-number] --approve
gh pr merge [PR-number] --squash
gh issue close [issue-number]
```

**Scenario C: New Week Submission - Quality Review Needed**

```bash
# Add content review to issue
gh issue comment [issue-number] --body-file feedback/week-XX-content-review.md

# Comment on PR
gh pr comment [PR-number] --body "Content review posted to Issue #X. Please review feedback before I merge."
```

---

## Common Issues and Responses

### Issue: Mixed Work in Single PR

**Violation**: PR contains both corrections AND new week work

**Response:**
```markdown
❌ This PR mixes Week X corrections with Week Y new work.

What to Do:
1. Close this PR: `gh pr close [PR] --comment "Splitting into separate PRs"`
2. Create Week X corrections PR first (see [Scenario B](../docs/mentor/pr-workflow.md#scenario-b))
3. After merged, create Week Y PR separately (see [Scenario A](../docs/mentor/pr-workflow.md#scenario-a))
```

**Why short**: Points to workflow guide for details.

### Issue: Open Issues Not Addressed

**Violation**: Started new week while previous week has open issues

**Response:**
```markdown
❌ Issue #X has open feedback that must be addressed first.

What to Do:
1. Review Issue #X: `gh issue view X`
2. Create corrections branch and fix issues
3. Only after corrections merged, submit new week work

Rule: Always address open issues BEFORE starting new week.

See [Workflow Rule](../docs/mentor/pr-workflow.md#scenario-b-open-issues-exist---corrections-needed)
```

### Issue: File Naming Violations

**Violation**: Uses underscores instead of hyphens

**Response:**
```markdown
❌ File names use underscores (should be hyphens)

Fix with:
\`\`\`bash
git mv mentee-work/week-XX/test_cases.md mentee-work/week-XX/test-cases.md
# Repeat for all files
git commit -m "Fix file naming: hyphens instead of underscores"
\`\`\`

See [File Naming Standards](../docs/mentor/pr-workflow.md#file-naming-standards)
```

### Issue: Wrong Language (Not English)

**Violation**: Content in native language instead of English

**Response:**
```markdown
❌ Content must be in English

Fix:
1. Translate all content in `file.md` to English
2. Commit: `git commit -m "Translate content to English"`

See [Language Standard](../docs/mentor/pr-workflow.md#language-standard)
```

### Issue: PR Not Assigned

**Violation**: PR created without assigning to mentor

**Response:**
```markdown
❌ PR not assigned to reviewer

Fix: `gh pr edit [PR-number] --add-assignee aslavchev`

For future PRs, use `--assignee aslavchev` when creating:
See [PR Creation](../docs/mentor/pr-workflow.md#6-create-pull-request-with-assignment)
```

---

## When to Use Issues vs PR Comments

### Use GitHub Issues For:

✅ **Comprehensive content feedback**
- Initial week submission review
- Quality assessment with grades
- Multiple exercises to review
- Feedback that needs tracking across sessions

✅ **Tracking work to be done**
- "Corrections needed" status
- Can be referenced from multiple PRs
- Remains open until fully resolved

**Pattern:**
```bash
# Create issue for content feedback
gh issue create \
  --title "Week XX Feedback: Corrections Required" \
  --body-file feedback/week-XX-content-review.md \
  --label "week-XX,feedback,corrections-needed" \
  --assignee [mentee-username]
```

### Use PR Comments For:

✅ **Process/workflow violations**
- Wrong branch name
- Mixed work in PR
- File naming issues
- Missing assignment

✅ **Short, actionable feedback**
- Quick fixes needed before merge
- Pointing to workflow guides
- Approval/merge decisions

✅ **Specific code/content line feedback**
- Use inline PR review for specific lines

**Pattern:**
```bash
# Short feedback on PR
gh pr comment [PR-number] --body "Issues: [list]. Fix: [steps]. See: [guide link]"
```

### Combined Approach (Today's Example)

**Initial Week Submission with Issues:**

1. **Create comprehensive content review** → GitHub Issue
   - Detailed assessment of all exercises
   - Quality grades
   - Conceptual feedback

2. **Identify process violations** → PR Comment
   - Short list of workflow issues
   - Exact commands to fix
   - Links to guides

**Why this works:**
- Content feedback tracked long-term (Issue)
- Process fixes happen immediately (PR)
- Mentee has clear separation of concerns

---

## Quality Assessment Approach

### Content Grading Scale

Use 100-point scale for objectivity:

- **90-100: Excellent** - Exceeds expectations, minor improvements only
- **80-89: Good** - Meets expectations, some refinement needed
- **70-79: Satisfactory** - Basic requirements met, notable gaps
- **60-69: Needs Improvement** - Significant issues, major revision required
- **Below 60: Incomplete** - Does not meet minimum requirements

### Per-Exercise Assessment

**Structure:**
```markdown
## Exercise X: [Title]
Grade: XX/100

### What Went Well
- [Specific strength 1]
- [Specific strength 2]

### Areas for Improvement
- [Specific issue 1]
- [Specific issue 2]

### Actionable Feedback
- [Concrete suggestion 1]
- [Concrete suggestion 2]
```

### Positive Reinforcement

**Always include:**
- What the mentee did well (even if small)
- Specific examples of good work
- Encouragement for effort

**Example from Week 1 Review:**
> "Excellent work discovering 3 real bugs in SauceDemo! This demonstrates strong exploratory testing skills. Your bug descriptions are clear and reproducible - exactly what a developer needs."

---

## Documentation Pattern

### When to Create New Guides

Create a permanent guide in `docs/mentor/` when:

1. **You're explaining the same thing twice**
   - First time: inline explanation
   - Second time: create guide

2. **The concept is process/workflow related**
   - How to submit PRs
   - How to fix common issues
   - Git workflow patterns

3. **It prevents future confusion**
   - Today's example: Long feedback confused mentee
   - Solution: Create comprehensive guide, reference it

### Guide Structure

```markdown
# [Guide Title]

## Overview
[Brief description]

## [Scenario A]: [Use Case]
[Step-by-step instructions with commands]

## [Scenario B]: [Use Case]
[Step-by-step instructions with commands]

## Common Commands Quick Reference
[Cheat sheet section]

## Troubleshooting
[Common problems and solutions]

## Examples
[Real-world examples]
```

### Updating README

Add brief section + link to detailed guide:

```markdown
### 📤 [Topic]

Brief explanation (2-3 lines)

**Complete Guide**: [link to detailed guide]

**Quick Start:**
```bash
# Essential commands only
```

**Key Rules:**
- Rule 1
- Rule 2
```

---

## Case Study: Week 1-2 Review (November 2024)

### Situation

**Week 1 Initial Submission:**
- Wrong directory (root instead of mentee-work/)
- Bulgarian language instead of English
- File naming violations (underscores)
- Committed directly to main

**Week 2 Submission (PR #2):**
- Mixed Week 1 corrections with Week 2 new work
- Week 1 issues still not fixed
- PR not assigned to mentor

### Approach Taken

**First Review (Issue #1 - Too Long):**
- Created 308-line comprehensive feedback
- Detailed explanation of every issue
- Result: **Mentee got confused, didn't follow workflow**

**Lesson Learned:**
> "issue we created last week was too long and maybe Kamen got confused. So I need tight straight to the point draft with clear instructions."

**Second Review (PR #2 - Improved):**

1. **Created comprehensive PR workflow guide** (`docs/mentor/pr-workflow.md`)
   - 500+ lines of detailed instructions
   - Scenarios, examples, troubleshooting
   - Reusable for all future weeks

2. **Updated README** with brief section + link to guide

3. **Provided SHORT PR feedback** (~40 lines)
   - Listed 3 main issues
   - Exact commands to fix
   - Links to relevant guide sections

4. **Committed docs directly to main**
   - Infrastructure changes, not deliverables
   - Unblocks mentee immediately
   - No bureaucratic PR for process docs

**Result:**
- Mentee has clear, actionable steps
- Permanent documentation for future reference
- Mentor can reference guide in all future feedback
- Professional, systematic approach

### Key Takeaways

1. **Short feedback + detailed guide** > Long feedback
2. **Create infrastructure first**, then reference it
3. **Separate content quality from process issues**
4. **One PR = one concern** - enforce strictly
5. **Always start from clean main** - emphasize constantly

---

## Feedback Quality Checklist

Before posting any feedback, verify:

### Content
- [ ] Short and focused (under 50 lines for PR comments)
- [ ] Lists specific issues clearly
- [ ] Provides exact commands to fix
- [ ] Links to relevant guides/sections
- [ ] Includes positive reinforcement (if applicable)
- [ ] Uses clear formatting (bullets, code blocks)

### Actionability
- [ ] Mentee knows EXACTLY what to do next
- [ ] Steps are in correct order
- [ ] Commands are copy-paste ready
- [ ] No ambiguity about expectations

### Tone
- [ ] Professional and supportive
- [ ] Focuses on learning, not criticism
- [ ] Acknowledges effort and improvements
- [ ] Encourages questions

### Technical Accuracy
- [ ] Commands tested and verified
- [ ] Links work correctly
- [ ] Branch names match conventions
- [ ] File paths are accurate

---

## Mentor Workflow Quick Reference

### Initial Week Submission

```bash
# 1. Review PR
gh pr view [PR-number]

# 2. Assess content quality
# Create: feedback/week-XX-content-review.md

# 3. Create issue with content feedback
gh issue create \
  --title "Week XX Feedback" \
  --body-file feedback/week-XX-content-review.md \
  --label "week-XX,feedback" \
  --assignee [mentee-username]

# 4. Check for process issues
# If none: approve and merge
gh pr review [PR-number] --approve
gh pr merge [PR-number] --squash

# If issues: provide short feedback
gh pr comment [PR-number] --body-file feedback/pr-X-review.md
```

### Corrections PR

```bash
# 1. Review PR
gh pr view [PR-number]

# 2. Check issue was addressed
gh issue view [issue-number]

# 3. Verify all points fixed
gh pr diff [PR-number]

# 4. If good: approve, merge, close issue
gh pr review [PR-number] --approve --body "All corrections addressed!"
gh pr merge [PR-number] --squash
gh issue close [issue-number] --comment "Corrections merged. Well done!"

# If still issues: add comment with remaining items
gh pr comment [PR-number] --body "Still need to fix: [list]"
```

### Workflow Violation

```bash
# 1. Comment on PR with short feedback
gh pr comment [PR-number] --body-file feedback/pr-X-review.md

# 2. Request changes (blocks merge)
gh pr review [PR-number] --request-changes --body "See comment above"

# 3. Mentee fixes and updates
# 4. Re-review
gh pr review [PR-number] --approve
gh pr merge [PR-number] --squash
```

---

## Tips for Effective Mentoring

### 1. Consistency is Key
- Use same patterns for similar issues
- Reference guides consistently
- Apply rules uniformly

### 2. Teach Process, Not Just Content
- Git workflow is as important as QA knowledge
- Professional practices matter
- Portfolio quality matters

### 3. Encourage Questions
- "Let me know if you have questions" in every feedback
- Answer promptly (within 24 hours)
- Meet in person for complex issues

### 4. Balance Rigor with Support
- Enforce standards strictly
- But provide clear path to fix issues
- Celebrate improvements

### 5. Document Everything
- Your feedback becomes their portfolio
- GitHub is their professional showcase
- Quality matters

### 6. Iterate on Your Approach
- Notice what works (short + guides)
- Notice what doesn't (long essays)
- Adjust and improve

---

## Conclusion

Effective mentoring requires:
1. **Clear, short feedback** pointing to comprehensive guides
2. **Separation** of content quality vs process issues
3. **Consistency** in applying standards
4. **Documentation** of repeatable patterns
5. **Balance** between rigor and support

By following this systematic approach, you create a professional learning environment that prepares mentees for real-world software development workflows.

---

**Last Updated:** November 2024
**Based on:** Real mentoring sessions with junior QA engineers
**Status:** Living document - update as you learn
