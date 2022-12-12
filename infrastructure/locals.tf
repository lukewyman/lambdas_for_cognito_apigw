locals {

  tags = {
    created_by = "terraform"
  }

  app_prefix = "${var.app_prefix}-${terraform.workspace}"

  aws_ecr_url = "${data.aws_caller_identity.current.account_id}.dkr.ecr.${var.region}.amazonaws.com"
}