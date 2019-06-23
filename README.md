# ETL Example

This is an example of an ETL process written in Python. It was written for academic purposes to demonstrate how to separate code concerns and provide a plausible starting point for extracting data from an API and importing it into a database.

This script requests JSON data from the city of Los Angeles about its parking violations, and then it imports the downloaded files into a MySQL database (see the `schema.sql`).  There is one tricky transformation that is required in order to properly translate the the geographic coordinates.

The structure of the scripts is meant to be didactic: students should feel free to edit the functions or add new ones to suit their particular needs.

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
5. Run the extraction process: `python extract.py` -- if desired, edit the variables in this script to control its behavior.
6. Run the transform/load processes: `python transform.ply` 
