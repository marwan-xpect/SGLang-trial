# SGLang Paper Summarizer

This project is a simple **research paper summarization tool** powered by [SGLang](https://github.com/sgl-project/sglang) and the OpenAI API.
It takes a research paper (in plain text format), analyzes it, and produces a structured summary with key sections such as research question, methodology, findings, and impact.

---

## Features

- Uses **OpenAI GPT backend** through SGLang.
- Generates a **structured academic summary** with:
  1. Main Research Question
  2. Methodology Used
  3. Key Findings
  4. Significance / Impact
  5. Limitations
- Saves the generated summary into `paper_summary.txt`.

---

## Requirements

- Python
- [SGLang](https://github.com/sgl-project/sglang)
- An [OpenAI API key](https://platform.openai.com/account/api-keys)

Install dependencies:

```bash
pip install sglang openai
```

Adding the API key as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Citation

Sample paper used:
[https://www.science.org/doi/full/10.1126/science.adv9817](https://www.science.org/doi/full/10.1126/science.adv9817)