FROM nvidia/cuda:13.1.0-base-ubuntu22.04

CMD echo 'Starting GPU test...' && \
    nvidia-smi && \
    echo 'GPU test PASSED! ✅'
