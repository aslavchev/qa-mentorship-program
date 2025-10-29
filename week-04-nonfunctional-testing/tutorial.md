# Week 4: Non-Functional Testing

## 🎯 Learning Objectives
- Understand non-functional requirements (NFRs)
- Perform basic performance testing
- Conduct security assessment
- Evaluate usability
- Test compatibility across browsers/devices
- Assess accessibility compliance

## 📚 What is Non-Functional Testing?

Non-functional testing validates **how** the system performs, not **what** it does.

### Functional vs Non-Functional

| Functional | Non-Functional |
|------------|----------------|
| Does it work? | How well does it work? |
| Feature completeness | Performance, security, usability |
| Business logic | Quality attributes |

## 1️⃣ Performance Testing

### Types
- **Load Testing:** System behavior under expected load
- **Stress Testing:** System behavior under extreme load
- **Endurance Testing:** System behavior over extended time
- **Spike Testing:** Sudden load increases

### Manual Performance Assessment
1. **Page Load Time:** Use browser DevTools (Network tab)
2. **Response Time:** Measure time from action to response
3. **Resource Usage:** Check memory/CPU in DevTools

### SauceDemo Performance Tests
- Login page load time < 2 seconds
- Product catalog loads < 3 seconds
- Add to cart response < 1 second
- Images load progressively

## 2️⃣ Security Testing

### Basic Security Checks
- **Authentication:** Password masking, session management
- **Authorization:** Access control, privilege escalation
- **Data Protection:** Sensitive data handling
- **Input Validation:** SQL injection, XSS prevention

### SauceDemo Security Checklist
- [ ] Password not visible in plain text
- [ ] Session expires after logout
- [ ] Cannot access pages without login
- [ ] No sensitive data in URLs
- [ ] Form inputs validate/sanitize

## 3️⃣ Usability Testing

### Jakob Nielsen's 5 Usability Components
1. **Learnability:** Easy to learn?
2. **Efficiency:** Fast to use once learned?
3. **Memorability:** Easy to remember?
4. **Errors:** Few errors, easy to recover?
5. **Satisfaction:** Pleasant to use?

### SauceDemo Usability Evaluation
- Can new user complete purchase without help?
- Are error messages helpful?
- Is navigation intuitive?
- Are CTAs (Call-To-Action) clear?

## 4️⃣ Compatibility Testing

### Test Matrix
- **Browsers:** Chrome, Firefox, Safari, Edge
- **OS:** Windows, macOS, Linux
- **Devices:** Desktop, tablet, mobile
- **Screen Resolutions:** 1920x1080, 1366x768, mobile viewports

### SauceDemo Compatibility
Test on:
- Chrome (latest)
- Firefox (latest)
- Safari (if available)
- Different screen sizes

## 5️⃣ Accessibility Testing

### WCAG 2.1 Principles (POUR)
- **Perceivable:** Can users perceive content?
- **Operable:** Can users operate interface?
- **Understandable:** Is content understandable?
- **Robust:** Works with assistive technologies?

### Basic Accessibility Checks
- [ ] Keyboard navigation works (Tab, Enter, Esc)
- [ ] Alt text for images
- [ ] Sufficient color contrast
- [ ] Screen reader compatible
- [ ] Form labels present

### Tools
- Browser DevTools Accessibility tab
- WAVE extension
- axe DevTools
- Lighthouse audit

## 💡 Key Takeaways
1. NFRs are as important as functional requirements
2. Performance affects user experience
3. Security testing protects users and business
4. Usability determines product success
5. Compatibility ensures reach
6. Accessibility is ethical and often legally required

## 📝 Self-Assessment
1. What's the difference between functional and non-functional testing?
2. Name 3 types of performance testing
3. What security checks can you do manually?
4. What are Nielsen's 5 usability components?
5. Why is accessibility testing important?
