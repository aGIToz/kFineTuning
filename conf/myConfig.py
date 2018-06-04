# intialize the batch size and number of epochs for training
batch_size = 32
warmUp_epochs = 25 
epochs = 100

# determine layers to be unfreezed after warm-up phase.
# unfreezes the layer starting from specified below.
unfreeze_layer = 15

# test-train split ratio
split = 0.25
