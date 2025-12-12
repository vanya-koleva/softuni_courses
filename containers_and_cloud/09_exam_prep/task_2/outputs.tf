output "webapp_name" {
  value = azurerm_linux_web_app.alwa.default_hostname
}

output "webapp_ip_address" {
  value = azurerm_linux_web_app.alwa.outbound_ip_addresses
}
