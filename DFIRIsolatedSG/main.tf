provider "aws" {
  access_key = "${var.aws_access_key}"
  secret_key = "${var.aws_secret_key}"
  region     = "${var.aws_region}"
  profile    = "${var.profile}"
}

module "security-groups" {
  source       = "./modules/security-groups"
  environment  = "${var.environment}"
  vpc_id       = "${var.vpc_id}"
  tcp_protocol = "${var.tcp_protocol}"
  ssh_port     = "${var.ssh_port}"
  jumpbox_ip   = "${var.jumpbox_ip}"
}
