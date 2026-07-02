# Playwright MCP Agents

Playwright MCP has by default 3 agents
- Planner
- Generator
- Healer

## Steps to install Playwright MCP Agents
- Run `npx playwright init-agents --loop=vscode`

## Using Planner Agent
- Open the AI chat and write prompt as
```
Use the `playwright-demo/.github/agents/playwright-test-planner.agent.md` generate atleast 5 positive and negative test cases for the login page - https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
Save the test plan in specs folder
```
- You will notice that AI does read the entire webpage --> And write the test plan

## Using Generator Agent
- Open the AI chat and write prompt as
```
Use `playwright-test-generator.agent.md` and generate test for the `playwright-demo/specs/login-test-plan.md`
```
- You will see that it write the playwright test automatically

## Using Healer Agent
- Make sure your test has some issues. I purposefully changed 2-3 locators 
- Open the AI chat and write prompt as
```
Fix the failing test using `playwright-demo/.github/agents/playwright-test-healer.agent.md`
```
- You will notice that it does automatically run tests --> idenitify the issue --> fix them --> and rerun it