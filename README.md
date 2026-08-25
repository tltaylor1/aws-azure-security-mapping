# AWS to Azure security mapping

Ninety-nine AWS security concepts with the closest Azure comparable for
each, written while studying for the AWS Certified Security specialty
from an Azure background. It exists because most comparison tables map
compute and storage, then stop before the security services, which are
the ones whose names differ most.

Seven entries say **No clean equivalent**. Those are the useful ones. A
mapping that finds a match for everything is telling you what you want
to hear, and the places where the two clouds genuinely diverge are where
an assumption carried across will be wrong:

| AWS concept | Why nothing maps cleanly |
|---|---|
| IAM Permission boundaries | A ceiling attached to a principal rather than a scope; Azure bounds through role assignment scope and policy instead |
| Resource Control Policies | An organization-wide ceiling on resources rather than principals |
| KMS grants | Fine-grained, temporary, programmatic key permissions with no direct Azure Key Vault analogue |
| Cognito Identity Pools | Exchanges a federated identity for temporary cloud credentials, a step Entra External ID does not have |
| Amazon Verified Permissions | Externalized fine-grained authorization as a managed service |
| Automated Forensics Orchestrator | A published forensics automation pattern rather than a service |
| AI service opt-out policies | Organization-level control over service data use in training |

## How to read it

The Azure column is the closest comparable, not an equivalent. Several
say "rough" because the shape matches but the boundary does not. Use
this to find the right Azure thing to go read about, never as evidence
that two services behave alike.

Every row was checked against both platforms' current product names in
August 2026. Cloud services rename and retire constantly, so if a row
has drifted since then, that is a welcome correction.

The table is generated from [mapping.csv](mapping.csv), which is the
source. Edits belong in the CSV; a check keeps the two in agreement:

```bash
python3 scripts/render_table.py --check
```

## The mapping

<!-- BEGIN MAPPING TABLE: generated from mapping.csv -->

