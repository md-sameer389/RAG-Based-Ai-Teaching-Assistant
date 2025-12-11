**RAG Video Course — Retrieval-Augmented Generation**

This repository implements a simple RAG pipeline for a video-based web-development course. It converts videos to audio, transcribes audio into timestamped chunks, embeds those chunks, stores embeddings, and performs retrieval + generation using a local LLM server.

**Quick Overview**
- **Purpose:** Answer course-related questions by locating relevant video timestamps and returning human-friendly guidance.
- **Flow:** `VIDEOS/` -> `audios/` -> `jsons/` -> `embeddings.joblib` -> interactive query (`process.py`).

**Files**
- `test.py`: Extract audio from videos using `ffmpeg` (writes `audios/`).
- `chunks.py`: Batch transcribe `audios/` using Whisper; writes chunked JSON files to `jsons/`.
- `STT.py`: Example single-audio transcription with Whisper.
- `CTT.py`: Create embeddings for each chunk (calls local `/api/embed`) and saves `embeddings.joblib`.
- `process.py`: Interactive retrieval + generation. Loads `embeddings.joblib`, finds top-N similar chunks, constructs a prompt, calls the local `/api/generate` and writes `prompt.txt` / `response.txt`.
- `jsons/`: Per-audio JSON chunk outputs.
- `audios/`: MP3s produced by `test.py` (input to transcription).

**Requirements**
- System: `ffmpeg` in PATH.
- Python packages: `pandas`, `numpy`, `scikit-learn`, `requests`, `joblib`, `whisper` (OpenAI Whisper) and its dependencies (`torch`).

Install example:
```bash
pip install pandas numpy scikit-learn requests joblib git+https://github.com/openai/whisper.git
```

**Local services expected**
- A local model server reachable at `http://localhost:11434` with these endpoints:
  - `POST /api/embed` — body: `{"model":"bge-m3","input":["text1","text2"]}` returns `{"embeddings":[...]}`
  - `POST /api/generate` — body: `{"model":"llama3.2","prompt":"...","stream":false}` returns a JSON with a `response` string.

**Quick start (minimal)**
1. Ensure `ffmpeg` installed and local LLM/embedding server running at `http://localhost:11434`.
2. Extract audio from videos:
```bash
python test.py
```
3. Transcribe audios to `jsons/`:
```bash
python chunks.py
```
4. Generate embeddings and save `embeddings.joblib`:
```bash
python CTT.py
```
5. Run interactive query (retrieval + generation):
```bash
python process.py
```

**Notes & Limitations**
- Embeddings and generation calls assume the exact local API format above.
- `whisper` is called with model `large-v2` — large GPU memory required. Use smaller models for faster runs.
- Embeddings are stored in `embeddings.joblib` (Pandas DataFrame). Retrieval uses in-memory cosine similarity — fine for small datasets, not optimized for scale.
- Paths and server URLs are hard-coded. No authentication or retries implemented.

**Suggested Improvements**
- Move configuration (paths, host, model names) to environment variables or a config file.
- Add `requirements.txt` and lightweight Docker image.
- Use FAISS (or another vector DB) for scalable retrieval.
- Add CLI wrapper to orchestrate the full pipeline and add logging/robust error handling.

**Want me to**
- add `requirements.txt`, or
- implement FAISS-backed retrieval, or
- add a CLI orchestrator and config file?

---
Created to document and make the pipeline reproducible. See `process.py`, `CTT.py`, and `chunks.py` for the implementation details.
