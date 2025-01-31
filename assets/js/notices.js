document.addEventListener("DOMContentLoaded", function() {
    const noticesUrl = "https://blobserver.dc.scilifelab.se/blob/freya-notices.json";
    const currentSite = "pathogens-portal"; // Change this to dynamically detect the current site if needed.

    fetch(noticesUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            const currentDate = new Date();
            if (!data.notices || !Array.isArray(data.notices)) {
                throw new Error("Invalid notices data");
            }

            data.notices.forEach(notice => {
                try {
                    let shouldDisplay = false;

                    if (!notice.target || !Array.isArray(notice.target) || !notice.target.includes(currentSite)) {
                        return; // Skip this notice if the target does not include the current site.
                    }

                    if (notice.type === "scheduled") {
                        const startDate = new Date(notice.start_date);
                        const endDate = new Date(notice.end_date);
                        if (currentDate >= startDate && currentDate <= endDate) {
                            shouldDisplay = true;
                        }

                        // Format dates to a readable format (e.g., '20th December')
                        const formattedStartDate = startDate.toLocaleDateString('en-US', { day: 'numeric', month: 'long' });
                        const formattedEndDate = endDate.toLocaleDateString('en-US', { day: 'numeric', month: 'long' });

                        // Replace placeholders in the messages
                        notice.message_en = notice.message_en.replace('{{start_date}}', formattedStartDate).replace('{{end_date}}', formattedEndDate);
                        notice.message_sv = notice.message_sv.replace('{{start_date}}', formattedStartDate).replace('{{end_date}}', formattedEndDate);
                    } else if (notice.type === "incidental" && notice.active) {
                        shouldDisplay = true;
                    }

                    if (shouldDisplay) {
                        const noticeContainer = document.createElement('div');
                        noticeContainer.className = 'notice alert d-flex justify-content-center align-items-center rounded-0'; // Use Bootstrap classes
                        
                        // Check if style property is provided and not empty, otherwise use default styles
                        let style = notice.style;
                        if (!style || style.trim() === "") {
                            style = notice.type === "scheduled" 
                                ? "background-color: #d4de27; color: #000000;" 
                                : "background-color: #ffc107; color: #000000;";
                        }
                        noticeContainer.style = `${style}; margin-top: 15px; text-align: center;`; // Add top margin and center text

                        const siteLanguage = document.documentElement.lang;
                        let message = notice.message_en;
                        if (siteLanguage === "sv") {
                            message = notice.message_sv;
                        }

                        const noticeMessage = document.createElement('div');
                        noticeMessage.innerHTML = `<i class="bi bi-info-circle-fill"></i> <strong>${notice.title}:</strong> ${message}`;
                        noticeMessage.className = "alert-body"; // Use Bootstrap class for alert body

                        noticeContainer.appendChild(noticeMessage);

                        // Insert the notice at the top of the body
                        document.body.insertBefore(noticeContainer, document.body.firstChild);
                    }
                } catch (error) {
                    console.error('Error processing notice:', error);
                }
            });
        })
        .catch(error => console.error('Error fetching notices:', error));
});
