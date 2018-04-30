variable "environment" {}
variable "vpc_id" {}
variable "jumpbox_ip" {}
variable "ssh_port" {}
variable "tcp_protocol" {}

resource "aws_security_group" "isolated_sg" {
  name = "isolated_security_group"

  vpc_id = "${var.vpc_id}"

  tags {
    Environment = "${var.environment}"
  }
}

resource "aws_security_group_rule" "allow_ssh" {
  type              = "ingress"
  security_group_id = "${aws_security_group.isolated_sg.id}"
  description       = "Allow incoming SSH from Jumpbox only"

  from_port = "${var.ssh_port}"
  to_port   = "${var.ssh_port}"
  protocol  = "${var.tcp_protocol}"

  cidr_blocks = ["${var.jumpbox_ip}"]
}

resource "aws_security_group_rule" "allow_egress" {
  type              = "egress"
  security_group_id = "${aws_security_group.isolated_sg.id}"
  description       = "Allow communication to jumpbox only"

  from_port   = 0
  to_port     = 0
  protocol    = "-1"
  cidr_blocks = ["${var.jumpbox_ip}"]
}

output "isolated_sg_id" {
  value = "${aws_security_group.isolated_sg.id}"
}
