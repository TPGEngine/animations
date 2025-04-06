<div align="center">
<h3 align="center">Animations</h3>

  <p align="center">
    Animated explanations for Tangled Program Graphs, powered by Manim.
  </p>
</div>

## Table of Contents

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#key-features">Key Features</a></li>
      </ul>
    </li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This project aims to create animated explanations for Tangled Program Graphs (TPGs) using Manim, a powerful animation engine for explanatory math videos. It provides a framework for visualizing and understanding complex program graphs through engaging and informative animations.

### Key Features

- **Manim Integration:** Leverages the capabilities of Manim to create high-quality animations.
- **TPG Visualization:** Specifically designed to visualize Tangled Program Graphs.
- **Modular Structure:** Organized directory structure for assets, scenes, and utilities.
- **Dependency Management:** Uses `pyproject.toml` and `uv.lock` for managing project dependencies and ensuring reproducibility.

## Built With

- [Manim](https://www.manim.community/): An animation engine for explanatory math videos.
- [Pydub](https://github.com/jiaaro/pydub): Manipulate audio with an simple and easy high level interface.
- [uv](https://github.com/astral-sh/uv): An extremely fast Python package installer and resolver, written in Rust.

## Getting Started

To get started with the project, follow the instructions below.

### Prerequisites

- Python 3.12 or higher
  ```sh
  brew install python@3.12 # Example for macOS using Homebrew
  ```
- uv
  ```sh
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation

**Note:** ensure that you have `uv` installed

1. Clone the repository:
   ```sh
   git clone https://github.com/tpgengine/animations.git
   cd animations
   ```
2. Install the dependencies using uv:
   ```sh
   uv sync
   ```

## Acknowledgments

- This README was created using [gitreadme.dev](https://gitreadme.dev) — an AI tool that looks at your entire codebase to instantly generate high-quality README files.