| Concept | Summary | Azure Comparable |
|---|---|---|
| AI service opt-out policies (Orgs) | Org control over AI data use (new) | No clean equivalent |
| Amazon API Gateway logging | Logs API request activity | API Management diagnostics |
| Amazon Athena | SQL queries over logs in S3 | Azure Data Explorer / Log Analytics |
| Amazon Aurora | High-performance managed relational DB | Azure SQL Database |
| Amazon Bedrock (security) | Guardrails + model access controls (new) | Azure OpenAI security |
| Amazon CloudFront | Edge CDN and TLS termination | Azure Front Door / CDN |
| Amazon CloudWatch | Metrics, logs, and alarms | Azure Monitor / Log Analytics |
| Amazon CodeGuru Security | Automated secure code review | Defender for DevOps / GitHub Advanced Security |
| Amazon Cognito | App/customer identity provider | Entra External ID (formerly Azure AD B2C) |
| Amazon Detective | Investigates and analyzes findings | Sentinel investigation / hunting |
| Amazon DynamoDB | Managed NoSQL key-value database | Azure Cosmos DB |
| Amazon EBS | Block storage volumes for EC2 | Azure Managed Disks |
| Amazon ECR | Container registry with image scanning | Azure Container Registry |
| Amazon ECS | Managed container orchestration | Azure Container Apps / ACI |
| Amazon EFS | Managed elastic file storage | Azure Files |
| Amazon EKS | Managed Kubernetes clusters | Azure Kubernetes Service (AKS) |
| Amazon EMR | Big-data platform, inter-node encryption | Azure HDInsight |
| Amazon EventBridge | Event routing for security automation | Azure Event Grid |
| Amazon GuardDuty | Threat detection from AWS logs | Defender for Cloud (threat) |
| Amazon Inspector | Scans for vulnerabilities | Defender for Cloud vuln assessment |
| Amazon Macie | Discovers sensitive data in S3 | Microsoft Purview |
| Amazon Managed Grafana | Security dashboards and visualization (new) | Azure Managed Grafana |
| Amazon OpenSearch Service | Search and analyze log data | Azure Data Explorer / Elastic |
| Amazon Q Developer | AI assistant flags code vulns in pipeline | GitHub Copilot security (rough) |
| Amazon RDS | Managed relational database service | Azure SQL Database |
| Amazon Redshift | Managed data warehouse | Azure Synapse Analytics |
| Amazon Route 53 | DNS and DNSSEC | Azure DNS |
| Amazon SageMaker AI | Managed ML platform security | Azure Machine Learning |
| Amazon Security Lake | Central security data lake, OCSF (new) | Sentinel Data Lake |
| Amazon Verified Permissions | Fine-grained authz via Cedar (new) | No clean equivalent |
| Amazon VPC | Isolated virtual network boundary | Virtual Network (VNet) |
| Application Recovery Controller | Automated recovery orchestration (new) | Azure Site Recovery |
| Automated Forensics Orchestrator (EC2) | Automated EC2 forensic collection (new) | No clean equivalent |
| AWS Artifact | On-demand compliance reports | Microsoft Service Trust Portal |
| AWS Audit Manager | Automates compliance evidence collection | Microsoft Purview Compliance Manager |
| AWS Backup | Centralized backup with Vault Lock | Azure Backup |
| AWS Certificate Manager (ACM) | Manages TLS certificate lifecycle | Key Vault certs / App Gateway |
| AWS Client VPN | Managed remote-access VPN | Azure VPN Gateway (P2S) |
| AWS CloudHSM | Dedicated hardware security module | Azure Dedicated HSM |
| AWS CloudTrail | Records all AWS API calls | Azure Activity Log |
| AWS CloudTrail Lake | Queryable managed audit log store (new) | Sentinel / Log Analytics query |
| AWS Config | Tracks config and compliance | Azure Policy |
| AWS Control Tower | Governed multi-account landing zone | Azure Landing Zones |
| AWS Direct Connect | Private dedicated network link | Azure ExpressRoute |
| AWS Directory Service | Managed Active Directory | Microsoft Entra Domain Services |
| AWS Fargate | Serverless container compute | Azure Container Instances |
| AWS Fault Injection Service (FIS) | Chaos testing of resilience (new) | Azure Chaos Studio |
| AWS Firewall Manager | Central WAF/firewall policy management | Azure Firewall Manager |
| AWS IAM Identity Center | Workforce SSO and multi-account access | Entra ID SSO / enterprise apps |
| AWS Identity and Access Management (IAM) | Core identity + access policies for AWS | Entra ID + Azure RBAC |
| AWS Key Management Service (KMS) | Encryption key management service | Azure Key Vault (keys) |
| AWS Lambda | Serverless functions for automation | Azure Functions |
| AWS Network Firewall | Managed network firewall | Azure Firewall |
| AWS Organizations | Multi-account management | Management Groups |
| AWS Private Certificate Authority | Issues private TLS certificates | Azure Private CA / Key Vault |
| AWS PrivateLink / VPC Endpoints | Private access to services | Private Link / Private Endpoints |
| AWS Resilience Hub | Validates recovery objectives (new) | Azure Site Recovery (rough) |
| AWS Resource Access Manager (RAM) | Share resources across accounts | Azure Lighthouse (rough) |
| AWS Secrets Manager | Stores and rotates secrets/credentials | Azure Key Vault (secrets) |
| AWS Security Hub | Posture aggregation and scoring | Defender for Cloud (CSPM) |
| AWS Shield / Shield Advanced | DDoS protection | Azure DDoS Protection |
| AWS Site-to-Site VPN | Encrypted tunnel to on-prem | Azure VPN Gateway (S2S) |
| AWS Step Functions | Orchestrates IR automation workflows | Azure Logic Apps |
| AWS STS (AssumeRole) | Issues temporary credentials on assume | Managed identity token / PIM |
| AWS Systems Manager | Patch, run command, state mgmt | Azure Automation / Update Mgr |
| AWS Transit Gateway | Hub connecting many VPCs | Azure Virtual WAN |
| AWS User Notifications | Central notification management (new) | Azure Monitor action groups |
| AWS Verified Access | Zero-trust access, VPN replacement (new) | Entra Private Access / App Proxy |
| AWS WAF | Web application firewall | Azure WAF |
| CloudFront access logging | Edge access logs | Front Door / CDN logs |
| Cognito Identity Pools | Exchanges login for temp AWS creds | No clean equivalent |
| Config Conformance Packs | Bundled compliance rule sets | Azure Policy initiatives |
| Declarative policies (Orgs) | Org-wide enforced config baseline (new) | Azure Policy (deny/enforce) |
| EC2 Auto Scaling | Secure automatic scaling of instances | VM Scale Sets |
| EC2 Image Builder | Builds hardened machine images | Azure VM Image Builder |
| EC2 Instance Connect | Short-lived SSH access to EC2 | Azure Bastion (rough) |
| EC2 Instance Metadata Service (IMDSv2) | Token-protected instance metadata | Azure IMDS (token-style) |
| Elastic Load Balancing (ELB) | TLS termination and traffic distribution | Azure Load Balancer / App Gateway |
| ELB access logs (ALB/NLB) | Load balancer traffic logs | App Gateway / Load Balancer logs |
| Envelope encryption (concept) | Data key encrypted by a master key | Key Vault CMK envelope |
| GenAI OWASP Top 10 for LLM (concept) | Guardrails against LLM app risks | Azure AI Content Safety (rough) |
| IAM Permission boundaries | Ceiling on what a role can be granted | No clean equivalent |
| IAM Roles | Assumed temporary identity, no long creds | Managed Identities + Entra roles |
| KMS grants | Temporary scoped permission to a key | No clean equivalent |
| KMS key policies | Root of trust controlling a key | Key Vault access policy / RBAC |
| Network ACLs (NACLs) | Stateless subnet-level filter | NSG (no stateless equivalent) |
| Nitro encryption (concept) | Hardware-level EC2 encryption | Azure confidential computing |
| Resource Control Policies (RCPs) | Org-wide guardrail on resources (new) | No clean equivalent |
| Route 53 Resolver DNS Firewall | Blocks malicious DNS queries | Azure DNS security policies |
| Route 53 Resolver Query Logs | DNS query logging | Azure DNS Analytics |
| S3 Block Public Access | Prevents public S3 exposure | Storage public-access controls |
| S3 Bucket Policies | Resource policy controlling S3 access | Storage RBAC + SAS |
| S3 Object Lock | WORM storage for forensic evidence | Blob immutable storage |
| S3 server access logging | Records requests to S3 objects | Storage analytics logging |
| Security Groups (EC2/VPC) | Stateful instance-level firewall | Network Security Group (NSG) |
| Service Control Policies (SCPs) | Org-wide max-permission guardrail | Mgmt Group + Azure Policy |
| Systems Manager Session Manager | Shell access without open ports | Azure Bastion (rough) |
| Transit Gateway Flow Logs | Traffic logs across connected VPCs | Azure vWAN / NSG Flow Logs |
| VPC Flow Logs | Records VPC network traffic metadata | NSG Flow Logs |

<!-- END MAPPING TABLE -->

## Corrections

Corrections are welcome, particularly on the "rough" and "no clean
equivalent" rows. Open an issue or a pull request against `mapping.csv`
and say what the boundary difference actually is.

## Related

Built alongside [control-plane](https://github.com/tltaylor1/control-plane),
a security engineering program whose current application,
[role-call](https://github.com/tltaylor1/role-call), governs non-human
identities in AWS accounts.

## License

[CC BY 4.0](LICENSE). Use it, adapt it, credit it.
