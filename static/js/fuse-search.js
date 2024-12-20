document.addEventListener("DOMContentLoaded", function () {
    const lang = document.documentElement.lang || "en"; // Detect active language
    const searchFile = lang === "sv" ? "/sv/search-index.json" : "/search-index.json";

    fetch(searchFile)
        .then((response) => response.json())
        .then((data) => {
            const options = {
                keys: ["title", "tags", "keywords"], // Fields to search
                threshold: 0.4, // Fuzzy matching sensitivity
            };
            const fuse = new Fuse(data, options);

            const searchInput = document.getElementById("search-input");
            const searchResultsContainer = document.getElementById("search-results-container");
            const searchResultsList = document.getElementById("search-results");
            const searchResultsMessage = document.getElementById("search-results-message");

            if (searchInput && searchResultsList && searchResultsMessage) {
                searchInput.addEventListener("input", function () {
                    const query = searchInput.value.trim();
                    const results = fuse.search(query);

                    if (results.length > 0) {
                        searchResultsMessage.style.display = "none";
                        searchResultsList.innerHTML = results
                            .map(
                                (result) => `
                                    <li class="list-group-item">
                                        <a href="${result.item.url}" class="text-decoration-none">
                                            ${result.item.title}
                                        </a>
                                    </li>
                                `
                            )
                            .join("");
                    } else {
                        searchResultsMessage.style.display = "block";
                        searchResultsList.innerHTML = "";
                    }
                });
            }
        })
        .catch((err) => console.error("Error loading search index:", err));
});
