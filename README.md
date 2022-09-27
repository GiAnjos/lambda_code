# lambda_code
Here you can find a code for a lambda function that finds the latest file from a folder, moves it to a new folder and starts two workflows inside of AWS Glue.

For the lambda function to work you need to do the proper configurations. First you need to create or find an existing role inside of AWS IAM with the areas of AWS that you need access to change. I will show here step-by-step of how I created my role and what permissions it has.

To create a role go to the area "roles" inside of IAM and select "Create":
![image](https://user-images.githubusercontent.com/93729823/192641111-8fdcdffe-0ad1-43a9-8559-d1a565804559.png)


 
