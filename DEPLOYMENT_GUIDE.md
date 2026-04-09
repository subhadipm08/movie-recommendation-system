# 🚀 End-to-End Deployment Guide: Render Free Plan

This guide provides a step-by-step walkthrough for deploying the **Movie Recommendation System** to Render using the optimized Docker configuration.

## 📋 Prerequisites

1.  **GitHub Account**: Your project must be pushed to a GitHub repository (Done).
2.  **Render Account**: Create a free account at [render.com](https://render.com).
3.  **TMDB API Key**: 
    - Sign up at [The Movie Database (TMDB)](https://www.themoviedb.org/).
    - Navigate to **Settings > API** to generate your API Key.

---

## 🛠️ Step 1: Project Preparation

We have already optimized the project for the 512MB RAM limit on Render:
- **Reduced Precision**: Similarity matrix uses `float16` to save RAM.
- **Multi-Stage Build**: Dockerfile is optimized to keep the image small.
- **Production Requirements**: `requirements-prod.txt` is used for the runtime.

---

## ☁️ Step 2: Create a Render Web Service

1.  Log in to your **Render Dashboard**.
2.  Click the **"New +"** button and select **"Web Service"**.
3.  **Connect your Repository**: Select your GitHub repository (`movie-recommendation-system`).

---

## ⚙️ Step 3: Configure Deployment Settings

In the creation screen, use the following settings:

| Setting | Value |
| :--- | :--- |
| **Name** | `movie-recommender` (or your choice) |
| **Region** | Select the one closest to you (e.g., Singapore or Oregon) |
| **Branch** | `main` |
| **Runtime** | **Docker** |
| **Instance Type** | **Free** ($0 / month) |

---

## 🔑 Step 4: Set Environment Variables

> [!IMPORTANT]
> The application will not fetch movie posters correctly without the TMDB API Key.

1.  Click on the **"Advanced"** button or go to the **"Environment"** tab.
2.  Add the following secret:
    - **Key**: `TMDB_API_KEY`
    - **Value**: `your_api_key_here`

---

## 🚀 Step 5: Deploy and Verify

1.  Click **"Create Web Service"**.
2.  **Monitor the Build**:
    - Render will pull your code and start the Docker build.
    - **Stage 1**: It will install dependencies and run `main.py` (generating the models). This may take 2-4 minutes.
    - **Stage 2**: It will switch to the slim runtime and start the Flask server.
3.  **Check the Logs**: Watch for the message `* Running on http://0.0.0.0:5000`.
4.  **Open the App**: Once the status turns **"Live"**, click the URL provided by Render (e.g., `https://movie-recommender.onrender.com`).

---

## 💡 Troubleshooting & Tips

- **Cold Starts**: Render's free plan spins down services after 15 minutes of inactivity. The first request after a break might take ~30 seconds to wake up the service.
- **Memory Limits**: If you see an `OOM` (Out of Memory) error in the logs, ensure that you haven't added massive new datasets. The current `float16` optimization is designed to stay within the 512MB limit.
- **Re-training**: Any time you push new code to GitHub, Render will automatically rebuild the image and re-generate the similarity matrix.

---

## 👤 Support
If you encounter issues during deployment, check the Render logs for specific error messages or refer back to the project's [README.md](file:///d:/ML/Movie_recomandation_System/README.md).
