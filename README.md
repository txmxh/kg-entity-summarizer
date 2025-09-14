# kg-entity-summarizer
A Python project for summarizing entities in knowledge graphs by selecting the most relevant facts based on the local frequency of properties. The goal is to generate concise and informative summaries for each entity.

## Project Overview
Knowledge graphs (KGs) are structured networks of entities and their relationships, enabling applications such as semantic search, recommendation systems, and question answering. However, entities in KGs may be described by hundreds of facts, not all of which are equally useful. This project implements and evaluates entity summarization methods to extract the most informative, relevant, and representative facts for each entity.

## Features
- **Entity Summarization** using local frequency of properties
- Modular Python implementation for easy extension
- Readable summaries for downstream applications
- Easy integration into other KG/NLP pipelines

## Approach
The core approach is **property local frequency** (LF): properties (predicates) that occur more often for an entity are considered more important. We:
- Count how many times each property appears among an entity's triples
- Rank triples by property frequency
- Select the top-*k* triples as the summary
This method offers a simple and interpretable baseline for entity summarization.

## Project Structure
kg-entity-summarizer/
├── main.py # Example use case and execution
├── count_local_frequency.py # Function to compute property frequency
├── triple_ranking.py # Function to rank triples
├── generate_entity_summary.py # Main summarization function
├── README.md # Project documentation (this file)

## Requirements
- Python 3.7+
- (No external dependencies by default)

## Output
<img width="563" height="104" alt="image" src="https://github.com/user-attachments/assets/06fef49e-f748-4e13-8601-1ce67b4c1a27" />

## Installation
```bash
git clone https://github.com/txmxh/kg-entity-summarizer.git
cd kg-entity-summarizer
python3 main.py
