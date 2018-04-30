output "vpc_id" {
  value = "${module.security-groups.isolated_sg_id}"
}
