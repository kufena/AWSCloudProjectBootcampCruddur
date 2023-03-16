# Cognito stuff.

This template and code creates a Cognito User Pool and User Pool Client, together with a post confirmation trigger Lambda function, that
puts the user in a database table.

The postgres RDS instance is already created, in fixed security group and subnets, which are hard coded here.

You need to pass the parameters to the dotnet deploy command, as so:

```
dotnet lambda deploy-serverless CruddurUserPool2 --s3-bucket thegatehousewereham.home --region eu-west-2 -tp "ConnectionHost="Host=<host>;ConnectionDB=<db>;ConnectionUsername=<username>;ConnectionPassword=<pwd>"
```

Note the use of quotes around the whole environment/parameter list, as semicolons cause the CLI to think it's a new command (semicolons cause all sorts of issues.)

This sets up the user pool and client as per the instructions in the Free AWS Cloud Boot Camp, but the trigger writes to the DB three times.  I don't know why.

Oh, one last thing - to allow the DB and Trigger and User Pool/Client to talk to each other, you need to allow All TCP communications inside the Security Group.  You'll have to add this manually at the moment.  I started creating a Cloud Formation template for the database, but haven't got very far.  When I have that, I can create a specific VPC set up and dedicated Security Group.