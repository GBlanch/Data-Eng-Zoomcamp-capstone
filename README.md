# DTC-Data-Eng.-zoomcamp-project

work in progress

<br>

## Main summary  

### Problem description

The aim of these project is to analyze a dataset on sleep health and lifestyle compound by a small sample. By doing so, we intend to extract meaningful patterns and correlations so that we can shed some light onto some possible relationship between sleep quality, lifestyle choices, and overall health.

For that end, the structure of an OLAP approach/system was followed. This is to say: beginning by loading the dataset from a remote repository until rendering of a dashboard for analytic purposes. 

More instructions and details about these pipelines, processes, resources, tools utilized and project reproducibility can be found within the sections that follow from here.

<br>

### Cloud usage

The project has been developed in the cloud using Google Cloud Platform as a sole resource/service provider, and these **resources have been provisioned, managed and deployed** via **Terraform as Infrastructure as Code tool**.

<br>

### Data ingestion 


[Dataset:](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset?select=Sleep_health_and_lifestyle_dataset.csv)

The data ingestion was characterized to be of a batch workflow orchestration with Mage, all developed and deployed using Google Run after initializing and enabling/applying Terraform as IaC

This end-to-end ingestion pipeline is compound by two separated batch pipelines with multiple steps/modules. These were created utilizing Mage, and they can be found in [this directory](https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/tree/main/capstone%20project/workflow%20orchestration)

The ingestion of the first batch pipeline begun loading the dataset from a raw CSV file hosted on GitHub, and finalized by exporting/staging the dataset into a GCS Bucket. It is important to notice that we technically didn't have to load from any API as we didn't make any GET request to any API endpoint.

The second batch pipeline commenced by fetching the staged data from our GCS bucket - as though in a Data Lake, i.e. ADLS in Azure - and concluded by pushing this transformed dataset into BigQuery. 

You will note that in each of these pipelines, there were Transformation blocks, these being detailed further on. The existence of these two transformation blocks in different pipelines was for showcasing purposes. 

Please note that it would have been more efficient to execute all the transformation before staging the data in the data lake/storage, this is to say, within the 1st batch pipeline. 

<br>

### Data warehouse

Tables were created into BigQuery without any need to partition or cluster data due to the nature of the dataset.

The queries for the table creation were the following:

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

### Transformations utilizing Mage

We can see that transformation blocks exist in each of the two pipelines created. All these transformations were executed utilizing Pandas and Numpy libraries, and these were distributed as follows:

- First batch pipeline

  - unifying classes in the `weight` category
  - creation of two different categories for `systolic` and `diastolic pressure` 
  - deletion of the unified `blood pressure` category

- Second batch pipeline

  - parsing all the letters of the categories as lowercase
  - dropped the category `blood_pressure` which contains 2 two values separated by a slash

<br>

### Dashboard

The dashboard was done using Looker Studio, an it was elaborated rather briefly as it can be told, with just 2 tiles, and these can be seen [in this GCP link]()


<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/2-tile-dashboard.png"  width="88%" height="88%">

We found that amongst the small sample of the population, `Nurses, Teaches, Sales person and Scientist` are the occupations that tend to have some kind of sleeping disorder. 

Also it can be noticed that `Nurses, Doctors and Engineers` compose more than the half of the professions in the dataset. Having done some EDA prior to executing and documenting this project would have helped notice and tackle this issue.

<br>

### Reproducibility

I tried to provide concise instructions on how I developed and deployed this project. If you're encountering any trouble while reproducing this project, feel free to ping me and tell me about it:

#### Creating GCS Bucket:

In 'IAM & Admin' section on GCP, we first create a Service Account. Then we grant permissions / roles to administer BigQuery, Storage and Compute Engine resources with this Service Account.

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
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-gcs-bucket.png"  width="88%" height="88%">

And so our bucket `sleep-health-de-bucket` was created:


<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-gcs-bucket.png"  width="88%" height="88%">

<br>

#### Transformation stage 

Next we are to orchestrate an end-to-end-pipeline from our public repository to Google BigQuery Warehouse. For this, we will use Terraform as IaC to spin up an instance and develop all our blocks there.

We clone 

      git clone https://github.com/mage-ai/mage-ai-terraform-templates.git

After cd-ing into `gcp` directory, we can open VS Code and adjust the main and variable.tf files. Basically, we will add our credentials the same way we did when creating our bucket with Terraform. The ones used fot this project are located within this folder [____]()

We also have to configure and enable Cloud Filestore API

Once all this is done, we are ready to run in our bash terminal:

      terraform init

      terraform apply



<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-cloud-run.png"  width="88%" height="88%">

When going to Google Run, we see a new service :


<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/terraform/terraform-cloud-run-1.png"  width="88%" height="88%">

Before opening the URL of this instance in our local machine, it's safer to whitelist our IP so that we can restrict the access to these service.

<p align="center">
<img src="https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/blob/main/capstone%20project/assets/mage/running-in-vm.png"  width="88%" height="88%">

Now we're ready to build and develop our pipelines in this virtual environment.

As said in the introductory section of this markdown file, for demonstration purposes, you will note that two pipelines have been created to perform different transformations.

The Python blocks that were used in the two pipelines mentioned in the section []() can be found in [this directory](https://github.com/GBlanch/DTC-Data-Engineering-Zoomcamp/tree/main/capstone%20project/workflow%20orchestration)

These are some of the screenshots as a sample of Mage GUI:

(Mage screenshots)

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

<br>

#### Bigquery

Once our dataset is loaded into BigQuery, we can create the tables we want to use in LookerStudio later on. As mentioned in [section__](), these were build by running the following queries:

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



