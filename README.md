# Docugami Knowledge Graph Retrieval Augmented Generation (KG-RAG) Datasets

This repository contains various datasets for advanced RAG over a multiple documents. We created these since we noticed that existing eval datasets were not adequately reflecting RAG use cases that we see in production. Specifically, they were doing Q&A over a single (or just a few) docs when in reality customers often need to RAG over larger sets of documents.

The goal with our dataset is to reflect real-life customer usage by incorporating:

1. QnA over multiple documents, more than just a few
2. Use more realistic long-form documents that are similar to documents customers use, not just standard academic examples
3. Include questions of varying degree of difficulty, including:
    1. **Single-Doc, Single-Chunk RAG:** Questions where the answer can be found in a contiguous region (text or table chunk) of a single doc. To correctly answer, the RAG system needs to retrieve the correct chunk and pass it to the LLM context. For example: `What did Microsoft report as its net cash from operating activities in the Q3 2022 10-Q?`
    2. **Single-Doc, Multi-Chunk RAG:** Questions where the answer can be found in multiple non-contiguous regions (text or table chunks) of a single doc. To correctly answer, the RAG system needs to retrieve multiple correct chunks from a single doc which can be challenging for certain types of questions. For example: `For Amazon's Q1 2023, how does the share repurchase information in the financial statements correlate with the equity section in the management discussion?`
    3. **Multi-Doc RAG:** Questions where the answer can be found in multiple non-contiguous regions (text or table chunks) across multiple docs. To correctly answer, the RAG system needs to retrieve multiple correct chunks from multiple docs. For example: `How has Apple's revenue from iPhone sales fluctuated across quarters?`

## Status

Current status for each dataset:

Dataset                                 | Status | # of Documents  | # of QnA pairs |
----------------------------------------|--------|-----------------|----------------|
[SEC 10-Q](./sec-10-q/README.md)        | [v1](./sec-10-q/data/v1/)     | [20](./sec-10-q/data/v1/docs/)              | [195](./sec-10-q/data/v1/qna_data.csv)            | 
[NTSB Aviation Incident Accident Reports](./ntsb-aviation-incident-accident-reports/README.md) | Draft  | [20](./ntsb-aviation-incident-accident-reports/data/v1/docs/)              | in progress    |
[NIH Clinical Trial Protocols](./nih-clinical-trial-protocols/README.md)        | Draft     | [20](./nih-clinical-trial-protocols/data/v1/docs/)              | in progress    |
[US Federal Agency Reports](./us-fed-agency-reports/README.md)        | Draft     | [20](./us-fed-agency-reports/data/v1/docs/)              | in progress    |
