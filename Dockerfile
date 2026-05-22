FROM ghcr.io/astral-sh/uv:python3.14-alpine AS docbuilder

WORKDIR /bigbrotherdocs

COPY mkdocs.yml .
COPY docs ./docs
COPY src ./src

RUN uv pip install --no-cache-dir -r ./docs/requirements.txt --system && \
    zensical build

FROM ghcr.io/astral-sh/uv:python3.14-alpine

COPY src /bigbrother
COPY --from=docbuilder /bigbrotherdocs/site /bigbrother/docs

WORKDIR /bigbrother

RUN addgroup -g 2000 biggroup && adduser -S -u 1001 -G biggroup bigbrother && \
    uv pip install --no-cache-dir -r requirements.txt --system && rm requirements.txt

USER bigbrother

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "/bigbrother/logging_config.yml", "--proxy-headers", "--forwarded-allow-ips", "*"]
