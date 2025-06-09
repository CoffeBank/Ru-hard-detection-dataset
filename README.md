# Ru-hard-detection-dataset [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/CoffeBank/Ru-hard-detection-dataset)

A dataset for evaluating the detection of generated texts in Russian language. It collects original human texts, AI generated versions and paraphrased variants across several genres.

## Dataset Structure

The root directory contains two main directories:
- **main** – the core part of the dataset, containing three themes:
  - **news** – news articles
  - **essay** – essays
  - **scientific_texts** – scientific articles

- **long_sc** – additional scientific research texts

Each JSON file is a list of records with the following fields:

- `id` – unique integer identifier
- `text` – text of the example
- `dataset` – origin of the text (e.g., `Lenta.ru news`)
- `source` – `human` for original texts, `ai` for generated ones and `ai+rew` for paraphrased variants
- `model` – generating model name (only for generated and paraphrased files)
- `paraphrasing_type` – paraphrase strength: `LP` (light) or `DP` (deep) where present

Each of these folders contains three files:
1. **Original** 
2. **Generated text** – generated based on the summarization of the original. In other words, key information was extracted from the original text and used as a basis for generating new, similar text.
3. **Paraphrased text** – rewritten original using two variants: weak and strong paraphrasing.

| Location | File | Records |
|----------|------|--------:|
| `main/news` | `original_news.json` | 480 |
| | `generated_news.json` | 480 |
| | `paraphrased_news.json` | 480 |
| `main/essay` | `original_essay.json` | 480 |
| | `generated_essays.json` | 480 |
| | `paraphrased_essays.json` | 480 |
| `main/scientific_texts` | `orig_scientific.json` | 479 |
| | `generated_scientific.json` | 479 |
| | `paraphrased_scientific.json` | 479 |
| `long_sc` | `rus_scientific_articles_part1.json` | 1239 |
| | `rus_scientific_articles_part2.json` | 1239 |
| | `generated_articles.json` | 1449 |
| | `paraphrased_generated_articles.json` | 1625 |

## Models and Sources

The JSON entries keep track of the origin of each text and the model that produced it.
Generation was performed from short summaries of the originals using the following models:
`gemini-2.0-flash`, `chatgpt-4o-mini`, `chatgpt-o1-mini`, `deepseek-chat` and `deepseek-reasoner`.
Paraphrases were created with the same models in two modes – `LP` (light) and `DP` (deep).
Original texts were collected from **Lenta.ru** news articles, the **Corus Essays** corpus, a Russian summarization dataset and a collection of Russian scientific articles.
