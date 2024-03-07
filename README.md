# DTC-Data-Eng-Zoomcamp-capstone

work in progress

## Table of Contents

- [DTC-Data-Engineering-zoomcamp-capstone](#dtc-data-engineering-zoomcamp-capstone)
  - [Table of Contents](#table-of-contents)
    - [Foreword](#foreword)
    - [Problem description](#problem-description)
    - [Cloud usage](#cloud-usage)
    - [Data ingestion](#data-ingestion)
    - [Data warehouse within BigQuery](#data-warehouse-within-bigquery)
    - [Transformations utilizing Mage](#transformations-utilizing-mage)
    - [Dashboard](#dashboard)
    - [Reproducibility](#reproducibility)
      - [Creating GCS Bucket](#creating-gcs-bucket)
      - [Transformation stage](#transformation-stage)
      - [Alternative (local) method proposed:](#alternative-local-method-proposed)
      - [Bigquery](#bigquery)
      - [LookerStudio](#lookerstudio)
    - [Improvement Notes](#improvement-notes)

<br>

---

<br>


### Foreword

Mainly to the peer reviewers: I tried to structure this markdown so that evaluating could be more accessible if following the evaluation criteria found in [this markdown file](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/projects/README.md) located in the `cohort 2024` directory on the main branch of the DTC-data-engineering default repo.

You probably have seen here two new sections: this one -`Foreword`- and `Improvement notes`. The former one is self-explanatory I believe. Regarding the latter one, I created it to briefly summarize some of the many aspects and details that I would have liked to do better had I invested more time, energy and resources - I guess this last attribute it's a combination of the first two- on this project.

<br>


### Problem description

The aim of these project is to showcase an end-to-end data pipeline execution being deployed in the cloud. We also aim to identify which professions are more prone to have sleeping disorders amongst a very small sample of a dataset on [sleep health and lifestyles](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?select=Sleep_health_and_lifestyle_dataset.csv).

For that end, the structure of an OLAP approach/system was followed. This is to say: beginning by loading the dataset from a remote repository until rendering of a dashboard for analytic purposes. 

More instructions and details about these pipelines, processes, resources, tools utilized and project reproducibility can be found within the sections that follow from here.

<br>

### Cloud usage

The project has been developed in the cloud using Google Cloud Platform as a sole resource/service provider, and these **resources have been provisioned, managed and deployed** via **Terraform as Infrastructure as Code tool**.

<br>

### Data ingestion 

The data ingestion was characterized to be of a batch workflow orchestration with Mage, all developed and deployed using Google Run after initializing and enabling/applying Terraform as IaC.

<<<<<<< HEAD
[Dataset:](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?select=Sleep_health_and_lifestyle_dataset.csv)

The data ingestion was characterized to be of a batch workflow orchestration with Mage, all developed and deployed using Google Run after initializing and enabling/applying Terraform as IaC

This end-to-end ingestion pipeline is compound by two separated batch pipelines with multiple steps/modules. These were created utilizing Mage, and they can be found in [this directory](https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/tree/main/capstone%20project/workflow%20orchestration)
=======
This end-to-end ingestion pipeline is compound by two separated batch pipelines with multiple steps/modules. These were created utilizing Mage, and they can be found in [this directory](https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/tree/main/workflow%20orchestration)
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

The ingestion of the first batch pipeline begun loading the dataset from a raw CSV file hosted on GitHub, and finalized by exporting/staging the dataset into a GCS Bucket. It is important to notice that we technically didn't have to load from any API as we didn't make any GET request to any API endpoint.

The second batch pipeline commenced by fetching the staged data from our GCS bucket - as though in a Data Lake, i.e. ADLS in Azure - and concluded by pushing this transformed dataset into BigQuery. 

You will note that in each of these pipelines, there were Transformation blocks, these being detailed further on. The existence of these two transformation blocks in different pipelines was for showcasing purposes. 

Please note that it would have been more efficient to execute all the transformation before staging the data in the data lake/storage, this is to say, within the 1st batch pipeline. 

<<<<<<< HEAD
<br>
=======
[Back to Table of Contents](#table-of-contents)
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

<br>

### Data warehouse within BigQuery

Tables were created into BigQuery without any need to partition or cluster data due to the nature of the dataset.

The only `DDL statements` for the table creation were the following:

```
CREATE TABLE IF NOT EXISTS `data-eng-zoomcamp-cohort24.sleep_health_dataset.stress_sleeping`
AS 
SELECT
  sleep_duration,
  stress_level,
  occupation
FROM
  `data-eng-zoomcamp-cohort24.sleep_health_dataset.data_table`;
```

```
CREATE TABLE IF NOT EXISTS `data-eng-zoomcamp-cohort24.sleep_health_dataset.sleep_bmi`
AS 
SELECT
  occupation,
  sleep_disorder
FROM
  `data-eng-zoomcamp-cohort24.sleep_health_dataset.data_table`;
```
<<<<<<< HEAD
<br>
=======

[Back to Table of Contents](#table-of-contents)

<br>

>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

### Transformations utilizing Mage

We can see that transformation blocks exist in each of the two pipelines created. All these transformations were executed utilizing Pandas and Numpy libraries, and these were distributed as follows:

<<<<<<< HEAD
- First batch pipeline
=======
- First batch pipeline: from API to GCS bucket
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

  - unifying classes in the `weight` category
  - creation of two different categories for `systolic` and `diastolic pressure` 
  - deletion of the unified `blood pressure` category

<<<<<<< HEAD
- Second batch pipeline
=======
- Second batch pipeline: from GCS bucket to BigQuery
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

  - parsing all the letters of the categories as lowercase
  - dropped the category `blood_pressure` which contains 2 two values separated by a slash

<<<<<<< HEAD
=======
[Back to Table of Contents](#table-of-contents)

>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f
<br>

### Dashboard

<<<<<<< HEAD
The dashboard was done using Looker Studio, an it was elaborated rather briefly as it can be told, with just 2 tiles, and these can be seen [in this GCP link]()


<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/2-tile-dashboard.png"  width="88%" height="88%">
=======
The dashboard was done using Looker Studio, an it was elaborated rather briefly as it can be noticed, with only 2 tiles, and these can be seen [in this GLS link](https://lookerstudio.google.com/reporting/e643ddeb-cb89-4966-8339-d39f1fa66136)


<p align="center">
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/2-tile-dashboard.png"  width="88%" height="88%">
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

We found that amongst the small sample of the population, `Nurses, Teaches, Sales person and Scientist` are the occupations that tend to have some kind of sleeping disorder. 

Also it can be noticed that `Nurses, Doctors and Engineers` compose more than the half of the professions in the dataset. If performing an EDA had been within the scope of this project, we would have noticed and tackled this issue prior to executing and documenting it.

[Back to Table of Contents](#table-of-contents)

<br>

<br>

### Reproducibility

<<<<<<< HEAD
I tried to provide concise instructions on how I developed and deployed this project. If you're encountering any trouble while reproducing this project, feel free to ping me and tell me about it:
=======
I tried to provide concise instructions on how I developed and deployed this project. If you're encountering any trouble while reproducing these steps, feel free to ping me and ask me about it.

#### Creating GCS Bucket
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

In `IAM & Admin` section on GCP, we first create a Service Account. Then we grant permissions / roles to administer BigQuery, Storage and Compute Engine resources with this Service Account.

Next we create a new key in json type. Once we've downloaded the json file with it, copy and paste its content into a json file, and store it in a directory inside your main project's Terraform folder. N.b: Make sure to add this folder into your `.gitignore` amongst other files with sensitive information.

In order to pass our key/credentials and so initialize Terraform, instead of hardcoding our credentials, we are going to use Google SDK to authenticate ourselves:

    export GOOGLE_CREDENTIALS='<your-path-directory-to-your-keys>/my-creds.json'

We can echo this out to check the export went trough:

      echo $GOOGLE_CREDENTIALS

The output being:

      <your-path-directory-to-your-keys>/my-creds.json

We can now run `terraform init` to let the provider `GOOGLE_CREDENTIALS` pass our key.

Next, we are ready now to start scripting our .tf files, in this case these being basically two:

* main.tf:  This file will contain the main configuration for our infrastructure. It defines the resources we want to create, modify, or manage by utilizing Terraform. Amongst other kind of configuration settings, in this file we can include mainly resource, data or provider blocks.

* variables.tf: This file will allow us to avoid hardcoding values directly into your configuration files. This is to say, we use it to define and pass the input variables for our Terraform configuration. These input variables allow us to parameterize the configuration of our project architecture and so making this more flexible.

It is highly suggested to get the VS Code extension like `HashiCorp Terraform` in order to ease the scripting of the `.tf` files.

Once we've passed all the values, we can run the following commands in our bash terminal to execute the configuration of our infrastructure in GCP:

      terraform plan

      terraform apply

There is no auto-confirmation in Terraform when scripting by CLI, so we will need to type `yes` when applying changes:

<p align="center">
<<<<<<< HEAD
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-gcs-bucket.png"  width="88%" height="88%">

And so our bucket `sleep-health-de-bucket` was created:

=======
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/terraform/terraform-gcs-bucket.png"  width="88%" height="88%">

And so our bucket `sleep-health-de-bucket` was created:


<p align="center">
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/terraform/terraform-gcs-bucket-2.png"  width="88%" height="88%">

[Back to Table of Contents](#table-of-contents)

<br>
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-gcs-bucket.png"  width="88%" height="88%">

<br>

#### Transformation stage

Next we are to orchestrate an end-to-end-pipeline from our public repository to Google BigQuery Warehouse. For this, we will use Terraform as IaC to spin up an instance and develop all our blocks there.

We clone 

      git clone https://github.com/mage-ai/mage-ai-terraform-templates.git

After cd-ing into `gcp` directory, we can open VS Code and adjust the main and variable.tf files. Basically, we will validate our credentials the same way we did when creating our bucket with Terraform. The .tf files utilized for this project are located in [this directory](https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/tree/main/terraform)

<<<<<<< HEAD
We also have to configure and enable Cloud Filestore API
=======
We also have to configure and enable Cloud Filestore API. Once all this is done, we are ready to run in our bash terminal:
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

      terraform init

<<<<<<< HEAD
      terraform init

      terraform apply
=======
      terraform apply

<p align="center">
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/terraform/terraform-cloud-run.png"  width="88%" height="88%">
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

When accessing to Google Run, we see a new service running :

<<<<<<< HEAD

<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-cloud-run.png"  width="88%" height="88%">

When going to Google Run, we see a new service :


<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-cloud-run-1.png"  width="88%" height="88%">
=======
<p align="center">
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/terraform/terraform-cloud-run-1.png"  width="88%" height="88%">
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

Before opening the URL of this instance in our local machine, it's safer to whitelist our IP so that we can restrict the access to these service.

<p align="center">
<<<<<<< HEAD
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/mage/running-in-vm.png"  width="88%" height="88%">
=======
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/mage/running-in-vm.png"  width="88%" height="88%">
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

Now we're ready to build and develop our pipelines in this virtual environment.

As said in the introductory section of this markdown file, for demonstration purposes, you will note that two pipelines have been created to perform different transformations.

<<<<<<< HEAD
The Python blocks that were used in the two pipelines mentioned in the section []() can be found in [this directory](https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/tree/main/capstone%20project/workflow%20orchestration)
=======
The Python blocks that were used in the two pipelines mentioned in the section []() can be found in [this directory](https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/tree/main/workflow%20orchestration)
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

This is a sample of how the GUI of Mage looks like:

<p align="center">
<img src="https://github.com/GBlanch/Data-Eng-Zoomcamp-capstone/blob/main/assets/mage/mage-load.png"  width="88%" height="88%">

<<<<<<< HEAD
=======
- First transformation: `API to GCS bucket` batch pipeline

    ```python
    if 'transformer' not in globals():
        from mage_ai.data_preparation.decorators import transformer
    if 'test' not in globals():
        from mage_ai.data_preparation.decorators import test

    import numpy as np
    import pandas as pd

    @transformer
    def transform(data, *args, **kwargs):

        # To make data handling less cumbersome, replace spaces with underscores
        data.columns = [spaces.replace(' ', '_') for spaces in data.columns] 

        # Unify 'Normal' and 'Normal weight' weight
        data["BMI_Category"] = data["BMI_Category"]\
                              .apply(lambda x: x.replace("Normal Weight",
                                                          "Normal"))
        # impute NaNs
        data = data.replace(np.nan, 'None',
                            regex = True)


        data[['Systolic_BP', 'Diastolic_BP']] = data["Blood_Pressure"]\
                                              .apply(lambda x: pd.Series(str(x)\
                                                                        .split("/")))

        return data


    @test
    def test_output(output, *args):
        """
        Template code for testing the output of the block.
        """
        assert output.isnull()\
                    .sum().any() == False, 'NaNs still exist in the dataframe'
    ```


- Second transformation: `GCS bucket to BigQuery` batch pipeline
  
    ```python
    if 'transformer' not in globals():
        from mage_ai.data_preparation.decorators import transformer
    if 'test' not in globals():
        from mage_ai.data_preparation.decorators import test


    @transformer
    def transform(data, *args, **kwargs):

        data.columns = data.columns.str.lower()
        data.drop('blood_pressure',
                  axis = 1,
                  inplace = True)

        return data
    ```

[Back to Table of Contents](#table-of-contents)

>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f
<br>

  #### Alternative (local) method proposed: 

  If preferred, instead of running and deploying from within the cloud, you can also run Mage locally following this steps:

  clone the repo from Mage github:

      git clone https://github.com/mage-ai/mage-zoomcamp.git mage-zoomcamp

  After cd-ing into mage-zoomcamp directory, we copy `dev.env` file into `.env` file so that we can name it in our gitignore file:

        cp dev.env .env

  Then we build and start the container with the following commands, respectively:

        docker compose build

        docker compose up
  In case we get a notification that there's a latest version of the `mageai` image, we just need to run 

        docker pull mageai/mageai:latest

  In any case, it is always advisable to run docker scout to analyze the images we're about to compose up:

        docker scout view

  Opening our localhost:6789 should take you to the main Mage UI. The rest of the block creation and configuration is the same as the process we have just described in our virtual instance. The main difference would be that the pipelines would be developed and run locally, instead of using a VM.

<<<<<<< HEAD
<br>
=======
[Back to Table of Contents](#table-of-contents)

<br>

>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

#### Bigquery

Once our dataset is loaded into BigQuery, we can create the tables we want to use in LookerStudio later on. As mentioned in [section__](), these were build by running these `DDL statements` :

```
CREATE TABLE IF NOT EXISTS `data-eng-zoomcamp-cohort24.sleep_health_dataset.stress_sleeping`
AS 
SELECT
  sleep_duration,
  stress_level,
  occupation
FROM
  `data-eng-zoomcamp-cohort24.sleep_health_dataset.data_table`;
```

```
CREATE TABLE IF NOT EXISTS `data-eng-zoomcamp-cohort24.sleep_health_dataset.sleep_bmi`
AS 
SELECT
  occupation,
  sleep_disorder
FROM
  `data-eng-zoomcamp-cohort24.sleep_health_dataset.data_table`;
```

<br>

#### LookerStudio

Once we have imported these tables into LookerStudio, we will build and adjust all the dashboard using LookerStudio GUI. The brief result was presented in the section [Dashboard](#dashboard).
<<<<<<< HEAD
=======

[Back to Table of Contents](#table-of-contents)

<br>
>>>>>>> 878c135f9e893645ad5960f9c0516885f7ccb60f

### Improvement Notes

If more time had been allotted to design, execute and document this project -and I still had free credits for GCP usage - ,  it would be much preferable to:

- Consume a larger dataset and get deep understanding of the data dictionary and the categories of the dataset
- After performing EDA, aim to solve more intricate matters and so posing better questions  
- Have more usage within the Data Warehouse so as to solve this new questions
- Finally, elaborate a much more complete dashboard, and to my preference, utilize Tableau Public

[Back to Table of Contents](#table-of-contents)

