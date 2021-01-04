# StopInstances
<h3>Description:</h3>

Amazon EC2 is used to launch virtual servers in the cloud as you need. You only pay for what you use. But what if you’re done with the usage and forgot to stop your instance?? Here’s a way to stop your EC2 instance automatically so that you don’t get billed unnecessarily.
In my case, I used to launch the instance at 6:00pm everyday and later I forget to stop the instance. But now I’ve automated it using Boto3 so that even if I don’t stop the instance, this script will do it for me.
<br /><h3>Step-1:</h3> 
If my code has to run everyday on schedule, it would not be a feasible method to invoke it from my system everyday and hence has to be hosted on a server. The server should be able to support the script, and has to respond as to when the code has to run. Hence, I’ve chosen AWS Lambda to host my code as it can run the code after an event has been triggered.
<br /><h3>Step-2:</h3> 
The Cron daemon is a built-in Linux utility that runs processes on your system at a scheduled time. To invoke Lambda function daily on schedule, it is achieved by using CloudWatch events. In my case, I use the expression, “0/0 19 * * ? *” as a CloudWatch rule to trigger my Lambda function.
<br /><h3>Step -3:</h3> 
To stop your instance, first you need to identify whether your EC2 instance exists or not. If it exists then go to Step-4 or else exit, as we cannot change the state of any instance if it does not exists.
<br /><h3>Step -4:</h3> 
Find the state of the instance. The states available in EC2 instance are: pending, running, shutting-down, terminated, stopping and stopped. If the state of the instance is not terminated or stopped, then go to step 5. Because it is not necessary to stop a terminated or already stopped instance.
<br /><h3>Step -5:</h3> 
Hence after verifying that the instance exists and is running, we make an API call to stop the running instance.<br />
<br />
Thus, I am able to stop the running instance and avoid myself from unnecessary billing.
