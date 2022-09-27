# lambda_code
Here you can find a code for a lambda function that finds the latest file from a folder, moves it to a new folder and starts two workflows inside of AWS Glue.

For the lambda function to work you need to do the proper configurations. First you need to create or find an existing role inside of AWS IAM with the areas of AWS that you need access to change. I will show here step-by-step of how I created my role and what permissions it has.

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




