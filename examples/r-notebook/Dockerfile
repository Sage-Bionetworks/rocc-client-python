FROM tschaffter/rstudio:0.2.1

# Create conda environment named "rocc"
RUN conda create --name rocc python=3.8.5 \
    && conda run --name rocc pip install \
        rocc-client==0.1.3 \
    # Fix libssl issue that affects conda env used with reticulate
    && cp /usr/lib/x86_64-linux-gnu/libssl.so.1.1 \
        /opt/miniconda/envs/rocc/lib/libssl.so.1.1