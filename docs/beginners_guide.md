# Beginner’s Guide to LLM Agents

If you’re new to large language models or software development in general, this guide will help you get started with the
curated LLM apps repository.  It emphasises concepts rather than code and points you to user‑friendly resources.

## What is an agent?

An **agent** is a software component that combines a large language model with tools (such as web access, databases or other
APIs) to accomplish a goal.  For example, an agent might read a document, summarise it and then store the summary in a file.
Agents can also collaborate in teams, where one agent plans a task and another executes it.

## Exploring without coding

You don’t need to be a programmer to experiment with this repository:

* Try the **Streamlit Summariser** and **Gradio FAQ Bot** in the `web_apps` folder.  These apps run locally and provide
  graphical interfaces for summarisation and questions about the project.
* Open the **Getting Started Notebook** in the `notebooks` folder using JupyterLab or VS Code.  It walks you through
  inspecting a dataset and teaches you how agents can work with structured data.
* Browse the **design assets** in the `design` folder to visualise how different agent components interact.

## When you’re ready to code

If you’d like to build your own agent or contribute to the project:

1. Read the **Framework Comparison** document to understand which agent framework suits your needs.
2. Use the **Generator Script** (`scripts/create_agent.py`) to scaffold a new agent directory.  You’ll get a
   `README.md` and `main.py` ready for your logic.
3. Look at the **Starter** agents under `agents/starter` for inspiration on how to implement simple tasks.
4. Follow the **Best Practices** in the documentation to learn how to promote and maintain open source projects【806548062083687†L539-L551】.

## Going deeper

Once the basics click, the handbook has a full operating manual ready for you:

- **Agent OS concepts** — [agent_os/README.md](../agent_os/README.md)
- **Templates** to copy into your project — [templates/](../templates/)
- **Blueprints** for common agent shapes — [blueprints/](../blueprints/)
- **Safety + evals** before you ship — [safety/](../safety/), [evals/](../evals/)

## Need help?

If you run into trouble or have questions, open an issue on GitHub or ask the **Gradio FAQ Bot**. We welcome feedback from everyone, regardless of technical background.