terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.54.0"
    }
  }
}

provider "azurerm" {
  features {}
#   subscription_id is set in ARM_SUBSCRIPTION_ID environment variable
}

resource "azurerm_resource_group" "azure-rg" {
  name     = "azure-rg"
  location = "Sweden Central"
}
