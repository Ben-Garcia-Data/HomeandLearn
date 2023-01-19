I've made the following alterations from the instructions:

In Superheroes:

I've added a print_data function to the Superpowered class to cut down on messy boilerplate code & assigning variables for data which is already within a variable. I think my way is more legible and cuts down on memory useage.

In Database Project:

The DB interface can be accessed from localhost/phpmyadmin on the local machine.

I'm only using "form = tk.Tk()" once as twice didn't seem neccesary and was causing this error: https://stackoverflow.com/questions/23224574/tkinter-create-image-function-error-pyimage1-does-not-exist

The instruction of the code was:
"jobLabelTabOne = tk.Label(tab1, text="Job Title:")"
The text example was:
"jobLabelTabOne = tk.Label(tab1, text="Address:")"
This happens twice. I've used Job Titles.

I've rearranged the following lines to fix an issue where the Tkinter form was not filling with my data.