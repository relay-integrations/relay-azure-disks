FROM relaysh/core:latest-python
RUN ["/bin/bash", "-c", "apk --no-cache add --virtual=relay-azure-build-deps \\\n    gcc \\\n    musl-dev \\\n    libffi-dev \\\n    make \\\n    openssl-dev \u0026\u0026 \\\n  pip install azure-common azure-mgmt-compute azure-mgmt-network azure-mgmt-storage \u0026\u0026 \\\n  apk del relay-azure-build-deps\n"]
COPY "./step.py" "/entrypoint.py"
ENTRYPOINT []
CMD ["python3", "/entrypoint.py"]

LABEL "org.opencontainers.image.title"="Delete Azure Disks"
LABEL "org.opencontainers.image.description"="This task immediately deletes a set of Azure Disks."
LABEL "com.puppet.nebula.sdk.version"="v1"
