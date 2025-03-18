# Contributing to HerpAI

Thank you for your interest in contributing to **HerpAI** — an open-source, AI-driven discovery framework focused on accelerating a cure for HSV-1 and HSV-2.

This project is part of the **OpenBioCure** initiative and welcomes contributions from developers, researchers, scientists, data engineers, and anyone passionate about open biomedical innovation.

---

## 📌 How to Contribute

### 1. Fork the Repository
Create a personal copy of the project by forking it to your GitHub account.

### 2. Clone Your Fork
```
git clone https://github.com/<your-username>/HerpAI.git
cd HerpAI
```

### 3. Create a New Branch
```
git checkout -b feature/my-feature-name
```

### 4. Make Your Changes
Please keep your code modular, clean, and well-commented. Add tests where applicable.

### 5. Commit and Push
```
git commit -m "Add new feature/fix"
git push origin feature/my-feature-name
```

### 6. Submit a Pull Request (PR)
Create a PR against the `main` branch with a clear description of your changes.

---

## 📂 Areas You Can Help With
- Writing or improving AI agents (VirologyAgent, DrugDesignAgent, etc.)
- Prompt engineering and prompt testing
- Enhancing the orchestrator or API interface
- Integrating molecular tools (RDKit, SwissADME, AutoDock)
- Writing documentation, scientific reports, or whitepaper sections
- Suggesting or building use-case examples
- Helping test and validate discovery outputs

---

## 📋 Code Guidelines
- Use **clear naming conventions** and keep modules self-contained
- Add **docstrings and comments** to explain logic
- Structure code in alignment with the project architecture
- Keep top-level folders lowercase (except `LICENSE`, `README.md`)

---

## ✅ Commit Message Guidelines

To maintain consistency and improve collaboration across contributions, we follow a standardized commit message format inspired by Conventional Commits.

Please structure your commits as follows:

```
<type>(optional-scope): <short description>
```

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc.)
- `refactor`: Code refactoring that neither fixes a bug nor adds a feature
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `build`: Changes that affect the build system or dependencies
- `ci`: Continuous Integration/Deployment related changes

✅ Example:
```
feat(agent): add CRISPRDesignAgent prompt template
docs: update README with simulation sample
```

👉 Consider setting up a Git pre-commit hook to enforce this automatically.

---

## 📢 Communication
If you want to discuss your contribution idea or ask questions, feel free to:
- Open a GitHub Issue
- Start a Discussion (coming soon)
- Email: **openbiocure@gmail.com**

---

Let's build something powerful — together.

**– The OpenBioCure Project**
