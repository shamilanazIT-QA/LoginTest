Project Overview
This repository contains a Page Object Model (POM) based automation suite for testing web applications. The framework is designed for scalability and maintainability, separating the page logic from the test scripts.

The current suite focuses on the Login Functionality of the Herokuapp test site, handling edge cases like invalid characters and successful authentication.

🛠️ Tech Stack
Language: Python 3.10+

Core Library: Selenium WebDriver

Test Runner: Pytest

Pattern: Page Object Model (POM)

CI/CD: GitHub Actions (Ubuntu-latest)

🏗️ Framework Structure
The project is organized to follow industry standards for clean code:

Plaintext
├── .github/workflows/  # CI/CD pipeline (YAML)
├── pages/              # Page Objects
│   ├── base.py         # Base Page with reusable Selenium methods
│   └── Login_Page.py   # Locators and actions for the Login page
├── mytest/             # Test Suite
│   ├── conftest.py     # Fixtures (Driver setup/teardown)
│   └── login_test.py   # Actual test cases
└── report.xml          # Automated test execution reports
🚀 Key Features
Automated CI/CD: Tests run automatically on every push or pull_request to the master branch using GitHub Actions.

Headless Execution: Configured to run in headless mode for efficient server-side testing.

Explicit Waits: Utilizes WebDriverWait for stable element interaction and synchronization.

Scalable POM: Easy to add new pages by extending the BasePage class.
Challenges & Solutions
Issue: Environment mismatch between local Windows and GitHub Linux servers.

Solution: Implemented flexible Chrome Options and PYTHONPATH environment variables to ensure seamless execution in both environments.

Issue: Unstable XPaths due to dynamic web elements.

Solution: Refactored locators to use contains() functions for more robust element finding.
