# Project-Based-Python

A hands-on, project-based path to Python and Machine Learning mastery — **52 projects**, five levels, no tutorials, no copy-pasted solutions.

This repo tracks my progress working through a project-based roadmap that starts with raw Python fundamentals and ends with a full end-to-end ML product (data → model → API → deployment). The rule throughout: build it before you `import` it. Every "from scratch" project exists so libraries like NumPy, pandas, scikit-learn, and PyTorch stop feeling like magic.

## Philosophy

- **No solutions handed over.** Each project describes *what* to build and *why*, never *how*.
- **Struggle is the point.** If a project feels too easy, add a stretch goal. If it feels impossible, an earlier concept probably wasn't fully internalized — rebuild it from memory first.
- **From-scratch before library.** Linear regression by hand before scikit-learn. A matrix class before NumPy. Backprop by hand before PyTorch autograd.
- **Correct → Readable → Maintainable → Efficient**, in that order.

## Stack

Python 3.12+, then progressively: NumPy, pandas, matplotlib/seaborn, scikit-learn, PyTorch, Hugging Face `transformers`, FastAPI.

## Roadmap Structure

| Level | Projects | Focus |
|---|---|---|
| **1 — Python Fundamentals, Data-Flavored** | 1–10 | Variables, functions, loops, file I/O, JSON/CSV, from-scratch stats & regression |
| **2 — Core Python & OOP for ML Code** | 11–20 | Classes, inheritance, dunder methods, dataclasses, generators, decorators, context managers |
| **3 — NumPy, Pandas & Data Analysis** | 21–30 | Vectorization, DataFrames, cleaning, EDA, feature engineering, statistical testing |
| **4 — Classical ML with scikit-learn** | 31–40 | Train/test split, regression & classification models, evaluation metrics, CV/tuning, pipelines, ensembles, clustering, imbalanced data |
| **5 — Deep Learning, NLP & Real-World ML** | 41–52 | Neural nets from scratch, PyTorch, CNNs, NLP/TF-IDF, transfer learning, model serving, experiment tracking, performance profiling |

Each level ends in a **capstone project** combining everything learned so far. The roadmap closes with 5 **no-tutorial skill-assessment projects** to confirm the skills actually transfer to unfamiliar problems.

## Progress Tracker

- [ ] Level 1 — Python Fundamentals (1–10)
- [ ] Level 2 — OOP for ML (11–20)
- [ ] Level 3 — NumPy, Pandas & EDA (21–30)
- [ ] Level 4 — Classical ML (31–40)
- [ ] Level 5 — Deep Learning, NLP & Deployment (41–52)
- [ ] Skill Assessment Projects (post-roadmap, no guidance)

## Repo Layout

```
Project-Based-Python/
├── level-1-python-fundamentals/
│   ├── 01-statistics-calculator/
│   ├── 02-linear-regression-scratch/
│   └── ...
├── level-2-oop-for-ml/
├── level-3-numpy-pandas/
├── level-4-classical-ml/
├── level-5-deep-learning-nlp/
├── skill-assessments/
└── README.md
```

Each project folder includes its own short README with the goal, key concepts practiced, and notes on design decisions made along the way.

## Timeline

Following a 14-day realistic plan (2–4 focused hrs/day), with Level 4 and Level 5 given extra room since they're the densest sections. An aggressive 7-day plan exists for reference but isn't the primary target — rushing evaluation, cross-validation, or backprop-by-hand undermines everything built afterward.

## Mastery Criteria

A project isn't "done" when it runs. For each major project I should be able to:

- Explain the architecture and key design decisions
- Handle common edge cases
- Debug basic failures without re-reading the original solution
- Modify the project to meet a new requirement
- Refactor part of it for readability or performance

---

*Status: in progress. Last updated with initial commit.*
