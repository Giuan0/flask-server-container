# Flask server container for classification of the imagenet database

# Build image
```
sh build.sh
```

# Run image
```
sh run-development.sh
```

# Classification request
```
curl -X POST -F image=@images/bird.jpg http://localhost:5000/classification
```