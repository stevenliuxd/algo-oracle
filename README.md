# algo-oracle

AI Financial & Stock Market Analysis

## Run Docker with GPU

### Build the Container
```bash
docker build -t cuda-nightly -f .\Dockerfile.cuda .
docker build -t gpu-test -f ./Dockerfile .
```

### Run the Container
```bash
docker run --gpus all gpu-test
```
