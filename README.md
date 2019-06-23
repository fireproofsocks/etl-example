# ETL Example

This is an example of an ETL process written in Python. It was written for academic purposes to demonstrate how to separate code concerns and provide a plausible starting point for extracting data from an API and importing it into a database.

## Setup

Create a Python Virtual Environment using `conda` and then install the required modules using `pip install`:

```
conda create -n my-etl python=3.7
pip install -r requirements.txt
```

## Installation

1. Create a MySQL database
2. Run the queries contained in `schema.sql` (e.g. by importing the file).
3. Create a `.env` file by copying the provided `.env.example`.
4. Adjust the values in your `.env` file to match your database name and credentials.
5. Run the extraction process: `python extract.py`
6. Run the transform/load processes: `python transform.ply` 
