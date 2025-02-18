document.addEventListener('DOMContentLoaded', () => {
  const LANG_DEFAULT = "en";
  const DEBOUNCE_DELAY = 300;
  const SEARCH_FILE_PATH = {
    en: "/search/index.json",
    sv: "/sv/search/index.json",
  };

  const lang = document.documentElement.lang || LANG_DEFAULT;
  const searchFile = SEARCH_FILE_PATH[lang] || SEARCH_FILE_PATH[LANG_DEFAULT];
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');

  let fuse = null;

  // Utility: Debounce function to limit rapid calls
  const debounce = (func, delay) => {
    let timeout;
    return (...args) => {
      clearTimeout(timeout);
      timeout = setTimeout(() => func(...args), delay);
    };
  };

  // Fetch and initialize Fuse.js
  fetch(searchFile)
    .then((response) => response.json())
    .then((data) => {
      fuse = new Fuse(data, {
        keys: [
          { name: 'permalink', weight: 0.4 },
          { name: 'title', weight: 0.3 },
          { name: 'tags', weight: 0.2 },
          { name: 'summary', weight: 0.1 },
        ],
        threshold: 0.2,
        useExtendedSearch: true,
        ignoreLocation: true,
        includeScore: true,
      });
    })
    .catch((error) => {
      console.error("Failed to load search index:", error);
      displayMessage("Failed to load search results. Please try again later.", "text-danger");
    });

  // Event Listener: Debounced search input handling
  searchInput.addEventListener(
    "input",
    debounce(() => {
      if (!fuse) {
        displayMessage("Initializing search...", "text-muted-dark");
        return;
      }
      const query = searchInput.value.trim();
      if (query) {
        handleSearch(query);
      } else {
        displayMessage("Start typing to see results ...", "text-muted-dark");
      }
    }, DEBOUNCE_DELAY)
  );

  /**
   * Handles displaying search results
   */
  function handleSearch(query) {
    const results = fuse.search(query);
    searchResults.innerHTML = ""; // Clear previous results

    if (results.length === 0) {
      displayMessage("No results found.", "text-muted-dark");
      return;
    }

    const fragment = document.createDocumentFragment();
    results.forEach(({ item }) => {
      const resultDiv = createSearchResult(item, query);
      fragment.appendChild(resultDiv);
    });

    searchResults.appendChild(fragment);
  }

  /**
   * Creates a single search result element with highlights
   */
  function createSearchResult(item, query) {
    const resultDiv = document.createElement("div");
    resultDiv.classList.add("mb-4", "pb-3", "border-bottom");

    const highlightedTitle = highlightMatch(item.title, query);

    resultDiv.innerHTML = `
      <span class="mb-1">
        <a href="${item.permalink}">${highlightedTitle}</a>
      </span>
    `;
    return resultDiv;
  }

  /**
   * Highlights matching parts of a text
   */
  function highlightMatch(text, query) {
    const regex = new RegExp(`(${query})`, "gi");
    return text.replace(regex, (match) => `<mark>${match}</mark>`);
  }

  /**
   * Displays a message in the search results container
   */
  function displayMessage(message, className = "text-muted-dark") {
    searchResults.innerHTML = `<p class="${className}">${message}</p>`;
  }
});