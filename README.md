# 🌐 Selenium POM Automation Framework

## 📌 Project Overview
This repository contains a professional **Page Object Model (POM)** automation suite. It is designed to demonstrate clean code practices, maintainability, and full integration with a **CI/CD pipeline**.

The framework automates the login functionality of a web application, ensuring that the authentication flow works correctly across different environments.

---

## 🚀 Key Features
*   **Page Object Model (POM):** Enhances code reusability by separating page-specific locators from test logic.
*   **CI/CD Integration:** Fully automated test execution using **GitHub Actions** on every code push.
*   **Headless Execution:** Optimized to run on cloud servers (Ubuntu) without a graphical interface.
*   **Explicit Waits:** Implemented `WebDriverWait` to handle dynamic elements and prevent "flaky" tests.

---

## 🛠️ Tech Stack
*   **Language:** Python 3.10
*   **Automation:** Selenium WebDriver
*   **Test Runner:** Pytest
*   **CI/CD:** GitHub Actions
*   **Environment:** Linux (GitHub Runner) & Windows (Local)

---

## 🏗️ Project Structure
```text
├── .github/workflows/  # CI/CD configuration (test.yml)
├── pages/              # Page Object classes
│   ├── base.py         # Reusable Selenium wrappers
│   └── Login_Page.py   # Locators & actions for Login
├── mytest/             # Test scripts
│   ├── conftest.py     # Driver setup & fixtures
│   └── login_test.py   # Functional test cases
└── README.md           # Project documentation
