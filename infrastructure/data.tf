data "aws_caller_identity" "current" {}

data "aws_ecr_authorization_token" "token" {}

data "aws_iam_policy_document" "lambda_assume_role" {

  statement {
    effect  = "Allow"
    actions = ["sts:AssumeRole"]
    sid     = "SidToOverride"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

data "aws_iam_policy_document" "lambda_logging_policy" {

  statement {
    effect = "Allow"
    actions = [
      "logs:CreateLogGroup",
      "logs:CreateLogStream",
      "logs:PutLogEvents"
    ]

    resources = [
      "arn:aws:logs:*:*:*"
    ]
  }
}

data "aws_iam_policy_document" "lambda_dynamodb_policy" {
  statement {
    effect = "Allow"
    actions = [
      "dynamodb:PutItem",
      "dynamodb:UpdateItem",
      "dynamodb:GetItem",
      "dynamodb:Get*",
      "dynamodb:DeleteItem",
    ]
    resources = [
      aws_dynamodb_table.products.arn,
      "${aws_dynamodb_table.products.arn}/*"
    ]
  }
}