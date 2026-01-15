const input = document.getElementById("movieInput");
const suggestions = document.getElementById("suggestions");
const resultsDiv = document.getElementById("results");
const resultsTitle = document.getElementById("resultsTitle");


input.addEventListener("input", async () => {
    const query = input.value.trim();
    if (!query) {
        suggestions.innerHTML = "";
        return;
    }

    try {
        const res = await fetch(`/autocomplete?q=${query}`);
        const data = await res.json();

        suggestions.innerHTML = "";

        data.forEach(title => {
            const li = document.createElement("li");
            li.textContent = title;

            li.onclick = () => {
                input.value = title;
                suggestions.innerHTML = "";
            };

            suggestions.appendChild(li);
        });
    } catch (err) {
        console.error("Autocomplete error:", err);
    }
});


document.getElementById("recommendBtn").addEventListener("click", async () => {
    const movie = input.value.trim();
    if (!movie) return;

    resultsTitle.innerText = "Top 5 Recommended Movies";
    resultsDiv.innerHTML = "<p>Loading...</p>";

    try {
        const res = await fetch("/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ movie })
        });

        const data = await res.json();

        if (!data.success) {
            resultsDiv.innerHTML = `<p>${data.error}</p>`;
            return;
        }

        resultsDiv.innerHTML = "";

        data.data.forEach((m, index) => {
            const card = document.createElement("div");
            card.className = "movie-card";

            card.innerHTML = `
                <img id="poster-${index}"
                     src="${m.poster}"
                     alt="${m.title}"
                     referrerpolicy="no-referrer">
                <h4>${m.title}</h4>
            `;

            resultsDiv.appendChild(card);

            // 🔄 Fetch poster asynchronously
            fetch(`/poster/${m.movie_id}`)
                .then(res => res.json())
                .then(p => {
                    if (p.poster) {
                        document.getElementById(`poster-${index}`).src = p.poster;
                    }
                })
                .catch(err => console.error("Poster fetch error:", err));
        });

    } catch (err) {
        console.error("Recommendation error:", err);
        resultsDiv.innerHTML = "<p>Something went wrong</p>";
    }
});


