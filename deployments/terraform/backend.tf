terraform {
  backend "gcs" {
    bucket  = "fuchicorp-bucket-seil"
    prefix  = "qa/hello-world"
    project = "fuchicorp-gke-cluster"
  }
}
