# lambda_code
Here you can find a code for a lambda function that finds the latest file from a folder, moves it to a new folder and starts two workflows inside of AWS Glue.

For the lambda function to work you need to do the proper configurations. First you need to create or find an existing role inside of AWS IAM with the areas of AWS that you need access to change. I will show here step by step of how I created my role and what permissions it has.

To create a role go to the area "roles" inside of IAM and select "Create":
![image](https://user-images.githubusercontent.com/93729823/192641111-8fdcdffe-0ad1-43a9-8559-d1a565804559.png)

Select the first option in the "trusted entity type" area:
![image](https://user-images.githubusercontent.com/93729823/192641910-b47348dc-63a1-425a-85d2-3771678dac0f.png)

Select Lambda as an option for the area "use case":
![image](https://user-images.githubusercontent.com/93729823/192642312-ca73e56b-d147-4550-aa2a-921ada1f5085.png)

After that you will need to select the permissions you need for the project. Just select them all and click next in the end of the page. In this case we are going to use these permissions:
![image](https://user-images.githubusercontent.com/93729823/192642610-54e291aa-5b0c-44c7-8093-c843b62a1c66.png)

In the end create a name for you role, review everything and click create role. 

The role is ready so now you need to create the function. 

Go to Lambda in AWS and click create function. After that select "author from scratch" in the first area and also create the name of your function:
![image](https://user-images.githubusercontent.com/93729823/192644939-4e9eaeac-a890-4a65-9fa9-82cb14d4f42b.png)

Select the language that you are going to write your function. In this case Pyhton 3.9:
![image](https://user-images.githubusercontent.com/93729823/192645644-11fae88e-09f6-4e8c-9132-187a3d55a541.png)

For permissions you can search for the role that you created previously:
![image](https://user-images.githubusercontent.com/93729823/192645970-4b719c62-4b21-4acd-aaeb-78c682e9ed07.png)

Go to your function and add a trigger so it knows when to start the function. My function was created to be triggered when a file gets posted in a the "OLDEST FOLDER" as you can see on the code. So lets go to the step by step.

To create a trigger select S3 as a source:
![image](https://user-images.githubusercontent.com/93729823/192646978-a5fe6f47-20c4-4ae2-96de-df983c7095dd.png)

Put the name of the bucket that you are using for the project and add the prefix or suffix of the folder that you want. I added a prefix "OLDEST FOLDER/" for this project:
![image](https://user-images.githubusercontent.com/93729823/192648248-a6a437c9-42db-44f5-8969-3e364796bbde.png)

Don't forget to a acknowledge the following message and click add:
![image](https://user-images.githubusercontent.com/93729823/192648370-d3dfc852-880e-4b23-8bd3-bb3181ef39ba.png)

Add the code in this area of your function and click test:
![image](https://user-images.githubusercontent.com/93729823/192648808-1938d86e-9467-4bee-b6b7-05b4ed28a4e1.png)

When you click on test it will open a pop-up with the test configurations. Add a name for your test and select if you want to share the test with others or not:
![image](https://user-images.githubusercontent.com/93729823/192649222-f37763db-43fb-4d7d-9835-61c28d1692b8.png)

For the test template I used cloudwatch:
![image](https://user-images.githubusercontent.com/93729823/192649472-60f751fa-22b3-4408-85e9-966f9e8adc01.png)

You can check the results of your test in the execution results tab:
![image](https://user-images.githubusercontent.com/93729823/192650073-18e6463a-4c8b-4760-a23b-b933934b5cb8.png)

Click deploy if you have the approval to do so and all done!! 




