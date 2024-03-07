terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials)
  project     = var.project
  region      = var.region
}

# google_storage_bucket
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket

# 1st name is local, 2nd has to be globally unique across all GCP

resource "google_storage_bucket" "sleep-health-bucket" {
  name          = var.gcs_bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}
# resource name and local name ( as in bucket )
resource "google_bigquery_dataset" "sleep-health-dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}