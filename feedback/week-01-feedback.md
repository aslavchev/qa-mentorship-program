# Week 1 Feedback: Kamen Asenov

**Date:** November 2, 2024
**Reviewer:** Alex (Mentor)
**Status:** 🟡 Corrections Requested

---

## 🎉 Great Job on Completing Week 1!

Hi Kamen! 👋

First, **congratulations on completing all Week 1 exercises!** I can see you put in solid effort and completed all 5 deliverables. That's excellent progress for your first week! 🚀

I've reviewed your submission and have some important feedback to help you align with professional standards and program expectations.

---

## ✅ What You Did Well

- **Completeness:** All 5 exercises completed ✅
- **Content Quality:** Good understanding of concepts demonstrated
- **Timeliness:** Work submitted on schedule
- **Git Usage:** Properly committed your work

Great foundation to build on!

---

## 🎯 Required Corrections

I need you to make the following corrections before we can approve Week 1. These are important for maintaining professional standards and aligning with the program structure.

### 1. 📁 **Directory Structure**

**Issue:** Your work is in `week-01/` but should be in `mentee-work/week-01/`

**Why it matters:**
- `week-01-qa-foundations/` contains the **program curriculum** (tutorials, exercises)
- `mentee-work/week-01/` is where **your deliverables** should live
- This separation keeps the program clean and makes your portfolio easy to navigate

**Files to move:**
```
week-01/qa_qc_testing_comparison.md  → mentee-work/week-01/qa-qc-testing-comparison.md
week-01/sdlc_comparison.md           → mentee-work/week-01/sdlc-comparison.md
week-01/saucedemo_analysis.md        → mentee-work/week-01/saucedemo-analysis.md
week-01/sdlc_activities.md           → mentee-work/week-01/sdlc-activities.md
week-01/quality_attributes.md        → mentee-work/week-01/quality-attributes.md
```

---

### 2. 🌐 **Language: English Required**

**Issue:** The file `qa_qc_testing_comparison.md` contains Bulgarian text in the comparison table

**Affected content:**
- Definition row
- Focus row
- Approach row
- Timing row
- Responsibility row
- Example Activity row

**Example of what needs translation:**
```markdown
Current (Bulgarian):
| Definition | Процес, насочен към **предотвратяване** на дефекти... |

Required (English):
| Definition | Process focused on **preventing** defects... |
```

**Why it matters:**
- I need to review your work thoroughly in English
- This becomes part of your professional portfolio
- English is the standard for tech documentation

**Action required:** Translate all Bulgarian content in the comparison table to English

---

### 3. 📝 **File Naming Convention**

**Issue:** Using underscores (`_`) instead of hyphens (`-`)

**Current naming:**
```
qa_qc_testing_comparison.md  ❌
sdlc_comparison.md            ❌
saucedemo_analysis.md         ❌
sdlc_activities.md            ❌
quality_attributes.md         ❌
```

**Correct naming:**
```
qa-qc-testing-comparison.md  ✅
sdlc-comparison.md            ✅
saucedemo-analysis.md         ✅
sdlc-activities.md            ✅
quality-attributes.md         ✅
```

**Why it matters:**
- Industry standard (URLs, file systems prefer hyphens)
- Consistency across the program
- Professional portfolio standards

---

### 4. 🔄 **Git Workflow for Future Weeks**

**Issue:** You committed directly to `main` branch

**Why it matters:**
- No opportunity for me to review before finalizing
- No audit trail of review process
- Not following professional Git workflows

**NEW WORKFLOW for Week 2 and beyond:**

I've now set up **branch protection** on the `main` branch. Starting with Week 2, you MUST follow this workflow:

#### **Step-by-Step Workflow:**

**1. Create Feature Branch**
```bash
git checkout main
git pull origin main
git checkout -b week-02-work
```

**2. Do Your Work**
- Complete exercises in `mentee-work/week-02/`
- Commit as you go

**3. Commit Your Work**
```bash
git add mentee-work/week-02/
git commit -m "Week 2 exercises complete"
```

**4. Push Branch**
```bash
git push -u origin week-02-work
```

**5. Create Pull Request on GitHub**
- Go to https://github.com/aslavchev/qa-fundamentals-11weeks
- Click "Pull Requests" tab
- Click "New Pull Request"
- Select your branch: `week-02-work`
- Add description of what you completed
- Click "Create Pull Request"

**6. Wait for My Review**
- I'll review your PR
- I may request changes
- Once approved, I'll merge to main

