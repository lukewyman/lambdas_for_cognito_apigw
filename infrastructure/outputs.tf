output "lambdas" {
  description = "A map of lambda logical names and their ARNs."
  value = {
    for k, function in aws_lambda_function.lambda_function : k => {
      name : function.function_name
      arn : function.arn
    }
  }
}