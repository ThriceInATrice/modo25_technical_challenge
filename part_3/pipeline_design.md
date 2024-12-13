# Pipeline design 

This is a high level design for a data pipeline, taking data from REST APIs and storing it in a data warehouse. There are three phases to the process, following an Extract/Transform/Load model.

### Terraform 
In order to remove the need for dedicated in house servers, the pipeline will be built in Amazon Web Services using Terraform to lay out and deploy the digital infrasctructure. Terraform is an excellent tool for laying out AWS infrastructure in code without needing direct access to the AWS console or credentials, and can also be used to rapidly deploy or tear down AWS infrastructure when needed.

### AWS Lambda and State Machine
Each phase of the process would be invoked by a state machine triggered at regular intervals by a job scheduler. All the code will be Python running in AWS Lambda in order to minimise expense on server time, and data will be stored in AWS S3 between phases. The Boto3 package is used to interface with AWS systems such as S3 and Secret Manager. AWS is chosen for this process because it has good integration between different functions, and allows for much of the work to be simplified with Terraform and Boto3. Similarly, Boto3 is chosen for its excellent documentation and applicability across multiple AWS services.

### Extract
In the first phase, FastAPI is used to access the target API and extract the desired data. The data is stored in an S3 bucket and the time of extraction is noted so that the next extraction can access only data that is more recent. FastAPI is chosen for its ease of deployment and asynchronous functionality.

### Transform
In the second phase, Python code is used to transform the data into a star schema to match the data warehouse. A star schema denormalises the data and makes it simple for querying and analysis. The transformed data is again stored in an S3 bucket.

### Load
In the third phase, psycopg2 is used to load the data into the data warehouse. Psycopg2 is useful for its suitability for asynchronous use and multithreading utility as multiple cursors can use a single connections.

### Security
For security, credentials for the API and database can be stored in AWS Secrets Manager, to minimise exposure and prevent the need for sensitive information to be present in the code. When deployed using Terraform on the users AWS account, the pipeline is able to use the account AWS credentials to access the secrets manager. This also allows the pipeline to be provided as a complete package to a customer, who does not need to share any of the credentials or alter the code.

### Monitoring
AWS Cloudwatch is used for logging the progress of the pipeline, and alerts are sent by email when important issues arise. Cloudwatch is chosen as being within the AWS system makes its integration extremely simple.