 # Workspace Organizer

Workspace Organizer is a simple workspace organizer written in python

## About the Project

This small application takes all the files in a directory and compresses them, leaving the `.zip` file in another directory ordered by dates.

## Requeriments

- Windows 8 or higher
- Python 3

## Settings

The following `json` configuration file is available to configure the directories:

- `config.json`

Before running the application for the first time, you should create this configuration file, using the following example template:

```json
{
    "folder": "D:\\Downloads\\Workdir\\",
    "destination": "D:\\Historical\\",
    "last_date": "2021-01-01"
}
```

Parameters:

- `folder`: This is the path of the folder you want to compress, in Windows you must use `\\` to separate the subdirectories.
- `destination`: This is the path of the folder where the `.zip` files will be saved
- `last_date`: The date of the last execution is stored here, this should only be modified the first time it is executed.

## Running the App

If you are using windows you can just run the `run-windows.bat` file

A scheduled task at system startup is recommended.

## Considerations

This application does not identify if a file was created or modified on a specific day.

This application removes the source files once compressed, so care must be taken.

The application only compresses if the date of the `last_date` variable is less than the current date, therefore if the application is executed many times during a single day, only the first execution will be effective.

The application will set as the file name the date of the `last_date` variable instead of the current date.