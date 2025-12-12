variable "prefix" {
  type        = string
  description = "Prefix for all Azure resources"
}

variable "location" {
  type        = string
  description = "Azure region for resource deployment"
}

variable "subscription_id" {
  type = string
  description = "Azure Subscription ID"
}

variable "repo_url" {
  type = string
  description = "The URL of the GitHub repository for source control"
}

variable "admin_login" {
  type = string
  description = "The administrator username for the SQL server"
}

variable "admin_password" {
  type        = string
  description = "The administrator password for the SQL server"
}
