# Slideshow

A web application that loops through pictures and gifs, each being displayed for a specified period of time.

# Preconditions
1. `slideshow` is dependent on Flask being installed. 

### Example Usage
To start the slideshow, simply type
```
user@hostname:~ % python run.py
```
then visit `127.0.0.1:5000` in a browser to view the slideshow.

#### Upload a picture 
To add a picture or video to the slideshow visit `127.0.0.1:5000/upload`

#### Delete a picture 
To delete a picture or video to the slideshow visit `127.0.0.1:5000/delete`

#### Reorder the slideshow
To change the order of the slideshow visit `127.0.0.1:5000/reorder`

### Structure
The pictures and videos uploaded get stored in a folder called `pictures`. An example of what the directory structure looks like:

```
slideshow
├── static
    ├── pictures
    ├── picture1.jpg
    ├── pitcure2.jpg
    ├── picture3.jpg
```