**Important:** You will NOT be able to push directly to `main` anymore. This is intentional and follows industry best practices.

---

## 🛠️ How to Fix Week 1

Please create a **corrections branch** and fix the issues above:

### **Commands to Execute:**

```bash
# 1. Make sure you're on main and up to date
git checkout main
git pull origin main

# 2. Create corrections branch
git checkout -b week-01-corrections

# 3. Move files to correct location with correct names
mkdir -p mentee-work/week-01

# Move and rename files (you can use git mv or just move + rename)
git mv week-01/qa_qc_testing_comparison.md mentee-work/week-01/qa-qc-testing-comparison.md
git mv week-01/sdlc_comparison.md mentee-work/week-01/sdlc-comparison.md
git mv week-01/saucedemo_analysis.md mentee-work/week-01/saucedemo-analysis.md
git mv week-01/sdlc_activities.md mentee-work/week-01/sdlc-activities.md
git mv week-01/quality_attributes.md mentee-work/week-01/quality-attributes.md

# 4. Remove old directory
rmdir week-01

# 5. Open qa-qc-testing-comparison.md and translate Bulgarian to English
# (Use your text editor to edit the file)

# 6. Commit changes
git add mentee-work/week-01/
git commit -m "Week 1 corrections: structure, language, naming

- Move files from week-01/ to mentee-work/week-01/
- Rename files using hyphens instead of underscores
- Translate Bulgarian content to English in comparison table"

# 7. Push corrections branch
git push -u origin week-01-corrections

# 8. Create Pull Request on GitHub
# Go to GitHub and create PR from week-01-corrections to main
```

---

## 📋 Correction Checklist

Before submitting your PR, verify:

- [ ] All files moved to `mentee-work/week-01/`
- [ ] All files renamed with hyphens (no underscores)
- [ ] Bulgarian text translated to English in `qa-qc-testing-comparison.md`
- [ ] Old `week-01/` directory deleted
- [ ] Changes committed to `week-01-corrections` branch
- [ ] Branch pushed to GitHub
- [ ] Pull Request created with clear description

---

## 💡 Why These Standards Matter

### Professional Development
- **Directory structure:** Separates curriculum from your work (portfolio organization)
- **English language:** Universal tech communication standard
- **Naming conventions:** Industry best practices, URL-friendly, consistent
- **PR workflow:** How real dev teams work, creates review trail

### Your Portfolio
This GitHub repository becomes your **professional portfolio**. When you apply for QA jobs, you'll share this repo. Clean structure and professional standards make a strong impression.

### Learning Opportunity
Making these corrections teaches you:
- Professional Git workflows (branching, PRs, reviews)
- Attention to detail (critical QA skill)
- Following standards and conventions
- Responding to feedback professionally

---

## 🎯 Next Steps

### Immediate (This Week):
1. ✅ Create `week-01-corrections` branch
2. ✅ Move files to `mentee-work/week-01/`
3. ✅ Rename files (hyphens not underscores)
4. ✅ Translate Bulgarian content to English
5. ✅ Push corrections branch
6. ✅ Create Pull Request
7. ⏳ Wait for my review and approval

### For Week 2 (Starting Next Week):
1. ✅ Read `week-02-test-levels/tutorial.md`
2. ✅ Complete exercises in `mentee-work/week-02/`
3. ✅ Use proper Git workflow (feature branch → PR)
4. ✅ All content in English
5. ✅ Use hyphens in file names

---

## 📚 Reference Documents

I've created a helpful guide for you:

📖 **Read:** `mentee-work/README.md`

This file contains:
- Complete directory structure explanation
- Step-by-step Git workflow for every week
- File naming conventions
- Examples and quick reference commands

**Please read it carefully before starting Week 2!**

---

## ❓ Questions?

If you have any questions about these corrections or the workflow:

1. **Create a GitHub Issue** with tag `question`
2. **Ask during our next mentor session**
3. **Comment on your Pull Request** (once created)

I'm here to help you succeed! 🎓

---

## 🎉 Keep Up the Great Work!

Don't be discouraged by these corrections - they're a normal part of the learning process! Your content quality is good, and these are just structural/formatting adjustments.

**You're on the right track!** Making these corrections will set you up for success in the remaining 10 weeks.

Looking forward to your corrected Pull Request! 🚀

---

**Review Status:** 🟡 Corrections Requested
**Next Action:** Kamen to create `week-01-corrections` PR
**Estimated Time:** 30-45 minutes to complete corrections
