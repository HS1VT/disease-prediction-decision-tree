First, we have to make a decision tree using tree_maker.ipynb. For that first we import dataset.csv and load it into a variable using pd.read.csv(). Then, we try to see that how many unique diseases are there. Then we make the X_train, Y_train, X_test and Y_test lists and then we feed it into out decision tree model using the sklearn library as emntioned in the question page on Canvas.

We download the desicion tree as an image file for reference. We them import pickle, that saves our decision tree in a file called disease_prediction.pkl and then we download that disease_prediction.pkl.

Now, we open the python file called Web_App.py. This python file contains the code that we use to make the web app. All the detailed steps that we follow in the web page is taken as screenshots and stored in a folder called 'Working Screenshots'.

For the web app we use a library called pywebio and use Flask to integrate it in an HTML page,and we install it using 
pip install pywebio

Now we open the .pkl file that we generated in the initial step. The .pkl file conatins the decision tree and will help us in making our web application, and we use flask for the given purpose. We define the function that identifies all the symptoms which are listed in a list format below and user sees the below functions to choose from, and the code will predict the disease and the cure based on the following function called predict().

Now we read the symptom_Description.csv and symptom_precaution.csv into two variables and then using the same variables, we will then use the decision tree to output that what are the descriptions of the disease that the patient is going through, and using the precaution csv, we will tell the user that what are the precautions that you need to keep in mind that will save you from the given disease. Now we declare a list in which we'll store the expected diseases, we create a drop down menu for the user to select from the 17 diseases.

Now we ask the user about what symptoms she/he is observing in her/his body and we check that if a particular disease is selected by the user, then we will give that disease a number 1 and if it is not selected, then it is 0.

After we are done with all this, we will finally enter our information in the columns of the web page and there we go! :)