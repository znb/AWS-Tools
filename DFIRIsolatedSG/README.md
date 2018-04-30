# DFIR Isolated Security Group


 * You have a compromised host. 
 * You want to isolate it but still have access to perform IR things
 

## How

 1. Use Terraform to create this security group
 2. Use AWS CLI to apply the security group to your affected VPC


```
aws ec2 modify-instance-attribute --instance-id i-INSTANCE-ID --groups sg-BLOCK-ID 
```


I took the code examples from [here](https://github.com/toniblyx/aws-forensic-tools) and applied them to my fuzzy logic.