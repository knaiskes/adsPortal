resource "vultr_instance" "adsPortal" {
  plan = "vc2-1c-1gb"
  region = "ams"
  os_id = "387"
  enable_ipv6 = true
}
