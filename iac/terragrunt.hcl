terraform {
  extra_arguments "common_vars" {
    // commands = get_terraform_commands_that_need_vars()
    commands = [
      "plan",
      "import",
      "push",
      "refresh",
      "destroy"
    ]
    required_var_files = [
      find_in_parent_folders("common.json"),
    ]
    optional_var_files = [
      find_in_parent_folders("region.json"),
    ]
  }
  // extra_arguments "plan_args" {
  //   commands = [
  //     "plan"
  //   ]

  //   arguments = [
  //     "-out", 
  //     "${get_parent_terragrunt_dir()}/${path_relative_to_include()}/tf.p"
  //   ]
  // }

  // extra_arguments "apply_args" {
  //   commands = [
  //     "apply"
  //   ]

  //   arguments = [
  //     "${get_parent_terragrunt_dir()}/${path_relative_to_include()}/tf.p",
  //   ]
  // }
}

locals {
  app    = jsondecode(file(find_in_parent_folders("app.json")))
  common = jsondecode(file("common.json"))
}

generate "main_provider" {
  path      = "_provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
provider "aws" {
  profile                 = var.profile
  region                  = var.region
  default_tags {
   tags = {
     Terraform   = "true"
    }
  }
}
EOF
}

generate "common-vars" {
  path      = "common-vars.tf"
  if_exists = "overwrite"
  contents  = <<EOF
variable "region" { type = string }
variable "profile" { type = string }
EOF
}



remote_state {
  backend = "s3"
  generate = {
    path      = "_backend.tf"
    if_exists = "overwrite_terragrunt"
  }
  config = {
    bucket = "rei-tf-state-s3"
    key    = "${local.app.app}/${path_relative_to_include()}/terraform.tfstate"
    region = "${local.common.region}"
  }
}
