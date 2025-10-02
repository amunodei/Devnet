

variable "linode_token" {
   description = "Linode API token"
   type = string
}
variable "region" {
  description = "Linode region (Atlanta)"
  type = string
  default = "us-southeast"
}

variable "instance_type" {
  description = "Linode plan (4 GB shared-CPU)"
  type = string
  default = "g6-standard-2"

}