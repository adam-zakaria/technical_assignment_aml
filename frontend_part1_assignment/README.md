# Install required packages
`python -m pip install -r requirements.txt`

`npm i`

```
cd tqdm_ui
npm i 
npm run dev
```

There is no way to tell from the process metadata how long it will take or how long it has taken. Assume the python writes a progress.json file describing the progress.


# Notes

a. using the TQDM progress bar, write a short python program that would automatically update the TQDM progress for a given python process into a mongoDB progress bar collection.

I'm not totally clear on what's being asked here. Specifically, I'm not sure what 'TQDM progress' is. I've never used TQDM, but my understanding from the GitHub (https://github.com/tqdm/tqdm) is that tqdm() can wrap an iterator to print a progress bar, or can run on the command line and have input piped into to print a progress bar. I cannot find any mention of TQDM outputting values (that can then be written to a collection).

I've done my best to do something close to what's being asked :) Please contact me with any questions or desired updates.

What I've done is wrap a loop with tqdm so that a progress bar gets displayed in the terminal. Progress also gets written to a collection in the form of current_iteration and total steps