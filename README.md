# Network Performance Diagnostics Suite

An automated telemetry pipeline that samples local network throughput performance over a continuous timeline, structures historical logs, and compiles analytical visualization graphics for performance evaluation.

## System Architecture

The pipeline splits responsibilities across three decoupled core layers:
1. **Ingestion Engine (`tracker.py`):** Leverages the `speedtest` API to sample download and upload bitrates, scaling raw results to network-standard decimal Mbps.
2. **Daemon Automation (`scheduler.py`):** Uses stateful scheduling intervals to trigger safe telemetry sampling precisely on the hour.
3. **Analytics Pipeline (`analysis.ipynb`):** An object-oriented data analysis interface that generates 4-panel grids mapping numerical distributions, hourly variations, daily timelines, and temporal heatmaps.

## How To Install & Execute

1. Clone the repository to your environment.
2. Install the production dependencies:
   ```bash
   pip install -r requirements.txt
