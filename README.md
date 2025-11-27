# Prompting-Strategies-CodeGen-Study

**Chain-of-Thought vs. Few-Shot: A Comparative Study of Prompting Strategies for Code Generation**

This repository accompanies the research study and provides the code, dataset, and analysis artifacts referenced in the paper ([see Associated Publication](#associated-publication)).

---

## Contents

### 1) Token Counter Program
- Authored by us; uses the `tiktoken` library for tokenization.
- Installation instructions for `tiktoken` are available in the official repository: <https://github.com/openai/tiktoken>.

### 2) Data & Analytics Excel File
- Contains the raw data for prompts, responses, and human evaluations.
- Includes basic analytics for quick inspection.

### 3) ANOVA Analysis Excel File
- ANOVA conducted using the **Analysis ToolPak** add-in.
- Effect sizes (eta-squared, partial eta-squared, and omega-squared) were calculated manually using standard definitions ([see Effect Sizes](#effect-sizes)).
- To enable the add-in in Excel:
  1. **File → Options → Add-ins**
  2. From **Manage**, select **Excel Add-ins**, click **Go…**
  3. Check **Analysis ToolPak**, click **OK**.

### 4) Dataset
- Organized by the combination of **Reasoning-Style** (CoT vs. Non-CoT) and **Example-Context** (Zero-Shot vs. Few-Shot).
- Each combination contains **20 tasks (cases)**.
- Each task has **three files**:
  - **Prompt file**: the prompt authored by the LLM.
  - **Response file**: the LLM’s response to that prompt.
  - **Data file**: structured metadata, evaluation results, and other task-level information.

Example layout:
```
Dataset/
├─ CoT Few-Shot (CFS)/
│  ├─ CFS 1/
│  │  ├─ task_031_data.json
│  │  ├─ task_031_prompt.txt
│  │  └─ task_031_response.txt
│  ├─ CFS 2/
│  │  ├─ ...
│  │  └─ ...
│  └─ ...
├─ CoT Zero-Shot (CZS)/
│  ├─ CZS 1/
│  │  ├─ ...
│  │  └─ ...
│  └─ ...
├─ Non-CoT Few-Shot (NCFS)/
│  ├─ NCFS 1/
│  │  ├─ ...
│  │  └─ ...
│  └─ ...
└─ Non-CoT Zero-Shot (NCZS)/
   ├─ NCZS 1/
   │  ├─ ...
   │  └─ ...
   └─ ...
```

---

## Data Files

- Data files are designed to store information about the prompt and response.
- These files were **originally produced by the LLM** and then **edited by humans**  to **correct metadata and add additional information** where necessary to ensure accuracy and completeness.

**Notes on stored evaluations:**
- **Self-evaluation** refers to the model’s own assessment (values typically on a 1–10 scale). These were retained for completeness but **disregarded** in analysis due to unreliability.
- **Supervised (human) evaluations** were performed by real evaluators. The rubric fields are:

| field                    | weight | range          | explanation |
|--------------------------|:------:|:--------------:|-------------|
| `factual_correctness`    |  25%   | 1 to 5         | Are the facts and steps correct? |
| `Reasoning_quality`      |  25%   | 1 to 5         | Is the logic transparent? |
| `coherency_and_clarity`  |  20%   | 1 to 5         | Is the response clear and easy to follow? |
| `completeness`           |  20%   | 1 to 5         | Does it cover all required aspects? |
| `understanding_depth`    |  10%   | 1 to 5         | Does it show insight beyond surface-level? |
| `weighted_total`         |  N/A   | 0 to 100 (pct) | Final composite score from weights |

**Weighted total formula**  
Our paper does **not** include a formula for `weighted_total`. We compute it as:

$$
\text{Weighted Total} = \left( \frac{\sum_{i=1}^{n} ( \text{Score}_i \times \text{weight}_i )}{5} \right) \times 100
$$

(where scores are 1–5 and weights sum to 1.0). 

---

## Effect Sizes

- Eta-squared (η²), partial eta-squared (η<sub>p</sub>²), and omega-squared (ω²) were derived from the ANOVA results using their standard formulas based on sums-of-squares (SS), mean-squares (MS) and degrees-of-freedom (df).

$$
\eta^{2} = \frac{SS_{\text{effect}}}{SS_{\text{total}}}
$$
$$
\text{partial } \eta^{2} = 
\frac{SS_{\text{effect}}}{SS_{\text{effect}} + SS_{\text{error}}}
$$
$$
\omega^{2} =
\frac{
SS_{\text{effect}} - (df_{\text{effect}})(MS_{\text{error}})
}{
SS_{\text{total}} + MS_{\text{error}}
}
$$

- Some formulas are **not presented in our paper**
- For more information regarding the formulas, see the reference below.

**Reference for effect-size formulas**  
B. G. Tabachnick and L. S. Fidell, *Using Multivariate Statistics*, 6th ed., Upper Saddle River, NJ: Pearson Education, 2013, pp. 54–55.

---

## Associated Publication

This repository contains the source code and materials for the work described in our paper, "Chain-of-Thought vs. Few-Shot: A Comparative Study of Prompting Strategies for Code Generation," by K. Nobakhtfar, K. Cakilci, R. Zilan. 

Status: Submitted to the 5th International Informatics and Software Engineering Conference (IISEC 2026).

Note: The final, peer-reviewed version of the paper may contain minor changes. We will update this section upon acceptance or publication.
