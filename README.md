1. Quantized model inference server
Serve a small/distilled ML model (e.g. a sentiment classifier or sentence-embedding model) via ONNX Runtime + a minimal ASGI app (Starlette, not FastAPI — skip the pydantic overhead). Goal: sub-10ms p99 latency, low memory footprint. Good if you want to touch both "efficient model" and "efficient API" in one projec
