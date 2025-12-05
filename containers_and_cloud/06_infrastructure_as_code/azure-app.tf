terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.55.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "3.7.2"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_resource_group" "arg" {
  name     = "ContactBookRG${random_integer.ri.result}"
  location = "Sweden Central"
}


resource "azurerm_service_plan" "asp" {
  name                = "contact-book-${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.arg.name
  location            = azurerm_resource_group.arg.location
  os_type             = "Linux"
  sku_name            = "F1"
}

resource "azurerm_linux_web_app" "alwa" {
  name                = "ContactBookApp${random_integer.ri.result}"
  resource_group_name = azurerm_resource_group.arg.name
  location            = azurerm_service_plan.asp.location
  service_plan_id     = azurerm_service_plan.asp.id

  site_config {
    application_stack {
      node_version = "16-lts"
    }
    always_on = false
  }
}

resource "azurerm_app_service_source_control" "github" {
  app_id                 = azurerm_linux_web_app.alwa.id
  repo_url               = "https://github.com/nakov/ContactBook"
  branch                 = "master"
  use_manual_integration = true
}

