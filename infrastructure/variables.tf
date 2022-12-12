variable "region" {
  default = "us-west-2"
}

variable "lambda_folders" {
  description = "Map of lambda names and their corresponding directory names"
  type        = map(map(string))
  default = {
    create-product = {
      context   = "create_product"
      image_tag = 4
    }
    delete-product = {
      context   = "delete_product"
      image_tag = 2
    }
    get-product = {
      context   = "get_product"
      image_tag = 2
    }
  }
}

variable "app_prefix" {
  default = "lambdas-for-cognito"
}
