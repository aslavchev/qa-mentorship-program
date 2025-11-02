# GitHub Branch Protection Setup Guide

**Purpose:** Prevent direct commits to `main` branch and require Pull Request reviews

**Time Required:** 5 minutes

---

## 🎯 Why Branch Protection?

Branch protection ensures:
- ✅ All changes go through Pull Request review process
- ✅ Mentor can provide feedback before code is merged
- ✅ Prevents accidental direct commits to main
- ✅ Creates audit trail of all changes
- ✅ Teaches professional Git workflow

---

## 📋 Step-by-Step Setup

### Step 1: Navigate to Repository Settings

1. Go to your GitHub repository:
   ```
   https://github.com/aslavchev/qa-fundamentals-11weeks
   ```

2. Click **"Settings"** tab (top navigation)
   - If you don't see Settings tab, you may not have admin access

### Step 2: Access Branch Protection Rules

1. In left sidebar, click **"Branches"** (under "Code and automation")

2. Under "Branch protection rules", click **"Add branch protection rule"**

### Step 3: Configure Protection Rule

**Branch name pattern:**
```
main
```
(Type exactly: `main`)

**Enable the following settings:**

#### ✅ **Require a pull request before merging**
- Check this box
- This prevents direct pushes to main

**Within this option, also enable:**
- ✅ **Require approvals:** Set to `1`
  - This requires your approval before PR can be merged

- ✅ **Dismiss stale pull request approvals when new commits are pushed**
  - Re-review required if mentee pushes new commits after your approval

#### ✅ **Require status checks to pass before merging** (Optional)
- Only if you set up CI/CD later
- Leave unchecked for now

#### ✅ **Require conversation resolution before merging** (Recommended)
- Ensures all your comments are addressed
- Check this box

#### ✅ **Include administrators** (Optional but Recommended)
- Applies rules to you too (best practice)
- Check this box

### Step 4: Save Protection Rule

1. Scroll to bottom
2. Click **"Create"** button (green)

---

## ✅ Verification

After setup, verify it works:

### Test 1: Try to Push Directly to Main
```bash
# This should FAIL
echo "test" > test.txt
git add test.txt
git commit -m "Test direct push"
git push origin main

# Expected error:
# remote: error: GH006: Protected branch update failed
```

### Test 2: Verify PR Requirement
1. Create a test branch
2. Make a change
3. Push branch
4. Create Pull Request
5. Verify you can't merge without approval
6. Approve your own PR (as admin)
7. Merge should now work
8. Delete test branch

---

## 📊 Branch Protection Summary

Once configured, your repository will:

| Action | Before Protection | After Protection |
|--------|------------------|------------------|
| Push to main | ✅ Allowed | ❌ Blocked |
| Create branch | ✅ Allowed | ✅ Allowed |
| Push to branch | ✅ Allowed | ✅ Allowed |
| Create PR | ✅ Allowed | ✅ Allowed |
| Merge PR (no approval) | ✅ Allowed | ❌ Blocked |
| Merge PR (with approval) | ✅ Allowed | ✅ Allowed |

---

## 🔄 Workflow Impact

### What Changes for Mentee:

**Old Workflow (Week 1):**
```bash
git add .
git commit -m "Week 1 complete"
git push origin main  # ✅ This worked
```

**New Workflow (Week 2+):**
```bash
git checkout -b week-02-work
git add .
git commit -m "Week 2 complete"
git push origin week-02-work  # ✅ Push to branch still works
# Then create PR on GitHub
git push origin main  # ❌ This will now FAIL (by design)
```

---

## 🎓 Educational Value

This teaches your mentee:
1. **Professional Git workflow** - Industry standard practice
2. **Code review process** - How real teams collaborate
3. **Pull Request creation** - Critical skill for any developer/QA
4. **Responding to feedback** - Important soft skill

---

## 🚨 Troubleshooting

### Issue: "I don't see Settings tab"
**Solution:** You need admin/owner access to the repository

### Issue: "Branch protection not working"
**Solution:**
- Verify branch name is exactly `main` (case-sensitive)
- Check that rule was saved (green checkmark appears)
- Try logging out and back in to GitHub

### Issue: "I need to push to main urgently"
**Solution:**
- As admin, you can temporarily disable protection
- Better: Create PR and approve yourself
- Best: Follow the PR workflow

---

## 📝 Next Steps

After setting up branch protection:

1. ✅ **Test it** - Try pushing to main (should fail)
2. ✅ **Inform mentee** - Send the feedback message
3. ✅ **Wait for corrections PR** - Review when ready
4. ✅ **Continue with Week 2** - Proper workflow from now on

---

**Branch Protection Status:** ⏳ To Be Configured
**Expected Time:** 5 minutes
**Difficulty:** Easy (follow screenshots if needed)
