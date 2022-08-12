terraform {
  source = "git::git@github.com:ei-roslyakov/terraform-modules.git//aws_eip/?ref=tags/v0.0.2"
}

include "root" {
  path = find_in_parent_folders()
}

locals {
  region = jsondecode(file(find_in_parent_folders("region.json")))
  env    = jsondecode(file(find_in_parent_folders("env.json")))
  app    = jsondecode(file(find_in_parent_folders("app.json")))
  common = jsondecode(file(find_in_parent_folders("../common.json")))
}

inputs = {
  name      = "${local.env.env}-${local.app.app}-nlb-ip"
  count_eip = 10
  tags = {
    Name = "${local.env.env}-${local.app.app}-nlb-ip"
    App  = "${local.app.app}"
  }
}