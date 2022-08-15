terraform {
  source = "git::git@github.com:ei-roslyakov/terraform-modules.git//aws_ecr/?ref=tags/v0.0.2"
}

include "root" {
  path = find_in_parent_folders()
}

locals {
  region = jsondecode(file(find_in_parent_folders("region.json")))
  env    = jsondecode(file(find_in_parent_folders("env.json")))
  app    = jsondecode(file(find_in_parent_folders("app.json")))
  common = jsondecode(file(find_in_parent_folders("common.json")))
}


inputs = {
  image_names = [
    "some-name-${local.env.env}-${local.app.app}-1",
    "some-name-${local.env.env}-${local.app.app}-2",
    "some-name-${local.env.env}-${local.app.app}-3",
    "some-name-${local.env.env}-${local.app.app}-4",
    "some-name-${local.env.env}-${local.app.app}-5",
    "some-name-${local.env.env}-${local.app.app}-6",
    "some-name-${local.env.env}-${local.app.app}-7",
    "some-name-${local.env.env}-${local.app.app}-8",
    "some-name-${local.env.env}-${local.app.app}-9",
    "some-name-${local.env.env}-${local.app.app}-10",
    "some-name-${local.env.env}-${local.app.app}-11",
    "some-name-${local.env.env}-${local.app.app}-12",
    "some-name-${local.env.env}-${local.app.app}-13",
    "some-name-${local.env.env}-${local.app.app}-14",
    "some-name-${local.env.env}-${local.app.app}-15",
    "some-name-${local.env.env}-${local.app.app}-16",
    "some-name-${local.env.env}-${local.app.app}-17",
    "some-name-${local.env.env}-${local.app.app}-18",
    "some-name-${local.env.env}-${local.app.app}-19",
    "some-name-${local.env.env}-${local.app.app}-20",
    "some-name-${local.env.env}-${local.app.app}-21",
    "some-name-${local.env.env}-${local.app.app}-22",
    "some-name-${local.env.env}-${local.app.app}-23",
    "some-name-${local.env.env}-${local.app.app}-24",
    "some-name-${local.env.env}-${local.app.app}-25",
  ]
  tags = {
    Name = "some-name-${local.env.env}-${local.app.app}"
  }
}