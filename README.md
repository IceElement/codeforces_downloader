# codeforces_downloader
Downloads all accepted solutions of a codeforces user using codeforces API

If there are multiple accepted submissions for a problem, downloads the most recent one.

Codeforces sends an invalid response for some submissions, this happens because the submission page is not visible to the public.
Such files have to downloaded manually, these are usually very few 1-2%.

Tries 5 times to get the file from the server, if the network is extremely slow or not connected, the tries will fail and program exits.
In case that happens, run the program again.

Usage: open the source code and change the "user_handle" variable to target user's handle, then simply run "python file_name.py" on cmd or terminal.

Its written in python 3, so you might need to use "python3 file_name.py" if you have both distributions of python.

Files will be saved in "./codeforces/username", contest no. ,problem code, and problem name will be used to create the file name.
