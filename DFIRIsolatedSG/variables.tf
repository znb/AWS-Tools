variable "aws_access_key" {}
variable "aws_secret_key" {}

variable "aws_region" {
  default = "eu-west-2"
}

variable "environment" {
  default = "infosec"
}

variable "availability_zone" {
  default = "eu-west-2a"
}

variable "profile" {
  default = "terraform"
}

variable "vpc_id" {
  description = "Modify me accordingly"
  default     = "vpc-example"
}

variable "jumpbox_ip" {
  description = "Modify me accordingly"
  default     = "192.168.152.1/32"
}

variable "ssh_port" {
  default = "22"
}

variable "tcp_protocol" {
  default = "tcp"
}
