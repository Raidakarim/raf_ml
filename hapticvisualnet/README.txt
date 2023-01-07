Setting up:
# Download the code + dataset
# All dependencies are managed by Docker:
cd docker
./docker_build.py

Running the training code:
cd docker
./docker_run.py
# Run the training code on the provided dataset in datasets/ which will save to a directory called checkpoints
python train.py --use_haptic --use_rgb

# Configure the path to the saved checkpoint in analysis.py
python analysis.py
# Will dump to a folder called vis containing the predictions
