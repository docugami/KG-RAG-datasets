# SEC 10-Q

> Status: [v1](./data/v1/) (documents and human reviewed qna_data)

## Data Preparation

1. The documents were downloaded (manually) in PDF format from the investor relations sites for various tech companies: AAPL, AMZN, INTC, MSFT, NVDA.

2. The documents were renamed (manually) using the following naming convention: `2022 Q3 AAPL.pdf`. This was an important step to bootstrap question and answer creation with LLMs.

3. Different types of questions were created (manually) for each company, similar to what a financial analyst may ask against these documents.

4. For each question, using the naming convention above, source docs were identified. For example, if the question was about the latest quarter for AAPL, we manually entered `*2023 Q3 AAPL*` as the source doc. Similarly, if the question was about all the quarters for MSFT, we manually entered `*MSFT*` as the source docs.

5. The questions with manually annotated source docs can be found here: [questions.csv](./data/raw_questions/questions.csv)

6. We now used the [process_docs](./process_docs.ipynb) notebook to process the PDFs, extract text, and get draft answers using an LLM (GPT-4-Turbo). We used the source docs annotations in `questions.csv` to make sure that only the relevant documents (in their entirety) were passed as LLM context, ensuring that there were no retrieval related problems and make sure the draft answers were as high quality as possible. The specific prompt used and other details are in the notebook.

7. The questions with draft LLM-generated answers can be found here: [questions_with_LLM_answers.csv](./data/raw_questions/questions_with_LLM_answers.csv)

8. We manually reviewed the LLM-generated answers, dividing up the task across the Docugami team internally. This is a time-consuming task, and reviewing/correcting approximately 20 questions took our team members approximately 2 days each with some internal discussion in case of ambiguity.

9. The final reviewed and corrected questions and answers were saved as `qna_data` under [./data](./data)