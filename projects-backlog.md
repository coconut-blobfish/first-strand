# 🧬 3-Month Computational Biology & AI Roadmap (Ages 13+)

## 📅 Month 1: Sequence Analysis & Mutation Tracking (Level: Easy)
* **Core Biological Concept:** Genetic mutation. When organisms or viruses evolve, their DNA letters change. We track these changes to understand how diseases spread.
* **Core Computational Concept:** File I/O (Input/Output), string manipulation, and dictionary mapping.
* **The Python Tools:** BioPython, standard libraries (json, collections).
* **Project Name:** The Viral Variant Tracker
* **Project Description:** 
  Write a script that loads two different strains of a virus from a text file. Have your code compare them side-by-side to flag the exact positions where letters changed (e.g., "Position 412 changed from A to G"). Count the total mutation rate.
* **Where to Find Public Data:** 
  Download the FASTA files (the standard text format for DNA strings) for different variants of Influenza (the flu) or Ebola from the National Center for Biotechnology Information (NCBI Virus database).

---

## 📅 Month 2: Gene Expression & Visual Analytics (Level: Moderate)
* **Core Biological Concept:** Gene regulation. Every cell has the same DNA, but a brain cell acts differently than a liver cell because different genes are turned "on" or "off" (expressed). 
* **Core Computational Concept:** Data frames, matrix math, data cleaning, and statistical plotting.
* **The Python Tools:** pandas, NumPy, seaborn, matplotlib.
* **Project Name:** Cancer Gene Expression Visualizer
* **Project Description:** 
  Load a large matrix spreadsheet containing gene expression data from healthy tissue versus tumor tissue. Write code to filter out low-value background noise, calculate the mean expression values, and generate a heatmap visualization that clearly highlights which genes are hyper-active in cancer cells.
* **Where to Find Public Data:** 
  Look for "Gene Expression Classification" datasets on Kaggle, or download curated, beginner-friendly public tables originating from The Cancer Genome Atlas (TCGA).

---

## 📅 Month 3: Machine Learning & AI Diagnostics (Level: Intermediate)
* **Core Biological Concept:** Biomarkers and phenotypes. Finding hidden patterns across thousands of DNA sequences that dictate whether an organism will develop a specific trait or condition.
* **Core Computational Concept:** Feature engineering, tokenization (k-mer counting), model training, and supervised classification.
* **The Python Tools:** scikit-learn, BioPython.
* **Project Name:** Genetic Disease Predictor AI
* **Project Description:** 
  Convert raw DNA text strings into numbers using "k-mer counting" (slicing DNA into small, overlapping sub-strings of length *k*). Split your data into training and testing sets. Train a machine learning classifier (like a Random Forest or Support Vector Machine) to predict whether a DNA sequence belongs to a healthy patient or a sick patient.
* **Where to Find Public Data:** 
  Use open-source genetic datasets from the UCI Machine Learning Repository (search for "Molecular Biology" or "Promoter Gene sequences").

---

## 💡 Best Practices for This Roadmap
1. **The Copilot Comment Method:** Write out your logic in English comments first (e.g., `# Step 1: Filter rows where gene expression is > 5.0`). Then let Copilot suggest the syntax. Never accept code you cannot explain out loud.
2. **Build Your Portfolio:** Save your code for every single project on GitHub. Documenting your 3-month progress online will be an incredible advantage for future science fairs, internships, or academic opportunities.
