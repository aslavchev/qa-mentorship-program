# Contributing to QA Fundamentals Program

## 📋 How to Submit Your Work

### Weekly Workflow

1. **Create a Branch**
   ```bash
   git checkout -b week-XX-your-name
   ```

2. **Complete Your Exercises**
   - Work in `mentee-work/week-XX/` directory
   - Follow the templates provided in `curriculum/templates/`
   - Complete all exercises in `curriculum/week-XX-topic/exercises.md`

3. **Commit Your Changes**
   ```bash
   git add mentee-work/week-XX/
   git commit -m "Week XX: [Topic] - [Your Name]"
   ```

4. **Push to Repository**
   ```bash
   git push origin week-XX-your-name
   ```

5. **Create Pull Request**
   - Go to GitHub repository
   - Click "New Pull Request"
   - Select your branch
   - Fill out the PR template
   - Submit for review

## ✅ Quality Standards

### Test Cases
- Use proper format from `curriculum/templates/test-case-template.md`
- Include: Test ID, preconditions, steps, expected results
- Number steps sequentially
- Be specific and detailed

### Bug Reports
- Use format from `curriculum/templates/bug-report-template.md`
- Include: severity, priority, steps to reproduce
- Add screenshots when applicable
- Clear, concise description

### Documentation
- Professional formatting
- Proper grammar and spelling
- Use markdown formatting
- Clear section headers

## 🔍 What Mentors Look For

### Content Quality (40%)
- Completeness of deliverables
- Accuracy of technical information
- Following proper templates

### Critical Thinking (30%)
- Edge case identification
- Thoughtful analysis
- Good questions asked

### Professionalism (20%)
- Clean formatting
- Proper documentation structure
- Attention to detail

### Git Workflow (10%)
- Proper branch naming
- Clear commit messages
- Clean PR descriptions

## 🚫 Common Mistakes to Avoid

- ❌ Submitting incomplete work
- ❌ Not following templates
- ❌ Vague test steps ("Click button")
- ❌ Missing edge cases
- ❌ Poor formatting
- ❌ Committing to main branch directly
- ❌ Unclear commit messages

## 💡 Tips for Success

- ✅ Read the entire tutorial before starting exercises
- ✅ Use the checklist to track progress
- ✅ Ask questions during mentor sessions
- ✅ Review previous week feedback
- ✅ Test your test cases against SauceDemo
- ✅ Commit frequently with clear messages
- ✅ Review your work before submitting PR

## 📁 File Organization

```
mentee-work/
└── week-XX/
    ├── test-cases.md
    ├── bug-reports.md
    ├── test-plan.md
    └── exercises/
        ├── exercise-1.md
        ├── exercise-2.md
        └── ...
```

## 🔄 Review Process

1. **Submit PR** - You create pull request
2. **Mentor Review** - Mentor reviews within 48 hours
3. **Feedback** - You receive comments/change requests
4. **Revisions** - You address feedback
5. **Approval** - Mentor approves and merges
6. **Session** - Weekly 1-hour mentor session

## 🎯 Grading Criteria

- **90-100**: Exceptional work, exceeds expectations
- **80-89**: Strong work, meets all criteria
- **70-79**: Good work, minor improvements needed
- **60-69**: Acceptable work, significant improvements needed
- **Below 60**: Does not meet standards, revision required

## 📞 Getting Help

- **During Session**: Ask mentor directly
- **Between Sessions**: Leave PR comments
- **Urgent Issues**: Contact mentor via agreed channel
- **General Questions**: Review curriculum materials first

## 🤝 Code of Conduct

- Be professional and respectful
- Ask questions when unclear
- Accept feedback graciously
- Help fellow mentees when appropriate
- Give credit where due
- Focus on learning and growth

---

**Remember**: Quality over speed. Take time to do it right!
