"""
The project designed to sort files.

You may need it to clean up your downloads folder.

When running the script, enter the path to the folder as an argument and all the work will be done for you.

Namely:

-   all images are transferred to the "images" folder
-   all documents are transferred to the "documents" folder
    -all audio files are portable up to "audio"
    -all video files up to "video"
    -all archives are unpacked and can be transferred to the "archives" folder
-   all files, extensions of which are unknown or without it, will be transferred to the "unknown" folder
-   all filenames will be normalized to English
-   all empty folders will be deleted

"""
