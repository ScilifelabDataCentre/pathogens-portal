// Fetch the banner title for homepage from the blobserver and update the page title
document.addEventListener("DOMContentLoaded", async function() {
    try {
        // Fetch the banner titles
        const response = await fetch('https://blobserver.dc.scilifelab.se/blob/freya-banner_titles.json');
        if (!response.ok) {
            throw new Error(`Failed to fetch banner titles. Status: ${response.status}`);
        }
        const data = await response.json();

        // Get the current language
        const lang = document.documentElement.lang;

        // Select the title element
        const titleElement = document.querySelector('h1');

        // Find the title for the 'portal' target
        const title = data.banner_titles.find(title => title.target === 'portal');

        if (title && title[lang] && title['active']) {
            // Update the title if it exists and is active
            titleElement.textContent = title[lang];
        } else {
            console.warn('No active title found for the "portal" target.');
        }
    } catch (error) {
        console.error('An error occurred while fetching banner titles:', error);
    } finally {
        // Show the hidden banner regardless of whether titles were fetched successfully
        const banner1 = document.getElementById("banner1");
        if (banner1) {
            banner1.classList.remove("d-none");
        } else {
            console.warn('Banner element with ID "banner1" not found.');
        }
    }
});
