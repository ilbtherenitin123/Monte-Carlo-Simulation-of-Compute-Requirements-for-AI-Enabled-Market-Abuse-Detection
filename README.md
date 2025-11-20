# Monte-Carlo-Simulation-of-Compute-Requirements-for-AI-Enabled-Market-Abuse-Detection
B. A GitHub-ready README (so it looks like a real research project)
A Research Project by Nitin Ranjan
🧠 Overview

This project models the compute requirements, GPU-hour consumption, latency distribution, and operating cost of an AI-enabled market abuse detection system deployed by regulators (SEC, FCA, ESMA).

Using 10,000 Monte Carlo simulations, the model estimates how compute demand fluctuates with:

Market volume

Anomaly prevalence

Model complexity

GPU throughput

Latency behavior

GPU price variance

This project demonstrates applied work at the intersection of:

AI economics

Regulatory technology (RegTech)

Compute modeling

Financial market microstructure

Risk & surveillance systems

🎯 Core Research Questions

How many GPU-hours are required to run a full-day market abuse detection pipeline?

How sensitive is compute demand to trade volume, anomaly rates, and model complexity?

What is the probability of latency-based system failure during peak market periods?

What is the expected daily cost of running this system under realistic GPU pricing?

📊 Simulation Design

We generate 10,000 simulations with stochastic variables:

Variable	Distribution	Interpretation
Trade Volume	Lognormal(μ=14, σ=0.8)	Realistic daily trading load
Anomaly Rate	Uniform(0.03%–0.12%)	Spoofing / wash trading prevalence
Inference Cost	Normal(0.9e-6, 0.2e-6)	GPU-hours per inference
Model Complexity	{1.0, 1.2, 1.5}	Baseline → heavy multi-agent policy models
GPU Throughput	Triangular(900,1200,1600)	Trades processed per second
Latency	Gamma(k=2, θ=8)	Realistic inference latency distribution
GPU Price	Uniform($1.2–$2.8/hr)	Global GPU spot-market pricing

We calculate:

GPU-hours per day

Latency distribution + failure rates

Daily operating cost

Scaling curve vs. trade volume
