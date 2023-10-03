# **Movie Data ETL Pipeline**

## **Overview of Project**
The goal of this project is to construct an Extract-Transform-Load (ETL) data
pipeline using movie and movie rating data from both Wikipedia and Kaggle. The
focus is restricted to just the creation of the pipeline yielding cleaned and
stored data; any analysis of the data is outside the scope of the project.

The task was completed using four jupyter notebooks that build on each other,
successively adding each stage of the ETL process. The final objective was to
have one script that automates the entire process, starting with the extract
stage and ending with the loading of data into a PostgreSQL database.
Additionally, the transform stage was broken into four segments, one for the
necessary cleaning operations of each dataset and a final one for the merge
operations.

#### **Script Reference Table**
| No. | Script                                                                                                        | Operation                                                                  |
| --- | ------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| 1   | *[ETL_function_test.ipynb](https://github.com/cdpeters/movies-ETL/blob/main/ETL_function_test.ipynb)*         | Extract data from their source files                                       |
| 2   | *[ETL_clean_wiki_movies.ipynb](https://github.com/cdpeters/movies-ETL/blob/main/ETL_clean_wiki_movies.ipynb)* | Adds Wikipedia movie data transformations                                  |
| 3   | *[ETL_clean_kaggle_data.ipynb](https://github.com/cdpeters/movies-ETL/blob/main/ETL_clean_kaggle_data.ipynb)* | Adds Kaggle metadata and ratings data transformations and DataFrame merges |
| 4   | *[ETL_create_database.ipynb](https://github.com/cdpeters/movies-ETL/blob/main/ETL_create_database.ipynb)*     | Adds loading of data into a PostgreSQL database                            |

The scripts above were constructed after the prototyping process. The prototyped
pipeline can be found in the file *[module_script.ipynb](https://github.com/cdpeters/movies-ETL/blob/main/module_script.ipynb)*.

## **Extract**
The Wikipedia movie dataset
(*[wikipedia_movies.json](https://github.com/cdpeters/movies-ETL/tree/main/Resources)*) contains the
result of a scrape (in JSON format) of Wikipedia for all movies released since
1990. The two Kaggle datasets contain movie metadata
(*[movies_metadata.csv](https://github.com/cdpeters/movies-ETL/tree/main/Resources)*) from over 45,000
movies and over 26 million movie ratings (*ratings.csv*) from MovieLens.

>##### Note: *ratings.csv* is not included in this repository due to its size. The dataset was downloaded from *[The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset/)* page on Kaggle.

The source files mentioned above are read into the jupyter environment using
Pandas and the json library. All three datasets are then converted to DataFrames
ready for cleaning in scripts 2-3. These operations are all contained within the
`extract_transform_load()` function of script 1 (see script reference table for
script name).

## **Transform**
### **Wikipedia Movie Data**
Script 2 focuses only on the raw Wikipedia DataFrame. To start off, the function
`clean_movie()` is added with the purpose of reducing the columns that contain
alternate titles to one column along with consolidating columns representing the
same information.

Additional Transformations:
- filtering out non-movies
- dropping duplicate imdb ID's
- dropping columns with mostly null values
- parsing currency data
- converting dates to datetime objects
- converting running times into the correct numeric values

The `clean_movie()` function, along with the other transformations mentioned
above are all added to the `extract_transform_load()` function from script 1 so
that it now performs the extract stage and the first transformation stage.

### **Kaggle Data and DataFrame Merges**
The dataset transformations in script 3 cover the Kaggle metadata and ratings
data. Additionally, two merges are performed to produce a complete table of
movies, metadata, and ratings. These operations were added to the
`extract_transform_load()` function from script 2 so that it now extracts the
data and performs all the transformations prior to the loading stage. The
transformations added in script 3 are outlined below.

#### **Kaggle Movie Metadata**
Transformations:
- drop 'adult' column where the value is `False`
- convert the values of Boolean columns to actual Boolean values
- convert numeric values to numeric data types
- convert dates to datetime objects

#### **Kaggle Movie Rating Data**
Transformations:
- convert the 'timestamp' column to datetime objects
- group the data by 'movieId'
- gather counts of each rating value
- pivot the data so that it is ready to be merged

#### **Merge the Data**
Transformations:
- merge the Wikipedia data with the Kaggle metadata to form the movies DataFrame
- merge the new movies DataFrame with the ratings DataFrame to make a complete
  movie with ratings DataFrame

## **Load**
Script 4 combines the previous extract and transformation stages with the final
load stage where the first merged DataFrame from script 3 (the movies DataFrame
without ratings) and the raw ratings data are loaded into a PostgreSQL database.
SQLAlchemy is used to create the connection to the database and the Pandas
method `pd.to_sql()` is used to load the data.

It is important to note that the second merged table (movies with ratings) is
not being loaded in this step. The choice to keep the movies and ratings tables
separate is done to replicate a possible database schema where this data is
stored in separate tables. The focus is not on the schema but on the process of
loading multiple tables into the database.

Additionally, because of the size of the ratings DataFrame, the decision is made
to load this data in chunks. To achieve this, a further decision is made to use
the `pd.read_csv()` function with its `chunksize` parameter to deliver slices of
the DataFrame to the loading function `pd.to_sql()`. Based on this approach, the
raw ratings file is used as opposed to the cleaned ratings DataFrame from
earlier steps. The entire loading operation for the ratings data can be seen in
the `for` loop at the bottom of the `extract_transform_load()` function.

## **Summary**
Script 4 completes the automation of the ETL process for this movie and ratings
data. After running this final script, the data is stored and ready for future
analysis. Please note that the choice of tables for cleaning and loading reflect
that this project in its entirety is meant to be an exercise and not equivalent
to how the project might be structured in an industry setting.
