terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }

    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.19.0"
    }
  }

  backend "remote" {
    hostname     = "app.terraform.io"
    organization = "spikes"

    workspaces {
      prefix = "lambdas-for-cognito-"
    }
  }
}