# Ru-hard-detection-dataset [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CoffeBank/Ru-hard-detection-dataset)

A dataset for evaluating the detection of generated texts in Russian language, including texts of different genres and style variations.

## Dataset Structure

The root directory contains two main directories:
- **main** – the core part of the dataset, containing three themes:
  - **news** – news articles
  - **essay** – essays
  - **scientific_texts** – scientific articles

- **long sc** – additional scientific research texts

Each of these folders contains three files:
1. **Original** 
2. **Generated text** – generated based on the summarization of the original. In other words, key information was extracted from the original text and used as a basis for generating new, similar text.
3. **Paraphrased text** – rewritten original using two variants: weak and strong paraphrasing.

## Models and Sources

The file records indicate the models and sources used:
- Generation models (e.g., `gemini-2.0-flash`)
- Paraphrasing models (e.g., `chatgpt-4o-mini`, `deepseek-chat`, `deepseek-reasoner`)
- Data sources (e.g., Lenta.ru news, Rus scientific articles)
