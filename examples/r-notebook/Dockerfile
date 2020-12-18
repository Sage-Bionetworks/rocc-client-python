FROM tschaffter/rstudio:0.2.1

# Create conda environment named "rocc"
RUN conda create --name rocc python=3.8 \
    && conda run --name rocc pip install \
        rocc-client==0.1.2 \
        # TODO remove the dependecies below once included in setup.py
        certifi>=14.05.14 \
        python_dateutil>=2.5.3 \
        setuptools>=21.0.0 \
        six>=1.10 \
        urllib3>=1.15.1 \
    # Fix libssl issue that affects conda env used with reticulate
    && cp /usr/lib/x86_64-linux-gnu/libssl.so.1.1 \
        /opt/miniconda/envs/rocc/lib/libssl.so.1.1