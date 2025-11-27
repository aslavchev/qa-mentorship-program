# Setup Guide for Mentees

## 🚀 Getting Started

Welcome to the 11-Week QA Fundamentals Program! Follow these steps to get set up.

## 📋 Prerequisites

- **GitHub Account** - Create at [github.com](https://github.com)
- **Git Installed** - Download from [git-scm.com](https://git-scm.com)
- **Text Editor** - VS Code recommended ([code.visualstudio.com](https://code.visualstudio.com))
- **Web Browser** - Chrome or Firefox preferred

## 🔧 Initial Setup

### 1. Clone the Repository

```bash
git clone [repository-url]
cd qa-fundamentals-11weeks
```

### 2. Configure Git

```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### 3. Verify Access to Test Application

- **URL**: https://www.saucedemo.com
- **Test Credentials**:
  - Username: `standard_user`
  - Password: `secret_sauce`

Try logging in to verify access.

### 4. Create Your First Branch

```bash
git checkout -b week-01-your-name
```

## 📁 Repository Structure

```
qa-fundamentals-11weeks/
├── README.md                    # Program overview
├── CONTRIBUTING.md              # How to submit work
├── SETUP.md                     # This file
├── curriculum/                  # Learning materials
│   ├── templates/              # Professional templates
│   ├── week-01-qa-foundations/
│   ├── week-02-test-levels/
│   └── ...
└── mentee-work/                # Your work goes here
    ├── week-01/
    ├── week-02/
    └── ...
```

## 📚 Weekly Workflow

### Before Your Session

1. **Read the Tutorial**
   - Navigate to `curriculum/week-XX-topic/tutorial.md`
   - Take notes as you read
   - Allow 2-3 hours for reading

2. **Review the Checklist**
   - Open `curriculum/week-XX-topic/checklist.md`
   - Track your progress

3. **Check Templates**
   - Review relevant templates in `curriculum/templates/`
   - Understand the expected format

### During Your Session

1. **Discuss Tutorial Content** with mentor
2. **Ask Questions** about concepts
3. **Get Guidance** on exercises
4. **Clarify Expectations** for deliverables

### After Your Session

1. **Complete Exercises**
   - Work in `mentee-work/week-XX/` folder
   - Follow templates provided
   - Allow 5-7 hours for exercises

2. **Test Your Work**
   - Verify against SauceDemo
   - Review your own work first
   - Check for completeness

3. **Commit and Push**
   ```bash
   git add mentee-work/week-XX/
   git commit -m "Week XX: [Topic] - [Your Name]"
   git push origin week-XX-your-name
   ```

4. **Create Pull Request**
   - Go to GitHub repository
   - Click "New Pull Request"
   - Fill out PR template
   - Submit for review

## 🎯 Key Resources

### Test Application
- **SauceDemo**: https://www.saucedemo.com
- Use `standard_user` / `secret_sauce` for testing

### Templates
All templates are in `curriculum/templates/`:
- `test-case-template.md` - Test case format
- `bug-report-template.md` - Bug report format
- `test-plan-template.md` - Test plan format
- `test-strategy-template.md` - Strategy format
- Plus 3 more professional templates

### Documentation
- **CONTRIBUTING.md** - Submission guidelines
- **README.md** - Program overview
- Weekly tutorials in `curriculum/week-XX-topic/`

## 💡 Tips for Success

### Git Basics

**Clone Repository**
```bash
git clone [repository-url]
```

**Create Branch**
```bash
git checkout -b week-XX-your-name
```

**Check Status**
```bash
git status
```

**Add Changes**
```bash
git add mentee-work/week-XX/
```

**Commit Changes**
```bash
git commit -m "Week XX: Description"
```

**Push to GitHub**
```bash
git push origin week-XX-your-name
```

**Update from Main**
```bash
git checkout main
git pull origin main
git checkout week-XX-your-name
git merge main
```

### Time Management

- **Reading**: 2-3 hours
- **Exercises**: 5-7 hours
- **Review**: 30-60 minutes
- **Total**: 8-10 hours per week

Break work into manageable sessions!

### Quality Standards

- ✅ Follow templates exactly
- ✅ Be specific in test steps
- ✅ Think about edge cases
- ✅ Use professional formatting
- ✅ Proofread before submitting

## 🔍 Testing SauceDemo

### Available Users
- `standard_user` - Normal user (use this primarily)
- `locked_out_user` - Locked out
- `problem_user` - Has issues
- `performance_glitch_user` - Slow performance
- `error_user` - Gets errors
- `visual_user` - Visual differences

All use password: `secret_sauce`

### Key Features to Test
- Login/Logout
- Product browsing
- Add to cart
- Remove from cart
- Checkout flow
- Sorting options
- Filtering
- Menu navigation

## ❓ Common Questions

**Q: How often do we meet?**
A: Weekly 1-hour sessions, same day/time each week.

**Q: How long does each week take?**
A: 8-10 hours total (reading, exercises, review).

**Q: Can I work ahead?**
A: Focus on current week for best learning. Quality over speed.

**Q: What if I need more time?**
A: Communicate with mentor. Extension possible if needed.

**Q: How is work graded?**
A: On quality, completeness, critical thinking, professionalism (see CONTRIBUTING.md).

**Q: Can I ask questions between sessions?**
A: Yes! Leave comments on your PR or use agreed communication channel.

**Q: What if I find a bug in SauceDemo?**
A: Great! Document it properly - that's part of learning.

## 🆘 Troubleshooting

### Git Issues

**"Permission denied"**
- Check SSH keys are set up
- Or use HTTPS clone URL

**"Merge conflict"**
- Ask mentor for help first time
- Learn to resolve conflicts

**"Can't push"**
- Make sure you're on your branch
- Check you have write access

### SauceDemo Issues

**Can't log in**
- Verify credentials: `standard_user` / `secret_sauce`
- Try different browser
- Clear cache/cookies

**Site not loading**
- Check internet connection
- Try different browser
- Site may be temporarily down

### General

**Unclear instructions**
- Re-read tutorial section
- Check templates for examples
- Ask mentor in session

**Taking too long**
- Focus on quality, not speed
- Break work into sessions
- Ask for help if stuck

## 📞 Getting Help

1. **Review Materials** - Check tutorial and templates first
2. **Self-Research** - Try to find answer independently
3. **Ask Mentor** - During session or via PR comments
4. **Be Specific** - Describe what you tried and what happened

## 🎓 Program Completion

After 11 weeks, you'll have:
- ✅ Professional QA portfolio
- ✅ 100+ pages of documentation
- ✅ Complete test suite for SauceDemo
- ✅ 50+ test cases
- ✅ 10+ bug reports
- ✅ Test planning experience
- ✅ Mid-level QA confidence

## 🤝 Community Guidelines

- Be respectful and professional
- Ask questions when unclear
- Accept feedback graciously
- Focus on learning and growth
- Help others when appropriate
- Give credit where due

---

**Ready to Start?**

1. ✅ Complete this setup
2. ✅ Read Week 1 tutorial in `curriculum/week-01-qa-foundations/tutorial.md`
3. ✅ Attend your first mentor session
4. ✅ Begin exercises

**Good luck on your QA journey!** 🚀
